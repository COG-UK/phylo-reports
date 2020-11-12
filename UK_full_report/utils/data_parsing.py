
from collections import defaultdict
from epiweeks import Week,Year
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
    introductions = set()
    intro_countries = defaultdict(list)
    intro_object_dict = {}
    intro_acctrans = defaultdict(set)
    acctrans_to_intro = defaultdict(set)
    omitted = []
    acctrans_to_seqs = defaultdict(list)

    pillar2_seqs = []
    pillar1_seqs = []

    taxon_dictionary = {}
    introduction_int_list = []
    new_lineages = set()

    info_dict = defaultdict(list)

    epiweeks = time.make_epiweeks()

    intros_to_taxa = defaultdict(list)

    min_intros = set()
    max_intros = set()

    country_specific_lineages = []
    country_specific_taxa = []
    specific_min = set()
    specific_max = set()
    specific_smalls = []
    specific_bigs = []

    with open(metadata_file, "r") as f:
        reader = csv.DictReader(f)
        in_data = [r for r in reader]
        for sequence in in_data:
            if sequence['country'] == "UK":
                seq_name = sequence['sequence_name']
                adm1 = sequence["adm1"]
                adm2 = sequence['adm2']
                date = sequence['sample_date']
                epiweek = sequence['epi_week']
                glob_lin = sequence['lineage']
                intro_name = sequence['uk_lineage']
                #acctrans = sequence['acc_lineage'] #minimum number
                #del_intros = sequence['del_introduction'] #max number
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

                # if sequencing_centre == "" and filter_country != "":
                #     if country == filter_country:
                #         specific_min.add(acctrans)
                #         specific_max.add(del_intros)

                if sequencing_centre is not None and sequencing_centre != "" and sequencing_centre != extracted_sequencing_centre:
                    continue

                pillar_2_seq = False
                for place in pillar_2s:
                    if place in seq_name:
                        pillar_2_seq = True

                # min_intros.add(acctrans)
                # max_intros.add(del_intros)
                
                try:
                    metadata = info_dict[seq_name]
                    new = case_def.taxon(seq_name, country, intro_name, metadata, pillar_2_seq, sub_date)

                    # acctrans_to_seqs[acctrans].append(new)
                    taxon_dictionary[seq_name] = new

                    taxa_list.append(new)

                    if intro_name != "":
                        introductions.add(intro_name)
                        intro_countries[intro_name].append(country)
                        # intro_acctrans[intro_name].add(acctrans)
                        # acctrans_to_intro[acctrans].add(intro_name)
                        intros_to_taxa[intro_name].append(new)

                        introduction_int_list.append(int(intro_name.lstrip("UK")))

                    if new.date_dt != "NA":
                        tax_with_dates.append(new)

                    if pillar_2_seq:
                        pillar2_seqs.append(new)
                    else:
                        pillar1_seqs.append(new)

                except KeyError: #if it's not in metadata
                    omitted.append(seq_name)



    if sequencing_centre == "" and filter_country != "":
        specific_taxa = [i for i in tax_with_dates if i.country == filter_country]
        most_recent_sample = sorted(specific_taxa, key=sortkey2, reverse = True)[0].date_dt
    else:
        most_recent_sample = sorted(tax_with_dates, key=sortkey2, reverse = True)[0].date_dt

    introduction_int_list = sorted(introduction_int_list)

    intro_alls = []
    intro_smalls = []
    intro_bigs = []

    for intro, taxa in intros_to_taxa.items():

        i_o = case_def.introduction(intro, taxa, most_recent_sample, filter_country, sequencing_centre)
        i_o.acctrans_designations = intro_acctrans[i_o.id]

        if len(i_o.acctrans_designations) > 1:
            i_o.split = True

        if len(i_o.taxa) > 5 and i_o.last_sampled < 28:
            intro_bigs.append(i_o)
        else:
            intro_smalls.append(i_o)

        intro_alls.append(i_o)

        intro_object_dict[intro] = i_o

    intro_bigs = sorted(intro_bigs, key=sort_on_taxa_len, reverse=False)

    specific_singletons = 0

    if sequencing_centre == "" and filter_country != "":

        for intro in intro_alls:

            if len(intro.country_specific_taxa) != 0:

                country_specific_lineages.append(intro)

                for i in intro.country_specific_taxa:
                    country_specific_taxa.append(i)

                if len(intro.country_specific_taxa) == 1:
                    specific_singletons += 1
                if len(intro.country_specific_taxa) > 5 and intro.last_sampled < 28:
                    specific_bigs.append(intro)
                else:
                    specific_smalls.append(intro)


    return intro_bigs, intro_smalls, intro_alls, intro_countries, intro_object_dict, omitted, taxa_list, taxon_dictionary, most_recent_sample, introduction_int_list, lineage_version, country_specific_lineages, country_specific_taxa, specific_smalls, specific_bigs, specific_singletons, pillar1_seqs, pillar2_seqs
