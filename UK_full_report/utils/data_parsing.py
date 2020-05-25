
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


def parse_metadata(metadata_file, sequencing_centre):
    count = 0
    taxa_list = []
    tax_with_dates = []
    introductions = set()
    intro_countries = defaultdict(list)
    intro_object_dict = {}
    intro_acctrans = defaultdict(set)
    acctrans_to_intro = defaultdict(set)
    omitted = []
    acctrans_to_seqs = defaultdict(list)
    new_acctrans_to_lineage = {}

    unclear_taxa = []

    taxon_dictionary = {}
    introduction_int_list = []
    new_lineages = set()

    info_dict = defaultdict(list)

    epiweeks = time.make_epiweeks()

    intros_to_taxa = defaultdict(list)

    min_intros = set()
    max_intros = set()

    with open(metadata_file, "r") as f:
        reader = csv.DictReader(f)
        in_data = [r for r in reader]
        for sequence in in_data:
            if sequence['country'] == "UK":
                count += 1
                seq_name = sequence['sequence_name']
                adm1 = sequence["adm1"]
                adm2 = sequence['adm2']
                date = sequence['sample_date']
                epiweek = sequence['epi_week']
                glob_lin = sequence['lineage']
                intro_name = sequence['uk_lineage']
                acctrans = sequence['acc_lineage'] #also going to be min number of intros
                del_intros = sequence['del_introduction'] #max number - NEED TO CHANGE THIS FOR NEW RUN
                extracted_sequencing_centre = sequence['sequencing_org_code']
                #extracted_sequencing_centre = sequence["sequence_name"].split("/")[1].split("-")[0]

                min_intros.add(acctrans)
                max_intros.add(del_intros)

                lineage_version = sequence["lineages_version"] 
            
                info_dict[seq_name] = [date, epiweek, adm2, glob_lin]

                # country = seq_name.split("/")[0].lower()
                country_prep = adm1.split("-")[1]
                if country_prep == "ENG":
                    country = "england"
                elif country_prep == "WLS":
                    country = "wales"
                elif country_prep == "SCT":
                    country = "scotland"
                elif country_prep == "NIR":
                    country = "northern_ireland"
                
                if sequencing_centre is not None and sequencing_centre != "" and sequencing_centre != extracted_sequencing_centre:
                    continue

                try:
                    metadata = info_dict[seq_name]
                    new = case_def.taxon(seq_name, country, intro_name, acctrans, metadata)

                    acctrans_to_seqs[acctrans].append(new)
                    taxon_dictionary[seq_name] = new
            
                    taxa_list.append(new)

                    if intro_name != "":
                        introductions.add(intro_name)
                        intro_countries[intro_name].append(country)
                        intro_acctrans[intro_name].add(acctrans)
                        acctrans_to_intro[acctrans].add(intro_name)
                        intros_to_taxa[intro_name].append(new)

                        introduction_int_list.append(int(intro_name.lstrip("UK")))

                    if new.date_dt != "NA":
                        tax_with_dates.append(new)

                except KeyError: #if it's not in metadata
                    omitted.append(seq_name)


    most_recent_sample = sorted(tax_with_dates, key=sortkey2, reverse = True)[0].date_dt
    
    introduction_int_list = sorted(introduction_int_list)

    intro_alls = []
    intro_smalls = []
    intro_bigs = []

    for intro, taxa in intros_to_taxa.items():
        
        i_o = case_def.introduction(intro, taxa, most_recent_sample)
        #i_o.overall_lineage = taxa[0].overall_lineage
        i_o.acctrans_designations = intro_acctrans[i_o.id]

        if len(i_o.acctrans_designations) > 1:
            i_o.split = True
        
        if len(i_o.taxa) > 5 and i_o.last_sampled < 28:
            intro_bigs.append(i_o)
        else:
            intro_smalls.append(i_o)
        
        intro_alls.append(i_o)

        intro_object_dict[intro] = i_o

    intro_bigs = sorted(intro_bigs, key=sort_key, reverse=False)

    return intro_bigs, intro_smalls, intro_alls, count, intro_countries, intro_object_dict, omitted, taxa_list, new_acctrans_to_lineage, taxon_dictionary, most_recent_sample, introduction_int_list, unclear_taxa, max_intros, min_intros, lineage_version
