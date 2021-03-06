import datetime as dt
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import os
from epiweeks import Week,Year
from UK_full_report.utils.time_functions import *
import numpy as np

class taxon():
    
    def __init__(self, record_id, country, lineage, metadata,pillar, sub_date):
    
        self.id = record_id
        self.lineage = lineage
        self.country = country
        self.pillar2 = pillar

        if metadata[0] == "None":
            self.date = "NA"
        else:
            date = metadata[0]

        self.adm2 = metadata[2]
        self.global_lineage = metadata[3]
        self.sequencing_centre = metadata[4]

        if metadata[1] != "":
            epiweek = int(metadata[1])
            if epiweek > 0 and epiweek < 54:
                self.epiweek = Week(2020, epiweek)
            elif epiweek >= 53:
                self.epiweek = Week(2021, epiweek - 53)
            elif epiweek == 0:
                self.epiweek = Week(2019, 52)
        else:
            self.epiweek = "NA"
        
        if "/" in date:
            print("ERROR DATE FORMAT INCORRECT")
        
        try:
            self.date_dt = dt.datetime.strptime(date, "%Y-%m-%d").date()
        except:
            self.date_dt = "NA"   
        try:
            self.sub_date = dt.datetime.strptime(sub_date, "%Y-%m-%d").date()
        except:
            self.sub_date = "NA"
            
class lineage():
    
    def __init__(self, name, taxa, current_day, filter_country, sequencing_centre):
        
        self.id = name

        self.taxa = taxa
        self.global_lineages = []
        self.largest_global_lineages = []
        
        self.dates = []
        self.epiweeks = []
        self.gaps = []

        self.week_to_adm2 = defaultdict(set)
        
        self.locations = set()
        self.adm1 = []

        self.always_active = False
        self.newly_active = False
        self.pending = False
        self.extinct = False
        self.quiet = False

        self.get_global_lineages()
        self.get_date_loc_info(current_day, filter_country, sequencing_centre)
        self.define_status(current_day)

        self.country_specific_taxa = []
        self.country_specific_dates = []

        if filter_country != "" and sequencing_centre == "":
            for tax in self.taxa:
                if tax.country == filter_country:
                    self.country_specific_taxa.append(tax)
                    if tax.date_dt != "NA":
                        self.country_specific_dates.append(tax.date_dt)
        
        
    def get_date_loc_info(self, current_date, filter_country, sequencing_centre):
       
        for tax in self.taxa:
            if tax.date_dt != "NA": #and tax.epiweek != "NA":
                if filter_country != "" and sequencing_centre == "":
                    if tax.country == filter_country:
                        self.week_to_adm2[tax.epiweek].add(tax.adm2)

                else:
                    self.week_to_adm2[tax.epiweek].add(tax.adm2)

                self.dates.append(tax.date_dt)
                self.epiweeks.append(tax.epiweek)
                self.locations.add(tax.adm2)
                self.adm1.append(tax.country)

        self.epiweek_counts = Counter(self.epiweeks)
        self.date_counts = Counter(self.dates)
                
        if self.dates == []:
            pass
        else:   
            self.mrd = max(self.dates)
            self.oldest = min(self.dates)
            
            self.pretty_mrd = self.mrd.strftime('%b-%d')
            self.pretty_oldest = self.oldest.strftime('%b-%d')

            self.length = (self.mrd - self.oldest).days

            #This section deals with if sc's or adm1 don't contain the most recent sample in the lineage
            if self.mrd <= current_date:
                self.mrd = self.mrd
            else:
                self.mrd = min(self.dates)
                for d in self.dates:
                    if d <= current_date and d > self.mrd:
                        self.mrd=d
            
            self.last_sampled = (current_date - self.mrd).days

            self.define_activity_level()

    def define_activity_level(self):

        self.sorted_dates = sorted(self.dates)
        
        for index, date in enumerate(self.sorted_dates):
            
            if index > 0:
            
                gap = (date - self.sorted_dates[index-1]).days
                
                self.gaps.append(gap)
                
                
        self.average_gap = np.mean(self.gaps)

        if self.last_sampled != 0:
            self.activity_score = str((self.average_gap/self.last_sampled).round(4))
        else:
            self.activity_score = "active today"
        
    def get_global_lineages(self):

        for tax in self.taxa:
            if tax.global_lineage != "":
                self.global_lineages.append(tax.global_lineage)

        global_counts = Counter(self.global_lineages)

        total = len(self.global_lineages)

        most_common_counts = global_counts.most_common(3)

        for i in most_common_counts:
            lin = i[0]
            count = i[1]
            percentage = round((count/total)*100,2)
            pretty_percentage = " (" + str(percentage) + "%) "

            self.largest_global_lineages.append(lin + pretty_percentage)
                    
        
    def define_status(self, current_date): 
    
        if self.last_sampled < 7:
            for tax in self.taxa:
                date_diff = (current_date - tax.date_dt).days
                if date_diff > 7 and date_diff < 14:
                    self.status = "Continuing"
                    break
                else:
                    self.status = "Reactivated"
            
        elif self.last_sampled >= 7 and self.last_sampled < 14:
            self.status = "Gone quiet" 
        elif self.last_sampled >= 14 and self.last_sampled < 28:
            self.status = "Pending extinction"
        elif self.last_sampled >=28:
            self.status="Extinct"

        if not self.status:
            print("failed to assign status to " + self.name) 

        
        
