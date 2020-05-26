
from collections import defaultdict 
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import datetime as dt
import matplotlib.font_manager as font_manager

def get_preliminary_info(intro_countries):

	singletons_count = 0
	smalls_count = 0
	for k,v in intro_countries.items():
		if len(v) == 1:
			singletons_count += 1
		if len(v) <=5 :
			smalls_count += 1

	return singletons_count, smalls_count


def prep_dicts(intro_countries):
	intro_total_numbers = {}

	intro_country_counts = defaultdict(dict)

	intro_country_percentages = defaultdict(dict)
	intro_country_together = defaultdict(dict)

	for key, value in intro_countries.items():
	

		total = len(value)
		
		intro_total_numbers[key] = total 
		
		counts = Counter(value)
		
		intro_country_counts[key] = counts 
		
		
		individual_freqs = {}
		individuals_together = defaultdict(tuple)
		
		for key2, value2 in counts.items():
			
			perc = round((value2/total)*100,2)
			
			individual_freqs[key2] = perc
			
			individuals_together[key2] = (str(value2), str(perc) + "%")
				
			
		intro_country_percentages[key] = individual_freqs 
		
		
		intro_country_together[key] = individuals_together

	return(intro_country_counts, intro_country_percentages, intro_country_together, intro_total_numbers)


def make_dataframe(intro_country_together, intro_total_numbers, intro_object_dict):

	#intro_country_together is a dict which has dicts of tuples as its values
	#Can add in extra columns of stuff by keying the dictionary that holds the lineage objects

	global_lins = []
	date_ranges = []
	last_sampled = []

	for key, value in intro_country_together.items():
		intro_object = intro_object_dict[key]
		global_lins.append(intro_object.global_lineages)
		
		if intro_object.dates != []:
			date_ranges.append((intro_object.pretty_oldest, intro_object.pretty_mrd))
			last_sampled.append(intro_object.last_sampled)
		else:
			date_ranges.append(('NA','NA'))
			last_sampled.append('NA')

	df_together_prep = pd.DataFrame(intro_country_together)
	df_together = df_together_prep.transpose()

	df_together.fillna(0, inplace=True, )

	totals = pd.Series(intro_total_numbers)

	df_together["Date range"] = date_ranges
	df_together["Total sequences"] = totals
	df_together["Global lineage"] = global_lins
	df_together["Time since last sample (days)"] = last_sampled

	non_country_list = ["Date range", "Total sequences", "Global lineage", "Time since last sample (days)"]

	df_together.sort_values(by=["Total sequences"], ascending=False, inplace=True)

	df_together = df_together[df_together["Total sequences"] > 5]
	
	countries = [i for i in df_together.columns if i not in non_country_list] 

	#Tidying
	new_lineages = []
	for i in df_together["Global lineage"]:
		new_lin = str(i).strip("{").strip("}").replace("'","")
		new_lineages.append(new_lin)
	df_together["Global lineage"] = new_lineages

	new_dates = []
	for i in df_together["Date range"]:
		new_date = str(i).strip("(").strip(")").replace("'","")
		new_dates.append(new_date)
	df_together["Date range"] = new_dates


	for country in countries:
		new_country = []
		for i in df_together[country]:
			c_spl = i
			if type(c_spl) == tuple:
				second_part = c_spl[1].strip("'").lstrip(" ").strip("'")
				new_second = "(" + second_part + ")"
				new_first = c_spl[0].strip("'")
			else:
				new_first = c_spl
				new_second = "(0%)"
				
			new = str(new_first) + " " + str(new_second)
			
			new_country.append(new)
		
    
		df_together[country] = new_country

	new_header_list = []
	for header in df_together.columns:
		if header == "northern_ireland":
			new = "Northern Ireland"
		else:
			new = header
		
		new_header_list.append(new)

	df_together.columns = new_header_list
	
	df_together.index.name = 'Lineage name'
	tree_order = list(df_together.index)

	return df_together, tree_order

def make_country_specific_dataframe(lineages, filter_country, most_recent_sample):

	global_lins = []
	date_ranges = []
	statuses = []
	last_sampled = []
	totals = []
	names = []
	
	df_dict = defaultdict(list)

	for lin in lineages:

		names.append(lin.id)
		
		new_dates = []
		total = 0

		for tax in lin.taxa:
			if tax.country = filter_country:
				total += 1
				global_lins.add(tax.global_lineage)
				if tax.date_dt != "NA":
					new_dates.append(tax.date_dt)
		
		totals.append(total)

		if new_dates != []:

			mrd = max(new_dates)
            oldest = min(new_dates)

			pretty_mrd = mrd.strftime('%b-%d')
            pretty_oldest = oldest.strftime('%b-%d')

			last_sampled = (most_recent_sample - mrd).days
			
			date_ranges.append((pretty_oldest, pretty_mrd))
			last_sampled.append(last_sampled)

		else:
			date_ranges.append(('NA','NA'))
			last_sampled.append('NA')


	df_dict["Lineage name"] = names	
	df_dict["Date range"] = date_ranges
	df_dict["Number of sequences"] = totals
	df_dict["Global lineage"] = global_lins
	df_dict["Time since last sample (days)"] = last_sampled

	df = pd.DataFrame(df_dict)

	df.fillna(0, inplace=True, )

	new_lineages = []
	for i in df["Global lineage"]:
		new_lin = str(i).strip("{").strip("}").replace("'","")
		new_lineages.append(new_lin)
	df["Global lineage"] = new_lineages

	new_dates = []
	for i in df["Date range"]:
		new_date = str(i).strip("(").strip(")").replace("'","")
		new_dates.append(new_date)
	df["Date range"] = new_dates

	df.index.name = 'Lineage name'
	tree_order = list(df_together.index)

	return df, tree_order


	





