







# Lineages report for EDIN




This report gives summaries of UK specific lineages sequenced by EDIN for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-26. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1104 sequences in the UK from the sequencing centre EDIN have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 464 and the maximum is 538


Sequences which were replicates or too error-prone were removed from this analysis.



433 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 19 that remain:
7 are pending extinction, ie last seen three weeks ago.
6 lineages have gone quiet, ie haven't been seen this week.
3 lineages have reactivated.
3 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Scotland    | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) |   Activity score |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|-----------------:|
| UK36           | 91 (100.0%) | Mar-21, May-04 |                91 | B.1              |                              22 |           0.0222 |
| UK2464         | 43 (100.0%) | Mar-20, May-12 |                43 | B.1.p11          |                              14 |           0.0901 |
| UK5            | 35 (100.0%) | Mar-18, May-18 |                35 | B.1.1.1          |                               8 |           0.2243 |
| UK53           | 28 (100.0%) | Apr-16, May-21 |                28 | B.1.1.4          |                               5 |           0.2593 |
| UK44           | 25 (100.0%) | Mar-17, May-01 |                25 | B                |                              25 |           0.075  |
| UK296          | 25 (100.0%) | Apr-08, May-13 |                25 | B.1.5            |                              13 |           0.1122 |
| UK21           | 24 (100.0%) | Mar-18, May-23 |                24 | B.1.40           |                               3 |           0.9565 |
| UK2912         | 19 (100.0%) | Apr-12, May-13 |                19 | B.1.p11          |                              13 |           0.1325 |
| UK461          | 19 (100.0%) | Apr-18, May-19 |                19 | B.1.5            |                               7 |           0.246  |
| UK558          | 17 (100.0%) | Apr-24, May-22 |                17 | B.1.5            |                               4 |           0.4375 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/EDIN/figures/report_EDIN_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 10 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/EDIN/figures/report_EDIN_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/EDIN/figures/report_EDIN_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/EDIN/figures/report_EDIN_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/EDIN/figures/report_EDIN_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 97 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/EDIN/figures/report_EDIN_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Scotland    | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK36           | 91 (100.0%) | Mar-21, May-04 |                91 | B.1              |                              22 | 0.0222           |
| UK2464         | 43 (100.0%) | Mar-20, May-12 |                43 | B.1.p11          |                              14 | 0.0901           |
| UK5            | 35 (100.0%) | Mar-18, May-18 |                35 | B.1.1.1          |                               8 | 0.2243           |
| UK53           | 28 (100.0%) | Apr-16, May-21 |                28 | B.1.1.4          |                               5 | 0.2593           |
| UK44           | 25 (100.0%) | Mar-17, May-01 |                25 | B                |                              25 | 0.075            |
| UK296          | 25 (100.0%) | Apr-08, May-13 |                25 | B.1.5            |                              13 | 0.1122           |
| UK21           | 24 (100.0%) | Mar-18, May-23 |                24 | B.1.40           |                               3 | 0.9565           |
| UK2912         | 19 (100.0%) | Apr-12, May-13 |                19 | B.1.p11          |                              13 | 0.1325           |
| UK461          | 19 (100.0%) | Apr-18, May-19 |                19 | B.1.5            |                               7 | 0.246            |
| UK558          | 17 (100.0%) | Apr-24, May-22 |                17 | B.1.5            |                               4 | 0.4375           |
| UK304          | 17 (100.0%) | Apr-16, May-26 |                17 | B.1.1.14         |                               0 | active today     |
| UK2735         | 16 (100.0%) | Mar-18, May-02 |                16 | B.1.1            |                              24 | 0.125            |
| UK150          | 16 (100.0%) | Mar-21, Apr-22 |                16 | B.1.1.p12        |                              34 | 0.0627           |
| UK2200         | 15 (100.0%) | Mar-25, May-05 |                15 | B.1.5.6, B.1.5   |                              21 | 0.1395           |
| UK66           | 14 (100.0%) | Mar-28, May-20 |                14 | B.1.1.8          |                               6 | 0.6795           |
| UK156          | 14 (100.0%) | Mar-18, Apr-18 |                14 | B.1.71           |                              38 | 0.0628           |
| UK43           | 14 (100.0%) | Mar-26, Apr-18 |                14 | A.5              |                              38 | 0.0466           |
| UK499          | 13 (100.0%) | Apr-24, May-15 |                13 | B.1.5            |                              11 | 0.1591           |
| UK1539         | 13 (100.0%) | May-09, May-25 |                13 | B.1.5            |                               1 | 1.3333           |
| UK1667         | 13 (100.0%) | Mar-31, Apr-28 |                13 | B.1.p9           |                              28 | 0.0833           |
| UK225          | 11 (100.0%) | Mar-17, Apr-05 |                11 | B.2              |                              51 | 0.0373           |
| UK436          | 11 (100.0%) | Apr-13, May-14 |                11 | B.1.5            |                              12 | 0.2583           |
| UK414          | 10 (100.0%) | Apr-05, Apr-22 |                10 | B.1.5            |                              34 | 0.0556           |
| UK562          | 10 (100.0%) | Mar-27, Apr-25 |                10 | B.1              |                              31 | 0.1039           |
| UK434          | 9 (100.0%)  | Apr-20, May-07 |                 9 | B.1.5            |                              19 | 0.1118           |
| UK1548         | 9 (100.0%)  | Apr-13, Apr-24 |                 9 | B.1.5.5, B.1.5   |                              32 | 0.043            |
| UK14           | 8 (100.0%)  | Mar-21, Apr-27 |                 8 | B                |                              29 | 0.1823           |
| UK554          | 8 (100.0%)  | Apr-23, May-06 |                 8 | B.1.5            |                              20 | 0.0929           |
| UK560          | 7 (100.0%)  | Apr-15, Apr-27 |                 7 | B.1.5            |                              29 | 0.069            |
| UK555          | 6 (100.0%)  | Apr-13, Apr-25 |                 6 | B.1.5            |                              31 | 0.0774           |
| UK133          | 6 (100.0%)  | Mar-22, Apr-25 |                 6 | B.1              |                              31 | 0.2194           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | EDIN     |            10 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK36 |   UK2464 |   UK5 |   UK53 |   UK44 |   UK296 |   UK21 |   UK2912 |   UK461 |   UK558 |
|:------------------|-------:|---------:|------:|-------:|-------:|--------:|-------:|---------:|--------:|--------:|
| 2020-03-15        |      1 |        2 |     1 |      0 |      1 |       0 |      2 |        0 |       0 |       0 |
| 2020-03-22        |      2 |        4 |     2 |      0 |      3 |       0 |      1 |        0 |       0 |       0 |
| 2020-03-29        |      4 |        5 |     1 |      0 |      3 |       0 |      2 |        0 |       0 |       0 |
| 2020-04-05        |      3 |        4 |     2 |      0 |      2 |       1 |      0 |        0 |       0 |       0 |
| 2020-04-12        |      6 |        2 |     2 |      1 |      1 |       1 |      3 |        2 |       1 |       0 |
| 2020-04-19        |      5 |        2 |     3 |      1 |      2 |       1 |      2 |        1 |       2 |       1 |
| 2020-04-26        |      4 |        2 |     3 |      2 |      1 |       2 |      1 |        4 |       1 |       1 |
| 2020-05-03        |      1 |        3 |     3 |      1 |      0 |       0 |      2 |        1 |       1 |       2 |
| 2020-05-10        |      0 |        2 |     0 |      1 |      0 |       1 |      0 |        1 |       1 |       1 |
| 2020-05-17        |      0 |        0 |     1 |      2 |      0 |       0 |      1 |        0 |       1 |       1 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-04 |                            1 |                                1 |       2 |
| 2020-03-05 |                            1 |                                0 |       1 |
| 2020-03-06 |                            1 |                                1 |       2 |
| 2020-03-07 |                            2 |                                0 |       2 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-09 |                            3 |                                1 |       4 |
| 2020-03-11 |                            8 |                                1 |       9 |
| 2020-03-12 |                            8 |                                1 |       9 |
| 2020-03-13 |                            4 |                                0 |       4 |
| 2020-03-14 |                            2 |                                0 |       2 |
| 2020-03-15 |                            2 |                                0 |       2 |
| 2020-03-17 |                            1 |                                2 |       3 |
| 2020-03-18 |                            1 |                                5 |       6 |
| 2020-03-19 |                            2 |                                0 |       2 |
| 2020-03-20 |                            5 |                                4 |       9 |
| 2020-03-21 |                            9 |                                4 |      13 |
| 2020-03-22 |                            7 |                                2 |       9 |
| 2020-03-23 |                            6 |                                1 |       7 |
| 2020-03-24 |                            9 |                                0 |       9 |
| 2020-03-25 |                            2 |                                2 |       4 |
| 2020-03-26 |                            9 |                                2 |      11 |
| 2020-03-27 |                           15 |                                1 |      16 |
| 2020-03-28 |                            9 |                                1 |      10 |
| 2020-03-29 |                            5 |                                1 |       6 |
| 2020-03-30 |                           20 |                                5 |      25 |
| 2020-03-31 |                           16 |                                4 |      20 |
| 2020-04-01 |                           13 |                                1 |      14 |
| 2020-04-02 |                           10 |                                1 |      11 |
| 2020-04-03 |                           12 |                                1 |      13 |
| 2020-04-04 |                           12 |                                2 |      14 |
| 2020-04-05 |                           11 |                                2 |      13 |
| 2020-04-06 |                           17 |                                1 |      18 |
| 2020-04-07 |                           11 |                                1 |      12 |
| 2020-04-08 |                            7 |                                2 |       9 |
| 2020-04-09 |                            3 |                                0 |       3 |
| 2020-04-10 |                            1 |                                1 |       2 |
| 2020-04-11 |                            1 |                                1 |       2 |
| 2020-04-12 |                            6 |                                2 |       8 |
| 2020-04-13 |                            5 |                                5 |      10 |
| 2020-04-14 |                            5 |                                1 |       6 |
| 2020-04-15 |                            8 |                                3 |      11 |
| 2020-04-16 |                            3 |                                5 |       8 |
| 2020-04-17 |                            4 |                                1 |       5 |
| 2020-04-18 |                            1 |                                1 |       2 |
| 2020-04-19 |                            9 |                                1 |      10 |
| 2020-04-20 |                            7 |                                2 |       9 |
| 2020-04-21 |                            6 |                                0 |       6 |
| 2020-04-22 |                            3 |                                1 |       4 |
| 2020-04-23 |                            3 |                                3 |       6 |
| 2020-04-24 |                            7 |                                3 |      10 |
| 2020-04-25 |                            1 |                                3 |       4 |
| 2020-04-26 |                            2 |                                1 |       3 |
| 2020-04-27 |                            5 |                                1 |       6 |
| 2020-04-28 |                            3 |                                0 |       3 |
| 2020-04-29 |                            5 |                                0 |       5 |
| 2020-04-30 |                            4 |                                0 |       4 |
| 2020-05-01 |                            6 |                                0 |       6 |
| 2020-05-02 |                            1 |                                0 |       1 |
| 2020-05-03 |                            1 |                                2 |       3 |
| 2020-05-04 |                            2 |                                0 |       2 |
| 2020-05-05 |                            2 |                                1 |       3 |
| 2020-05-06 |                            2 |                                0 |       2 |
| 2020-05-08 |                            4 |                                0 |       4 |
| 2020-05-09 |                            1 |                                1 |       2 |
| 2020-05-10 |                            3 |                                0 |       3 |
| 2020-05-11 |                            1 |                                0 |       1 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-13 |                            1 |                                1 |       2 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            4 |                                0 |       4 |
| 2020-05-18 |                            1 |                                0 |       1 |
| 2020-05-19 |                            3 |                                0 |       3 |
| 2020-05-21 |                            2 |                                0 |       2 |
| 2020-05-22 |                            1 |                                0 |       1 |
| 2020-05-23 |                            2 |                                0 |       2 |
| 2020-05-24 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   Scotland |
|:-----------|-----------:|
| 2020-03-04 |          2 |
| 2020-03-05 |          1 |
| 2020-03-06 |          2 |
| 2020-03-07 |          2 |
| 2020-03-08 |          1 |
| 2020-03-09 |          4 |
| 2020-03-10 |          1 |
| 2020-03-11 |          9 |
| 2020-03-12 |         10 |
| 2020-03-13 |          5 |
| 2020-03-14 |          3 |
| 2020-03-15 |          3 |
| 2020-03-17 |          5 |
| 2020-03-18 |          7 |
| 2020-03-19 |          3 |
| 2020-03-20 |         11 |
| 2020-03-21 |         14 |
| 2020-03-22 |         16 |
| 2020-03-23 |         16 |
| 2020-03-24 |         12 |
| 2020-03-25 |          8 |
| 2020-03-26 |         18 |
| 2020-03-27 |         20 |
| 2020-03-28 |         13 |
| 2020-03-29 |         11 |
| 2020-03-30 |         37 |
| 2020-03-31 |         30 |
| 2020-04-01 |         26 |
| 2020-04-02 |         24 |
| 2020-04-03 |         23 |
| 2020-04-04 |         27 |
| 2020-04-05 |         20 |
| 2020-04-06 |         27 |
| 2020-04-07 |         23 |
| 2020-04-08 |         18 |
| 2020-04-09 |          7 |
| 2020-04-10 |          7 |
| 2020-04-11 |         11 |
| 2020-04-12 |         18 |
| 2020-04-13 |         29 |
| 2020-04-14 |         32 |
| 2020-04-15 |         25 |
| 2020-04-16 |         27 |
| 2020-04-17 |         13 |
| 2020-04-18 |         22 |
| 2020-04-19 |         25 |
| 2020-04-20 |         32 |
| 2020-04-21 |         27 |
| 2020-04-22 |         28 |
| 2020-04-23 |         23 |
| 2020-04-24 |         35 |
| 2020-04-25 |         28 |
| 2020-04-26 |         21 |
| 2020-04-27 |         31 |
| 2020-04-28 |         16 |
| 2020-04-29 |         16 |
| 2020-04-30 |         20 |
| 2020-05-01 |         17 |
| 2020-05-02 |          4 |
| 2020-05-03 |         14 |
| 2020-05-04 |          6 |
| 2020-05-05 |         13 |
| 2020-05-06 |         17 |
| 2020-05-07 |          2 |
| 2020-05-08 |         10 |
| 2020-05-09 |          2 |
| 2020-05-10 |          9 |
| 2020-05-11 |          3 |
| 2020-05-12 |          4 |
| 2020-05-13 |          8 |
| 2020-05-14 |          1 |
| 2020-05-15 |          7 |
| 2020-05-16 |          1 |
| 2020-05-17 |          7 |
| 2020-05-18 |          3 |
| 2020-05-19 |          8 |
| 2020-05-20 |          8 |
| 2020-05-21 |          4 |
| 2020-05-22 |          2 |
| 2020-05-23 |          4 |
| 2020-05-24 |          2 |
| 2020-05-25 |          2 |
| 2020-05-26 |          1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country   |   Number of sequences | Sequence group   |
|:-----------------------|:----------|----------------------:|:-----------------|
| ABERDEEN               | Scotland  |                     1 | 1-10             |
| ABERDEENSHIRE          | Scotland  |                     5 | 1-10             |
| ANGUS                  | Scotland  |                    13 | 10-50            |
| CLACKMANNANSHIRE       | Scotland  |                     2 | 1-10             |
| DUMFRIES AND GALLOWAY  | Scotland  |                     2 | 1-10             |
| DUNDEE                 | Scotland  |                    82 | 50-100           |
| EAST LOTHIAN           | Scotland  |                    54 | 50-100           |
| EDINBURGH              | Scotland  |                   416 | 400-500          |
| FALKIRK                | Scotland  |                     4 | 1-10             |
| FIFE                   | Scotland  |                    43 | 10-50            |
| GLASGOW                | Scotland  |                     1 | 1-10             |
| MIDLOTHIAN             | Scotland  |                   131 | 100-150          |
| NORTHUMBERLAND         | England   |                     3 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland  |                    18 | 10-50            |
| SCOTTISH BORDERS       | Scotland  |                   132 | 100-150          |
| SOUTH LANARKSHIRE      | Scotland  |                     4 | 1-10             |
| WEST LOTHIAN           | Scotland  |                    95 | 50-100           |

\pagebreak






