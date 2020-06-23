







# Lineages report for SHEF




This report gives summaries of UK specific lineages sequenced by SHEF for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-01. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1398 sequences in the UK from the sequencing centre SHEF have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 57 and the maximum is 488


Sequences which were replicates or too error-prone were removed from this analysis.



96 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 7 that remain:
2 are pending extinction, ie last seen three weeks ago.
2 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 722 (100.0%) | Mar-02, Jun-01 |               722 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK319          | 70 (100.0%)  | Mar-28, Jun-01 |                70 | B.1              |                               0 | active today     |
| UK107          | 64 (100.0%)  | Mar-05, May-03 |                64 | B.2.1            |                              29 | 0.0323           |
| UK42           | 29 (100.0%)  | Mar-20, Apr-22 |                29 | B.1              |                              40 | 0.0295           |
| UK240          | 24 (100.0%)  | Mar-20, Apr-27 |                24 | B, B.2           |                              35 | 0.0472           |
| UK51           | 22 (100.0%)  | Mar-25, May-25 |                22 | B.1.36           |                               7 | 0.415            |
| UK2916         | 22 (100.0%)  | Mar-03, Apr-23 |                22 | B.1              |                              39 | 0.0623           |
| UK24           | 19 (100.0%)  | Mar-21, Apr-10 |                19 | B.2.1            |                              52 | 0.0214           |
| UK167          | 18 (100.0%)  | Mar-24, May-01 |                18 | B.1              |                              31 | 0.0721           |
| UK384          | 18 (100.0%)  | Mar-15, Apr-02 |                18 | B.2.1            |                              60 | 0.0176           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SHEF/figures/report_SHEF_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 18 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SHEF/figures/report_SHEF_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SHEF/figures/report_SHEF_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SHEF/figures/report_SHEF_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SHEF/figures/report_SHEF_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 5 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SHEF/figures/report_SHEF_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 722 (100.0%) | Mar-02, Jun-01 |               722 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK319          | 70 (100.0%)  | Mar-28, Jun-01 |                70 | B.1              |                               0 | active today     |
| UK107          | 64 (100.0%)  | Mar-05, May-03 |                64 | B.2.1            |                              29 | 0.0323           |
| UK42           | 29 (100.0%)  | Mar-20, Apr-22 |                29 | B.1              |                              40 | 0.0295           |
| UK240          | 24 (100.0%)  | Mar-20, Apr-27 |                24 | B, B.2           |                              35 | 0.0472           |
| UK51           | 22 (100.0%)  | Mar-25, May-25 |                22 | B.1.36           |                               7 | 0.415            |
| UK2916         | 22 (100.0%)  | Mar-03, Apr-23 |                22 | B.1              |                              39 | 0.0623           |
| UK24           | 19 (100.0%)  | Mar-21, Apr-10 |                19 | B.2.1            |                              52 | 0.0214           |
| UK167          | 18 (100.0%)  | Mar-24, May-01 |                18 | B.1              |                              31 | 0.0721           |
| UK384          | 18 (100.0%)  | Mar-15, Apr-02 |                18 | B.2.1            |                              60 | 0.0176           |
| UK2539         | 18 (100.0%)  | Mar-24, May-14 |                18 | B.1.1.5          |                              18 | 0.1667           |
| UK23           | 17 (100.0%)  | Mar-23, May-02 |                17 | B.9              |                              30 | 0.0833           |
| UK72           | 16 (100.0%)  | Mar-01, Apr-09 |                16 | B                |                              53 | 0.0491           |
| UK6            | 16 (100.0%)  | Mar-22, May-01 |                16 | B.1              |                              31 | 0.086            |
| UK607          | 15 (100.0%)  | Mar-08, Apr-21 |                15 | B                |                              41 | 0.0767           |
| UK131          | 15 (100.0%)  | Mar-20, Apr-10 |                15 | B.15             |                              52 | 0.0288           |
| UK1177         | 15 (100.0%)  | Apr-22, May-29 |                15 | B.1.1            |                               3 | 0.881            |
| UK501          | 15 (100.0%)  | Mar-23, Apr-29 |                15 | B.1              |                              33 | 0.0801           |
| UK199          | 13 (100.0%)  | Mar-24, May-10 |                13 | B.1.5            |                              22 | 0.178            |
| UK5741         | 13 (100.0%)  | Mar-29, May-01 |                13 | B.1              |                              31 | 0.0887           |
| UK85           | 12 (100.0%)  | Mar-20, Apr-09 |                12 | B.3              |                              53 | 0.0343           |
| UK2735         | 10 (100.0%)  | Mar-24, Apr-21 |                10 | B.1.1            |                              41 | 0.0759           |
| UK5561         | 10 (100.0%)  | Mar-06, Apr-06 |                10 | B.2.2            |                              56 | 0.0615           |
| UK601          | 10 (100.0%)  | Mar-22, Apr-29 |                10 | B.10             |                              33 | 0.1279           |
| UK15           | 9 (100.0%)   | Mar-02, Apr-01 |                 9 | B.1.1            |                              61 | 0.0615           |
| UK12           | 8 (100.0%)   | Mar-26, Apr-22 |                 8 | B.1.p11          |                              40 | 0.0964           |
| UK4            | 7 (100.0%)   | Mar-07, Apr-02 |                 7 | B                |                              60 | 0.0722           |
| UK173          | 6 (100.0%)   | Mar-22, Mar-30 |                 6 | B                |                              63 | 0.0254           |
| UK116          | 6 (100.0%)   | Mar-24, Apr-02 |                 6 | B.1              |                              60 | 0.03             |
| UK2464         | 6 (100.0%)   | Mar-28, May-22 |                 6 | B.1.p11          |                              10 | 1.1              |
| UK5084         | 6 (100.0%)   | Mar-29, Apr-16 |                 6 | B.1              |                              46 | 0.0783           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | SHEF     |            18 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK319 |   UK51 |   UK2539 |   UK1177 |   UK199 |   UK2464 |
|:------------------|------:|--------:|-------:|---------:|---------:|--------:|---------:|
| 2020-03-01        |     1 |       0 |      0 |        0 |        0 |       0 |        0 |
| 2020-03-08        |     1 |       0 |      0 |        0 |        0 |       0 |        0 |
| 2020-03-15        |     2 |       0 |      0 |        0 |        0 |       0 |        0 |
| 2020-03-22        |     2 |       1 |      1 |        1 |        0 |       1 |        1 |
| 2020-03-29        |     1 |       1 |      1 |        1 |        0 |       1 |        1 |
| 2020-04-05        |     2 |       1 |      1 |        1 |        0 |       1 |        0 |
| 2020-04-12        |     3 |       1 |      1 |        0 |        0 |       1 |        0 |
| 2020-04-19        |     1 |       1 |      1 |        1 |        1 |       0 |        1 |
| 2020-04-26        |     1 |       1 |      1 |        0 |        1 |       0 |        1 |
| 2020-05-03        |     1 |       1 |      1 |        1 |        0 |       0 |        0 |
| 2020-05-10        |     1 |       1 |      1 |        1 |        1 |       1 |        0 |
| 2020-05-17        |     1 |       0 |      0 |        0 |        0 |       0 |        1 |
| 2020-05-24        |     1 |       0 |      1 |        0 |        1 |       0 |        0 |
| 2020-05-31        |     1 |       1 |      0 |        0 |        0 |       0 |        0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-01 |                            0 |                                1 |       1 |
| 2020-03-02 |                            0 |                                3 |       3 |
| 2020-03-03 |                            0 |                                1 |       1 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-06 |                            0 |                                1 |       1 |
| 2020-03-07 |                            0 |                                1 |       1 |
| 2020-03-08 |                            1 |                                1 |       2 |
| 2020-03-15 |                            0 |                                1 |       1 |
| 2020-03-16 |                            1 |                                0 |       1 |
| 2020-03-17 |                            0 |                                1 |       1 |
| 2020-03-19 |                            2 |                                1 |       3 |
| 2020-03-20 |                            1 |                                5 |       6 |
| 2020-03-21 |                            1 |                                4 |       5 |
| 2020-03-22 |                            2 |                                3 |       5 |
| 2020-03-23 |                            2 |                                4 |       6 |
| 2020-03-24 |                            7 |                                7 |      14 |
| 2020-03-25 |                            9 |                                5 |      14 |
| 2020-03-26 |                            3 |                                3 |       6 |
| 2020-03-27 |                            1 |                                3 |       4 |
| 2020-03-28 |                            0 |                                2 |       2 |
| 2020-03-29 |                            1 |                                3 |       4 |
| 2020-03-30 |                            1 |                                1 |       2 |
| 2020-03-31 |                            1 |                                0 |       1 |
| 2020-04-01 |                            3 |                                1 |       4 |
| 2020-04-02 |                            2 |                                3 |       5 |
| 2020-04-03 |                            4 |                                0 |       4 |
| 2020-04-04 |                            2 |                                0 |       2 |
| 2020-04-05 |                            4 |                                0 |       4 |
| 2020-04-06 |                            1 |                                0 |       1 |
| 2020-04-09 |                            1 |                                0 |       1 |
| 2020-04-10 |                            1 |                                0 |       1 |
| 2020-04-11 |                            2 |                                1 |       3 |
| 2020-04-13 |                            1 |                                0 |       1 |
| 2020-04-14 |                            1 |                                0 |       1 |
| 2020-04-15 |                            2 |                                0 |       2 |
| 2020-04-16 |                            2 |                                0 |       2 |
| 2020-04-19 |                            1 |                                1 |       2 |
| 2020-04-20 |                            1 |                                0 |       1 |
| 2020-04-21 |                            1 |                                0 |       1 |
| 2020-04-22 |                            0 |                                1 |       1 |
| 2020-04-23 |                            1 |                                1 |       2 |
| 2020-04-27 |                            1 |                                0 |       1 |
| 2020-04-28 |                            1 |                                0 |       1 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-30 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-01 |         1 |
| 2020-03-02 |         4 |
| 2020-03-03 |         2 |
| 2020-03-05 |         1 |
| 2020-03-06 |         1 |
| 2020-03-07 |         1 |
| 2020-03-08 |         2 |
| 2020-03-09 |         2 |
| 2020-03-12 |         3 |
| 2020-03-13 |         1 |
| 2020-03-15 |         3 |
| 2020-03-16 |         5 |
| 2020-03-17 |         4 |
| 2020-03-18 |        13 |
| 2020-03-19 |         9 |
| 2020-03-20 |        14 |
| 2020-03-21 |        24 |
| 2020-03-22 |        24 |
| 2020-03-23 |        31 |
| 2020-03-24 |        53 |
| 2020-03-25 |        73 |
| 2020-03-26 |        53 |
| 2020-03-27 |        36 |
| 2020-03-28 |        30 |
| 2020-03-29 |        30 |
| 2020-03-30 |        55 |
| 2020-03-31 |        30 |
| 2020-04-01 |        53 |
| 2020-04-02 |        70 |
| 2020-04-03 |        35 |
| 2020-04-04 |        19 |
| 2020-04-05 |        13 |
| 2020-04-06 |        18 |
| 2020-04-07 |        11 |
| 2020-04-08 |        22 |
| 2020-04-09 |        34 |
| 2020-04-10 |        39 |
| 2020-04-11 |        40 |
| 2020-04-12 |        24 |
| 2020-04-13 |        16 |
| 2020-04-14 |        26 |
| 2020-04-15 |        26 |
| 2020-04-16 |        24 |
| 2020-04-17 |        33 |
| 2020-04-18 |        34 |
| 2020-04-19 |        23 |
| 2020-04-20 |        16 |
| 2020-04-21 |        25 |
| 2020-04-22 |        33 |
| 2020-04-23 |        16 |
| 2020-04-24 |         4 |
| 2020-04-25 |         3 |
| 2020-04-26 |         6 |
| 2020-04-27 |        30 |
| 2020-04-28 |        17 |
| 2020-04-29 |        26 |
| 2020-04-30 |        12 |
| 2020-05-01 |        17 |
| 2020-05-02 |        15 |
| 2020-05-03 |         7 |
| 2020-05-04 |        10 |
| 2020-05-05 |         4 |
| 2020-05-06 |         5 |
| 2020-05-07 |         5 |
| 2020-05-08 |         9 |
| 2020-05-09 |         2 |
| 2020-05-10 |         9 |
| 2020-05-11 |        10 |
| 2020-05-12 |         3 |
| 2020-05-13 |         7 |
| 2020-05-14 |         3 |
| 2020-05-15 |         4 |
| 2020-05-16 |         2 |
| 2020-05-18 |         2 |
| 2020-05-20 |         2 |
| 2020-05-22 |         2 |
| 2020-05-23 |         3 |
| 2020-05-24 |         3 |
| 2020-05-25 |         3 |
| 2020-05-26 |         5 |
| 2020-05-27 |         5 |
| 2020-05-28 |         4 |
| 2020-05-29 |         1 |
| 2020-05-30 |         1 |
| 2020-06-01 |         2 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                   | Country   |   Number of sequences | Sequence group   |
|:-------------------------|:----------|----------------------:|:-----------------|
| DERBYSHIRE               | England   |                    14 | 10-50            |
| EAST RIDING OF YORKSHIRE | England   |                     8 | 1-10             |
| SOUTH YORKSHIRE          | England   |                  1371 | >500             |

\pagebreak






