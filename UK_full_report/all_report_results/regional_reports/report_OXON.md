







# Lineages report for OXON




This report gives summaries of UK specific lineages sequenced by OXON for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-19. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
780 sequences in the UK from the sequencing centre OXON have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 82 and the maximum is 323


Sequences which were replicates or too error-prone were removed from this analysis.



75 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 12 that remain:
9 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage                   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:---------------------------------|--------------------------------:|:-----------------|
| UK5            | 450 (100.0%) | Mar-17, May-14 |               450 | B.1.1.4, B.1.1.1, B.1.1, B.1.1.2 |                               5 | 0.0258           |
| UK109          | 17 (100.0%)  | Apr-07, May-06 |                17 | B.1.5                            |                              13 | 0.1394           |
| UK376          | 16 (100.0%)  | Apr-05, May-03 |                16 | B.1.1.9                          |                              16 | 0.1167           |
| UK370          | 15 (100.0%)  | Apr-04, Apr-27 |                15 | B.1.1.10                         |                              22 | 0.0747           |
| UK107          | 13 (100.0%)  | Mar-28, Apr-16 |                13 | B.2.1                            |                              33 | 0.048            |
| UK42           | 12 (100.0%)  | Mar-11, Apr-25 |                12 | B.1, B.1.72                      |                              24 | 0.1705           |
| UK167          | 12 (100.0%)  | Mar-23, Apr-24 |                12 | B.1                              |                              25 | 0.1164           |
| UK653          | 11 (100.0%)  | Apr-07, May-19 |                11 | B.1.1                            |                               0 | active today     |
| UK2464         | 10 (100.0%)  | Apr-05, Apr-18 |                10 | B.1.p11                          |                              31 | 0.0466           |
| UK276          | 9 (100.0%)   | Apr-05, May-01 |                 9 | B.1.1                            |                              18 | 0.1806           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/OXON/figures/report_OXON_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 45 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/OXON/figures/report_OXON_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/OXON/figures/report_OXON_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/OXON/figures/report_OXON_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/OXON/figures/report_OXON_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 580 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/OXON/figures/report_OXON_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage                   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:---------------------------------|--------------------------------:|:-----------------|
| UK5            | 450 (100.0%) | Mar-17, May-14 |               450 | B.1.1.4, B.1.1.1, B.1.1, B.1.1.2 |                               5 | 0.0258           |
| UK109          | 17 (100.0%)  | Apr-07, May-06 |                17 | B.1.5                            |                              13 | 0.1394           |
| UK376          | 16 (100.0%)  | Apr-05, May-03 |                16 | B.1.1.9                          |                              16 | 0.1167           |
| UK370          | 15 (100.0%)  | Apr-04, Apr-27 |                15 | B.1.1.10                         |                              22 | 0.0747           |
| UK107          | 13 (100.0%)  | Mar-28, Apr-16 |                13 | B.2.1                            |                              33 | 0.048            |
| UK42           | 12 (100.0%)  | Mar-11, Apr-25 |                12 | B.1, B.1.72                      |                              24 | 0.1705           |
| UK167          | 12 (100.0%)  | Mar-23, Apr-24 |                12 | B.1                              |                              25 | 0.1164           |
| UK653          | 11 (100.0%)  | Apr-07, May-19 |                11 | B.1.1                            |                               0 | active today     |
| UK2464         | 10 (100.0%)  | Apr-05, Apr-18 |                10 | B.1.p11                          |                              31 | 0.0466           |
| UK276          | 9 (100.0%)   | Apr-05, May-01 |                 9 | B.1.1                            |                              18 | 0.1806           |
| UK64           | 8 (100.0%)   | Apr-02, Apr-15 |                 8 | B.1                              |                              34 | 0.0546           |
| UK5676         | 8 (100.0%)   | Mar-17, Apr-17 |                 8 | B.2                              |                              32 | 0.1384           |
| UK5498         | 8 (100.0%)   | Mar-17, Apr-20 |                 8 | B.2                              |                              29 | 0.1675           |
| UK5561         | 8 (100.0%)   | Mar-12, Apr-15 |                 8 | B.2.2                            |                              34 | 0.1429           |
| UK72           | 7 (100.0%)   | Mar-23, Apr-24 |                 7 | B                                |                              25 | 0.2133           |
| UK263          | 7 (100.0%)   | Mar-30, Apr-13 |                 7 | B.1.p11                          |                              36 | 0.0648           |
| UK83           | 7 (100.0%)   | Apr-02, Apr-13 |                 7 | B.1.1                            |                              36 | 0.0509           |
| UK1003         | 7 (100.0%)   | Apr-02, Apr-22 |                 7 | B.1.1                            |                              27 | 0.1235           |
| UK2913         | 7 (100.0%)   | Apr-03, May-01 |                 7 | B.1.p11                          |                              18 | 0.2593           |
| UK5180         | 7 (100.0%)   | Apr-05, May-04 |                 7 | B.1.1.7                          |                              15 | 0.3222           |
| UK9            | 6 (100.0%)   | Apr-04, Apr-18 |                 6 | B.1.13                           |                              31 | 0.0903           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | OXON     |            45 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK109 |   UK376 |   UK370 |   UK167 |   UK42 |   UK653 |   UK276 |   UK1003 |   UK72 |
|:------------------|------:|--------:|--------:|--------:|--------:|-------:|--------:|--------:|---------:|-------:|
| 2020-03-08        |     0 |       0 |       0 |       0 |       0 |      1 |       0 |       0 |        0 |      0 |
| 2020-03-15        |     3 |       0 |       0 |       0 |       0 |      0 |       0 |       0 |        0 |      0 |
| 2020-03-22        |     2 |       0 |       0 |       0 |       1 |      0 |       0 |       0 |        0 |      1 |
| 2020-03-29        |     3 |       0 |       0 |       1 |       0 |      1 |       0 |       0 |        1 |      0 |
| 2020-04-05        |     3 |       3 |       3 |       1 |       1 |      2 |       1 |       1 |        3 |      1 |
| 2020-04-12        |     5 |       1 |       1 |       2 |       3 |      1 |       0 |       1 |        1 |      1 |
| 2020-04-19        |     3 |       1 |       1 |       3 |       2 |      1 |       0 |       1 |        1 |      2 |
| 2020-04-26        |     1 |       1 |       1 |       1 |       0 |      0 |       0 |       1 |        0 |      0 |
| 2020-05-03        |     1 |       1 |       1 |       0 |       0 |      0 |       1 |       0 |        0 |      0 |
| 2020-05-10        |     1 |       0 |       0 |       0 |       0 |      0 |       1 |       0 |        0 |      0 |
| 2020-05-17        |     0 |       0 |       0 |       0 |       0 |      0 |       1 |       0 |        0 |      0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-11 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                1 |       1 |
| 2020-03-16 |                            1 |                                0 |       1 |
| 2020-03-17 |                            0 |                                3 |       3 |
| 2020-03-19 |                            1 |                                0 |       1 |
| 2020-03-23 |                            3 |                                2 |       5 |
| 2020-03-24 |                            0 |                                1 |       1 |
| 2020-03-28 |                            2 |                                1 |       3 |
| 2020-03-30 |                            0 |                                3 |       3 |
| 2020-03-31 |                            0 |                                1 |       1 |
| 2020-04-02 |                            0 |                                3 |       3 |
| 2020-04-03 |                            0 |                                2 |       2 |
| 2020-04-04 |                            0 |                                4 |       4 |
| 2020-04-05 |                            4 |                                8 |      12 |
| 2020-04-06 |                            3 |                                5 |       8 |
| 2020-04-07 |                            8 |                                5 |      13 |
| 2020-04-08 |                            2 |                                3 |       5 |
| 2020-04-09 |                            1 |                                0 |       1 |
| 2020-04-10 |                            1 |                                0 |       1 |
| 2020-04-11 |                            1 |                                0 |       1 |
| 2020-04-12 |                            2 |                                1 |       3 |
| 2020-04-13 |                            3 |                                1 |       4 |
| 2020-04-14 |                            0 |                                1 |       1 |
| 2020-04-16 |                            2 |                                1 |       3 |
| 2020-04-17 |                            2 |                                1 |       3 |
| 2020-04-18 |                            3 |                                0 |       3 |
| 2020-04-19 |                            2 |                                1 |       3 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-22 |                            0 |                                1 |       1 |
| 2020-05-04 |                            2 |                                0 |       2 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-08 |         1 |
| 2020-03-11 |         1 |
| 2020-03-12 |         1 |
| 2020-03-16 |         1 |
| 2020-03-17 |         3 |
| 2020-03-19 |         2 |
| 2020-03-20 |         1 |
| 2020-03-23 |         6 |
| 2020-03-24 |         3 |
| 2020-03-27 |         1 |
| 2020-03-28 |         5 |
| 2020-03-29 |         4 |
| 2020-03-30 |        17 |
| 2020-03-31 |         4 |
| 2020-04-01 |         2 |
| 2020-04-02 |        10 |
| 2020-04-03 |         6 |
| 2020-04-04 |        17 |
| 2020-04-05 |        64 |
| 2020-04-06 |        38 |
| 2020-04-07 |        91 |
| 2020-04-08 |        64 |
| 2020-04-09 |        35 |
| 2020-04-10 |        43 |
| 2020-04-11 |        19 |
| 2020-04-12 |        19 |
| 2020-04-13 |        30 |
| 2020-04-14 |        23 |
| 2020-04-15 |        27 |
| 2020-04-16 |        22 |
| 2020-04-17 |        30 |
| 2020-04-18 |        27 |
| 2020-04-19 |        24 |
| 2020-04-20 |        21 |
| 2020-04-21 |        14 |
| 2020-04-22 |        10 |
| 2020-04-23 |        15 |
| 2020-04-24 |        12 |
| 2020-04-25 |         7 |
| 2020-04-26 |         5 |
| 2020-04-27 |        10 |
| 2020-04-28 |         7 |
| 2020-04-29 |         3 |
| 2020-04-30 |         2 |
| 2020-05-01 |         5 |
| 2020-05-02 |         2 |
| 2020-05-03 |         3 |
| 2020-05-04 |         7 |
| 2020-05-05 |         4 |
| 2020-05-06 |         3 |
| 2020-05-07 |         1 |
| 2020-05-08 |         1 |
| 2020-05-11 |         1 |
| 2020-05-12 |         2 |
| 2020-05-14 |         2 |
| 2020-05-19 |         2 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country   |   Number of sequences | Sequence group   |
|:-----------------|:----------|----------------------:|:-----------------|
| BERKSHIRE        | England   |                    10 | 10-50            |
| BUCKINGHAMSHIRE  | England   |                    10 | 10-50            |
| GREATER LONDON   | England   |                     1 | 1-10             |
| HAMPSHIRE        | England   |                   108 | 100-150          |
| HERTFORDSHIRE    | England   |                     2 | 1-10             |
| ISLE OF WIGHT    | England   |                     1 | 1-10             |
| NORTHAMPTONSHIRE | England   |                     1 | 1-10             |
| OXFORDSHIRE      | England   |                    67 | 50-100           |

\pagebreak






