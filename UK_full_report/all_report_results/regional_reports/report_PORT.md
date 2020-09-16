







# Lineages report for PORT




This report gives summaries of UK specific lineages sequenced by PORT for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-08-18. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
665 sequences in the UK from the sequencing centre PORT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 5 and the maximum is 263


Sequences which were replicates or too error-prone were removed from this analysis.



85 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 1 that remain:
1 has reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+------------------+----------+
| Lineage name   | England      | Date range     | Global lineage   | Total    |
+================+==============+================+==================+==========+
| UK5            | 115 (100.0%) | Mar-21, Aug-18 | B.1.1.10, B.1.1  | 115 taxa |
+----------------+--------------+----------------+------------------+----------+
| UK107          | 86 (100.0%)  | Mar-17, Jun-08 | B.2.1            | 86 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK928          | 50 (100.0%)  | Mar-20, May-09 | B.1.1            | 50 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1278         | 46 (100.0%)  | Mar-24, May-29 | B.1.1            | 46 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2464         | 37 (100.0%)  | Mar-18, May-27 | B.1              | 37 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK218          | 29 (100.0%)  | Mar-21, Jun-02 | B.1              | 29 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2068         | 28 (100.0%)  | Mar-28, May-05 | B.1.1.4, B.1.1   | 28 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1219         | 19 (100.0%)  | Apr-01, May-14 | B.1.1            | 19 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2045         | 18 (100.0%)  | Apr-03, May-09 | B.1              | 18 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK738          | 15 (100.0%)  | Mar-18, Jun-07 | B.1.1            | 15 taxa  |
+----------------+--------------+----------------+------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_PORT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-2620455843ef> in
<module>
      2     lag_dict, lags = dp.sequencing_centre_lags(taxa, sc_dict,
current_date, country)
      3 elif sequencing_centre != "":
----> 4     print("The lag for this sequencing centre is " +
str(lags[sequencing_centre]) + " days")
NameError: name 'lags' is not defined
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](figures/report_PORT_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_PORT_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by PORT is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_PORT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_PORT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 213 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_PORT_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+------------------+----------+
| Lineage name   | England      | Date range     | Global lineage   | Total    |
+================+==============+================+==================+==========+
| UK5            | 115 (100.0%) | Mar-21, Aug-18 | B.1.1.10, B.1.1  | 115 taxa |
+----------------+--------------+----------------+------------------+----------+
| UK107          | 86 (100.0%)  | Mar-17, Jun-08 | B.2.1            | 86 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK928          | 50 (100.0%)  | Mar-20, May-09 | B.1.1            | 50 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1278         | 46 (100.0%)  | Mar-24, May-29 | B.1.1            | 46 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2464         | 37 (100.0%)  | Mar-18, May-27 | B.1              | 37 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK218          | 29 (100.0%)  | Mar-21, Jun-02 | B.1              | 29 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2068         | 28 (100.0%)  | Mar-28, May-05 | B.1.1.4, B.1.1   | 28 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1219         | 19 (100.0%)  | Apr-01, May-14 | B.1.1            | 19 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2045         | 18 (100.0%)  | Apr-03, May-09 | B.1              | 18 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK738          | 15 (100.0%)  | Mar-18, Jun-07 | B.1.1            | 15 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2039         | 14 (100.0%)  | Mar-31, Jun-09 | B.1.1            | 14 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK387          | 12 (100.0%)  | Mar-21, May-01 | B.1              | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1126         | 12 (100.0%)  | Mar-23, Apr-22 | B.1.1            | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1060         | 12 (100.0%)  | Mar-20, May-17 | B.1.1            | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK167          | 11 (100.0%)  | Mar-20, May-31 | B.1              | 11 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1559         | 9 (100.0%)   | Mar-20, Apr-23 | B.1.11           | 9 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK72           | 7 (100.0%)   | Mar-17, Apr-02 | B.2, B           | 7 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK1951         | 7 (100.0%)   | Mar-25, Apr-25 | B.1.1.1, B.1.1   | 7 taxa   |
+----------------+--------------+----------------+------------------+----------+

<div style="page-break-after: always"></div>

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre



---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-9cc5d2177dab> in <module>
      1 if not pillar2:
----> 2     lag_df = pd.DataFrame(lag_dict)
      3     print(lag_df.to_markdown())
      4 else:
      5     print("Table S2 is not appropriate for this report and so has been omitted.")
NameError: name 'lag_dict' is not defined

<div style="page-break-after: always"></div>

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |
|:------------------|------:|
| 2020-03-15        |     1 |
| 2020-03-22        |     2 |
| 2020-03-29        |     3 |
| 2020-04-05        |     4 |
| 2020-04-12        |     4 |
| 2020-04-19        |     3 |
| 2020-04-26        |     2 |
| 2020-05-03        |     2 |
| 2020-05-10        |     1 |
| 2020-05-17        |     1 |
| 2020-05-31        |     1 |
| 2020-08-16        |     1 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-17 |                            0 |                                3 |       3 |
| 2020-03-18 |                            1 |                                2 |       3 |
| 2020-03-19 |                            1 |                                2 |       3 |
| 2020-03-20 |                            0 |                                4 |       4 |
| 2020-03-21 |                            0 |                                4 |       4 |
| 2020-03-22 |                            0 |                                1 |       1 |
| 2020-03-23 |                            0 |                                2 |       2 |
| 2020-03-24 |                            0 |                                1 |       1 |
| 2020-03-25 |                            2 |                                2 |       4 |
| 2020-03-26 |                            1 |                                0 |       1 |
| 2020-03-27 |                            1 |                                1 |       2 |
| 2020-03-28 |                            1 |                                2 |       3 |
| 2020-03-30 |                            0 |                                1 |       1 |
| 2020-03-31 |                            1 |                                3 |       4 |
| 2020-04-01 |                            0 |                                3 |       3 |
| 2020-04-02 |                            7 |                                1 |       8 |
| 2020-04-03 |                            4 |                                2 |       6 |
| 2020-04-04 |                            3 |                                2 |       5 |
| 2020-04-05 |                            2 |                                0 |       2 |
| 2020-04-06 |                            1 |                                1 |       2 |
| 2020-04-07 |                            1 |                                0 |       1 |
| 2020-04-10 |                            3 |                                1 |       4 |
| 2020-04-11 |                            3 |                                0 |       3 |
| 2020-04-12 |                            1 |                                1 |       2 |
| 2020-04-13 |                            0 |                                1 |       1 |
| 2020-04-15 |                            1 |                                1 |       2 |
| 2020-04-16 |                            2 |                                0 |       2 |
| 2020-04-17 |                            3 |                                1 |       4 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-21 |                            0 |                                2 |       2 |
| 2020-04-22 |                            0 |                                1 |       1 |
| 2020-04-23 |                            2 |                                0 |       2 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-04-26 |                            0 |                                1 |       1 |
| 2020-04-28 |                            1 |                                0 |       1 |
| 2020-05-01 |                            2 |                                0 |       2 |
| 2020-05-02 |                            1 |                                0 |       1 |
| 2020-05-05 |                            1 |                                0 |       1 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-09 |                            1 |                                0 |       1 |
| 2020-05-11 |                            1 |                                0 |       1 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |
| 2020-08-18 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-17 |         4 |
| 2020-03-18 |         9 |
| 2020-03-19 |        11 |
| 2020-03-20 |        10 |
| 2020-03-21 |         7 |
| 2020-03-22 |        11 |
| 2020-03-23 |        13 |
| 2020-03-24 |         9 |
| 2020-03-25 |        18 |
| 2020-03-26 |        12 |
| 2020-03-27 |         6 |
| 2020-03-28 |         9 |
| 2020-03-30 |        15 |
| 2020-03-31 |        19 |
| 2020-04-01 |        13 |
| 2020-04-02 |        23 |
| 2020-04-03 |        21 |
| 2020-04-04 |        17 |
| 2020-04-05 |        14 |
| 2020-04-06 |        20 |
| 2020-04-07 |         9 |
| 2020-04-08 |         1 |
| 2020-04-09 |         2 |
| 2020-04-10 |        15 |
| 2020-04-11 |        16 |
| 2020-04-12 |        10 |
| 2020-04-13 |        12 |
| 2020-04-14 |        13 |
| 2020-04-15 |        22 |
| 2020-04-16 |         5 |
| 2020-04-17 |        17 |
| 2020-04-18 |         7 |
| 2020-04-19 |         6 |
| 2020-04-20 |        10 |
| 2020-04-21 |        27 |
| 2020-04-22 |        22 |
| 2020-04-23 |        22 |
| 2020-04-24 |        17 |
| 2020-04-25 |         6 |
| 2020-04-26 |         6 |
| 2020-04-27 |        19 |
| 2020-04-28 |        11 |
| 2020-04-29 |         6 |
| 2020-04-30 |         5 |
| 2020-05-01 |        14 |
| 2020-05-02 |         5 |
| 2020-05-03 |         2 |
| 2020-05-04 |         4 |
| 2020-05-05 |         8 |
| 2020-05-06 |         8 |
| 2020-05-07 |         8 |
| 2020-05-08 |         4 |
| 2020-05-09 |         3 |
| 2020-05-10 |         1 |
| 2020-05-11 |         1 |
| 2020-05-12 |        10 |
| 2020-05-13 |         1 |
| 2020-05-14 |         3 |
| 2020-05-15 |        10 |
| 2020-05-16 |         1 |
| 2020-05-17 |         2 |
| 2020-05-18 |         1 |
| 2020-05-19 |         1 |
| 2020-05-20 |         2 |
| 2020-05-21 |         1 |
| 2020-05-22 |         1 |
| 2020-05-25 |         3 |
| 2020-05-27 |         1 |
| 2020-05-28 |         1 |
| 2020-05-29 |         2 |
| 2020-05-30 |         2 |
| 2020-05-31 |         2 |
| 2020-06-02 |         2 |
| 2020-06-05 |         1 |
| 2020-06-06 |         1 |
| 2020-06-07 |         1 |
| 2020-06-08 |         2 |
| 2020-06-09 |         2 |
| 2020-07-22 |         1 |
| 2020-07-24 |         3 |
| 2020-08-05 |         1 |
| 2020-08-18 |         2 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2            | Country   |   Number of sequences | Sequence group   |
|:------------------|:----------|----------------------:|:-----------------|
| BRIGHTON AND HOVE | England   |                    18 | 10-100           |
| HAMPSHIRE         | England   |                   432 | 400-500          |
| SURREY            | England   |                     2 | 1-10             |

<div style="page-break-after: always"></div>






