







# Lineages report for PORT




This report gives summaries of UK specific lineages sequenced by PORT for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-09. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
205 sequences in the UK from the sequencing centre PORT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 23 and the maximum is 79


Sequences which were replicates or too error-prone were removed from this analysis.



19 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 5 that remain:
2 are pending extinction, ie last seen three weeks ago.
2 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England     | Date range     |   Total sequences | Global lineage          |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:------------------------|--------------------------------:|:-----------------|
| UK5            | 62 (100.0%) | Mar-24, Jun-09 |                62 | B.1.1.1, B.1.1.4, B.1.1 |                               0 | active today     |
| UK107          | 29 (100.0%) | Mar-19, May-07 |                29 | B.2.1                   |                              33 | 0.053            |
| UK2464         | 19 (100.0%) | Mar-22, May-25 |                19 | B.1.p11                 |                              15 | 0.237            |
| UK2906         | 15 (100.0%) | Mar-21, Jun-02 |                15 | B.1                     |                               7 | 0.7449           |
| UK161          | 14 (100.0%) | Mar-26, May-09 |                14 | B.1.1                   |                              31 | 0.1092           |
| UK2045         | 11 (100.0%) | Apr-21, May-09 |                11 | B.1                     |                              31 | 0.0581           |
| UK370          | 10 (100.0%) | Apr-26, Jun-02 |                10 | B.1.1.10                |                               7 | 0.5873           |
| UK2888         | 8 (100.0%)  | Apr-12, May-14 |                 8 | B.1.1                   |                              26 | 0.1758           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/PORT/figures/report_PORT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 24 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/PORT/figures/report_PORT_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/PORT/figures/report_PORT_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/PORT/figures/report_PORT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/PORT/figures/report_PORT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 35 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/PORT/figures/report_PORT_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England     | Date range     |   Total sequences | Global lineage          |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:------------------------|--------------------------------:|:-----------------|
| UK5            | 62 (100.0%) | Mar-24, Jun-09 |                62 | B.1.1.1, B.1.1.4, B.1.1 |                               0 | active today     |
| UK107          | 29 (100.0%) | Mar-19, May-07 |                29 | B.2.1                   |                              33 | 0.053            |
| UK2464         | 19 (100.0%) | Mar-22, May-25 |                19 | B.1.p11                 |                              15 | 0.237            |
| UK2906         | 15 (100.0%) | Mar-21, Jun-02 |                15 | B.1                     |                               7 | 0.7449           |
| UK161          | 14 (100.0%) | Mar-26, May-09 |                14 | B.1.1                   |                              31 | 0.1092           |
| UK2045         | 11 (100.0%) | Apr-21, May-09 |                11 | B.1                     |                              31 | 0.0581           |
| UK370          | 10 (100.0%) | Apr-26, Jun-02 |                10 | B.1.1.10                |                               7 | 0.5873           |
| UK2888         | 8 (100.0%)  | Apr-12, May-14 |                 8 | B.1.1                   |                              26 | 0.1758           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | PORT     |            24 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2464 |   UK2906 |   UK370 |   UK2888 |
|:------------------|------:|---------:|---------:|--------:|---------:|
| 2020-03-15        |     0 |        0 |        1 |       0 |        0 |
| 2020-03-22        |     1 |        1 |        0 |       0 |        0 |
| 2020-03-29        |     1 |        1 |        1 |       0 |        0 |
| 2020-04-05        |     1 |        1 |        1 |       0 |        0 |
| 2020-04-12        |     2 |        0 |        0 |       0 |        2 |
| 2020-04-19        |     2 |        1 |        0 |       0 |        2 |
| 2020-04-26        |     1 |        1 |        0 |       1 |        1 |
| 2020-05-03        |     1 |        0 |        0 |       1 |        0 |
| 2020-05-10        |     1 |        0 |        1 |       0 |        1 |
| 2020-05-17        |     0 |        0 |        1 |       0 |        0 |
| 2020-05-24        |     0 |        1 |        0 |       0 |        0 |
| 2020-05-31        |     0 |        0 |        1 |       1 |        0 |
| 2020-06-07        |     2 |        0 |        0 |       0 |        0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-19 |                            1 |                                2 |       3 |
| 2020-03-21 |                            0 |                                1 |       1 |
| 2020-03-22 |                            0 |                                1 |       1 |
| 2020-03-24 |                            0 |                                2 |       2 |
| 2020-03-25 |                            0 |                                1 |       1 |
| 2020-03-26 |                            1 |                                1 |       2 |
| 2020-03-30 |                            3 |                                2 |       5 |
| 2020-03-31 |                            1 |                                1 |       2 |
| 2020-04-11 |                            0 |                                1 |       1 |
| 2020-04-12 |                            1 |                                1 |       2 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-21 |                            0 |                                2 |       2 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-26 |                            0 |                                1 |       1 |
| 2020-05-05 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-19 |         5 |
| 2020-03-20 |         3 |
| 2020-03-21 |         1 |
| 2020-03-22 |         1 |
| 2020-03-23 |         1 |
| 2020-03-24 |         7 |
| 2020-03-25 |         8 |
| 2020-03-26 |         6 |
| 2020-03-30 |        15 |
| 2020-03-31 |        11 |
| 2020-04-11 |         5 |
| 2020-04-12 |         8 |
| 2020-04-13 |         1 |
| 2020-04-16 |         1 |
| 2020-04-17 |         2 |
| 2020-04-20 |        10 |
| 2020-04-21 |         6 |
| 2020-04-22 |         2 |
| 2020-04-23 |        16 |
| 2020-04-24 |        11 |
| 2020-04-25 |         2 |
| 2020-04-26 |         3 |
| 2020-04-27 |        13 |
| 2020-04-28 |        10 |
| 2020-04-29 |         4 |
| 2020-04-30 |         5 |
| 2020-05-01 |         7 |
| 2020-05-02 |         1 |
| 2020-05-03 |         1 |
| 2020-05-05 |         3 |
| 2020-05-06 |         6 |
| 2020-05-07 |         6 |
| 2020-05-08 |         3 |
| 2020-05-09 |         2 |
| 2020-05-10 |         1 |
| 2020-05-12 |         8 |
| 2020-05-14 |         2 |
| 2020-05-15 |         1 |
| 2020-05-22 |         1 |
| 2020-05-25 |         1 |
| 2020-06-02 |         2 |
| 2020-06-07 |         1 |
| 2020-06-08 |         1 |
| 2020-06-09 |         1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2    | Country   |   Number of sequences | Sequence group   |
|:----------|:----------|----------------------:|:-----------------|
| HAMPSHIRE | England   |                   168 | 150-200          |

\pagebreak






