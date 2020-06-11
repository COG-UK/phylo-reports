







# Lineages report for OXON




This report gives summaries of UK specific lineages sequenced by OXON for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-04-14. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
363 sequences in the UK from the sequencing centre OXON have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 192 and the maximum is 201


Sequences which were replicates or too error-prone were removed from this analysis.



186 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 6 that remain:
6 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK238          | 41 (100.0%) | Mar-19, Apr-14 |                41 | B.1.1            |                               0 | active today     |
| UK514          | 19 (100.0%) | Mar-30, Apr-13 |                19 | B.1.1            |                               1 | 0.7778           |
| UK5            | 17 (100.0%) | Mar-17, Apr-12 |                17 | B.1.1.1          |                               2 | 0.8125           |
| UK888          | 14 (100.0%) | Apr-05, Apr-08 |                14 | B.1.1            |                               6 | 0.0385           |
| UK311          | 9 (100.0%)  | Mar-20, Apr-11 |                 9 | B.1.1            |                               3 | 0.9167           |
| UK89           | 7 (100.0%)  | Apr-05, Apr-08 |                 7 | B.1.1.9          |                               6 | 0.0833           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/OXON/figures/report_OXON_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 52 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/OXON/figures/report_OXON_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/OXON/figures/report_OXON_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/OXON/figures/report_OXON_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/OXON/figures/report_OXON_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 275 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/OXON/figures/report_OXON_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK238          | 41 (100.0%) | Mar-19, Apr-14 |                41 | B.1.1            |                               0 | active today     |
| UK514          | 19 (100.0%) | Mar-30, Apr-13 |                19 | B.1.1            |                               1 | 0.7778           |
| UK5            | 17 (100.0%) | Mar-17, Apr-12 |                17 | B.1.1.1          |                               2 | 0.8125           |
| UK888          | 14 (100.0%) | Apr-05, Apr-08 |                14 | B.1.1            |                               6 | 0.0385           |
| UK311          | 9 (100.0%)  | Mar-20, Apr-11 |                 9 | B.1.1            |                               3 | 0.9167           |
| UK89           | 7 (100.0%)  | Apr-05, Apr-08 |                 7 | B.1.1.9          |                               6 | 0.0833           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | OXON     |            52 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK238 |   UK514 |   UK5 |   UK888 |   UK311 |   UK89 |
|:------------------|--------:|--------:|------:|--------:|--------:|-------:|
| 2020-03-15        |       1 |       0 |     1 |       0 |       1 |      0 |
| 2020-03-22        |       0 |       0 |     1 |       0 |       0 |      0 |
| 2020-03-29        |       1 |       1 |     1 |       0 |       2 |      0 |
| 2020-04-05        |       2 |       1 |     2 |       2 |       1 |      3 |
| 2020-04-12        |       1 |       1 |     1 |       0 |       0 |      0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-08 |                            1 |                                0 |       1 |
| 2020-03-12 |                            1 |                                0 |       1 |
| 2020-03-16 |                            1 |                                0 |       1 |
| 2020-03-17 |                            1 |                                2 |       3 |
| 2020-03-19 |                            0 |                                1 |       1 |
| 2020-03-20 |                            1 |                                1 |       2 |
| 2020-03-23 |                            4 |                                0 |       4 |
| 2020-03-24 |                            0 |                                2 |       2 |
| 2020-03-27 |                            2 |                                0 |       2 |
| 2020-03-28 |                            2 |                                0 |       2 |
| 2020-03-29 |                            1 |                                0 |       1 |
| 2020-03-30 |                            1 |                                1 |       2 |
| 2020-04-01 |                            1 |                                0 |       1 |
| 2020-04-04 |                            4 |                                3 |       7 |
| 2020-04-05 |                           23 |                                9 |      32 |
| 2020-04-06 |                           19 |                                4 |      23 |
| 2020-04-07 |                           40 |                               10 |      50 |
| 2020-04-08 |                           12 |                                5 |      17 |
| 2020-04-09 |                            9 |                                1 |      10 |
| 2020-04-10 |                            9 |                                0 |       9 |
| 2020-04-11 |                            8 |                                2 |      10 |
| 2020-04-12 |                            7 |                                0 |       7 |
| 2020-04-13 |                            4 |                                0 |       4 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-08 |         1 |
| 2020-03-12 |         1 |
| 2020-03-16 |         1 |
| 2020-03-17 |         3 |
| 2020-03-19 |         1 |
| 2020-03-20 |         2 |
| 2020-03-23 |         5 |
| 2020-03-24 |         3 |
| 2020-03-27 |         2 |
| 2020-03-28 |         2 |
| 2020-03-29 |         4 |
| 2020-03-30 |         3 |
| 2020-04-01 |         2 |
| 2020-04-02 |         1 |
| 2020-04-04 |         8 |
| 2020-04-05 |        57 |
| 2020-04-06 |        36 |
| 2020-04-07 |        87 |
| 2020-04-08 |        47 |
| 2020-04-09 |        21 |
| 2020-04-10 |        26 |
| 2020-04-11 |        18 |
| 2020-04-12 |        16 |
| 2020-04-13 |        15 |
| 2020-04-14 |         1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country   |   Number of sequences | Sequence group   |
|:-----------------|:----------|----------------------:|:-----------------|
| BUCKINGHAMSHIRE  | England   |                    10 | 10-50            |
| HAMPSHIRE        | England   |                     9 | 1-10             |
| HERTFORDSHIRE    | England   |                     1 | 1-10             |
| NORTHAMPTONSHIRE | England   |                     1 | 1-10             |
| OXFORDSHIRE      | England   |                    67 | 50-100           |

\pagebreak






