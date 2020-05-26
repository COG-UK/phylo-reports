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
            self.date = "NA"
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
            self.epiweek = "NA"


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
            self.date_dt = "NA"

            
class introduction():
    
    def __init__(self, name, taxa, current_day, filter_country, sequencing_centre):
        
        self.id = name
        self.new = False

        self.taxa = taxa
        self.global_lineages = set()

        self.acctrans_designations = set()
        
        self.dates = []
        self.epiweeks = []

        self.week_to_adm2 = defaultdict(set)
        #self.adm2_to_week = defaultdict(set)
        
        self.locations = set()
        self.adm1 = []

        #self.weeks_to_locs = defaultdict(set)
        self.always_active = False
        self.newly_active = False
        self.pending = False
        self.extinct = False
        self.quiet = False

        self.split = False

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
                #self.adm2_to_week[tax.adm2].add(tax.adm2)
                self.adm1.append(tax.country)

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

        
        
