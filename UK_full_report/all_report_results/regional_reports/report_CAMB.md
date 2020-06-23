







# Lineages report for CAMB




This report gives summaries of UK specific lineages sequenced by CAMB for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-14. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1199 sequences in the UK from the sequencing centre CAMB have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 65 and the maximum is 589


Sequences which were replicates or too error-prone were removed from this analysis.



126 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 12 that remain:
7 are pending extinction, ie last seen three weeks ago.
3 lineages have gone quiet, ie haven't been seen this week.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage          |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:------------------------|--------------------------------:|:-----------------|
| UK5            | 448 (100.0%) | Mar-15, Jun-13 |               448 | B.1.1.1, B.1.1          |                               1 | 0.2013           |
| UK42           | 58 (100.0%)  | Mar-20, Jun-04 |                58 | B.1.35, B.1.5, B.1      |                              10 | 0.1333           |
| UK107          | 55 (100.0%)  | Mar-13, May-01 |                55 | B.2.1                   |                              44 | 0.0206           |
| UK3929         | 34 (100.0%)  | Mar-31, May-22 |                34 | B.1.1.3, B.1.1, B.1.1.4 |                              23 | 0.0685           |
| UK167          | 33 (100.0%)  | Mar-31, May-21 |                33 | B.1.66, B.1             |                              24 | 0.0664           |
| UK355          | 30 (100.0%)  | Apr-09, Jun-14 |                30 | B.1.1                   |                               0 | active today     |
| UK565          | 28 (100.0%)  | Mar-28, May-13 |                28 | B.1.1                   |                              32 | 0.0532           |
| UK5676         | 27 (100.0%)  | Mar-14, Apr-29 |                27 | B.2                     |                              46 | 0.0385           |
| UK494          | 21 (100.0%)  | Mar-20, Apr-29 |                21 | B.1.p11                 |                              46 | 0.0435           |
| UK2916         | 21 (100.0%)  | Mar-20, May-10 |                21 | B.1                     |                              35 | 0.0729           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/CAMB/figures/report_CAMB_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 5 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/CAMB/figures/report_CAMB_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/CAMB/figures/report_CAMB_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/CAMB/figures/report_CAMB_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/CAMB/figures/report_CAMB_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 30 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/CAMB/figures/report_CAMB_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage          |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:------------------------|--------------------------------:|:-----------------|
| UK5            | 448 (100.0%) | Mar-15, Jun-13 |               448 | B.1.1.1, B.1.1          |                               1 | 0.2013           |
| UK42           | 58 (100.0%)  | Mar-20, Jun-04 |                58 | B.1.35, B.1.5, B.1      |                              10 | 0.1333           |
| UK107          | 55 (100.0%)  | Mar-13, May-01 |                55 | B.2.1                   |                              44 | 0.0206           |
| UK3929         | 34 (100.0%)  | Mar-31, May-22 |                34 | B.1.1.3, B.1.1, B.1.1.4 |                              23 | 0.0685           |
| UK167          | 33 (100.0%)  | Mar-31, May-21 |                33 | B.1.66, B.1             |                              24 | 0.0664           |
| UK355          | 30 (100.0%)  | Apr-09, Jun-14 |                30 | B.1.1                   |                               0 | active today     |
| UK565          | 28 (100.0%)  | Mar-28, May-13 |                28 | B.1.1                   |                              32 | 0.0532           |
| UK5676         | 27 (100.0%)  | Mar-14, Apr-29 |                27 | B.2                     |                              46 | 0.0385           |
| UK494          | 21 (100.0%)  | Mar-20, Apr-29 |                21 | B.1.p11                 |                              46 | 0.0435           |
| UK2916         | 21 (100.0%)  | Mar-20, May-10 |                21 | B.1                     |                              35 | 0.0729           |
| UK2464         | 21 (100.0%)  | Mar-17, May-11 |                21 | B.1.p11                 |                              34 | 0.0809           |
| UK2735         | 20 (100.0%)  | Mar-31, May-27 |                20 | B.1.1                   |                              18 | 0.1667           |
| UK3126         | 17 (100.0%)  | May-04, May-19 |                17 | B.1.1                   |                              26 | 0.0361           |
| UK448          | 17 (100.0%)  | Apr-14, May-26 |                17 | B.1.1                   |                              19 | 0.1382           |
| UK2913         | 17 (100.0%)  | Mar-29, May-31 |                17 | B.1.p11                 |                              14 | 0.2812           |
| UK326          | 15 (100.0%)  | Apr-07, May-22 |                15 | B.1.1.10                |                              23 | 0.1398           |
| UK13           | 14 (100.0%)  | Mar-31, May-13 |                14 | B.1.1                   |                              32 | 0.1034           |
| UK51           | 12 (100.0%)  | Apr-20, Jun-07 |                12 | B.1.36                  |                               7 | 0.6234           |
| UK193          | 10 (100.0%)  | Mar-30, Apr-29 |                10 | B.1.1                   |                              46 | 0.0725           |
| UK5741         | 10 (100.0%)  | Apr-04, May-10 |                10 | B.1                     |                              35 | 0.1143           |
| UK9            | 9 (100.0%)   | Mar-28, May-05 |                 9 | B.1.13                  |                              40 | 0.1188           |
| UK342          | 8 (100.0%)   | Apr-02, Apr-23 |                 8 | B.1.1                   |                              52 | 0.0577           |
| UK37           | 8 (100.0%)   | Mar-29, May-03 |                 8 | B.1.30                  |                              42 | 0.119            |
| UK6            | 8 (100.0%)   | Mar-19, May-01 |                 8 | B.1                     |                              44 | 0.1396           |
| UK5503         | 8 (100.0%)   | Apr-15, May-11 |                 8 | B.1                     |                              34 | 0.1092           |
| UK113          | 7 (100.0%)   | May-25, Jun-02 |                 7 | B.1.1                   |                              12 | 0.1111           |
| UK370          | 6 (100.0%)   | Apr-05, Apr-29 |                 6 | B.1.1.10                |                              46 | 0.1043           |
| UK5180         | 6 (100.0%)   | Apr-09, Apr-28 |                 6 | B.1.1.7                 |                              47 | 0.0809           |
| UK36           | 6 (100.0%)   | Mar-30, Apr-15 |                 6 | B.1                     |                              60 | 0.0533           |
| UK274          | 6 (100.0%)   | Mar-19, May-11 |                 6 | B.3                     |                              34 | 0.3118           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | CAMB     |             5 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK42 |   UK3929 |   UK167 |   UK355 |   UK2735 |   UK3126 |   UK448 |   UK2913 |   UK326 |
|:------------------|------:|-------:|---------:|--------:|--------:|---------:|---------:|--------:|---------:|--------:|
| 2020-03-15        |     3 |      1 |        0 |       0 |       0 |        0 |        0 |       0 |        0 |       0 |
| 2020-03-22        |     5 |      2 |        0 |       0 |       0 |        0 |        0 |       0 |        0 |       0 |
| 2020-03-29        |     8 |      6 |        2 |       2 |       0 |        1 |        0 |       0 |        2 |       0 |
| 2020-04-05        |     8 |      4 |        1 |       2 |       1 |        1 |        0 |       0 |        1 |       1 |
| 2020-04-12        |     9 |      3 |        1 |       3 |       1 |        2 |        0 |       1 |        3 |       0 |
| 2020-04-19        |     8 |      3 |        2 |       3 |       1 |        2 |        0 |       1 |        1 |       0 |
| 2020-04-26        |     8 |      4 |        2 |       3 |       1 |        2 |        0 |       1 |        2 |       0 |
| 2020-05-03        |     7 |      2 |        1 |       0 |       0 |        1 |        1 |       0 |        0 |       2 |
| 2020-05-10        |     6 |      1 |        1 |       0 |       1 |        2 |        1 |       1 |        2 |       2 |
| 2020-05-17        |     6 |      0 |        2 |       3 |       1 |        1 |        1 |       1 |        0 |       1 |
| 2020-05-24        |     4 |      1 |        0 |       0 |       1 |        1 |        0 |       1 |        1 |       0 |
| 2020-05-31        |     5 |      4 |        0 |       0 |       1 |        0 |        0 |       0 |        1 |       0 |
| 2020-06-07        |     4 |      0 |        0 |       0 |       1 |        0 |        0 |       0 |        0 |       0 |
| 2020-06-14        |     0 |      0 |        0 |       0 |       1 |        0 |        0 |       0 |        0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-13 |                            1 |                                1 |       2 |
| 2020-03-14 |                            0 |                                1 |       1 |
| 2020-03-15 |                            0 |                                1 |       1 |
| 2020-03-16 |                            2 |                                1 |       3 |
| 2020-03-17 |                            3 |                                2 |       5 |
| 2020-03-18 |                            6 |                                2 |       8 |
| 2020-03-19 |                            2 |                                3 |       5 |
| 2020-03-20 |                            0 |                                4 |       4 |
| 2020-03-26 |                            4 |                                1 |       5 |
| 2020-03-27 |                            1 |                                3 |       4 |
| 2020-03-28 |                            1 |                                2 |       3 |
| 2020-03-29 |                            5 |                                4 |       9 |
| 2020-03-30 |                            2 |                                2 |       4 |
| 2020-03-31 |                            5 |                                9 |      14 |
| 2020-04-01 |                            2 |                                1 |       3 |
| 2020-04-02 |                            0 |                                2 |       2 |
| 2020-04-03 |                            1 |                                0 |       1 |
| 2020-04-04 |                            2 |                                1 |       3 |
| 2020-04-05 |                            1 |                                2 |       3 |
| 2020-04-06 |                            2 |                                4 |       6 |
| 2020-04-07 |                            2 |                                2 |       4 |
| 2020-04-08 |                            4 |                                4 |       8 |
| 2020-04-09 |                            0 |                                2 |       2 |
| 2020-04-10 |                            1 |                                1 |       2 |
| 2020-04-11 |                            1 |                                1 |       2 |
| 2020-04-12 |                            3 |                                0 |       3 |
| 2020-04-13 |                            2 |                                1 |       3 |
| 2020-04-14 |                            1 |                                1 |       2 |
| 2020-04-15 |                            1 |                                3 |       4 |
| 2020-04-16 |                            0 |                                1 |       1 |
| 2020-04-17 |                            2 |                                0 |       2 |
| 2020-04-18 |                            1 |                                0 |       1 |
| 2020-04-20 |                            1 |                                2 |       3 |
| 2020-04-21 |                            3 |                                1 |       4 |
| 2020-04-22 |                            1 |                                1 |       2 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-04-26 |                            1 |                                1 |       2 |
| 2020-04-27 |                            3 |                                1 |       4 |
| 2020-04-28 |                            2 |                                0 |       2 |
| 2020-04-29 |                            0 |                                2 |       2 |
| 2020-04-30 |                            0 |                                1 |       1 |
| 2020-05-01 |                            0 |                                2 |       2 |
| 2020-05-04 |                            1 |                                1 |       2 |
| 2020-05-05 |                            1 |                                0 |       1 |
| 2020-05-06 |                            0 |                                1 |       1 |
| 2020-05-07 |                            1 |                                2 |       3 |
| 2020-05-11 |                            0 |                                2 |       2 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-17 |                            1 |                                0 |       1 |
| 2020-05-25 |                            0 |                                2 |       2 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-13 |         3 |
| 2020-03-14 |         2 |
| 2020-03-15 |         3 |
| 2020-03-16 |         4 |
| 2020-03-17 |        11 |
| 2020-03-18 |        12 |
| 2020-03-19 |         9 |
| 2020-03-20 |        14 |
| 2020-03-21 |         1 |
| 2020-03-22 |         2 |
| 2020-03-24 |         1 |
| 2020-03-26 |        10 |
| 2020-03-27 |        13 |
| 2020-03-28 |        13 |
| 2020-03-29 |        19 |
| 2020-03-30 |        18 |
| 2020-03-31 |        37 |
| 2020-04-01 |        21 |
| 2020-04-02 |        16 |
| 2020-04-03 |        11 |
| 2020-04-04 |        15 |
| 2020-04-05 |        26 |
| 2020-04-06 |        28 |
| 2020-04-07 |        31 |
| 2020-04-08 |        27 |
| 2020-04-09 |        17 |
| 2020-04-10 |        16 |
| 2020-04-11 |        25 |
| 2020-04-12 |        27 |
| 2020-04-13 |        26 |
| 2020-04-14 |        25 |
| 2020-04-15 |        23 |
| 2020-04-16 |        23 |
| 2020-04-17 |        26 |
| 2020-04-18 |         9 |
| 2020-04-19 |        16 |
| 2020-04-20 |        31 |
| 2020-04-21 |        30 |
| 2020-04-22 |        22 |
| 2020-04-23 |        14 |
| 2020-04-24 |        12 |
| 2020-04-25 |        16 |
| 2020-04-26 |        24 |
| 2020-04-27 |        40 |
| 2020-04-28 |        24 |
| 2020-04-29 |        23 |
| 2020-04-30 |        20 |
| 2020-05-01 |        27 |
| 2020-05-02 |         9 |
| 2020-05-03 |         5 |
| 2020-05-04 |         9 |
| 2020-05-05 |         8 |
| 2020-05-06 |        10 |
| 2020-05-07 |        26 |
| 2020-05-08 |        10 |
| 2020-05-09 |        11 |
| 2020-05-10 |         6 |
| 2020-05-11 |        39 |
| 2020-05-12 |        14 |
| 2020-05-13 |        21 |
| 2020-05-14 |         8 |
| 2020-05-15 |        11 |
| 2020-05-16 |         4 |
| 2020-05-17 |         2 |
| 2020-05-18 |        20 |
| 2020-05-19 |        20 |
| 2020-05-20 |         7 |
| 2020-05-21 |         8 |
| 2020-05-22 |         8 |
| 2020-05-23 |         3 |
| 2020-05-24 |         1 |
| 2020-05-25 |        11 |
| 2020-05-26 |         5 |
| 2020-05-27 |         9 |
| 2020-05-28 |         4 |
| 2020-05-29 |         1 |
| 2020-05-30 |         3 |
| 2020-05-31 |         4 |
| 2020-06-01 |         6 |
| 2020-06-02 |         6 |
| 2020-06-03 |         3 |
| 2020-06-04 |         6 |
| 2020-06-05 |         1 |
| 2020-06-07 |         3 |
| 2020-06-08 |         3 |
| 2020-06-10 |         7 |
| 2020-06-12 |         2 |
| 2020-06-13 |         1 |
| 2020-06-14 |         1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country   |   Number of sequences | Sequence group   |
|:-----------------|:----------|----------------------:|:-----------------|
| BEDFORDSHIRE     | England   |                    35 | 10-50            |
| BUCKINGHAMSHIRE  | England   |                    57 | 50-100           |
| CAMBRIDGESHIRE   | England   |                   398 | 300-400          |
| ESSEX            | England   |                   270 | 250-300          |
| GREATER LONDON   | England   |                    85 | 50-100           |
| HERTFORDSHIRE    | England   |                   177 | 150-200          |
| NORFOLK          | England   |                     6 | 1-10             |
| NORTHAMPTONSHIRE | England   |                     3 | 1-10             |
| NOTTINGHAMSHIRE  | England   |                     1 | 1-10             |
| OXFORDSHIRE      | England   |                     1 | 1-10             |
| SUFFOLK          | England   |                   136 | 100-150          |

\pagebreak






