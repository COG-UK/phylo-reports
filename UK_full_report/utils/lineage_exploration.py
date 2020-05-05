
from collections import Counter
from collections import defaultdict
import pandas as pd
from epiweeks import Week, Year
import UK_full_report.utils.case_definitions as case_def

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



        
    



