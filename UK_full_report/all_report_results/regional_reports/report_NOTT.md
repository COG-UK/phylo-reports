







# Lineages report for NOTT




This report gives summaries of UK specific lineages sequenced by NOTT for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-27. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
915 sequences in the UK from the sequencing centre NOTT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 90 and the maximum is 329


Sequences which were replicates or too error-prone were removed from this analysis.



79 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 11 that remain:
4 are pending extinction, ie last seen three weeks ago.
3 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
3 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage            |   Time since last sample (days) |   Activity score |
|:---------------|:-------------|:---------------|------------------:|:--------------------------|--------------------------------:|-----------------:|
| UK5            | 320 (100.0%) | Mar-12, Jun-23 |               320 | B.1.1.p11, B.1.1, B.1.1.1 |                               4 |           0.0807 |
| UK2464         | 66 (100.0%)  | Mar-18, Jun-18 |                66 | B.1.p11                   |                               9 |           0.1573 |
| UK641          | 44 (100.0%)  | May-01, Jun-17 |                44 | B.1.1                     |                              10 |           0.1093 |
| UK89           | 43 (100.0%)  | Mar-22, Jun-22 |                43 | B.1.1.9                   |                               5 |           0.4381 |
| UK42           | 33 (100.0%)  | Mar-17, Apr-29 |                33 | B.1                       |                              59 |           0.0228 |
| UK4            | 32 (100.0%)  | Mar-04, Apr-29 |                32 | B                         |                              59 |           0.0306 |
| UK607          | 31 (100.0%)  | Mar-02, May-18 |                31 | B                         |                              40 |           0.0642 |
| UK5561         | 29 (100.0%)  | Mar-11, Apr-22 |                29 | B.2.2                     |                              66 |           0.0227 |
| UK107          | 24 (100.0%)  | Mar-16, Jun-02 |                24 | B.2.1                     |                              25 |           0.1357 |
| UK2787         | 22 (100.0%)  | May-30, Jun-26 |                22 | B.1.1                     |                               1 |           1.2857 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NOTT/figures/report_NOTT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 6 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NOTT/figures/report_NOTT_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NOTT/figures/report_NOTT_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NOTT/figures/report_NOTT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NOTT/figures/report_NOTT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 16 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NOTT/figures/report_NOTT_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage            |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:--------------------------|--------------------------------:|:-----------------|
| UK5            | 320 (100.0%) | Mar-12, Jun-23 |               320 | B.1.1.p11, B.1.1, B.1.1.1 |                               4 | 0.0807           |
| UK2464         | 66 (100.0%)  | Mar-18, Jun-18 |                66 | B.1.p11                   |                               9 | 0.1573           |
| UK641          | 44 (100.0%)  | May-01, Jun-17 |                44 | B.1.1                     |                              10 | 0.1093           |
| UK89           | 43 (100.0%)  | Mar-22, Jun-22 |                43 | B.1.1.9                   |                               5 | 0.4381           |
| UK42           | 33 (100.0%)  | Mar-17, Apr-29 |                33 | B.1                       |                              59 | 0.0228           |
| UK4            | 32 (100.0%)  | Mar-04, Apr-29 |                32 | B                         |                              59 | 0.0306           |
| UK607          | 31 (100.0%)  | Mar-02, May-18 |                31 | B                         |                              40 | 0.0642           |
| UK5561         | 29 (100.0%)  | Mar-11, Apr-22 |                29 | B.2.2                     |                              66 | 0.0227           |
| UK107          | 24 (100.0%)  | Mar-16, Jun-02 |                24 | B.2.1                     |                              25 | 0.1357           |
| UK2787         | 22 (100.0%)  | May-30, Jun-26 |                22 | B.1.1                     |                               1 | 1.2857           |
| UK2913         | 22 (100.0%)  | Mar-16, Jun-16 |                22 | B.1.p11                   |                              11 | 0.3983           |
| UK329          | 19 (100.0%)  | Mar-17, Apr-26 |                19 | B.1, B.1.34               |                              62 | 0.0358           |
| UK31           | 16 (100.0%)  | Mar-21, Jun-27 |                16 | B.3                       |                               0 | active today     |
| UK5676         | 12 (100.0%)  | Mar-18, May-06 |                12 | B.2                       |                              52 | 0.0857           |
| UK15           | 12 (100.0%)  | Mar-30, May-04 |                12 | B.1.1                     |                              54 | 0.0589           |
| UK199          | 11 (100.0%)  | Mar-23, Jun-08 |                11 | B.1, B.1.5                |                              19 | 0.4053           |
| UK266          | 11 (100.0%)  | Apr-06, Apr-30 |                11 | B.1                       |                              58 | 0.0414           |
| UK2916         | 10 (100.0%)  | Mar-25, Jun-10 |                10 | B.1                       |                              17 | 0.5033           |
| UK72           | 8 (100.0%)   | Mar-18, May-05 |                 8 | B, B.2.2                  |                              53 | 0.1294           |
| UK215          | 7 (100.0%)   | Mar-24, Apr-11 |                 7 | B.2                       |                              77 | 0.039            |
| UK320          | 6 (100.0%)   | Apr-11, Jun-02 |                 6 | B.1                       |                              25 | 0.416            |
| UK384          | 6 (100.0%)   | Mar-14, Mar-29 |                 6 | B.2.1                     |                              90 | 0.0333           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NOTT     |             6 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2464 |   UK641 |   UK89 |   UK107 |   UK2913 |   UK2787 |   UK31 |   UK199 |   UK2916 |
|:------------------|------:|---------:|--------:|-------:|--------:|---------:|---------:|-------:|--------:|---------:|
| 2020-03-08        |     1 |        0 |       0 |      0 |       0 |        0 |        0 |      0 |       0 |        0 |
| 2020-03-15        |     1 |        1 |       0 |      0 |       1 |        1 |        0 |      1 |       0 |        0 |
| 2020-03-22        |     2 |        1 |       0 |      1 |       1 |        2 |        0 |      1 |       1 |        1 |
| 2020-03-29        |     2 |        1 |       0 |      1 |       2 |        2 |        0 |      1 |       0 |        1 |
| 2020-04-05        |     1 |        1 |       0 |      1 |       1 |        1 |        0 |      0 |       1 |        0 |
| 2020-04-12        |     1 |        1 |       0 |      1 |       0 |        1 |        0 |      1 |       1 |        0 |
| 2020-04-19        |     2 |        1 |       0 |      1 |       0 |        0 |        0 |      0 |       0 |        0 |
| 2020-04-26        |     3 |        1 |       1 |      1 |       1 |        0 |        0 |      0 |       2 |        1 |
| 2020-05-03        |     2 |        1 |       1 |      2 |       0 |        0 |        0 |      0 |       2 |        0 |
| 2020-05-10        |     1 |        1 |       0 |      0 |       1 |        0 |        0 |      0 |       1 |        0 |
| 2020-05-17        |     1 |        1 |       1 |      1 |       1 |        0 |        0 |      0 |       0 |        0 |
| 2020-05-24        |     3 |        0 |       2 |      2 |       0 |        0 |        1 |      0 |       0 |        0 |
| 2020-05-31        |     5 |        1 |       4 |      2 |       1 |        1 |        2 |      0 |       0 |        1 |
| 2020-06-07        |     5 |        1 |       3 |      1 |       0 |        0 |        2 |      0 |       1 |        1 |
| 2020-06-14        |     3 |        2 |       1 |      1 |       0 |        1 |        1 |      0 |       0 |        0 |
| 2020-06-21        |     1 |        0 |       0 |      1 |       0 |        0 |        1 |      1 |       0 |        0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-02 |                            0 |                                1 |       1 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-11 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                2 |       2 |
| 2020-03-14 |                            1 |                                1 |       2 |
| 2020-03-16 |                            0 |                                4 |       4 |
| 2020-03-17 |                            1 |                                2 |       3 |
| 2020-03-18 |                            0 |                                3 |       3 |
| 2020-03-19 |                            1 |                                0 |       1 |
| 2020-03-20 |                            1 |                                1 |       2 |
| 2020-03-21 |                            0 |                                1 |       1 |
| 2020-03-22 |                            1 |                                2 |       3 |
| 2020-03-23 |                            0 |                                2 |       2 |
| 2020-03-24 |                            3 |                                2 |       5 |
| 2020-03-25 |                            3 |                                2 |       5 |
| 2020-03-27 |                            0 |                                1 |       1 |
| 2020-03-28 |                            2 |                                2 |       4 |
| 2020-03-29 |                            5 |                                0 |       5 |
| 2020-03-30 |                            4 |                                2 |       6 |
| 2020-03-31 |                            1 |                                0 |       1 |
| 2020-04-01 |                            2 |                                0 |       2 |
| 2020-04-02 |                            2 |                                0 |       2 |
| 2020-04-03 |                            1 |                                1 |       2 |
| 2020-04-04 |                            0 |                                2 |       2 |
| 2020-04-05 |                            4 |                                1 |       5 |
| 2020-04-06 |                            0 |                                1 |       1 |
| 2020-04-07 |                            2 |                                1 |       3 |
| 2020-04-09 |                            3 |                                1 |       4 |
| 2020-04-11 |                            0 |                                1 |       1 |
| 2020-04-13 |                            0 |                                1 |       1 |
| 2020-04-20 |                            1 |                                0 |       1 |
| 2020-04-23 |                            2 |                                0 |       2 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-26 |                            1 |                                0 |       1 |
| 2020-04-27 |                            1 |                                1 |       2 |
| 2020-04-29 |                            1 |                                2 |       3 |
| 2020-04-30 |                            2 |                                0 |       2 |
| 2020-05-01 |                            0 |                                1 |       1 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-04 |                            1 |                                1 |       2 |
| 2020-05-18 |                            1 |                                0 |       1 |
| 2020-05-30 |                            0 |                                1 |       1 |
| 2020-05-31 |                            1 |                                0 |       1 |
| 2020-06-05 |                            0 |                                1 |       1 |
| 2020-06-06 |                            1 |                                1 |       2 |
| 2020-06-13 |                            1 |                                0 |       1 |
| 2020-06-18 |                            1 |                                0 |       1 |
| 2020-06-23 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-02 |         1 |
| 2020-03-04 |         1 |
| 2020-03-07 |         1 |
| 2020-03-11 |         2 |
| 2020-03-12 |         4 |
| 2020-03-13 |         1 |
| 2020-03-14 |         6 |
| 2020-03-15 |         2 |
| 2020-03-16 |         4 |
| 2020-03-17 |         7 |
| 2020-03-18 |         9 |
| 2020-03-19 |         9 |
| 2020-03-20 |        11 |
| 2020-03-21 |        12 |
| 2020-03-22 |        16 |
| 2020-03-23 |        13 |
| 2020-03-24 |        19 |
| 2020-03-25 |        13 |
| 2020-03-26 |         3 |
| 2020-03-27 |         7 |
| 2020-03-28 |        23 |
| 2020-03-29 |        20 |
| 2020-03-30 |        31 |
| 2020-03-31 |        10 |
| 2020-04-01 |        21 |
| 2020-04-02 |        18 |
| 2020-04-03 |        23 |
| 2020-04-04 |        17 |
| 2020-04-05 |        20 |
| 2020-04-06 |         5 |
| 2020-04-07 |        20 |
| 2020-04-08 |        10 |
| 2020-04-09 |        15 |
| 2020-04-10 |        12 |
| 2020-04-11 |        19 |
| 2020-04-12 |        10 |
| 2020-04-13 |         6 |
| 2020-04-14 |         4 |
| 2020-04-15 |         3 |
| 2020-04-16 |         3 |
| 2020-04-17 |         8 |
| 2020-04-18 |         1 |
| 2020-04-19 |         4 |
| 2020-04-20 |        10 |
| 2020-04-21 |         5 |
| 2020-04-22 |        11 |
| 2020-04-23 |        16 |
| 2020-04-24 |         6 |
| 2020-04-25 |         4 |
| 2020-04-26 |         6 |
| 2020-04-27 |         7 |
| 2020-04-28 |        12 |
| 2020-04-29 |        32 |
| 2020-04-30 |        22 |
| 2020-05-01 |        20 |
| 2020-05-02 |        14 |
| 2020-05-03 |        11 |
| 2020-05-04 |        10 |
| 2020-05-05 |         8 |
| 2020-05-06 |         3 |
| 2020-05-07 |         3 |
| 2020-05-09 |         4 |
| 2020-05-11 |         3 |
| 2020-05-12 |         3 |
| 2020-05-13 |         3 |
| 2020-05-15 |         5 |
| 2020-05-16 |         3 |
| 2020-05-17 |         4 |
| 2020-05-18 |         9 |
| 2020-05-19 |         9 |
| 2020-05-20 |         5 |
| 2020-05-21 |         9 |
| 2020-05-22 |         7 |
| 2020-05-24 |         2 |
| 2020-05-26 |         6 |
| 2020-05-27 |         1 |
| 2020-05-28 |         8 |
| 2020-05-29 |         4 |
| 2020-05-30 |        20 |
| 2020-05-31 |        14 |
| 2020-06-01 |         6 |
| 2020-06-02 |         9 |
| 2020-06-03 |        10 |
| 2020-06-04 |         5 |
| 2020-06-05 |        13 |
| 2020-06-06 |         7 |
| 2020-06-07 |         6 |
| 2020-06-08 |        11 |
| 2020-06-09 |        11 |
| 2020-06-10 |        12 |
| 2020-06-11 |        14 |
| 2020-06-12 |         6 |
| 2020-06-13 |         3 |
| 2020-06-14 |         3 |
| 2020-06-15 |         6 |
| 2020-06-16 |         7 |
| 2020-06-17 |         7 |
| 2020-06-18 |         3 |
| 2020-06-19 |         2 |
| 2020-06-20 |         3 |
| 2020-06-21 |         1 |
| 2020-06-22 |         2 |
| 2020-06-23 |         3 |
| 2020-06-26 |         1 |
| 2020-06-27 |         1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country          |   Number of sequences | Sequence group   |
|:-----------------|:-----------------|----------------------:|:-----------------|
| ANTRIM           | Northern Ireland |                     1 | 1-10             |
| DERBYSHIRE       | England          |                     2 | 1-10             |
| LEICESTERSHIRE   | England          |                   104 | 100-150          |
| LINCOLNSHIRE     | England          |                    56 | 50-100           |
| NORTHAMPTONSHIRE | England          |                     3 | 1-10             |
| NOTTINGHAM       | England          |                   685 | >500             |
| NOTTINGHAMSHIRE  | England          |                    45 | 10-50            |
| STAFFORDSHIRE    | England          |                     2 | 1-10             |
| WARWICKSHIRE     | England          |                     1 | 1-10             |

\pagebreak






