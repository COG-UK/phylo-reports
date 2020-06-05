
# UK lineages summary report








This report gives summaries of UK specific lineages sequenced by CAMB for week 2020-05-29. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-23. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1128 sequences in the UK from the sequencing centre CAMB have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6130 and the maximum is 9084


Sequences which were replicates or too error-prone were removed from this analysis.



426 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 31 that remain:
12 are pending extinction, ie last seen three weeks ago.
8 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
10 lineages have been continuously circulating.


The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lienages is found in the appendix, along with the raw data for all of the other figures.

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 87 (100.0%) | Mar-15, May-22 |                87 | B.1.1.1          |                               1 | 0.7907           |
| UK57           | 31 (100.0%) | Apr-05, Apr-28 |                31 | B.1.1            |                              25 | 0.0307           |
| UK167          | 29 (100.0%) | Apr-01, May-21 |                29 | B.1.66           |                               2 | 0.8929           |
| UK26           | 27 (100.0%) | Apr-05, May-18 |                27 | B.1.1.3          |                               5 | 0.3308           |
| UK128          | 25 (100.0%) | Apr-09, May-23 |                25 | B.1.1            |                               0 | active today     |
| UK565          | 21 (100.0%) | Mar-31, May-13 |                21 | B.1.1            |                              10 | 0.215            |
| UK371          | 21 (100.0%) | Apr-10, May-19 |                21 | B.1.1            |                               4 | 0.4875           |
| UK494          | 20 (100.0%) | Mar-20, May-04 |                20 | B.1.p11          |                              19 | 0.1247           |
| UK701          | 20 (100.0%) | Mar-17, May-08 |                20 | B.1              |                              15 | 0.1825           |
| UK2464         | 20 (100.0%) | Mar-17, May-11 |                20 | B.1.p11          |                              12 | 0.2412           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 


![Number of sequences sampled in a lineage by country](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_geog_plot_1.png){#geog_plot }







These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.



There are 29 sequences without enough geographical information to map from this centre.
![Map showing the number of sequences sampled by adm2 region](UK_full_report/regional_reports/results/results_CAMB/figures/report_CAMB_map_1.png){#map }









Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 87 (100.0%) | Mar-15, May-22 |                87 | B.1.1.1          |                               1 | 0.7907           |
| UK57           | 31 (100.0%) | Apr-05, Apr-28 |                31 | B.1.1            |                              25 | 0.0307           |
| UK167          | 29 (100.0%) | Apr-01, May-21 |                29 | B.1.66           |                               2 | 0.8929           |
| UK26           | 27 (100.0%) | Apr-05, May-18 |                27 | B.1.1.3          |                               5 | 0.3308           |
| UK128          | 25 (100.0%) | Apr-09, May-23 |                25 | B.1.1            |                               0 | active today     |
| UK565          | 21 (100.0%) | Mar-31, May-13 |                21 | B.1.1            |                              10 | 0.215            |
| UK371          | 21 (100.0%) | Apr-10, May-19 |                21 | B.1.1            |                               4 | 0.4875           |
| UK494          | 20 (100.0%) | Mar-20, May-04 |                20 | B.1.p11          |                              19 | 0.1247           |
| UK701          | 20 (100.0%) | Mar-17, May-08 |                20 | B.1              |                              15 | 0.1825           |
| UK2464         | 20 (100.0%) | Mar-17, May-11 |                20 | B.1.p11          |                              12 | 0.2412           |
| UK113          | 19 (100.0%) | Apr-09, May-19 |                19 | B.1.1            |                               4 | 0.5556           |
| UK147          | 16 (100.0%) | Apr-14, May-22 |                16 | B.1.1            |                               1 | 2.5333           |
| UK326          | 15 (100.0%) | Apr-07, May-22 |                15 | B.1.1.10         |                               1 | 3.2143           |
| UK5322         | 15 (100.0%) | Mar-30, May-13 |                15 | B.1.1            |                              10 | 0.3143           |
| UK13           | 14 (100.0%) | Mar-31, May-13 |                14 | B.1.1            |                              10 | 0.3308           |
| UK31           | 13 (100.0%) | Mar-30, May-08 |                13 | B.1              |                              15 | 0.2167           |
| UK183          | 12 (100.0%) | Apr-06, Apr-28 |                12 | B.1.1            |                              25 | 0.08             |
| UK33           | 12 (100.0%) | Apr-05, May-15 |                12 | B.1.1            |                               8 | 0.4545           |
| UK5672         | 12 (100.0%) | Mar-22, Apr-29 |                12 | B.2              |                              24 | 0.1439           |
| UK30           | 11 (100.0%) | May-02, May-15 |                11 | B.1.1            |                               8 | 0.1625           |
| UK308          | 10 (100.0%) | Apr-09, May-18 |                10 | B.1.1            |                               5 | 0.8667           |
| UK19           | 10 (100.0%) | Apr-04, May-10 |                10 | B.1              |                              13 | 0.3077           |
| UK180          | 10 (100.0%) | Mar-30, Apr-29 |                10 | B.1.1            |                              24 | 0.1389           |
| UK9            | 9 (100.0%)  | Mar-28, May-05 |                 9 | B.1.13           |                              18 | 0.2639           |
| UK220          | 9 (100.0%)  | Mar-27, Apr-22 |                 9 | B.1.1            |                              31 | 0.1048           |
| UK51           | 8 (100.0%)  | Apr-20, May-19 |                 8 | B.1.36           |                               4 | 1.0357           |
| UK37           | 8 (100.0%)  | Mar-29, May-03 |                 8 | B.1.30           |                              20 | 0.25             |
| UK1849         | 8 (100.0%)  | Apr-11, Apr-29 |                 8 | B.1.1            |                              24 | 0.1071           |
| UK6            | 8 (100.0%)  | Mar-19, May-01 |                 8 | B.1              |                              22 | 0.2792           |
| UK67           | 8 (100.0%)  | Apr-22, May-21 |                 8 | B.1.1            |                               2 | 2.0714           |
| UK36           | 7 (100.0%)  | Mar-30, Apr-15 |                 7 | B.1              |                              38 | 0.0702           |
| UK329          | 6 (100.0%)  | Apr-22, May-09 |                 6 | B.1.1            |                              14 | 0.2429           |
| UK274          | 6 (100.0%)  | Mar-19, May-11 |                 6 | B.3              |                              12 | 0.8833           |

\pagebreak

**Table S2** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK57 |   UK167 |   UK26 |   UK128 |   UK565 |   UK371 |   UK494 |   UK701 |   UK2464 |
|:------------------|------:|-------:|--------:|-------:|--------:|--------:|--------:|--------:|--------:|---------:|
| 2020-03-15        |     1 |      0 |       0 |      0 |       0 |       0 |       0 |       1 |       2 |        1 |
| 2020-03-22        |     1 |      0 |       0 |      0 |       0 |       0 |       0 |       0 |       0 |        0 |
| 2020-03-29        |     4 |      0 |       1 |      0 |       0 |       1 |       0 |       1 |       3 |        3 |
| 2020-04-05        |     2 |      1 |       2 |      1 |       2 |       2 |       1 |       0 |       2 |        4 |
| 2020-04-12        |     5 |      1 |       2 |      1 |       1 |       2 |       1 |       5 |       2 |        3 |
| 2020-04-19        |     6 |      1 |       3 |      2 |       3 |       1 |       1 |       3 |       1 |        1 |
| 2020-04-26        |     7 |      1 |       3 |      1 |       1 |       0 |       0 |       2 |       1 |        2 |
| 2020-05-03        |     3 |      0 |       0 |      1 |       1 |       1 |       1 |       1 |       1 |        0 |
| 2020-05-10        |     4 |      0 |       0 |      1 |       1 |       1 |       1 |       0 |       0 |        1 |
| 2020-05-17        |     5 |      0 |       3 |      1 |       1 |       0 |       1 |       0 |       0 |        0 |

\pagebreak


Table S3 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S4** Raw data for figure six showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-13 |                            3 |                                0 |       3 |
| 2020-03-14 |                            2 |                                0 |       2 |
| 2020-03-15 |                            1 |                                2 |       3 |
| 2020-03-16 |                            4 |                                0 |       4 |
| 2020-03-17 |                            6 |                                4 |      10 |
| 2020-03-18 |                           10 |                                1 |      11 |
| 2020-03-19 |                            7 |                                2 |       9 |
| 2020-03-20 |                           10 |                                2 |      12 |
| 2020-03-21 |                            0 |                                1 |       1 |
| 2020-03-22 |                            1 |                                1 |       2 |
| 2020-03-24 |                            1 |                                0 |       1 |
| 2020-03-26 |                            8 |                                1 |       9 |
| 2020-03-27 |                            8 |                                4 |      12 |
| 2020-03-28 |                            9 |                                2 |      11 |
| 2020-03-29 |                           12 |                                4 |      16 |
| 2020-03-30 |                           10 |                                4 |      14 |
| 2020-03-31 |                           23 |                                6 |      29 |
| 2020-04-01 |                           11 |                                6 |      17 |
| 2020-04-02 |                            4 |                                5 |       9 |
| 2020-04-03 |                            4 |                                1 |       5 |
| 2020-04-04 |                            7 |                                4 |      11 |
| 2020-04-05 |                            9 |                                6 |      15 |
| 2020-04-06 |                           13 |                                7 |      20 |
| 2020-04-07 |                           15 |                                5 |      20 |
| 2020-04-08 |                           10 |                                6 |      16 |
| 2020-04-09 |                            1 |                                5 |       6 |
| 2020-04-10 |                            7 |                                1 |       8 |
| 2020-04-11 |                            6 |                                1 |       7 |
| 2020-04-12 |                           11 |                                0 |      11 |
| 2020-04-13 |                           10 |                                2 |      12 |
| 2020-04-14 |                            7 |                                2 |       9 |
| 2020-04-15 |                            9 |                                2 |      11 |
| 2020-04-16 |                            5 |                                2 |       7 |
| 2020-04-17 |                            5 |                                2 |       7 |
| 2020-04-18 |                            4 |                                0 |       4 |
| 2020-04-19 |                            2 |                                2 |       4 |
| 2020-04-20 |                            3 |                                4 |       7 |
| 2020-04-21 |                           11 |                                1 |      12 |
| 2020-04-22 |                            5 |                                4 |       9 |
| 2020-04-23 |                            5 |                                0 |       5 |
| 2020-04-24 |                            0 |                                1 |       1 |
| 2020-04-25 |                            3 |                                0 |       3 |
| 2020-04-26 |                            2 |                                2 |       4 |
| 2020-04-27 |                           11 |                                1 |      12 |
| 2020-04-28 |                            3 |                                1 |       4 |
| 2020-04-29 |                            3 |                                3 |       6 |
| 2020-04-30 |                            3 |                                1 |       4 |
| 2020-05-01 |                            2 |                                3 |       5 |
| 2020-05-02 |                            1 |                                1 |       2 |
| 2020-05-03 |                            3 |                                0 |       3 |
| 2020-05-04 |                            3 |                                0 |       3 |
| 2020-05-05 |                            3 |                                0 |       3 |
| 2020-05-06 |                            2 |                                0 |       2 |
| 2020-05-07 |                            5 |                                1 |       6 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-09 |                            0 |                                1 |       1 |
| 2020-05-10 |                            2 |                                0 |       2 |
| 2020-05-11 |                            4 |                                3 |       7 |
| 2020-05-12 |                            0 |                                1 |       1 |
| 2020-05-13 |                            1 |                                1 |       2 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-16 |                            0 |                                1 |       1 |
| 2020-05-18 |                            2 |                                0 |       2 |
| 2020-05-19 |                            1 |                                0 |       1 |
| 2020-05-21 |                            1 |                                0 |       1 |

\pagebreak

**Table S5** Raw data for figure seven showing the number of sequences taken over time.


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
| 2020-04-01 |        22 |
| 2020-04-02 |        15 |
| 2020-04-03 |        11 |
| 2020-04-04 |        15 |
| 2020-04-05 |        26 |
| 2020-04-06 |        29 |
| 2020-04-07 |        32 |
| 2020-04-08 |        27 |
| 2020-04-09 |        17 |
| 2020-04-10 |        17 |
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
| 2020-04-26 |        25 |
| 2020-04-27 |        42 |
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
| 2020-05-18 |        21 |
| 2020-05-19 |        21 |
| 2020-05-20 |         7 |
| 2020-05-21 |         7 |
| 2020-05-22 |         8 |
| 2020-05-23 |         2 |

\pagebreak

**Table S6** Raw data for the map with the number of sequences assigned to each admin2 region.


| Admin2           | Country   |   Number of sequences | Sequence group   |
|:-----------------|:----------|----------------------:|:-----------------|
| BEDFORDSHIRE     | England   |                    35 | 10-50            |
| BUCKINGHAMSHIRE  | England   |                    56 | 50-100           |
| CAMBRIDGESHIRE   | England   |                   370 | 300-400          |
| ESSEX            | England   |                   249 | 200-250          |
| GREATER LONDON   | England   |                    82 | 50-100           |
| HERTFORDSHIRE    | England   |                   173 | 150-200          |
| NORFOLK          | England   |                     5 | 1-10             |
| NORTHAMPTONSHIRE | England   |                     3 | 1-10             |
| NOTTINGHAMSHIRE  | England   |                     1 | 1-10             |
| OXFORDSHIRE      | England   |                     1 | 1-10             |
| SUFFOLK          | England   |                   124 | 100-150          |

\pagebreak






