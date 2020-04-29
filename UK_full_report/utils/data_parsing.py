
from collections import defaultdict 
from epiweeks import Week,Year
import os
import imp

case_def = imp.load_source("case_definitions", "utils/case_definitions.py")
time = imp.load_source("time_functions", "utils/time_functions.py")


def sort_key(obj):
    return obj.mrd
def sortkey2(taxon):
    return taxon.date_dt


def parse_metadata(metadata_file):

    info_dict = defaultdict(list)

    with open(metadata_file) as f:
        next(f)
        for l in f:
            toks = l.strip("\n").split(",")

            name = toks[8]
            adm2 = toks[11]
            date = toks[4]
            epiweek = toks[10]
            glob_lin = toks[13]


            info_dict[name] = [date, epiweek, adm2, glob_lin]

    return info_dict

def make_objects(input_dir, current_day, metadata_file):
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

    info_dict = parse_metadata(metadata_file)

    epiweeks = time.make_epiweeks()

    intros_to_taxa = defaultdict(list)

    for f in os.listdir(input_dir):
        if f != ".DS_Store" and f != "overall_trees" and f!= "alignments":
            lin_name = f 
            input_file = input_dir + f + "/traits.csv"

            with open(input_file) as f:
                next(f)
                for l in f:
                    toks = l.strip("\n").split(",")
                    if toks[1] == "UK": #this is in the traits.csv
                        count += 1
                        
                        seq_name = toks[0]
                        intro_name = toks[3]

                        acctrans = toks[4]

                        country = seq_name.split("/")[0].lower()

                        try:
                            metadata = info_dict[seq_name]
                            new = case_def.taxon(seq_name, country, intro_name, acctrans, metadata)

                            acctrans_to_seqs[acctrans].append(new)
                            taxon_dictionary[seq_name] = new
                            
                        #new.overall_lineage = toks[2]
                    
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
    
    current_week = Week.fromdate(most_recent_sample)

    introduction_int_list = sorted(introduction_int_list)

    #This should now all be done before the report
    # for tax in taxa_list: #Assigning taxa to lineages that hasn't been done in the tree
    #     if tax.introduction == "":
                
    #             possible_intro = acctrans_to_intro[tax.acctrans]
                
    #             if len(possible_intro) == 0: #this will be if the introduction is genuinely new
    #                 if tax.acctrans not in new_acctrans_to_lineage.keys():
                    
    #                     introduction_prep = (introduction_int_list[-1] + 1)
    #                     introduction = "UK" + str(introduction_prep)
    #                     introduction_int_list.append(introduction_prep)

    #                     new_acctrans_to_lineage[tax.acctrans] = introduction

    #                     tax.introduction = introduction
    #                     intros_to_taxa[introduction].append(tax)
    #                     intro_countries[introduction].append(tax.country)
    #                     intro_acctrans[introduction].add(tax.acctrans)
                    
    #                 else: #if it's not the sequence to be added to a new lineage

    #                     introduction = new_acctrans_to_lineage[tax.acctrans]

    #                     tax.introduction = introduction
    #                     intros_to_taxa[introduction].append(tax)
    #                     intro_countries[introduction].append(tax.country)
    #                     intro_acctrans[introduction].add(tax.acctrans)

    #             elif len(possible_intro) > 1: #usually a merged or split UK lineage
    #                 tax.unclear = True
    #                 unclear_taxa.append(tax)
                
    #             else: #if it just hasn't been labelled but it's clear it belongs to an existing lineage
    #                 introduction = list(possible_intro)[0]
                    
    #                 tax.introduction = introduction
    #                 intros_to_taxa[introduction].append(tax)
    #                 intro_countries[introduction].append(tax.country)
    #                 intro_acctrans[introduction].add(tax.acctrans)
                

    intro_alls = []
    intro_smalls = []
    intro_bigs = []

    for intro, taxa in intros_to_taxa.items():
        
        i_o = case_def.introduction(intro, taxa, most_recent_sample, current_week)
        #i_o.overall_lineage = taxa[0].overall_lineage
        i_o.acctrans_designations = intro_acctrans[i_o.id]

        if i_o.id in new_acctrans_to_lineage.values():
            i_o.new = True

        if len(i_o.acctrans_designations) > 1:
            i_o.split = True
        
        if len(i_o.taxa) <= 5:
            intro_smalls.append(i_o)
        else:
            intro_bigs.append(i_o)
        
        intro_alls.append(i_o)

        intro_object_dict[intro] = i_o

    intro_bigs = sorted(intro_bigs, key=sort_key, reverse=False)

    return intro_bigs, intro_smalls, intro_alls, count, intro_countries, intro_object_dict, omitted, taxa_list, new_acctrans_to_lineage, taxon_dictionary, most_recent_sample, introduction_int_list, unclear_taxa
