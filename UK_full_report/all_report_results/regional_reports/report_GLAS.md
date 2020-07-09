







# Lineages report for GLAS




This report gives summaries of UK specific lineages sequenced by GLAS for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-18. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
2069 sequences in the UK from the sequencing centre GLAS have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 129 and the maximum is 685


Sequences which were replicates or too error-prone were removed from this analysis.



114 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 14 that remain:
7 are pending extinction, ie last seen three weeks ago.
4 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Scotland     | Date range     |   Total sequences | Global lineage                                |   Time since last sample (days) |   Activity score |
|:---------------|:-------------|:---------------|------------------:|:----------------------------------------------|--------------------------------:|-----------------:|
| UK5098         | 390 (100.0%) | Mar-01, Jun-05 |               390 | B.1.p73, B.1                                  |                              13 |           0.019  |
| UK36           | 266 (100.0%) | Mar-20, Jun-06 |               266 | B.1                                           |                              12 |           0.0245 |
| UK5            | 205 (100.0%) | Feb-28, Jun-15 |               205 | B.1.1.p11, B.1.1.14, B.1.1.13, B.1.1.1, B.1.1 |                               3 |           0.1765 |
| UK40           | 153 (100.0%) | Mar-13, Jun-08 |               153 | B.16, B                                       |                              10 |           0.0572 |
| UK39           | 109 (100.0%) | Mar-12, May-29 |               109 | A.2                                           |                              20 |           0.0361 |
| UK5676         | 85 (100.0%)  | Mar-12, May-27 |                85 | B.2                                           |                              22 |           0.0411 |
| UK2464         | 69 (100.0%)  | Mar-19, May-22 |                69 | B.1.p11                                       |                              27 |           0.0349 |
| UK2913         | 68 (100.0%)  | Mar-19, May-19 |                68 | B.1.p11                                       |                              30 |           0.0303 |
| UK668          | 66 (100.0%)  | Mar-22, Jun-10 |                66 | B.1                                           |                               8 |           0.1538 |
| UK199          | 60 (100.0%)  | Mar-05, Apr-27 |                60 | B.1.p73, B.1.5, B.1                           |                              52 |           0.0173 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/GLAS/figures/report_GLAS_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 15 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/GLAS/figures/report_GLAS_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/GLAS/figures/report_GLAS_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/GLAS/figures/report_GLAS_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/GLAS/figures/report_GLAS_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
All sequences have been assigned clean adm2 data this week.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/GLAS/figures/report_GLAS_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Scotland     | Date range     |   Total sequences | Global lineage                                |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:----------------------------------------------|--------------------------------:|:-----------------|
| UK5098         | 390 (100.0%) | Mar-01, Jun-05 |               390 | B.1.p73, B.1                                  |                              13 | 0.019            |
| UK36           | 266 (100.0%) | Mar-20, Jun-06 |               266 | B.1                                           |                              12 | 0.0245           |
| UK5            | 205 (100.0%) | Feb-28, Jun-15 |               205 | B.1.1.p11, B.1.1.14, B.1.1.13, B.1.1.1, B.1.1 |                               3 | 0.1765           |
| UK40           | 153 (100.0%) | Mar-13, Jun-08 |               153 | B.16, B                                       |                              10 | 0.0572           |
| UK39           | 109 (100.0%) | Mar-12, May-29 |               109 | A.2                                           |                              20 | 0.0361           |
| UK5676         | 85 (100.0%)  | Mar-12, May-27 |                85 | B.2                                           |                              22 | 0.0411           |
| UK2464         | 69 (100.0%)  | Mar-19, May-22 |                69 | B.1.p11                                       |                              27 | 0.0349           |
| UK2913         | 68 (100.0%)  | Mar-19, May-19 |                68 | B.1.p11                                       |                              30 | 0.0303           |
| UK668          | 66 (100.0%)  | Mar-22, Jun-10 |                66 | B.1                                           |                               8 | 0.1538           |
| UK199          | 60 (100.0%)  | Mar-05, Apr-27 |                60 | B.1.p73, B.1.5, B.1                           |                              52 | 0.0173           |
| UK42           | 42 (100.0%)  | Mar-10, May-18 |                42 | B.1.5, B.1.p73, B.1                           |                              31 | 0.0543           |
| UK100          | 37 (100.0%)  | Apr-08, Jun-01 |                37 | B.1.5, B.1                                    |                              17 | 0.0882           |
| UK370          | 34 (100.0%)  | Mar-17, Jun-16 |                34 | B.1.1.10                                      |                               2 | 1.3788           |
| UK87           | 32 (100.0%)  | Mar-13, Apr-24 |                32 | B.1.70                                        |                              55 | 0.0246           |
| UK15           | 27 (100.0%)  | Mar-12, Apr-28 |                27 | B.1.1                                         |                              51 | 0.0354           |
| UK107          | 24 (100.0%)  | Mar-09, May-11 |                24 | B.2.1                                         |                              38 | 0.0721           |
| UK501          | 18 (100.0%)  | Mar-19, Jun-18 |                18 | B.1                                           |                               0 | active today     |
| UK14           | 17 (100.0%)  | Mar-14, Apr-10 |                17 | B                                             |                              69 | 0.0245           |
| UK44           | 16 (100.0%)  | Mar-17, Apr-23 |                16 | B                                             |                              56 | 0.044            |
| UK502          | 16 (100.0%)  | Mar-06, Mar-20 |                16 | B.1.69                                        |                              90 | 0.0104           |
| UK261          | 14 (100.0%)  | Mar-15, Apr-10 |                14 | A.3                                           |                              69 | 0.029            |
| UK72           | 14 (100.0%)  | Mar-07, Apr-02 |                14 | B                                             |                              77 | 0.026            |
| UK43           | 14 (100.0%)  | Mar-23, Apr-26 |                14 | A.5                                           |                              53 | 0.0493           |
| UK722          | 13 (100.0%)  | Apr-08, May-27 |                13 | B.1.5                                         |                              22 | 0.1856           |
| UK58           | 13 (100.0%)  | Mar-12, Apr-24 |                13 | B.1                                           |                              55 | 0.0652           |
| UK335          | 12 (100.0%)  | Apr-15, May-21 |                12 | B.1.1                                         |                              28 | 0.1169           |
| UK2200         | 10 (100.0%)  | Mar-31, May-04 |                10 | B.1.5                                         |                              45 | 0.084            |
| UK120          | 10 (100.0%)  | Mar-02, Apr-16 |                10 | B                                             |                              63 | 0.0794           |
| UK167          | 9 (100.0%)   | Mar-12, Apr-26 |                 9 | B.1                                           |                              53 | 0.1061           |
| UK137          | 8 (100.0%)   | Mar-09, Mar-29 |                 8 | B.1.1                                         |                              81 | 0.0353           |
| UK671          | 7 (100.0%)   | Apr-17, May-31 |                 7 | B.1.p73                                       |                              18 | 0.4074           |
| UK271          | 7 (100.0%)   | Apr-15, Apr-26 |                 7 | B.1                                           |                              53 | 0.0346           |
| UK2735         | 6 (100.0%)   | Apr-08, Apr-17 |                 6 | B.1.1                                         |                              62 | 0.029            |
| UK187          | 6 (100.0%)   | Apr-04, Apr-24 |                 6 | B.1                                           |                              55 | 0.0727           |
| UK601          | 6 (100.0%)   | Mar-14, Apr-01 |                 6 | B.10                                          |                              78 | 0.0462           |
| UK4735         | 6 (100.0%)   | Apr-22, May-27 |                 6 | B.1.1                                         |                              22 | 0.3182           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | GLAS     |            15 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5098 |   UK36 |   UK5 |   UK40 |   UK39 |   UK5676 |   UK2464 |   UK668 |   UK100 |   UK370 |
|:------------------|---------:|-------:|------:|-------:|-------:|---------:|---------:|--------:|--------:|--------:|
| 2020-02-23        |        0 |      0 |     1 |      0 |      0 |        0 |        0 |       0 |       0 |       0 |
| 2020-03-01        |        1 |      0 |     0 |      0 |      0 |        0 |        0 |       0 |       0 |       0 |
| 2020-03-08        |        0 |      0 |     3 |      1 |      1 |        3 |        0 |       0 |       0 |       0 |
| 2020-03-15        |        2 |      1 |     5 |      3 |      2 |        6 |        3 |       0 |       0 |       2 |
| 2020-03-22        |        3 |      3 |     4 |      4 |      3 |        4 |        5 |       3 |       0 |       3 |
| 2020-03-29        |        3 |      7 |     6 |      3 |      2 |        4 |        1 |       1 |       0 |       1 |
| 2020-04-05        |        9 |      8 |    11 |      7 |      8 |        2 |        3 |       4 |       3 |       2 |
| 2020-04-12        |       13 |     12 |    11 |      6 |      7 |        1 |       10 |       5 |       5 |       3 |
| 2020-04-19        |       15 |     11 |    10 |      8 |      4 |        6 |        6 |       6 |       6 |       2 |
| 2020-04-26        |        7 |      4 |     4 |      2 |      1 |        0 |        1 |       1 |       2 |       1 |
| 2020-05-03        |        6 |      6 |     3 |      1 |      2 |        4 |        2 |       3 |       1 |       1 |
| 2020-05-10        |       11 |      7 |     5 |      3 |      4 |        0 |        2 |       6 |       2 |       2 |
| 2020-05-17        |       10 |      6 |     5 |      1 |      2 |        1 |        1 |       2 |       1 |       2 |
| 2020-05-24        |        8 |      3 |     5 |      2 |      3 |        1 |        0 |       2 |       2 |       1 |
| 2020-05-31        |        4 |      5 |     0 |      0 |      0 |        0 |        0 |       2 |       1 |       1 |
| 2020-06-07        |        0 |      0 |     1 |      1 |      0 |        0 |        0 |       1 |       0 |       0 |
| 2020-06-14        |        0 |      0 |     1 |      0 |      0 |        0 |        0 |       0 |       0 |       1 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-02-28 |                            0 |                                1 |       1 |
| 2020-03-01 |                            0 |                                1 |       1 |
| 2020-03-02 |                            0 |                                1 |       1 |
| 2020-03-03 |                            0 |                                2 |       2 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-06 |                            0 |                                1 |       1 |
| 2020-03-07 |                            1 |                                1 |       2 |
| 2020-03-09 |                            1 |                                3 |       4 |
| 2020-03-10 |                            0 |                                2 |       2 |
| 2020-03-11 |                            1 |                                0 |       1 |
| 2020-03-12 |                            1 |                                8 |       9 |
| 2020-03-13 |                            6 |                                2 |       8 |
| 2020-03-14 |                            0 |                                3 |       3 |
| 2020-03-15 |                            0 |                                1 |       1 |
| 2020-03-16 |                            2 |                                0 |       2 |
| 2020-03-17 |                            4 |                                3 |       7 |
| 2020-03-18 |                            2 |                                1 |       3 |
| 2020-03-19 |                            2 |                                5 |       7 |
| 2020-03-20 |                            3 |                                3 |       6 |
| 2020-03-21 |                            2 |                                1 |       3 |
| 2020-03-22 |                            0 |                                2 |       2 |
| 2020-03-23 |                            4 |                                1 |       5 |
| 2020-03-24 |                            1 |                                0 |       1 |
| 2020-03-25 |                            2 |                                0 |       2 |
| 2020-03-26 |                            4 |                                0 |       4 |
| 2020-03-27 |                            5 |                                1 |       6 |
| 2020-03-28 |                            1 |                                0 |       1 |
| 2020-03-29 |                            4 |                                3 |       7 |
| 2020-03-30 |                            1 |                                0 |       1 |
| 2020-03-31 |                            0 |                                2 |       2 |
| 2020-04-01 |                            1 |                                0 |       1 |
| 2020-04-02 |                            2 |                                1 |       3 |
| 2020-04-03 |                            0 |                                1 |       1 |
| 2020-04-04 |                            2 |                                2 |       4 |
| 2020-04-05 |                            0 |                                1 |       1 |
| 2020-04-06 |                            1 |                                0 |       1 |
| 2020-04-07 |                            2 |                                0 |       2 |
| 2020-04-08 |                            2 |                                3 |       5 |
| 2020-04-10 |                            0 |                                1 |       1 |
| 2020-04-11 |                            2 |                                1 |       3 |
| 2020-04-12 |                            4 |                                1 |       5 |
| 2020-04-13 |                            1 |                                0 |       1 |
| 2020-04-14 |                            0 |                                1 |       1 |
| 2020-04-15 |                            1 |                                4 |       5 |
| 2020-04-16 |                            0 |                                3 |       3 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            2 |                                0 |       2 |
| 2020-04-20 |                            1 |                                1 |       2 |
| 2020-04-21 |                            1 |                                0 |       1 |
| 2020-04-22 |                            0 |                                4 |       4 |
| 2020-04-23 |                            1 |                                0 |       1 |
| 2020-04-24 |                            2 |                                0 |       2 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   Scotland |
|:-----------|-----------:|
| 2020-02-28 |          1 |
| 2020-03-01 |          1 |
| 2020-03-02 |          1 |
| 2020-03-03 |          2 |
| 2020-03-04 |          3 |
| 2020-03-05 |          2 |
| 2020-03-06 |          5 |
| 2020-03-07 |          3 |
| 2020-03-09 |          8 |
| 2020-03-10 |          4 |
| 2020-03-11 |          2 |
| 2020-03-12 |         22 |
| 2020-03-13 |         37 |
| 2020-03-14 |         10 |
| 2020-03-15 |          5 |
| 2020-03-16 |         14 |
| 2020-03-17 |         26 |
| 2020-03-18 |         17 |
| 2020-03-19 |         25 |
| 2020-03-20 |         21 |
| 2020-03-21 |         18 |
| 2020-03-22 |         13 |
| 2020-03-23 |         30 |
| 2020-03-24 |         16 |
| 2020-03-25 |         22 |
| 2020-03-26 |         35 |
| 2020-03-27 |         41 |
| 2020-03-28 |         26 |
| 2020-03-29 |         35 |
| 2020-03-30 |         22 |
| 2020-03-31 |         44 |
| 2020-04-01 |         45 |
| 2020-04-02 |         24 |
| 2020-04-03 |         35 |
| 2020-04-04 |         18 |
| 2020-04-05 |         27 |
| 2020-04-06 |         14 |
| 2020-04-07 |         18 |
| 2020-04-08 |         58 |
| 2020-04-09 |         31 |
| 2020-04-10 |         44 |
| 2020-04-11 |         44 |
| 2020-04-12 |         54 |
| 2020-04-13 |         61 |
| 2020-04-14 |         52 |
| 2020-04-15 |         56 |
| 2020-04-16 |         74 |
| 2020-04-17 |         57 |
| 2020-04-18 |         51 |
| 2020-04-19 |          5 |
| 2020-04-20 |         44 |
| 2020-04-21 |         79 |
| 2020-04-22 |         79 |
| 2020-04-23 |         58 |
| 2020-04-24 |         56 |
| 2020-04-25 |         38 |
| 2020-04-26 |         28 |
| 2020-04-27 |         22 |
| 2020-04-28 |         17 |
| 2020-04-29 |          1 |
| 2020-04-30 |          3 |
| 2020-05-01 |          6 |
| 2020-05-02 |          9 |
| 2020-05-03 |          2 |
| 2020-05-04 |          3 |
| 2020-05-05 |          3 |
| 2020-05-06 |         13 |
| 2020-05-07 |         30 |
| 2020-05-08 |         14 |
| 2020-05-09 |         18 |
| 2020-05-10 |         16 |
| 2020-05-11 |         18 |
| 2020-05-12 |         17 |
| 2020-05-13 |         16 |
| 2020-05-14 |         14 |
| 2020-05-15 |         10 |
| 2020-05-16 |         15 |
| 2020-05-17 |          7 |
| 2020-05-18 |         21 |
| 2020-05-19 |         21 |
| 2020-05-20 |          8 |
| 2020-05-21 |         16 |
| 2020-05-22 |         14 |
| 2020-05-23 |          4 |
| 2020-05-24 |          5 |
| 2020-05-25 |         11 |
| 2020-05-26 |          5 |
| 2020-05-27 |         10 |
| 2020-05-28 |          3 |
| 2020-05-29 |          1 |
| 2020-05-30 |          5 |
| 2020-05-31 |          6 |
| 2020-06-01 |          4 |
| 2020-06-02 |          3 |
| 2020-06-03 |          2 |
| 2020-06-04 |          2 |
| 2020-06-05 |          2 |
| 2020-06-06 |          2 |
| 2020-06-08 |          1 |
| 2020-06-09 |          1 |
| 2020-06-10 |          2 |
| 2020-06-11 |          1 |
| 2020-06-14 |          1 |
| 2020-06-15 |          1 |
| 2020-06-16 |          1 |
| 2020-06-18 |          1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country   |   Number of sequences | Sequence group   |
|:-----------------------|:----------|----------------------:|:-----------------|
| ABERDEEN               | Scotland  |                    19 | 10-50            |
| ARGYLL AND BUTE        | Scotland  |                    14 | 10-50            |
| CLACKMANNANSHIRE       | Scotland  |                     1 | 1-10             |
| DUMFRIES AND GALLOWAY  | Scotland  |                    42 | 10-50            |
| DUNDEE                 | Scotland  |                    11 | 10-50            |
| EAST AYRSHIRE          | Scotland  |                    59 | 50-100           |
| EAST DUNBARTONSHIRE    | Scotland  |                    73 | 50-100           |
| EAST RENFREWSHIRE      | Scotland  |                    40 | 10-50            |
| EDINBURGH              | Scotland  |                     9 | 1-10             |
| EILEAN SIAR            | Scotland  |                     2 | 1-10             |
| FALKIRK                | Scotland  |                    70 | 50-100           |
| FIFE                   | Scotland  |                     1 | 1-10             |
| GLASGOW                | Scotland  |                  1006 | >500             |
| HIGHLAND               | Scotland  |                     9 | 1-10             |
| INVERCLYDE             | Scotland  |                    42 | 10-50            |
| NORTH AYRSHIRE         | Scotland  |                    18 | 10-50            |
| NORTH LANARKSHIRE      | Scotland  |                   197 | 150-200          |
| NORTHAMPTONSHIRE       | England   |                     1 | 1-10             |
| ORKNEY ISLANDS         | Scotland  |                     1 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland  |                     2 | 1-10             |
| RENFREWSHIRE           | Scotland  |                   286 | 250-300          |
| SCOTTISH BORDERS       | Scotland  |                     1 | 1-10             |
| SHETLAND ISLANDS       | Scotland  |                    14 | 10-50            |
| SOUTH AYRSHIRE         | Scotland  |                     7 | 1-10             |
| SOUTH LANARKSHIRE      | Scotland  |                    66 | 50-100           |
| STIRLING               | Scotland  |                    16 | 10-50            |
| WEST DUNBARTONSHIRE    | Scotland  |                    49 | 10-50            |
| WEST LOTHIAN           | Scotland  |                     1 | 1-10             |

\pagebreak






