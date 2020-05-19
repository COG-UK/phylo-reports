
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



        
    



