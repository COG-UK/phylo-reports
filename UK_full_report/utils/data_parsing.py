
from collections import defaultdict
import os
import csv

import UK_full_report.utils.case_definitions as case_def
import UK_full_report.utils.time_functions as time

def sort_key(obj):
    return obj.mrd
def sortkey2(taxon):
    return taxon.date_dt

def sort_on_taxa_len(obj):
    return len(obj.taxa)


def parse_metadata(metadata_file, sequencing_centre, filter_country, pillar_2):

    pillar_2s = ["ALDP", "QEUH", "MILK", "CAMC"]

    taxa_list = []
    tax_with_dates = []
    lineages = set()
    lineage_to_countries = defaultdict(list)
    lineage_object_dict = {}
    lineage_to_taxa = defaultdict(list)

    taxon_dictionary = {}
    lineage_int_list = []

    info_dict = defaultdict(list)

    pillar2_seqs = []
    pillar1_seqs = []

    country_specific_lineages = []
    country_specific_taxa = []
    specific_min = set()
    specific_max = set()
    specific_smalls = []
    specific_bigs = []

    omitted = []

    with open(metadata_file, "r") as f:
        data = csv.DictReader(f)
        for sequence in data:
            if sequence['country'] == "UK":
                seq_name = sequence['sequence_name']
                adm1 = sequence["adm1"]
                adm2 = sequence['adm2']
                date = sequence['sample_date']
                epiweek = sequence['epi_week']
                glob_lin = sequence['lineage']
                lineage_name = sequence['uk_lineage']

                extracted_sequencing_centre = sequence['sequencing_org_code']
                sub_date = sequence["sequencing_submission_date"]

                lineage_version = sequence["lineages_version"]

                info_dict[seq_name] = [date, epiweek, adm2, glob_lin, extracted_sequencing_centre]

                country_prep = adm1.split("-")[1]
                if country_prep == "ENG":
                    country = "England"
                elif country_prep == "WLS":
                    country = "Wales"
                elif country_prep == "SCT":
                    country = "Scotland"
                elif country_prep == "NIR":
                    country = "Northern_Ireland"

                if sequencing_centre is not None and sequencing_centre != "" and sequencing_centre != extracted_sequencing_centre:
                    continue

                pillar_2_seq = False
                for place in pillar_2s:
                    if place in seq_name:
                        pillar_2_seq = True
                
                try:
                    metadata = info_dict[seq_name]
                    new_taxon = case_def.taxon(seq_name, country, lineage_name, metadata, pillar_2_seq, sub_date)

                    taxon_dictionary[seq_name] = new_taxon

                    taxa_list.append(new_taxon)

                    if lineage_name != "":
                        lineages.add(lineage_name)
                        lineage_to_countries[lineage_name].append(country)
                        lineage_to_taxa[lineage_name].append(new_taxon)

                        lineage_int_list.append(int(lineage_name.lstrip("UK"))) #do we use this?

                    if new_taxon.date_dt != "NA":
                        tax_with_dates.append(new_taxon)

                    if pillar_2_seq:
                        pillar2_seqs.append(new_taxon)
                    else:
                        pillar1_seqs.append(new_taxon)

                except KeyError: #if it's not in metadata
                    omitted.append(seq_name)



    if sequencing_centre == "" and filter_country != "":
        specific_taxa = [i for i in tax_with_dates if i.country == filter_country]
        most_recent_sample = sorted(specific_taxa, key=sortkey2, reverse = True)[0].date_dt
    else:
        most_recent_sample = sorted(tax_with_dates, key=sortkey2, reverse = True)[0].date_dt

    lineage_int_list = sorted(lineage_int_list)

    all_lineages = []
    small_lineages = []
    big_lineages = []

    for lineage, taxa in lineage_to_taxa.items():

        lineage_object = case_def.lineage(lineage, taxa, most_recent_sample, filter_country, sequencing_centre)

        if len(lineage_object.taxa) > 5 and lineage_object.last_sampled < 28:
            big_lineages.append(lineage_object)
        else:
            small_lineages.append(lineage_object)

        all_lineages.append(lineage_object)

        lineage_object_dict[lineage] = lineage_object

    big_lineages = sorted(big_lineages, key=sort_on_taxa_len, reverse=False)

    specific_singletons = 0

    if sequencing_centre == "" and filter_country != "":

        for lineage in all_lineages:

            if len(lineage.country_specific_taxa) != 0:

                country_specific_lineages.append(lineage)

                for i in lineage.country_specific_taxa:
                    country_specific_taxa.append(i)

                if len(lineage.country_specific_taxa) == 1:
                    specific_singletons += 1
                if len(lineage.country_specific_taxa) > 5 and lineage.last_sampled < 28:
                    specific_bigs.append(lineage)
                else:
                    specific_smalls.append(lineage)


    return big_lineages, small_lineages, all_lineages, lineage_to_countries, lineage_object_dict, omitted, taxa_list, taxon_dictionary, most_recent_sample, lineage_int_list, lineage_version, country_specific_lineages, country_specific_taxa, specific_smalls, specific_bigs, specific_singletons, pillar1_seqs, pillar2_seqs
