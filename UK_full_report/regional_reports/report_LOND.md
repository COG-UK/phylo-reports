







# Lineages report for LOND




This report gives summaries of UK specific lineages sequenced by LOND for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-14. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
422 sequences in the UK from the sequencing centre LOND have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 40 and the maximum is 315


Sequences which were replicates or too error-prone were removed from this analysis.



74 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 12 that remain:
10 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
1 has reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 132 (100.0%) | Mar-27, May-14 |               132 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK2906         | 31 (100.0%)  | Mar-27, May-04 |                31 | B.1              |                              10 | 0.1267           |
| UK42           | 31 (100.0%)  | Mar-31, Apr-20 |                31 | B.1              |                              24 | 0.0278           |
| UK5741         | 22 (100.0%)  | Apr-02, Apr-19 |                22 | B.1              |                              25 | 0.0324           |
| UK63           | 14 (100.0%)  | Apr-02, Apr-18 |                14 | B.1.1            |                              26 | 0.0473           |
| UK2916         | 11 (100.0%)  | Mar-27, Apr-19 |                11 | B.1              |                              25 | 0.092            |
| UK107          | 11 (100.0%)  | Mar-27, Apr-20 |                11 | B.2.1            |                              24 | 0.1              |
| UK376          | 10 (100.0%)  | Apr-04, Apr-18 |                10 | B.1.1.9          |                              26 | 0.0598           |
| UK2913         | 9 (100.0%)   | Apr-03, Apr-18 |                 9 | B.1.p11          |                              26 | 0.0721           |
| UK371          | 8 (100.0%)   | Apr-04, Apr-17 |                 8 | B.1.1            |                              27 | 0.0688           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/LOND/figures/report_LOND_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 36 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/LOND/figures/report_LOND_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/LOND/figures/report_LOND_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/LOND/figures/report_LOND_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/LOND/figures/report_LOND_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 241 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/LOND/figures/report_LOND_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 132 (100.0%) | Mar-27, May-14 |               132 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK2906         | 31 (100.0%)  | Mar-27, May-04 |                31 | B.1              |                              10 | 0.1267           |
| UK42           | 31 (100.0%)  | Mar-31, Apr-20 |                31 | B.1              |                              24 | 0.0278           |
| UK5741         | 22 (100.0%)  | Apr-02, Apr-19 |                22 | B.1              |                              25 | 0.0324           |
| UK63           | 14 (100.0%)  | Apr-02, Apr-18 |                14 | B.1.1            |                              26 | 0.0473           |
| UK2916         | 11 (100.0%)  | Mar-27, Apr-19 |                11 | B.1              |                              25 | 0.092            |
| UK107          | 11 (100.0%)  | Mar-27, Apr-20 |                11 | B.2.1            |                              24 | 0.1              |
| UK376          | 10 (100.0%)  | Apr-04, Apr-18 |                10 | B.1.1.9          |                              26 | 0.0598           |
| UK2913         | 9 (100.0%)   | Apr-03, Apr-18 |                 9 | B.1.p11          |                              26 | 0.0721           |
| UK371          | 8 (100.0%)   | Apr-04, Apr-17 |                 8 | B.1.1            |                              27 | 0.0688           |
| UK9            | 7 (100.0%)   | Mar-31, Apr-08 |                 7 | B.1.13           |                              36 | 0.037            |
| UK2464         | 7 (100.0%)   | Apr-02, Apr-19 |                 7 | B.1, B.1.p11     |                              25 | 0.1133           |
| UK37           | 6 (100.0%)   | Apr-02, Apr-19 |                 6 | B.1.30           |                              25 | 0.136            |
| UK2735         | 6 (100.0%)   | Apr-06, Apr-15 |                 6 | B.1.1            |                              29 | 0.0621           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | LOND     |            36 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK42 |   UK2906 |   UK5741 |   UK63 |   UK2916 |   UK107 |   UK376 |   UK2913 |   UK371 |
|:------------------|------:|-------:|---------:|---------:|-------:|---------:|--------:|--------:|---------:|--------:|
| 2020-03-22        |     3 |      0 |        1 |        0 |      0 |        1 |       1 |       0 |        0 |       0 |
| 2020-03-29        |     4 |      3 |        5 |        2 |      2 |        1 |       2 |       1 |        2 |       1 |
| 2020-04-05        |     3 |      2 |        6 |        2 |      0 |        1 |       1 |       0 |        2 |       1 |
| 2020-04-12        |     4 |      2 |        2 |        1 |      2 |        1 |       1 |       1 |        1 |       1 |
| 2020-04-19        |     1 |      1 |        1 |        1 |      0 |        1 |       1 |       0 |        0 |       0 |
| 2020-05-03        |     0 |      0 |        1 |        0 |      0 |        0 |       0 |       0 |        0 |       0 |
| 2020-05-10        |     1 |      0 |        0 |        0 |      0 |        0 |       0 |       0 |        0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-27 |                            0 |                                4 |       4 |
| 2020-03-31 |                            3 |                                2 |       5 |
| 2020-04-02 |                            2 |                                8 |      10 |
| 2020-04-03 |                            3 |                                3 |       6 |
| 2020-04-04 |                            6 |                                9 |      15 |
| 2020-04-06 |                            5 |                                4 |       9 |
| 2020-04-08 |                            5 |                                0 |       5 |
| 2020-04-11 |                            2 |                                1 |       3 |
| 2020-04-14 |                            2 |                                3 |       5 |
| 2020-04-15 |                            5 |                                0 |       5 |
| 2020-04-16 |                            1 |                                1 |       2 |
| 2020-04-17 |                            4 |                                1 |       5 |
| 2020-04-18 |                            4 |                                1 |       5 |
| 2020-04-19 |                            4 |                                0 |       4 |
| 2020-04-20 |                            3 |                                0 |       3 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-27 |         7 |
| 2020-03-31 |        17 |
| 2020-04-02 |        24 |
| 2020-04-03 |        11 |
| 2020-04-04 |        58 |
| 2020-04-06 |        46 |
| 2020-04-08 |        21 |
| 2020-04-09 |         8 |
| 2020-04-10 |        14 |
| 2020-04-11 |        14 |
| 2020-04-13 |         5 |
| 2020-04-14 |        26 |
| 2020-04-15 |        48 |
| 2020-04-16 |        32 |
| 2020-04-17 |        41 |
| 2020-04-18 |        14 |
| 2020-04-19 |        19 |
| 2020-04-20 |         8 |
| 2020-04-22 |         1 |
| 2020-04-23 |         4 |
| 2020-04-25 |         1 |
| 2020-05-04 |         1 |
| 2020-05-14 |         2 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2          | Country   |   Number of sequences | Sequence group   |
|:----------------|:----------|----------------------:|:-----------------|
| ABERDEEN        | Scotland  |                     1 | 1-10             |
| BERKSHIRE       | England   |                     1 | 1-10             |
| BUCKINGHAMSHIRE | England   |                     1 | 1-10             |
| ESSEX           | England   |                     4 | 1-10             |
| GREATER LONDON  | England   |                    91 | 50-100           |
| HERTFORDSHIRE   | England   |                    34 | 10-50            |
| KENT            | England   |                     3 | 1-10             |
| MERSEYSIDE      | England   |                     1 | 1-10             |
| SURREY          | England   |                     2 | 1-10             |

\pagebreak






