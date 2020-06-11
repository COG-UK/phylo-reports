







# Lineages report for NORW




This report gives summaries of UK specific lineages sequenced by NORW for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-21. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
758 sequences in the UK from the sequencing centre NORW have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 138 and the maximum is 178


Sequences which were replicates or too error-prone were removed from this analysis.



111 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 26 that remain:
6 are pending extinction, ie last seen three weeks ago.
7 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
12 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK200          | 76 (100.0%) | Apr-08, May-18 |                76 | B.1.p11          |                               3 | 0.1778           |
| UK6            | 57 (100.0%) | Apr-13, May-13 |                57 | B.1              |                               8 | 0.067            |
| UK199          | 57 (100.0%) | Apr-08, May-21 |                57 | B.1.5.5          |                               0 | active today     |
| UK204          | 56 (100.0%) | Apr-08, May-12 |                56 | B.1.1            |                               9 | 0.0687           |
| UK233          | 39 (100.0%) | Apr-08, May-21 |                39 | B.1.1            |                               0 | active today     |
| UK5660         | 33 (100.0%) | Apr-11, May-10 |                33 | B.1.1            |                              11 | 0.0824           |
| UK351          | 27 (100.0%) | Apr-13, May-21 |                27 | B.1.1.10, B.1.1  |                               0 | active today     |
| UK248          | 24 (100.0%) | Apr-08, May-16 |                24 | B.1.1            |                               5 | 0.3304           |
| UK214          | 23 (100.0%) | Apr-08, May-21 |                23 | B.1.1            |                               0 | active today     |
| UK36           | 20 (100.0%) | Apr-15, May-21 |                20 | B.1              |                               0 | active today     |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/NORW/figures/report_NORW_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 15 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/NORW/figures/report_NORW_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/NORW/figures/report_NORW_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/NORW/figures/report_NORW_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/NORW/figures/report_NORW_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 22 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/NORW/figures/report_NORW_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK200          | 76 (100.0%) | Apr-08, May-18 |                76 | B.1.p11          |                               3 | 0.1778           |
| UK6            | 57 (100.0%) | Apr-13, May-13 |                57 | B.1              |                               8 | 0.067            |
| UK199          | 57 (100.0%) | Apr-08, May-21 |                57 | B.1.5.5          |                               0 | active today     |
| UK204          | 56 (100.0%) | Apr-08, May-12 |                56 | B.1.1            |                               9 | 0.0687           |
| UK233          | 39 (100.0%) | Apr-08, May-21 |                39 | B.1.1            |                               0 | active today     |
| UK5660         | 33 (100.0%) | Apr-11, May-10 |                33 | B.1.1            |                              11 | 0.0824           |
| UK351          | 27 (100.0%) | Apr-13, May-21 |                27 | B.1.1.10, B.1.1  |                               0 | active today     |
| UK248          | 24 (100.0%) | Apr-08, May-16 |                24 | B.1.1            |                               5 | 0.3304           |
| UK214          | 23 (100.0%) | Apr-08, May-21 |                23 | B.1.1            |                               0 | active today     |
| UK36           | 20 (100.0%) | Apr-15, May-21 |                20 | B.1              |                               0 | active today     |
| UK5672         | 20 (100.0%) | Apr-19, May-13 |                20 | B.2              |                               8 | 0.1579           |
| UK3019         | 19 (100.0%) | Apr-08, May-07 |                19 | B.1              |                              14 | 0.1151           |
| UK135          | 18 (100.0%) | Apr-08, May-11 |                18 | B.1.p11          |                              10 | 0.1941           |
| UK278          | 14 (100.0%) | Apr-10, May-06 |                14 | B.1.1            |                              15 | 0.1333           |
| UK376          | 13 (100.0%) | Apr-08, May-08 |                13 | B.1.1            |                              13 | 0.1923           |
| UK5663         | 12 (100.0%) | Apr-11, May-02 |                12 | B.2              |                              19 | 0.1005           |
| UK147          | 12 (100.0%) | Apr-29, May-16 |                12 | B.1.1            |                               5 | 0.3091           |
| UK415          | 11 (100.0%) | Apr-19, May-06 |                11 | B.1              |                              15 | 0.1133           |
| UK125          | 10 (100.0%) | Apr-22, May-20 |                10 | B.1.1            |                               1 | 3.1111           |
| UK148          | 10 (100.0%) | Apr-12, May-13 |                10 | B.1.1            |                               8 | 0.4306           |
| UK91           | 9 (100.0%)  | Apr-14, May-06 |                 9 | B.1.1            |                              15 | 0.1833           |
| UK173          | 8 (100.0%)  | Apr-13, May-19 |                 8 | B                |                               2 | 2.5714           |
| UK28           | 8 (100.0%)  | Apr-13, May-01 |                 8 | B.1.1.10         |                              20 | 0.1286           |
| UK540          | 7 (100.0%)  | Apr-09, Apr-22 |                 7 | B.1.1.p15, B.1.1 |                              29 | 0.0747           |
| UK26           | 7 (100.0%)  | Apr-29, May-20 |                 7 | B.1.1.3          |                               1 | 3.5              |
| UK793          | 6 (100.0%)  | Apr-08, May-21 |                 6 | B.1, B.1.5       |                               0 | active today     |
| UK274          | 6 (100.0%)  | Apr-13, May-21 |                 6 | B.3              |                               0 | active today     |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NORW     |            15 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK200 |   UK6 |   UK199 |   UK204 |   UK233 |   UK5660 |   UK351 |   UK248 |   UK214 |   UK5672 |
|:------------------|--------:|------:|--------:|--------:|--------:|---------:|--------:|--------:|--------:|---------:|
| 2020-04-05        |       1 |     0 |       1 |       2 |       2 |        1 |       0 |       1 |       1 |        0 |
| 2020-04-12        |       1 |     2 |       3 |       2 |       2 |        1 |       1 |       0 |       1 |        0 |
| 2020-04-19        |       2 |     3 |       2 |       2 |       2 |        1 |       1 |       1 |       1 |        2 |
| 2020-04-26        |       3 |     4 |       2 |       3 |       2 |        1 |       3 |       2 |       1 |        3 |
| 2020-05-03        |       2 |     3 |       1 |       3 |       2 |        1 |       2 |       2 |       1 |        0 |
| 2020-05-10        |       1 |     1 |       1 |       1 |       1 |        1 |       3 |       2 |       1 |        2 |
| 2020-05-17        |       2 |     0 |       2 |       0 |       1 |        0 |       1 |       0 |       1 |        0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-04-08 |                           11 |                               15 |      26 |
| 2020-04-09 |                            4 |                                1 |       5 |
| 2020-04-10 |                            0 |                                1 |       1 |
| 2020-04-11 |                            7 |                                4 |      11 |
| 2020-04-12 |                            4 |                                1 |       5 |
| 2020-04-13 |                            4 |                                5 |       9 |
| 2020-04-14 |                            1 |                                2 |       3 |
| 2020-04-15 |                            1 |                                1 |       2 |
| 2020-04-16 |                            1 |                                0 |       1 |
| 2020-04-17 |                            1 |                                0 |       1 |
| 2020-04-18 |                            4 |                                0 |       4 |
| 2020-04-19 |                            1 |                                3 |       4 |
| 2020-04-20 |                            1 |                                2 |       3 |
| 2020-04-21 |                            5 |                                0 |       5 |
| 2020-04-22 |                            0 |                                1 |       1 |
| 2020-04-23 |                            2 |                                0 |       2 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-25 |                            2 |                                1 |       3 |
| 2020-04-26 |                            3 |                                0 |       3 |
| 2020-04-27 |                            3 |                                0 |       3 |
| 2020-04-28 |                            2 |                                1 |       3 |
| 2020-04-29 |                            1 |                                7 |       8 |
| 2020-04-30 |                            4 |                                3 |       7 |
| 2020-05-01 |                            3 |                                2 |       5 |
| 2020-05-03 |                            2 |                                0 |       2 |
| 2020-05-04 |                            1 |                                0 |       1 |
| 2020-05-05 |                            3 |                                0 |       3 |
| 2020-05-06 |                            4 |                                0 |       4 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-09 |                            2 |                                1 |       3 |
| 2020-05-11 |                            1 |                                1 |       2 |
| 2020-05-12 |                            2 |                                0 |       2 |
| 2020-05-13 |                            1 |                                1 |       2 |
| 2020-05-17 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-04-08 |        41 |
| 2020-04-09 |         6 |
| 2020-04-10 |         1 |
| 2020-04-11 |        25 |
| 2020-04-12 |        16 |
| 2020-04-13 |        20 |
| 2020-04-14 |        11 |
| 2020-04-15 |        15 |
| 2020-04-16 |        10 |
| 2020-04-17 |         8 |
| 2020-04-18 |        22 |
| 2020-04-19 |        19 |
| 2020-04-20 |        13 |
| 2020-04-21 |        14 |
| 2020-04-22 |        41 |
| 2020-04-23 |        23 |
| 2020-04-24 |         7 |
| 2020-04-25 |        12 |
| 2020-04-26 |        12 |
| 2020-04-27 |        14 |
| 2020-04-28 |        16 |
| 2020-04-29 |        42 |
| 2020-04-30 |        33 |
| 2020-05-01 |        30 |
| 2020-05-02 |        19 |
| 2020-05-03 |        29 |
| 2020-05-04 |        38 |
| 2020-05-05 |        25 |
| 2020-05-06 |        41 |
| 2020-05-07 |        14 |
| 2020-05-08 |        18 |
| 2020-05-09 |        12 |
| 2020-05-10 |        22 |
| 2020-05-11 |        20 |
| 2020-05-12 |        19 |
| 2020-05-13 |        11 |
| 2020-05-14 |         5 |
| 2020-05-16 |         4 |
| 2020-05-17 |         8 |
| 2020-05-18 |         7 |
| 2020-05-19 |         4 |
| 2020-05-20 |         3 |
| 2020-05-21 |         8 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2         | Country   |   Number of sequences | Sequence group   |
|:---------------|:----------|----------------------:|:-----------------|
| CAMBRIDGESHIRE | England   |                    34 | 10-50            |
| ESSEX          | England   |                    20 | 10-50            |
| GREATER LONDON | England   |                     2 | 1-10             |
| LINCOLNSHIRE   | England   |                    11 | 10-50            |
| MANCHESTER     | England   |                     1 | 1-10             |
| NORFOLK        | England   |                   541 | >500             |
| SUFFOLK        | England   |                   125 | 100-150          |
| WILTSHIRE      | England   |                     1 | 1-10             |

\pagebreak






