







# Lineages report for NORW




This report gives summaries of UK specific lineages sequenced by NORW for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-18. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
857 sequences in the UK from the sequencing centre NORW have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 50 and the maximum is 240


Sequences which were replicates or too error-prone were removed from this analysis.



41 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 9 that remain:
6 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
1 has reactivated.
1 lineage has been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage                                          |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:--------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | 262 (100.0%) | Apr-08, Jun-17 |               262 | B.1.1.1, B.1.1.p11, B.1.1.3, B.1.1, B.1.1.p15, B.1.1.10 |                               1 | 0.2682           |
| UK2913         | 107 (100.0%) | Apr-08, Jun-01 |               107 | B.1.p11                                                 |                              17 | 0.03             |
| UK6            | 80 (100.0%)  | Apr-08, May-13 |                80 | B.1                                                     |                              36 | 0.0123           |
| UK199          | 71 (100.0%)  | Apr-08, Jun-02 |                71 | B.1.5.5, B.1.5                                          |                              16 | 0.0491           |
| UK509          | 57 (100.0%)  | Apr-08, May-29 |                57 | B.1.1                                                   |                              20 | 0.0455           |
| UK5676         | 26 (100.0%)  | Apr-08, May-13 |                26 | B.2                                                     |                              36 | 0.0389           |
| UK712          | 24 (100.0%)  | Apr-08, Jun-18 |                24 | B.1, B.1.5                                              |                               0 | active today     |
| UK684          | 21 (100.0%)  | Apr-15, May-21 |                21 | B.1                                                     |                              28 | 0.0643           |
| UK448          | 18 (100.0%)  | Apr-29, May-22 |                18 | B.1.1                                                   |                              27 | 0.0501           |
| UK42           | 16 (100.0%)  | Apr-08, Jun-04 |                16 | B.1                                                     |                              14 | 0.2714           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORW/figures/report_NORW_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 15 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORW/figures/report_NORW_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORW/figures/report_NORW_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORW/figures/report_NORW_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORW/figures/report_NORW_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 27 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORW/figures/report_NORW_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage                                          |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:--------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | 262 (100.0%) | Apr-08, Jun-17 |               262 | B.1.1.1, B.1.1.p11, B.1.1.3, B.1.1, B.1.1.p15, B.1.1.10 |                               1 | 0.2682           |
| UK2913         | 107 (100.0%) | Apr-08, Jun-01 |               107 | B.1.p11                                                 |                              17 | 0.03             |
| UK6            | 80 (100.0%)  | Apr-08, May-13 |                80 | B.1                                                     |                              36 | 0.0123           |
| UK199          | 71 (100.0%)  | Apr-08, Jun-02 |                71 | B.1.5.5, B.1.5                                          |                              16 | 0.0491           |
| UK509          | 57 (100.0%)  | Apr-08, May-29 |                57 | B.1.1                                                   |                              20 | 0.0455           |
| UK5676         | 26 (100.0%)  | Apr-08, May-13 |                26 | B.2                                                     |                              36 | 0.0389           |
| UK712          | 24 (100.0%)  | Apr-08, Jun-18 |                24 | B.1, B.1.5                                              |                               0 | active today     |
| UK684          | 21 (100.0%)  | Apr-15, May-21 |                21 | B.1                                                     |                              28 | 0.0643           |
| UK448          | 18 (100.0%)  | Apr-29, May-22 |                18 | B.1.1                                                   |                              27 | 0.0501           |
| UK42           | 16 (100.0%)  | Apr-08, Jun-04 |                16 | B.1                                                     |                              14 | 0.2714           |
| UK125          | 16 (100.0%)  | Apr-22, May-29 |                16 | B.1.1                                                   |                              20 | 0.1233           |
| UK5660         | 16 (100.0%)  | Apr-25, May-08 |                16 | B.1.1                                                   |                              41 | 0.0211           |
| UK167          | 15 (100.0%)  | May-13, Jun-07 |                15 | B.1                                                     |                              11 | 0.1623           |
| UK2735         | 14 (100.0%)  | Apr-14, May-11 |                14 | B.1.1                                                   |                              38 | 0.0547           |
| UK165          | 13 (100.0%)  | Apr-13, May-19 |                13 | B                                                       |                              30 | 0.1              |
| UK5663         | 12 (100.0%)  | Apr-11, May-02 |                12 | B.2                                                     |                              47 | 0.0406           |
| UK415          | 11 (100.0%)  | Apr-19, May-06 |                11 | B.1                                                     |                              43 | 0.0395           |
| UK28           | 8 (100.0%)   | Apr-13, May-01 |                 8 | B.1.1.10                                                |                              48 | 0.0536           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NORW     |            15 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2913 |   UK199 |   UK509 |   UK712 |   UK448 |   UK125 |   UK42 |   UK167 |
|:------------------|------:|---------:|--------:|--------:|--------:|--------:|--------:|-------:|--------:|
| 2020-04-05        |     4 |        2 |       1 |       2 |       1 |       0 |       0 |      1 |       0 |
| 2020-04-12        |     3 |        2 |       3 |       2 |       1 |       0 |       0 |      2 |       0 |
| 2020-04-19        |     3 |        3 |       2 |       2 |       0 |       0 |       2 |      1 |       0 |
| 2020-04-26        |     7 |        3 |       2 |       3 |       0 |       1 |       2 |      3 |       0 |
| 2020-05-03        |     5 |        2 |       1 |       3 |       1 |       3 |       1 |      2 |       0 |
| 2020-05-10        |     5 |        2 |       1 |       1 |       1 |       1 |       1 |      0 |       1 |
| 2020-05-17        |     2 |        2 |       2 |       0 |       1 |       1 |       1 |      1 |       2 |
| 2020-05-24        |     3 |        2 |       3 |       1 |       0 |       0 |       1 |      0 |       2 |
| 2020-05-31        |     2 |        1 |       1 |       0 |       1 |       0 |       0 |      1 |       2 |
| 2020-06-07        |     0 |        0 |       0 |       0 |       0 |       0 |       0 |      0 |       1 |
| 2020-06-14        |     2 |        0 |       0 |       0 |       1 |       0 |       0 |      0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-04-08 |                            4 |                               13 |      17 |
| 2020-04-09 |                            2 |                                0 |       2 |
| 2020-04-11 |                            2 |                                3 |       5 |
| 2020-04-12 |                            0 |                                1 |       1 |
| 2020-04-13 |                            1 |                                3 |       4 |
| 2020-04-14 |                            1 |                                1 |       2 |
| 2020-04-15 |                            0 |                                1 |       1 |
| 2020-04-18 |                            1 |                                0 |       1 |
| 2020-04-19 |                            0 |                                1 |       1 |
| 2020-04-20 |                            1 |                                1 |       2 |
| 2020-04-21 |                            4 |                                0 |       4 |
| 2020-04-22 |                            0 |                                1 |       1 |
| 2020-04-23 |                            2 |                                0 |       2 |
| 2020-04-25 |                            0 |                                2 |       2 |
| 2020-04-26 |                            1 |                                0 |       1 |
| 2020-04-27 |                            0 |                                1 |       1 |
| 2020-04-28 |                            0 |                                1 |       1 |
| 2020-04-29 |                            0 |                                2 |       2 |
| 2020-04-30 |                            3 |                                1 |       4 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-11 |                            0 |                                1 |       1 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-13 |                            0 |                                1 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |

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
| 2020-04-28 |        17 |
| 2020-04-29 |        42 |
| 2020-04-30 |        33 |
| 2020-05-01 |        29 |
| 2020-05-02 |        21 |
| 2020-05-03 |        33 |
| 2020-05-04 |        49 |
| 2020-05-05 |        36 |
| 2020-05-06 |        42 |
| 2020-05-07 |        14 |
| 2020-05-08 |        18 |
| 2020-05-09 |        11 |
| 2020-05-10 |        22 |
| 2020-05-11 |        19 |
| 2020-05-12 |        19 |
| 2020-05-13 |        11 |
| 2020-05-14 |         5 |
| 2020-05-16 |         4 |
| 2020-05-17 |         8 |
| 2020-05-18 |         7 |
| 2020-05-19 |         4 |
| 2020-05-20 |         3 |
| 2020-05-21 |        13 |
| 2020-05-22 |         1 |
| 2020-05-23 |         2 |
| 2020-05-25 |         4 |
| 2020-05-26 |         3 |
| 2020-05-27 |         3 |
| 2020-05-28 |         8 |
| 2020-05-29 |         5 |
| 2020-05-30 |         1 |
| 2020-05-31 |         1 |
| 2020-06-01 |         8 |
| 2020-06-02 |         2 |
| 2020-06-03 |         2 |
| 2020-06-04 |         5 |
| 2020-06-05 |         3 |
| 2020-06-07 |         1 |
| 2020-06-09 |         1 |
| 2020-06-15 |         1 |
| 2020-06-17 |         4 |
| 2020-06-18 |        12 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2         | Country   |   Number of sequences | Sequence group   |
|:---------------|:----------|----------------------:|:-----------------|
| CAMBRIDGESHIRE | England   |                    37 | 10-50            |
| ESSEX          | England   |                    28 | 10-50            |
| GREATER LONDON | England   |                     3 | 1-10             |
| LINCOLNSHIRE   | England   |                    11 | 10-50            |
| MANCHESTER     | England   |                     1 | 1-10             |
| NORFOLK        | England   |                   602 | >500             |
| SUFFOLK        | England   |                   147 | 100-150          |
| WILTSHIRE      | England   |                     1 | 1-10             |

\pagebreak






