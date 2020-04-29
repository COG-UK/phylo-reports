
from collections import Counter
from collections import defaultdict
import pandas as pd
from epiweeks import Week, Year
import imp

case_def = imp.load_source('case_definitions ', 'utils/case_definitions.py')

def find_merged(lineage_objects):

    acctran_dict = defaultdict(list)
    acctran_to_merge = defaultdict(list)
    merged = {}
    merge_count = 0
    skip_list = []

    for lin in lineage_objects:         
        for i in lin.acctrans_designations: #should be only one
            acctran_dict[i].append(lin)
           
    for key, value in acctran_dict.items():
        if key not in skip_list:
            if len(value) > 1:
                for i in value:
                    merged[i.id] = True
                    merge_count += 1
                    if i not in acctran_to_merge[key]:
                        acctran_to_merge[key].append(i)

                    if i.split:
                        others = []
                        for j in i.acctrans_designations:
                            skip_list.append(j)
                            for k in acctran_dict[j]:
                                if k not in others and k not in acctran_to_merge[key]:
                                    others.append(k) #get the other lineages that need to go in
                        
                        acctran_to_merge[key].extend(others)
            else:
                if not i.split:
                    for i in value: #there will be one
                        merged[i.id] = False
        else:
            pass

    return merged, acctran_dict, acctran_to_merge, merge_count

def find_splits(lineage_objects):
    splits = []
    for i in lineage_objects:
        if i.split:
            splits.append(i)

    return splits

def describe_lineages(lineage_objects):

    statuses = []
    reactivated_lineages = []
    continuing_lineages = []
    unclear = []

    for lin in lineage_objects:
        statuses.append(lin.status)
        if lin.status == "Reactivated":
            reactivated_lineages.append(lin)
        elif lin.status == "Continuing":
            continuing_lineages.append(lin)
        
    status_counts = Counter(statuses)

    return status_counts, reactivated_lineages, continuing_lineages

def deal_with_merged(acctran_to_merge, lineage_object_dict, unclear_taxa, most_recent_sample, intro_alls, intro_bigs, intro_smalls, intro_countries):

    current_week = Week.fromdate(most_recent_sample)

    remove_list = []
    merged_dict = defaultdict(list)
    keep_ids = []

    for acctran, lineages in acctran_to_merge.items():

        taxa = []
        numbers = []
        for_df = []
    
        for lin in lineages:
            taxa.extend(lin.taxa)
            remove_list.append(lin)
            for_df.append(lin.id)
            numbers.append(int(lin.id.lstrip("UK")))

        test_taxa = set(taxa)
        if len(test_taxa) != len(taxa):
            print("error in merging" + str(lineages) + " " + str(len(test_taxa)) + " " + str(len(taxa)))
        

        new_uk = "UK" + str(min(numbers))
        keep_ids.append(new_uk)

        for tax in unclear_taxa:
            if tax.acctrans == acctran:
                tax.introduction = new_uk
                taxa.append(tax)

        
        merged_dict["New lineage"].append(new_uk)
        merged_dict["Old lineages"].append(for_df)

        i_o = case_def.introduction(new_uk, taxa, most_recent_sample, current_week)
        i_o.acctrans_designations = acctran

        for tax in i_o.taxa:
            intro_countries[i_o.id].append(tax.country)

        lineage_object_dict[i_o.id] = i_o      
        

        intro_alls.append(i_o)

        if len(taxa) > 5:
            intro_bigs.append(i_o)
        else:
            intro_smalls.append(i_o)

    for i in remove_list:
        if i in intro_bigs:
            intro_bigs.remove(i)
        elif i in intro_smalls:
            intro_smalls.remove(i)

        if i in intro_alls:
            intro_alls.remove(i)

        if i.id in intro_countries.keys() and i.id not in keep_ids:
            del intro_countries[i.id]

    return lineage_object_dict, intro_alls, intro_bigs, intro_smalls, intro_countries, merged_dict

def make_merged_df(merged_dict):

    df = pd.DataFrame(merged_dict)
    df.set_index("New lineage", inplace=True)

    new_lines = []

    for i in df["Old lineages"]:
        new = str(i).strip("[").strip("]").replace("'","")
        new_lines.append(new)
    df["Old lineages"] = new_lines

    return df


def find_new_countries(lineage): #This function isn't working 

    #I now have the appropriate dictionaries so should be ok

    new_countries = set()

    #this will actually have to change around a decent amount

    last_date = lineage.date_set[1] #these will change to epi weeks rather than single days
    mrd = lineage.date_set[0]

    #add a week to location dict - probably after the date to week

    old_locs = lineage.date_to_country[last_date]
    now_locs = lineage.date_to_country[mrd]

    for loc in now_locs:
        if loc not in old_locs:
            new_countries.add(loc)
    
    if len(new_countries) > 0:
        return new_countries
    else:
        return False 

def circulating_info(lineages): #that all needs to change

    new_country_dict = defaultdict(set)
    current_countries = defaultdict(set)

    for lin in lineages:
        new_countries = find_new_countries(lin)
        if new_countries:
            new_country_dict[lin] = new_countries

        mrd = lin.date_set[0]

        current_countries[lin] = lin.date_to_country[mrd] #this also isn't working, but it' because it's a date not an epi week, so we can just fix that

    return new_country_dict, current_countries



        
    



