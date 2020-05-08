import datetime as dt
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import os
from epiweeks import Week,Year
from UK_full_report.utils.time_functions import *

class taxon():
    
    def __init__(self, record_id, country, introduction, acctrans, metadata): #phylotype):
    
        self.id = record_id
        self.introduction = introduction
        #self.phylotype = phylotype
        self.country = country
        self.acctrans = acctrans

        if metadata[0] == "None":
            self.date = None
        else:
            self.date = metadata[0]

        self.adm2 = metadata[2]
        self.global_lineage = metadata[3]

        epiweek_prep = metadata[1]
        if epiweek_prep != "0" and epiweek_prep != "":
            self.epiweek = Week(2020, int(float(epiweek_prep)))
        elif epiweek_prep == "0":
            self.epiweek = Week(2019, 52)
        elif epiweek_prep == "":
            self.epiweek = None


        self.unclear = False

        
        if "/" in self.date:
            print("ERROR DATE FORMAT INCORRECT")
        #     self.date_dt = dateparser.parse(self.date,  settings={"DATE_ORDER":'DMY'}).date()
        #     date_bits = self.date.split("/")

        # date_bits = self.date.split("-")
        # self.date_dt = dateparser.parse(self.date).date()

        date_bits = self.date.split("-")

        if len(date_bits) == 3:
            self.date_dt = dt.date(int(date_bits[0]), int(date_bits[1]), int(date_bits[2]))
        else:
            self.date_dt = None

            
class introduction():
    
    def __init__(self, name, taxa, current_day, current_week):
        
        self.id = name
        self.new = False

        self.taxa = taxa
        self.global_lineages = set()

        self.acctrans_designations = set()
        
        self.dates = []
        self.epiweeks = []

        self.week_to_adm2 = defaultdict(set)
        self.adm2_to_week = defaultdict(set)
        
        self.locations = set()

        #self.weeks_to_locs = defaultdict(set)
        self.always_active = False
        self.newly_active = False
        self.pending = False
        self.extinct = False
        self.quiet = False

        self.split = False

        self.get_global_lineages()
        self.get_date_loc_info(current_day)
        self.define_status(current_week)

        self.mrd = None
        
        
    def get_date_loc_info(self, current_date):
       
        for tax in self.taxa:
            if tax.date_dt is None and tax.epiweek is None:
                self.dates.append(tax.date_dt)
                self.epiweeks.append(tax.epiweek)
                self.locations.add(tax.adm2)
                self.week_to_adm2[tax.epiweek].add(tax.adm2)
                self.adm2_to_week[tax.adm2].add(tax.adm2)

        self.epiweek_counts = Counter(self.epiweeks)
        self.date_counts = Counter(self.dates)
                
        if self.dates == []:
            #print(self.id)
            pass
        else:   
            self.mrd = max(self.dates)
            self.oldest = min(self.dates)
            
            self.pretty_mrd = self.mrd.strftime('%b-%d')
            self.pretty_oldest = self.oldest.strftime('%b-%d')

            self.length = (self.mrd - self.oldest).days

            self.last_sampled = (current_date - self.mrd).days

    def get_global_lineages(self):

        for tax in self.taxa:
            if tax.global_lineage != "":
                self.global_lineages.add(tax.global_lineage)
            
                    
        
    def define_status(self, current_week): 
    
        last_week = current_week - 1
        two_weeks_ago = current_week - 2
        last_two_weeks = [current_week-1, current_week-2]
        last_month = [current_week-1, current_week-2, current_week-3, current_week-4]

        int_list = []
        for k,v in self.epiweek_counts.items():
            if k in last_month:
                int_list.append(v)
        
        if self.epiweek_counts[current_week] != 0:
            if self.epiweek_counts[last_week] == 0:
                self.status = "Reactivated"
                self.newly_active = True

                count_list = list(self.epiweek_counts.values())

                self.latency_time = next((i for i, x in enumerate(count_list[1:]) if x), None) #in weeks
            
            else:
                self.status = "Continuing"
                self.always_active = True          

        else:
            if (self.epiweek_counts[last_week] == 0 and self.epiweek_counts[two_weeks_ago] != 0) or self.epiweek_counts[last_week] != 0: #not this week or last week, but week before
                self.status = "Gone quiet"
                self.quiet = True
            elif all([v==0 for v in int_list]):
                self.status = "Extinct"
                self.extinct = True
            else:
                self.status = "Pending extinction"
                self.pending = True

    
        if not self.status:
            print("failed to assign status to " + self.name) 

        
        
