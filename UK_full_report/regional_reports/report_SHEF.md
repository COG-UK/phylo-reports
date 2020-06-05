
# UK lineages summary report








This report gives summaries of UK specific lineages sequenced by SHEF for week 2020-05-29. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-13. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1148 sequences in the UK from the sequencing centre SHEF have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6130 and the maximum is 9084


Sequences which were replicates or too error-prone were removed from this analysis.



312 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 19 that remain:
11 are pending extinction, ie last seen three weeks ago.
7 lineages have gone quiet, ie haven't been seen this week.
1 lineage has been continuously circulating.


The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lienages is found in the appendix, along with the raw data for all of the other figures.

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 295 (100.0%) | Mar-13, May-13 |               295 | B.1, B.1.1.1     |                               0 | active today     |
| UK194          | 61 (100.0%)  | Mar-19, Apr-24 |                61 | B.1.1            |                              19 | 0.0316           |
| UK343          | 60 (100.0%)  | Mar-28, Apr-24 |                60 | B.1              |                              19 | 0.0241           |
| UK144          | 25 (100.0%)  | Mar-05, Apr-07 |                25 | B.2.1            |                              36 | 0.0382           |
| UK279          | 22 (100.0%)  | Mar-26, Apr-25 |                22 | B.1.1            |                              18 | 0.0794           |
| UK701          | 22 (100.0%)  | Mar-03, Apr-23 |                22 | B.1              |                              20 | 0.1214           |
| UK235          | 22 (100.0%)  | Mar-21, May-04 |                22 | B.1.1            |                               9 | 0.2328           |
| UK4            | 20 (100.0%)  | Mar-07, Apr-21 |                20 | B                |                              22 | 0.1077           |
| UK94           | 19 (100.0%)  | Mar-21, Apr-10 |                19 | B.2.1            |                              33 | 0.0337           |
| UK419          | 19 (100.0%)  | Mar-30, May-02 |                19 | B.1.1            |                              11 | 0.1667           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 


![Number of sequences sampled in a lineage by country](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_geog_plot_1.png){#geog_plot }







These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.



There are 5 sequences without enough geographical information to map from this centre.
![Map showing the number of sequences sampled by adm2 region](UK_full_report/regional_reports/results/results_SHEF/figures/report_SHEF_map_1.png){#map }









Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 295 (100.0%) | Mar-13, May-13 |               295 | B.1, B.1.1.1     |                               0 | active today     |
| UK194          | 61 (100.0%)  | Mar-19, Apr-24 |                61 | B.1.1            |                              19 | 0.0316           |
| UK343          | 60 (100.0%)  | Mar-28, Apr-24 |                60 | B.1              |                              19 | 0.0241           |
| UK144          | 25 (100.0%)  | Mar-05, Apr-07 |                25 | B.2.1            |                              36 | 0.0382           |
| UK279          | 22 (100.0%)  | Mar-26, Apr-25 |                22 | B.1.1            |                              18 | 0.0794           |
| UK701          | 22 (100.0%)  | Mar-03, Apr-23 |                22 | B.1              |                              20 | 0.1214           |
| UK235          | 22 (100.0%)  | Mar-21, May-04 |                22 | B.1.1            |                               9 | 0.2328           |
| UK4            | 20 (100.0%)  | Mar-07, Apr-21 |                20 | B                |                              22 | 0.1077           |
| UK94           | 19 (100.0%)  | Mar-21, Apr-10 |                19 | B.2.1            |                              33 | 0.0337           |
| UK419          | 19 (100.0%)  | Mar-30, May-02 |                19 | B.1.1            |                              11 | 0.1667           |
| UK24           | 17 (100.0%)  | Mar-19, Apr-30 |                17 | B.1.1            |                              13 | 0.2019           |
| UK23           | 17 (100.0%)  | Mar-23, May-02 |                17 | B.9              |                              11 | 0.2273           |
| UK384          | 16 (100.0%)  | Mar-15, Apr-02 |                16 | B.2.1            |                              41 | 0.0293           |
| UK6            | 15 (100.0%)  | Mar-22, May-01 |                15 | B.1              |                              12 | 0.2381           |
| UK131          | 15 (100.0%)  | Mar-20, Apr-10 |                15 | B.15             |                              33 | 0.0455           |
| UK95           | 15 (100.0%)  | Mar-21, May-03 |                15 | B.2.1            |                              10 | 0.3071           |
| UK51           | 14 (100.0%)  | Mar-25, May-04 |                14 | B.1.36           |                               9 | 0.3419           |
| UK501          | 13 (100.0%)  | Apr-03, Apr-22 |                13 | B, B.1           |                              21 | 0.0754           |
| UK802          | 9 (100.0%)   | Mar-21, Apr-22 |                 9 | B.1              |                              21 | 0.1905           |
| UK432          | 9 (100.0%)   | Mar-24, Apr-09 |                 9 | B.3              |                              34 | 0.0588           |
| UK12           | 8 (100.0%)   | Mar-26, Apr-22 |                 8 | B.1.p11          |                              21 | 0.1837           |
| UK72           | 8 (100.0%)   | Mar-22, Apr-22 |                 8 | B.10             |                              21 | 0.2109           |
| UK5505         | 7 (100.0%)   | Mar-29, Apr-21 |                 7 | B.1              |                              22 | 0.1742           |
| UK5084         | 6 (100.0%)   | Mar-29, Apr-16 |                 6 | B.1              |                              27 | 0.1333           |
| UK36           | 6 (100.0%)   | Mar-24, Apr-02 |                 6 | B.1              |                              41 | 0.0439           |
| UK173          | 6 (100.0%)   | Mar-22, Mar-30 |                 6 | B                |                              44 | 0.0364           |

\pagebreak

**Table S2** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK194 |   UK343 |   UK701 |   UK279 |   UK235 |   UK4 |   UK419 |   UK24 |   UK23 |
|:------------------|------:|--------:|--------:|--------:|--------:|--------:|------:|--------:|-------:|-------:|
| 2020-03-01        |     0 |       0 |       0 |       1 |       0 |       0 |     1 |       0 |      0 |      0 |
| 2020-03-08        |     1 |       0 |       0 |       0 |       0 |       0 |     1 |       0 |      0 |      0 |
| 2020-03-15        |     1 |       1 |       0 |       1 |       0 |       1 |     1 |       0 |      1 |      0 |
| 2020-03-22        |     2 |       1 |       1 |       1 |       1 |       1 |     2 |       0 |      1 |      1 |
| 2020-03-29        |     1 |       1 |       1 |       1 |       1 |       1 |     1 |       1 |      1 |      1 |
| 2020-04-05        |     1 |       1 |       1 |       0 |       1 |       1 |     0 |       1 |      1 |      1 |
| 2020-04-12        |     2 |       1 |       1 |       1 |       1 |       1 |     1 |       1 |      1 |      1 |
| 2020-04-19        |     1 |       1 |       1 |       1 |       1 |       0 |     1 |       0 |      1 |      1 |
| 2020-04-26        |     1 |       0 |       0 |       0 |       0 |       0 |     0 |       1 |      1 |      1 |
| 2020-05-03        |     1 |       0 |       0 |       0 |       0 |       1 |     0 |       0 |      0 |      0 |
| 2020-05-10        |     1 |       0 |       0 |       0 |       0 |       0 |     0 |       0 |      0 |      0 |

\pagebreak


Table S3 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S4** Raw data for figure six showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-01 |                            1 |                                0 |       1 |
| 2020-03-02 |                            4 |                                0 |       4 |
| 2020-03-03 |                            1 |                                1 |       2 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-06 |                            1 |                                0 |       1 |
| 2020-03-07 |                            0 |                                1 |       1 |
| 2020-03-08 |                            1 |                                0 |       1 |
| 2020-03-09 |                            2 |                                0 |       2 |
| 2020-03-12 |                            1 |                                1 |       2 |
| 2020-03-13 |                            0 |                                1 |       1 |
| 2020-03-15 |                            0 |                                1 |       1 |
| 2020-03-16 |                            0 |                                1 |       1 |
| 2020-03-17 |                            1 |                                1 |       2 |
| 2020-03-18 |                            0 |                                1 |       1 |
| 2020-03-19 |                            4 |                                2 |       6 |
| 2020-03-20 |                            6 |                                2 |       8 |
| 2020-03-21 |                            6 |                                8 |      14 |
| 2020-03-22 |                            3 |                                3 |       6 |
| 2020-03-23 |                            6 |                                5 |      11 |
| 2020-03-24 |                           17 |                                5 |      22 |
| 2020-03-25 |                           29 |                                9 |      38 |
| 2020-03-26 |                           19 |                                8 |      27 |
| 2020-03-27 |                           10 |                                2 |      12 |
| 2020-03-28 |                            8 |                                2 |      10 |
| 2020-03-29 |                            5 |                                6 |      11 |
| 2020-03-30 |                           11 |                                4 |      15 |
| 2020-03-31 |                            4 |                                0 |       4 |
| 2020-04-01 |                           13 |                                3 |      16 |
| 2020-04-02 |                           18 |                                5 |      23 |
| 2020-04-03 |                           10 |                                1 |      11 |
| 2020-04-04 |                            7 |                                0 |       7 |
| 2020-04-05 |                            5 |                                0 |       5 |
| 2020-04-06 |                            5 |                                0 |       5 |
| 2020-04-07 |                            1 |                                1 |       2 |
| 2020-04-08 |                            4 |                                1 |       5 |
| 2020-04-09 |                            6 |                                0 |       6 |
| 2020-04-10 |                           11 |                                0 |      11 |
| 2020-04-11 |                            6 |                                1 |       7 |
| 2020-04-12 |                            3 |                                1 |       4 |
| 2020-04-13 |                            3 |                                1 |       4 |
| 2020-04-14 |                            3 |                                1 |       4 |
| 2020-04-15 |                            4 |                                0 |       4 |
| 2020-04-16 |                            3 |                                1 |       4 |
| 2020-04-17 |                            1 |                                1 |       2 |
| 2020-04-20 |                            1 |                                1 |       2 |
| 2020-04-21 |                            3 |                                0 |       3 |
| 2020-04-22 |                            1 |                                2 |       3 |
| 2020-04-23 |                            1 |                                0 |       1 |
| 2020-05-01 |                            2 |                                0 |       2 |
| 2020-05-02 |                            0 |                                1 |       1 |
| 2020-05-04 |                            1 |                                0 |       1 |

\pagebreak

**Table S5** Raw data for figure seven showing the number of sequences taken over time.


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
| 2020-03-19 |         8 |
| 2020-03-20 |        12 |
| 2020-03-21 |        23 |
| 2020-03-22 |        22 |
| 2020-03-23 |        29 |
| 2020-03-24 |        50 |
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
| 2020-04-13 |        17 |
| 2020-04-14 |        26 |
| 2020-04-15 |        26 |
| 2020-04-16 |        24 |
| 2020-04-17 |        28 |
| 2020-04-18 |         6 |
| 2020-04-19 |         7 |
| 2020-04-20 |        14 |
| 2020-04-21 |        25 |
| 2020-04-22 |        33 |
| 2020-04-23 |        16 |
| 2020-04-24 |         4 |
| 2020-04-25 |         3 |
| 2020-04-26 |         1 |
| 2020-04-29 |         1 |
| 2020-04-30 |         3 |
| 2020-05-01 |        12 |
| 2020-05-02 |        15 |
| 2020-05-03 |         7 |
| 2020-05-04 |         6 |
| 2020-05-11 |         1 |
| 2020-05-13 |         1 |

\pagebreak

**Table S6** Raw data for the map with the number of sequences assigned to each admin2 region.


| Admin2                   | Country   |   Number of sequences | Sequence group   |
|:-------------------------|:----------|----------------------:|:-----------------|
| DERBYSHIRE               | England   |                    14 | 10-50            |
| EAST RIDING OF YORKSHIRE | England   |                     8 | 1-10             |
| SOUTH YORKSHIRE          | England   |                  1121 | >500             |

\pagebreak






