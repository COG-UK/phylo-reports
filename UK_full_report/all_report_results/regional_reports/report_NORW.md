







# Lineages report for NORW




This report gives summaries of UK specific lineages sequenced by NORW for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-08-31. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1198 sequences in the UK from the sequencing centre NORW have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 8 and the maximum is 462


Sequences which were replicates or too error-prone were removed from this analysis.



108 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 6 that remain:
3 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
2 lineages have reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+-------------------------------------+----------+
| Lineage name   | England      | Date range     | Global lineage                      | Total    |
+================+==============+================+=====================================+==========+
| UK5            | 218 (100.0%) | Mar-24, Aug-08 | B.1.1, B.1.1.10                     | 218 taxa |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2913         | 116 (100.0%) | Mar-21, Jun-01 | B.1.11, B.1                         | 116 taxa |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK6            | 89 (100.0%)  | Apr-08, Jul-17 | B.1.75, B.1                         | 89 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK983          | 59 (100.0%)  | Apr-21, Aug-18 | B.1.5.5, B.1                        | 59 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1819         | 51 (100.0%)  | Apr-08, May-11 | B.1.1                               | 51 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK175          | 42 (100.0%)  | Mar-06, Aug-07 | B.1.11, B.1, B.1.5, B.1.88, B.1.105 | 42 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1645         | 36 (100.0%)  | Aug-25, Aug-31 | B.1.1.2, B.1.1.15, B.1.1, B.1.1.10  | 36 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK701          | 35 (100.0%)  | Apr-13, May-21 | B.1.1                               | 35 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1242         | 35 (100.0%)  | Apr-08, Jun-17 | B.1.1                               | 35 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5676         | 34 (100.0%)  | Mar-21, May-13 | B.2                                 | 34 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_NORW_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_NORW_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_NORW_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by NORW is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_NORW_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_NORW_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 131 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_NORW_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+-------------------------------------+----------+
| Lineage name   | England      | Date range     | Global lineage                      | Total    |
+================+==============+================+=====================================+==========+
| UK5            | 218 (100.0%) | Mar-24, Aug-08 | B.1.1, B.1.1.10                     | 218 taxa |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2913         | 116 (100.0%) | Mar-21, Jun-01 | B.1.11, B.1                         | 116 taxa |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK6            | 89 (100.0%)  | Apr-08, Jul-17 | B.1.75, B.1                         | 89 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK983          | 59 (100.0%)  | Apr-21, Aug-18 | B.1.5.5, B.1                        | 59 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1819         | 51 (100.0%)  | Apr-08, May-11 | B.1.1                               | 51 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK175          | 42 (100.0%)  | Mar-06, Aug-07 | B.1.11, B.1, B.1.5, B.1.88, B.1.105 | 42 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1645         | 36 (100.0%)  | Aug-25, Aug-31 | B.1.1.2, B.1.1.15, B.1.1, B.1.1.10  | 36 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK701          | 35 (100.0%)  | Apr-13, May-21 | B.1.1                               | 35 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1242         | 35 (100.0%)  | Apr-08, Jun-17 | B.1.1                               | 35 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5676         | 34 (100.0%)  | Mar-21, May-13 | B.2                                 | 34 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2014         | 29 (100.0%)  | Apr-08, Jun-03 | B.1.1                               | 29 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK712          | 27 (100.0%)  | Apr-08, Jun-18 | B.1.5                               | 27 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK336          | 22 (100.0%)  | Mar-24, May-21 | B.1                                 | 22 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1030         | 21 (100.0%)  | Apr-08, May-14 | B.1.5, B.1.5.5, B.1                 | 21 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2111         | 20 (100.0%)  | Apr-29, May-22 | B.1.1                               | 20 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK945          | 20 (100.0%)  | Apr-14, May-11 | B.1.1                               | 20 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1535         | 18 (100.0%)  | Apr-29, Jun-03 | B.1.1, B.1.1.3                      | 18 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1075         | 16 (100.0%)  | Apr-22, May-29 | B.1.1                               | 16 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK167          | 16 (100.0%)  | May-12, Jun-04 | B.1                                 | 16 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1279         | 15 (100.0%)  | Apr-08, May-08 | B.1.1                               | 15 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK173          | 14 (100.0%)  | Apr-13, May-19 | B.2, B, B.21                        | 14 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK415          | 11 (100.0%)  | Apr-19, May-06 | B.1.111                             | 11 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK72           | 11 (100.0%)  | Mar-22, May-26 | B.2, B                              | 11 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1205         | 11 (100.0%)  | Apr-29, Aug-03 | B.1.1.1                             | 11 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK568          | 11 (100.0%)  | Apr-11, May-02 | B.2                                 | 11 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK107          | 10 (100.0%)  | Mar-20, Jul-20 | B.2.1                               | 10 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK719          | 10 (100.0%)  | Apr-25, Jun-09 | B.1.1                               | 10 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1899         | 8 (100.0%)   | May-05, May-29 | B.1.1                               | 8 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK597          | 7 (100.0%)   | Apr-22, Aug-31 | B.1                                 | 7 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1060         | 7 (100.0%)   | Apr-20, May-14 | B.1.1                               | 7 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1683         | 7 (100.0%)   | Jul-16, Aug-08 | B.1.1.1                             | 7 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK199          | 6 (100.0%)   | Mar-23, May-08 | B.1.5, B.1                          | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1126         | 6 (100.0%)   | Apr-29, Jun-15 | B.1.1                               | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+

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


| Week commencing   |   UK5 |   UK983 |   UK175 |   UK1645 |   UK1683 |   UK597 |
|:------------------|------:|--------:|--------:|---------:|---------:|--------:|
| 2020-03-01        |     0 |       0 |       1 |        0 |        0 |       0 |
| 2020-03-22        |     2 |       0 |       1 |        0 |        0 |       0 |
| 2020-04-05        |     5 |       0 |       1 |        0 |        0 |       0 |
| 2020-04-12        |     4 |       0 |       3 |        0 |        0 |       0 |
| 2020-04-19        |     3 |       2 |       1 |        0 |        0 |       1 |
| 2020-04-26        |     5 |       2 |       3 |        0 |        0 |       0 |
| 2020-05-03        |     4 |       1 |       2 |        0 |        0 |       1 |
| 2020-05-10        |     4 |       2 |       0 |        0 |        0 |       1 |
| 2020-05-17        |     2 |       2 |       1 |        0 |        0 |       0 |
| 2020-05-24        |     1 |       2 |       0 |        0 |        0 |       1 |
| 2020-05-31        |     1 |       2 |       0 |        0 |        0 |       0 |
| 2020-06-07        |     0 |       0 |       1 |        0 |        0 |       0 |
| 2020-06-21        |     1 |       0 |       0 |        0 |        0 |       0 |
| 2020-06-28        |     1 |       1 |       2 |        0 |        0 |       0 |
| 2020-07-12        |     0 |       1 |       0 |        0 |        1 |       0 |
| 2020-07-26        |     1 |       0 |       1 |        0 |        1 |       0 |
| 2020-08-02        |     1 |       0 |       1 |        0 |        1 |       0 |
| 2020-08-16        |     0 |       1 |       0 |        0 |        0 |       0 |
| 2020-08-23        |     0 |       0 |       0 |        1 |        0 |       1 |
| 2020-08-30        |     0 |       0 |       0 |        1 |        0 |       1 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-06 |                            0 |                                1 |       1 |
| 2020-03-20 |                            1 |                                1 |       2 |
| 2020-03-21 |                            0 |                                2 |       2 |
| 2020-03-22 |                            0 |                                3 |       3 |
| 2020-03-23 |                            8 |                                1 |       9 |
| 2020-03-24 |                            0 |                                4 |       4 |
| 2020-04-08 |                           10 |                               12 |      22 |
| 2020-04-09 |                            3 |                                0 |       3 |
| 2020-04-11 |                            4 |                                2 |       6 |
| 2020-04-12 |                            4 |                                1 |       5 |
| 2020-04-13 |                            3 |                                2 |       5 |
| 2020-04-14 |                            1 |                                1 |       2 |
| 2020-04-15 |                            1 |                                0 |       1 |
| 2020-04-18 |                            3 |                                0 |       3 |
| 2020-04-19 |                            1 |                                1 |       2 |
| 2020-04-20 |                            0 |                                2 |       2 |
| 2020-04-21 |                            3 |                                1 |       4 |
| 2020-04-22 |                            1 |                                2 |       3 |
| 2020-04-23 |                            2 |                                1 |       3 |
| 2020-04-25 |                            0 |                                2 |       2 |
| 2020-04-26 |                            1 |                                0 |       1 |
| 2020-04-27 |                            1 |                                1 |       2 |
| 2020-04-28 |                            2 |                                1 |       3 |
| 2020-04-29 |                            1 |                                6 |       7 |
| 2020-04-30 |                            6 |                                1 |       7 |
| 2020-05-01 |                            2 |                                0 |       2 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-04 |                            1 |                                0 |       1 |
| 2020-05-05 |                            1 |                                2 |       3 |
| 2020-05-06 |                            2 |                                0 |       2 |
| 2020-05-11 |                            0 |                                1 |       1 |
| 2020-05-12 |                            1 |                                1 |       2 |
| 2020-05-13 |                            2 |                                0 |       2 |
| 2020-05-14 |                            0 |                                1 |       1 |
| 2020-05-16 |                            1 |                                0 |       1 |
| 2020-05-19 |                            2 |                                0 |       2 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |
| 2020-06-18 |                            1 |                                0 |       1 |
| 2020-07-04 |                            0 |                                1 |       1 |
| 2020-07-09 |                            1 |                                0 |       1 |
| 2020-07-13 |                            1 |                                1 |       2 |
| 2020-07-15 |                            3 |                                0 |       3 |
| 2020-07-16 |                            0 |                                1 |       1 |
| 2020-07-28 |                            0 |                                2 |       2 |
| 2020-08-01 |                            0 |                                1 |       1 |
| 2020-08-03 |                            0 |                                2 |       2 |
| 2020-08-07 |                            1 |                                0 |       1 |
| 2020-08-25 |                            0 |                                1 |       1 |
| 2020-08-31 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-06 |         1 |
| 2020-03-20 |         2 |
| 2020-03-21 |         2 |
| 2020-03-22 |         5 |
| 2020-03-23 |        16 |
| 2020-03-24 |        13 |
| 2020-03-25 |         2 |
| 2020-04-08 |        52 |
| 2020-04-09 |         9 |
| 2020-04-10 |         1 |
| 2020-04-11 |        31 |
| 2020-04-12 |        25 |
| 2020-04-13 |        22 |
| 2020-04-14 |        12 |
| 2020-04-15 |        18 |
| 2020-04-16 |        11 |
| 2020-04-17 |         8 |
| 2020-04-18 |        24 |
| 2020-04-19 |        20 |
| 2020-04-20 |        15 |
| 2020-04-21 |        16 |
| 2020-04-22 |        44 |
| 2020-04-23 |        29 |
| 2020-04-24 |        27 |
| 2020-04-25 |        15 |
| 2020-04-26 |        12 |
| 2020-04-27 |        18 |
| 2020-04-28 |        25 |
| 2020-04-29 |        52 |
| 2020-04-30 |        49 |
| 2020-05-01 |        35 |
| 2020-05-02 |        22 |
| 2020-05-03 |        39 |
| 2020-05-04 |        57 |
| 2020-05-05 |        40 |
| 2020-05-06 |        48 |
| 2020-05-07 |        17 |
| 2020-05-08 |        20 |
| 2020-05-09 |        12 |
| 2020-05-10 |        24 |
| 2020-05-11 |        22 |
| 2020-05-12 |        27 |
| 2020-05-13 |        16 |
| 2020-05-14 |         8 |
| 2020-05-15 |         1 |
| 2020-05-16 |         7 |
| 2020-05-17 |         9 |
| 2020-05-18 |         8 |
| 2020-05-19 |         6 |
| 2020-05-20 |         2 |
| 2020-05-21 |        15 |
| 2020-05-22 |         1 |
| 2020-05-23 |         3 |
| 2020-05-25 |         5 |
| 2020-05-26 |         5 |
| 2020-05-27 |         4 |
| 2020-05-28 |         8 |
| 2020-05-29 |         5 |
| 2020-05-30 |         1 |
| 2020-05-31 |         1 |
| 2020-06-01 |         8 |
| 2020-06-02 |         1 |
| 2020-06-03 |         2 |
| 2020-06-04 |         7 |
| 2020-06-05 |         3 |
| 2020-06-08 |         1 |
| 2020-06-09 |         3 |
| 2020-06-15 |         2 |
| 2020-06-17 |         5 |
| 2020-06-18 |        13 |
| 2020-06-23 |         1 |
| 2020-06-25 |         1 |
| 2020-06-28 |         2 |
| 2020-06-29 |         1 |
| 2020-07-03 |         1 |
| 2020-07-04 |         2 |
| 2020-07-07 |         1 |
| 2020-07-09 |         1 |
| 2020-07-13 |         3 |
| 2020-07-14 |         1 |
| 2020-07-15 |         3 |
| 2020-07-16 |         3 |
| 2020-07-17 |         2 |
| 2020-07-20 |         1 |
| 2020-07-27 |         2 |
| 2020-07-28 |        12 |
| 2020-07-31 |         1 |
| 2020-08-01 |         5 |
| 2020-08-03 |         5 |
| 2020-08-04 |         1 |
| 2020-08-05 |         4 |
| 2020-08-06 |         1 |
| 2020-08-07 |         7 |
| 2020-08-08 |         8 |
| 2020-08-18 |         1 |
| 2020-08-25 |        28 |
| 2020-08-31 |        11 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2             | Country   |   Number of sequences | Sequence group   |
|:-------------------|:----------|----------------------:|:-----------------|
| CAMBRIDGESHIRE     | England   |                    46 | 10-100           |
| CHESHIRE           | England   |                     1 | 1-10             |
| ESSEX              | England   |                    35 | 10-100           |
| GREATER LONDON     | England   |                     3 | 1-10             |
| GREATER MANCHESTER | England   |                     1 | 1-10             |
| HERTFORDSHIRE      | England   |                     1 | 1-10             |
| LINCOLNSHIRE       | England   |                    11 | 10-100           |
| NORFOLK            | England   |                   771 | 700-1000         |
| SUFFOLK            | England   |                   197 | 100-200          |
| WILTSHIRE          | England   |                     1 | 1-10             |

<div style="page-break-after: always"></div>






