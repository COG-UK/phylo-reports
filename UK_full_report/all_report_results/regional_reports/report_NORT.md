







# Lineages report for NORT




This report gives summaries of UK specific lineages sequenced by NORT for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-31. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
433 sequences in the UK from the sequencing centre NORT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 75 and the maximum is 283


Sequences which were replicates or too error-prone were removed from this analysis.



79 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 7 that remain:
6 are pending extinction, ie last seen three weeks ago.
1 lineage has been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 161 (100.0%) | Mar-08, May-31 |               161 | B.1.1, B.1.1.1   |                               0 | active today     |
| UK240          | 45 (100.0%)  | Mar-04, May-08 |                45 | B.2              |                              23 | 0.0642           |
| UK199          | 21 (100.0%)  | Mar-21, May-07 |                21 | B.1.5, B.1       |                              24 | 0.0979           |
| UK335          | 17 (100.0%)  | Mar-07, May-12 |                17 | B.1.1            |                              19 | 0.2171           |
| UK5561         | 15 (100.0%)  | Mar-02, Apr-02 |                15 | B.2.2            |                              59 | 0.0375           |
| UK5676         | 12 (100.0%)  | Mar-24, May-08 |                12 | B.2              |                              23 | 0.1779           |
| UK107          | 9 (100.0%)   | Mar-23, Apr-05 |                 9 | B.2.1            |                              56 | 0.029            |
| UK42           | 7 (100.0%)   | Mar-12, May-14 |                 7 | B.1              |                              17 | 0.6176           |
| UK2916         | 7 (100.0%)   | Mar-29, May-08 |                 7 | B.1              |                              23 | 0.2899           |
| UK109          | 7 (100.0%)   | Mar-19, Apr-30 |                 7 | B.1.5            |                              31 | 0.2258           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORT/figures/report_NORT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 33 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORT/figures/report_NORT_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORT/figures/report_NORT_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORT/figures/report_NORT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORT/figures/report_NORT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 41 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/NORT/figures/report_NORT_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 161 (100.0%) | Mar-08, May-31 |               161 | B.1.1, B.1.1.1   |                               0 | active today     |
| UK240          | 45 (100.0%)  | Mar-04, May-08 |                45 | B.2              |                              23 | 0.0642           |
| UK199          | 21 (100.0%)  | Mar-21, May-07 |                21 | B.1.5, B.1       |                              24 | 0.0979           |
| UK335          | 17 (100.0%)  | Mar-07, May-12 |                17 | B.1.1            |                              19 | 0.2171           |
| UK5561         | 15 (100.0%)  | Mar-02, Apr-02 |                15 | B.2.2            |                              59 | 0.0375           |
| UK5676         | 12 (100.0%)  | Mar-24, May-08 |                12 | B.2              |                              23 | 0.1779           |
| UK107          | 9 (100.0%)   | Mar-23, Apr-05 |                 9 | B.2.1            |                              56 | 0.029            |
| UK42           | 7 (100.0%)   | Mar-12, May-14 |                 7 | B.1              |                              17 | 0.6176           |
| UK2916         | 7 (100.0%)   | Mar-29, May-08 |                 7 | B.1              |                              23 | 0.2899           |
| UK109          | 7 (100.0%)   | Mar-19, Apr-30 |                 7 | B.1.5            |                              31 | 0.2258           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NORT     |            33 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK240 |   UK199 |   UK335 |   UK5676 |   UK2916 |   UK42 |
|:------------------|------:|--------:|--------:|--------:|---------:|---------:|-------:|
| 2020-03-01        |     0 |       1 |       0 |       1 |        0 |        0 |      0 |
| 2020-03-08        |     1 |       1 |       0 |       0 |        0 |        0 |      1 |
| 2020-03-15        |     2 |       1 |       1 |       0 |        0 |        0 |      0 |
| 2020-03-22        |     5 |       3 |       1 |       2 |        3 |        0 |      1 |
| 2020-03-29        |     6 |       4 |       2 |       2 |        5 |        3 |      1 |
| 2020-04-05        |     1 |       0 |       1 |       0 |        0 |        0 |      1 |
| 2020-04-12        |     1 |       0 |       0 |       0 |        1 |        0 |      0 |
| 2020-04-19        |     1 |       0 |       1 |       0 |        0 |        0 |      0 |
| 2020-04-26        |     5 |       0 |       4 |       1 |        0 |        0 |      1 |
| 2020-05-03        |     6 |       2 |       2 |       1 |        1 |        1 |      1 |
| 2020-05-10        |     5 |       0 |       0 |       2 |        0 |        0 |      1 |
| 2020-05-17        |     2 |       0 |       0 |       0 |        0 |        0 |      0 |
| 2020-05-24        |     1 |       0 |       0 |       0 |        0 |        0 |      0 |
| 2020-05-31        |     1 |       0 |       0 |       0 |        0 |        0 |      0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-02 |                            0 |                                1 |       1 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-07 |                            0 |                                1 |       1 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-10 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                2 |       2 |
| 2020-03-14 |                            1 |                                0 |       1 |
| 2020-03-15 |                            1 |                                0 |       1 |
| 2020-03-18 |                            1 |                                0 |       1 |
| 2020-03-19 |                            2 |                                1 |       3 |
| 2020-03-20 |                            3 |                                2 |       5 |
| 2020-03-21 |                            3 |                                2 |       5 |
| 2020-03-22 |                            3 |                                0 |       3 |
| 2020-03-23 |                            3 |                                4 |       7 |
| 2020-03-24 |                            3 |                                5 |       8 |
| 2020-03-25 |                            2 |                                3 |       5 |
| 2020-03-26 |                            1 |                                0 |       1 |
| 2020-03-27 |                            2 |                                1 |       3 |
| 2020-03-28 |                            1 |                                3 |       4 |
| 2020-03-29 |                            2 |                                1 |       3 |
| 2020-03-31 |                            2 |                                3 |       5 |
| 2020-04-01 |                            0 |                                1 |       1 |
| 2020-04-02 |                            4 |                                1 |       5 |
| 2020-04-03 |                            5 |                                0 |       5 |
| 2020-04-05 |                            2 |                                0 |       2 |
| 2020-04-09 |                            1 |                                0 |       1 |
| 2020-04-10 |                            2 |                                0 |       2 |
| 2020-04-14 |                            0 |                                1 |       1 |
| 2020-04-15 |                            1 |                                0 |       1 |
| 2020-04-18 |                            0 |                                1 |       1 |
| 2020-04-27 |                            1 |                                0 |       1 |
| 2020-04-28 |                            1 |                                0 |       1 |
| 2020-04-29 |                            1 |                                0 |       1 |
| 2020-05-01 |                            1 |                                0 |       1 |
| 2020-05-04 |                            0 |                                1 |       1 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-09 |                            0 |                                1 |       1 |
| 2020-05-15 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-02 |         1 |
| 2020-03-04 |         1 |
| 2020-03-07 |         1 |
| 2020-03-08 |         1 |
| 2020-03-10 |         3 |
| 2020-03-12 |         2 |
| 2020-03-14 |         1 |
| 2020-03-15 |         2 |
| 2020-03-16 |         3 |
| 2020-03-17 |         1 |
| 2020-03-18 |         2 |
| 2020-03-19 |         7 |
| 2020-03-20 |         8 |
| 2020-03-21 |         7 |
| 2020-03-22 |         9 |
| 2020-03-23 |        21 |
| 2020-03-24 |        18 |
| 2020-03-25 |        23 |
| 2020-03-26 |        18 |
| 2020-03-27 |        15 |
| 2020-03-28 |        16 |
| 2020-03-29 |        22 |
| 2020-03-30 |         8 |
| 2020-03-31 |        22 |
| 2020-04-01 |         6 |
| 2020-04-02 |        14 |
| 2020-04-03 |        26 |
| 2020-04-04 |        13 |
| 2020-04-05 |         7 |
| 2020-04-06 |         1 |
| 2020-04-07 |         3 |
| 2020-04-08 |         1 |
| 2020-04-09 |         3 |
| 2020-04-10 |         3 |
| 2020-04-11 |         3 |
| 2020-04-12 |         3 |
| 2020-04-14 |         1 |
| 2020-04-15 |         1 |
| 2020-04-16 |         3 |
| 2020-04-17 |         1 |
| 2020-04-18 |         2 |
| 2020-04-22 |         1 |
| 2020-04-23 |         2 |
| 2020-04-24 |         1 |
| 2020-04-25 |         1 |
| 2020-04-26 |         1 |
| 2020-04-27 |         9 |
| 2020-04-28 |         7 |
| 2020-04-29 |         4 |
| 2020-04-30 |         6 |
| 2020-05-01 |         8 |
| 2020-05-02 |         3 |
| 2020-05-03 |         4 |
| 2020-05-04 |         3 |
| 2020-05-05 |         2 |
| 2020-05-06 |         6 |
| 2020-05-07 |        13 |
| 2020-05-08 |        10 |
| 2020-05-09 |         4 |
| 2020-05-10 |         5 |
| 2020-05-11 |         6 |
| 2020-05-12 |         8 |
| 2020-05-13 |         4 |
| 2020-05-14 |         3 |
| 2020-05-15 |         3 |
| 2020-05-16 |         2 |
| 2020-05-17 |         2 |
| 2020-05-18 |         1 |
| 2020-05-19 |         3 |
| 2020-05-20 |         1 |
| 2020-05-22 |         2 |
| 2020-05-23 |         1 |
| 2020-05-25 |         1 |
| 2020-05-26 |         1 |
| 2020-05-30 |         1 |
| 2020-05-31 |         1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2          | Country   |   Number of sequences | Sequence group   |
|:----------------|:----------|----------------------:|:-----------------|
| CUMBRIA         | England   |                    35 | 10-50            |
| DURHAM          | England   |                    38 | 10-50            |
| NORTH YORKSHIRE | England   |                    69 | 50-100           |
| NORTHUMBERLAND  | England   |                    41 | 10-50            |
| TYNE AND WEAR   | England   |                   208 | 200-250          |
| WEST YORKSHIRE  | England   |                     1 | 1-10             |

\pagebreak






