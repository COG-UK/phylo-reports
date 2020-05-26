
# UK lineages summary report





```
---------------------------------------------------------------------------FileNotFoundError
Traceback (most recent call last)<ipython-input-1-a08674dfc154> in
<module>
     12 import matplotlib.font_manager as font_manager
     13
---> 14 font_list =
font_manager.fontManager.addfont("%s/utils/helveticaneue/HelveticaNeue.ttf"
% scripts_directory)
     15 #font_list =
font_manager.fontManager.addfont("%s/utils/helveticaneue/HelveticaNeueBD.ttf"
% scripts_directory)
     16
~/anaconda3/envs/report/lib/python3.7/site-
packages/matplotlib/font_manager.py in addfont(self, path)
   1011             self.afmlist.append(prop)
   1012         else:
-> 1013             font = ft2font.FT2Font(path)
   1014             prop = ttfFontProperty(font)
   1015             self.ttflist.append(prop)
FileNotFoundError: [Errno 2] No such file or directory:
'/utils/helveticaneue/HelveticaNeue.ttf'
```





---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-d65db0711c7b> in <module>
      6     country = adm1
      7 
----> 8 current_date = time.make_current_week(week)
      9 
     10 intro_bigs, intro_smalls, intro_alls, count, intro_countries, intro_object_dict, omitted, taxa, new_lineages, taxon_dictionary, most_recent_sample, intro_int_list, unclear_taxa, max_intros, min_intros, lineage_version = parse.parse_metadata(metadata_file, sequencing_centre)
NameError: name 'time' is not defined

A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-93f4230c2a9c> in <module>
----> 1 print("The minimum number of introductions is " + str(len(min_intros)) + " and the maximum is " + str(len(max_intros)))
NameError: name 'min_intros' is not defined


Sequences which were replicates or too error-prone were removed from this analysis.




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-7ae2d9734456> in <module>
----> 1 print(str(smalls_count) + " are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity")
NameError: name 'smalls_count' is not defined


Furthermore, those sequences which haven't been sampled in the last month are not shown.




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-03a98ff85906> in <module>
      1 #split = lin_exp.find_splits(intro_alls)
      2 
----> 3 status_counts, reactivated_lineages, continuining_lineages = lin_exp.describe_lineages(intro_bigs)
      4 
      5 reactivateds = status_counts["Reactivated"]
NameError: name 'lin_exp' is not defined


The following table contains information about lineages and the number of sequences in each country in the UK for each lineage, in reverse size order. 

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-a988cb68b99a> in <module>
----> 1 print("The global lineages are correct as of the data release on " + lineage_version)
NameError: name 'lineage_version' is not defined


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-b780b7c016d8> in <module>
----> 1 intro_country_counts, intro_country_percentages, intro_country_together, intro_total_numbers = descrip.prep_dicts(intro_countries)
      2 dataframe, tree_order = descrip.make_dataframe(intro_country_together, intro_total_numbers, intro_object_dict)
      3 
      4 print(dataframe.to_markdown())
NameError: name 'descrip' is not defined


These data is represented in the stacked bar chart below. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 


```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-72123db9f5ce> in
<module>
----> 1 df_counts, df_thinned, df_acctrans_counts =
dp.make_plotting_dfs(intro_country_counts, intro_object_dict)
      2
      3 dp.plot_bars(intro_bigs, country, sequencing_centre)
NameError: name 'dp' is not defined
```





![](./figures/report_GLAS_stacked_bars_by_country_1.png)\


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown below. 
The raw data for the plot is shown below it, with each column representing a lineage, and the number of admin2 regions it is present in in each week.



```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-865e61bd73ac> in
<module>
----> 1 y_dict, week_list = dp.prep_geog_data(intro_bigs)
      2 #dp.stacked_geog_plot(y_dict, week_list, False)
      3 dp.plot_ridge_plot(week_list, y_dict)
      4 raw_geog = dp.make_raw_data_geog_plot(y_dict, week_list)
NameError: name 'dp' is not defined
```





![](./figures/report_GLAS_geog_plot_1.png)\




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-1717bce85b42> in <module>
----> 1 print(raw_geog.to_markdown())
NameError: name 'raw_geog' is not defined


The date of first sequence in the cluster is shown below for every cluster with date information. 


```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-5f5882fbc34d> in
<module>
----> 1 multi, single = dp.plot_starts(intro_alls)
      2 starts_raw = dp.raw_data_starts(single, multi)
NameError: name 'dp' is not defined
```




![](./figures/report_GLAS_firsts_plot_1.png)\




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-790228b7bbcc> in <module>
----> 1 print(starts_raw.to_markdown())
NameError: name 'starts_raw' is not defined

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-ec0091bbc410> in
<module>
----> 1 days, E, S, W, NI = dp.plot_sequences_over_time(taxa, country,
sequencing_centre)
      2 raw_seqs_over_time = dp.raw_data_seqs_over_time(days, E, S, W,
NI)
NameError: name 'dp' is not defined
```




![](./figures/report_GLAS_seqs_over_time_1.png)\




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-11e54f6867d7> in <module>
----> 1 print(raw_seqs_over_time.to_markdown())
NameError: name 'raw_seqs_over_time' is not defined


These lineages are shown on the timeline below. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.





---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-16d34d8cc75c> in <module>
----> 1 dp.make_timeline(intro_bigs)
      2 timeline_df = dp.raw_data_timeline(intro_bigs)
NameError: name 'dp' is not defined




![](./figures/report_GLAS_make_timeline_1.png)\


The map below shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.




---------------------------------------------------------------------------AttributeError                            Traceback (most recent call last)<ipython-input-1-73106a6ad69f> in <module>
      5 input_geojsons = [uk_json, channels, NI_json]
      6 
----> 7 map_output = map.make_map(input_geojsons, adm2_cleaning_file, metadata_file, output_directory, week, sequencing_centre, country)
      8 
      9 if type(map_output) != bool:
AttributeError: type object 'map' has no attribute 'make_map'




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-d5bc9d6e0357> in <module>
----> 1 if not no_seqs:
      2     print("![](" + fd + "/" + name_stem + "_map_1.png)\\")
NameError: name 'no_seqs' is not defined




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-c74ab00544a5> in <module>
----> 1 if not no_seqs:
      2     print(mapping_data.to_markdown())
NameError: name 'no_seqs' is not defined





---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-a78b9358e45e> in <module>
----> 1 if not no_seqs:
      2     if new_uncleans:
      3         print("There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.")
NameError: name 'no_seqs' is not defined





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak












```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-4758bb6fa688> in
<module>
----> 1 writing.write_summary_files(output_directory, dataframe,
omitted, week, intro_alls, timeline_df)
NameError: name 'writing' is not defined
```


