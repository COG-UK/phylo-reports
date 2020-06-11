







# Lineages report for BIRM




This report gives summaries of UK specific lineages sequenced by BIRM for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-24. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
94 sequences in the UK from the sequencing centre BIRM have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 45 and the maximum is 48


Sequences which were replicates or too error-prone were removed from this analysis.



42 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 3 that remain:
1 has gone quiet, ie hasn't been seen this week.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 24 (100.0%) | Apr-13, May-24 |                24 | B.1.1.1          |                               0 | active today     |
| UK4442         | 17 (100.0%) | May-10, May-24 |                17 | B.1.1            |                               0 | active today     |
| UK534          | 7 (100.0%)  | Apr-13, May-13 |                 7 | B.1.1            |                              11 | 0.4545           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/BIRM/figures/report_BIRM_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 12 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/BIRM/figures/report_BIRM_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/BIRM/figures/report_BIRM_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/BIRM/figures/report_BIRM_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/BIRM/figures/report_BIRM_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 2 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/BIRM/figures/report_BIRM_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 24 (100.0%) | Apr-13, May-24 |                24 | B.1.1.1          |                               0 | active today     |
| UK4442         | 17 (100.0%) | May-10, May-24 |                17 | B.1.1            |                               0 | active today     |
| UK534          | 7 (100.0%)  | Apr-13, May-13 |                 7 | B.1.1            |                              11 | 0.4545           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | BIRM     |            12 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK4442 |   UK534 |
|:------------------|------:|---------:|--------:|
| 2020-04-12        |     1 |        0 |       1 |
| 2020-04-26        |     1 |        0 |       1 |
| 2020-05-03        |     1 |        0 |       1 |
| 2020-05-10        |     3 |        1 |       1 |
| 2020-05-17        |     2 |        1 |       0 |
| 2020-05-24        |     1 |        1 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-22 |                            1 |                                0 |       1 |
| 2020-03-23 |                            3 |                                0 |       3 |
| 2020-03-24 |                            5 |                                2 |       7 |
| 2020-03-25 |                            1 |                                0 |       1 |
| 2020-04-13 |                            0 |                                2 |       2 |
| 2020-04-14 |                            1 |                                0 |       1 |
| 2020-04-15 |                            2 |                                0 |       2 |
| 2020-04-16 |                            4 |                                0 |       4 |
| 2020-04-26 |                            1 |                                0 |       1 |
| 2020-04-27 |                            2 |                                0 |       2 |
| 2020-04-29 |                            1 |                                0 |       1 |
| 2020-05-01 |                            1 |                                1 |       2 |
| 2020-05-04 |                            3 |                                0 |       3 |
| 2020-05-05 |                            4 |                                0 |       4 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-09 |                            1 |                                0 |       1 |
| 2020-05-10 |                            2 |                                1 |       3 |
| 2020-05-11 |                            1 |                                0 |       1 |
| 2020-05-18 |                            1 |                                0 |       1 |
| 2020-05-19 |                            1 |                                0 |       1 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-05-24 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-22 |         1 |
| 2020-03-23 |         3 |
| 2020-03-24 |         8 |
| 2020-03-25 |         1 |
| 2020-04-13 |         2 |
| 2020-04-14 |         3 |
| 2020-04-15 |         4 |
| 2020-04-16 |         7 |
| 2020-04-26 |         5 |
| 2020-04-27 |         2 |
| 2020-04-29 |         2 |
| 2020-05-01 |         2 |
| 2020-05-03 |         1 |
| 2020-05-04 |         3 |
| 2020-05-05 |         5 |
| 2020-05-07 |         1 |
| 2020-05-08 |         1 |
| 2020-05-09 |         1 |
| 2020-05-10 |         4 |
| 2020-05-11 |         7 |
| 2020-05-12 |         1 |
| 2020-05-13 |         1 |
| 2020-05-14 |         2 |
| 2020-05-16 |         2 |
| 2020-05-18 |         1 |
| 2020-05-19 |         5 |
| 2020-05-20 |         4 |
| 2020-05-21 |         2 |
| 2020-05-22 |         5 |
| 2020-05-23 |         3 |
| 2020-05-24 |         5 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2         | Country   |   Number of sequences | Sequence group   |
|:---------------|:----------|----------------------:|:-----------------|
| HEREFORDSHIRE  | England   |                     3 | 1-10             |
| STAFFORDSHIRE  | England   |                    21 | 10-50            |
| WEST MIDLANDS  | England   |                    45 | 10-50            |
| WORCESTERSHIRE | England   |                     5 | 1-10             |

\pagebreak






