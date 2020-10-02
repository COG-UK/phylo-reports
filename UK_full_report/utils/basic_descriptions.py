
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

	intro_country_counts = defaultdict(dict)

	intro_country_percentages = defaultdict(dict)
	intro_country_together = defaultdict(dict)

	for key, value in intro_countries.items():
	
		total = len(value)	
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

	return(intro_country_counts, intro_country_percentages, intro_country_together)


def make_dataframe(intro_country_together, intro_object_dict):

	#intro_country_together is a dict which has dicts of tuples as its values
	#Can add in extra columns of stuff by keying the dictionary that holds the lineage objects

	global_lins = []
	date_ranges = []
	last_sampled = []
	activity_scores = []
	totals = []

	for key, value in intro_country_together.items():
		intro_object = intro_object_dict[key]
		global_lins.append(intro_object.largest_global_lineages)
		totals.append(len(intro_object.taxa))
		
		if intro_object.dates != []:
			date_ranges.append((intro_object.pretty_oldest, intro_object.pretty_mrd))
			last_sampled.append(intro_object.last_sampled)
			activity_scores.append(intro_object.activity_score)

		else:
			date_ranges.append(('NA','NA'))
			last_sampled.append('NA')
			activity_scores.append("NA")

	df_together_prep = pd.DataFrame(intro_country_together)
	df_together = df_together_prep.transpose()

	df_together.fillna(0, inplace=True, )

	df_together["Date range"] = date_ranges
	df_together["Global lineage"] = global_lins
	df_together["Total"] = totals
	# df_together["Time since last sample"] = last_sampled
	#df_together["Activity score"] = activity_scores

	non_country_list = ["Date range", "Total", "Global lineage", "Time since last sample", "Activity score"]

	df_together.sort_values(by=["Total"], ascending=False, inplace=True)

	df_together = df_together[df_together["Total"] > 5]
	
	countries = [i for i in df_together.columns if i not in non_country_list] 

	#Tidying
	new_lineages = []
	for i in df_together["Global lineage"]:
		new_lin = str(i).strip("[").strip("]").replace("'","")
		new_lineages.append(new_lin)
	df_together["Global lineage"] = new_lineages

	new_dates = []
	for i in df_together["Date range"]:
		new_date = str(i).strip("(").strip(")").replace("'","")
		new_dates.append(new_date)
	df_together["Date range"] = new_dates

	new_totals = []
	for i in df_together["Total"]:
		new_total = str(i) + " taxa"
		new_totals.append(new_total)
	df_together["Total"] = new_totals

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
		if header == "Northern_Ireland":
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
	last_sampled_list = []
	totals = []
	names = []
	activity_scores = []
	
	df_dict = defaultdict(list)
	
	for lin in lineages:
		if len(lin.country_specific_taxa) > 5:

			names.append(lin.id)
			
			new_dates = []
			total = 0

			global_lineages = set()

			for tax in lin.country_specific_taxa:
				global_lineages.add(tax.global_lineage)
			
			totals.append(len(lin.country_specific_taxa))
			global_lins.append(global_lineages)

			if lin.country_specific_dates != []:

				oldest = min(lin.country_specific_dates)

				pretty_mrd = lin.mrd.strftime('%b-%d')
				pretty_oldest = oldest.strftime('%b-%d')
				
				date_ranges.append((pretty_oldest, pretty_mrd))
				last_sampled_list.append(str(lin.last_sampled) + " days")

				activity_scores.append(lin.activity_score)

			else:
				date_ranges.append(('NA','NA'))
				last_sampled_list.append('NA')


	df_dict["Lineage name"] = names	
	df_dict["Date range"] = date_ranges
	df_dict["Total"] = totals
	df_dict["Global lineage"] = global_lins
	df_dict["Time since last sample"] = last_sampled_list
	df_dict["Activity score"] = activity_scores

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

	df.set_index('Lineage name', inplace=True)
	df.sort_values(by=["Total"], ascending=False, inplace=True)


	new_totals = []
	for i in df["Total"]:
		new_total = str(i) + " taxa"
		new_totals.append(new_total)
	df["Total"] = new_totals


	tree_order = list(df.index)

	return df, tree_order


	





