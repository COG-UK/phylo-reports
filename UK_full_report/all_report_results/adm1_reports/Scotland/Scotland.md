







# Lineages report for Scotland




This report gives summaries of lineages sampled in Scotland for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-08. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
3232 sequences from Scotland have been included in this analysis.
225 lineages have been recorded, 114 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 132 and the maximum is 1169


Sequences which were replicates or too error-prone were removed from this analysis.



195 are lineages which were sampled less than five times in Scotland, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 30 that remain:
10 are pending extinction, ie last seen three weeks ago.
7 lineages have gone quiet, ie haven't been seen this week.
5 lineages have reactivated.
8 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Date range     |   Number of sequences | Global lineage                                           |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:---------------------------------------------------------|--------------------------------:|:-----------------|
| UK36           | Mar-20, Jun-03 |                   353 | B.1                                                      |                               5 | 0.0371           |
| UK5098         | Mar-16, May-27 |                   332 | B.1.p73                                                  |                              12 | 0.0178           |
| UK5            | Feb-28, Jun-08 |                   302 | B.1.1.p12, B.1.1.13, B.1.1.1, B.1.1.14, B.1.1, B.1.1.p11 |                               0 | active today     |
| UK42           | Mar-01, Jun-04 |                   237 | B.1.p73, B.1.71, B.1.p11, B.1, B.1.5                     |                               4 | 0.0233           |
| UK109          | Mar-12, Jun-08 |                   229 | B.1.5.5, B.1.5                                           |                               0 | active today     |
| UK40           | Mar-13, May-26 |                   164 | B.16, B                                                  |                              13 | 0.0333           |
| UK199          | Mar-05, Jun-08 |                   151 | B.1, B.1.p73, B.1.5                                      |                               0 | active today     |
| UK5676         | Mar-12, May-22 |                   137 | B.2                                                      |                              17 | 0.011            |
| UK2464         | Mar-19, Jun-07 |                   125 | B.1.p11                                                  |                               1 | 0.1848           |
| UK39           | Mar-12, May-24 |                   107 | A.2                                                      |                              15 | 0.0451           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 



NB the lineage may have started anywhere in the UK, but has been recorded at least once in Scotland



![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/Scotland/figures/Scotland_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Date range     |   Number of sequences | Global lineage                                           |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:---------------------------------------------------------|--------------------------------:|:-----------------|
| UK36           | Mar-20, Jun-03 |                   353 | B.1                                                      |                               5 | 0.0371           |
| UK5098         | Mar-16, May-27 |                   332 | B.1.p73                                                  |                              12 | 0.0178           |
| UK5            | Feb-28, Jun-08 |                   302 | B.1.1.p12, B.1.1.13, B.1.1.1, B.1.1.14, B.1.1, B.1.1.p11 |                               0 | active today     |
| UK42           | Mar-01, Jun-04 |                   237 | B.1.p73, B.1.71, B.1.p11, B.1, B.1.5                     |                               4 | 0.0233           |
| UK109          | Mar-12, Jun-08 |                   229 | B.1.5.5, B.1.5                                           |                               0 | active today     |
| UK40           | Mar-13, May-26 |                   164 | B.16, B                                                  |                              13 | 0.0333           |
| UK199          | Mar-05, Jun-08 |                   151 | B.1, B.1.p73, B.1.5                                      |                               0 | active today     |
| UK5676         | Mar-12, May-22 |                   137 | B.2                                                      |                              17 | 0.011            |
| UK2464         | Mar-19, Jun-07 |                   125 | B.1.p11                                                  |                               1 | 0.1848           |
| UK39           | Mar-12, May-24 |                   107 | A.2                                                      |                              15 | 0.0451           |
| UK2913         | Mar-19, Jun-01 |                    79 | B.1.p11                                                  |                               7 | 0.0297           |
| UK72           | Mar-07, May-27 |                    46 | B                                                        |                              12 | 0.029            |
| UK107          | Mar-09, Jun-02 |                    40 | B.2.1                                                    |                               6 | 0.0148           |
| UK198          | Mar-17, May-07 |                    37 | B.1, B.1.5                                               |                              32 | 0.027            |
| UK2200         | Mar-23, May-20 |                    35 | B.1.5.6, B.1.5                                           |                              19 | 0.0459           |
| UK304          | Apr-16, Jun-02 |                    34 | B.1.1.14                                                 |                               6 | 0.2374           |
| UK370          | Mar-17, Jun-02 |                    32 | B.1.1.10                                                 |                               6 | 0.0843           |
| UK3929         | Mar-06, Jun-03 |                    31 | B.1.1.4, B.1.1                                           |                               5 | 0.0848           |
| UK100          | Mar-30, May-25 |                    29 | B.1, B.1.5                                               |                              14 | 0.1429           |
| UK15           | Mar-07, May-06 |                    28 | B.1.1                                                    |                              33 | 0.0125           |
| UK43           | Mar-23, Apr-26 |                    28 | A.5                                                      |                              43 | 0.0374           |
| UK44           | Mar-17, Apr-19 |                    28 | B                                                        |                              50 | 0.0236           |
| UK14           | Mar-14, Apr-27 |                    28 | B                                                        |                              42 | 0.0378           |
| UK21           | Mar-18, May-23 |                    24 | B.1.40                                                   |                              16 | 0.1793           |
| UK87           | Mar-13, Apr-24 |                    23 | B.1.70                                                   |                              45 | 0.0424           |
| UK2735         | Mar-18, May-29 |                    23 | B.1.1                                                    |                              10 | 0.0293           |
| UK1667         | Mar-31, May-14 |                    20 | B.1.p9                                                   |                              25 | 0.0783           |
| UK167          | Mar-12, Jun-07 |                    19 | B.1                                                      |                               1 | 0.3376           |
| UK4493         | Apr-23, May-19 |                    18 | B.1                                                      |                              20 | 0.0765           |
| UK502          | Mar-06, Mar-30 |                    18 | B.1.69                                                   |                              70 | 0.0202           |
| UK66           | Mar-28, May-20 |                    17 | B.1.1.8                                                  |                              19 | 0.0304           |
| UK120          | Mar-02, May-05 |                    14 | B                                                        |                              34 | 0.0416           |
| UK261          | Mar-15, Apr-08 |                    12 | A.3                                                      |                              61 | 0.0358           |
| UK2916         | Mar-03, Jun-01 |                    12 | B.1                                                      |                               7 | 0.0525           |
| UK436          | Apr-13, May-14 |                    11 | B.1.5                                                    |                              25 | 0.1636           |
| UK137          | Mar-09, Mar-31 |                    11 | B.1.1                                                    |                              69 | 0.0266           |
| UK501          | Mar-19, Jun-02 |                    11 | B.1                                                      |                               6 | 0.1991           |
| UK5498         | Mar-12, May-28 |                    11 | B.2, B                                                   |                              11 | 0.0909           |
| UK601          | Mar-14, May-04 |                     8 | B.10                                                     |                              35 | 0.0168           |
| UK548          | Mar-14, Mar-30 |                     8 | B.2.1                                                    |                              70 | 0.0327           |
| UK594          | Apr-20, May-01 |                     8 | B                                                        |                              38 | 0.0414           |
| UK187          | Mar-23, Apr-30 |                     7 | B.1                                                      |                              39 | 0.0212           |
| UK271          | Apr-15, Apr-26 |                     7 | B.1                                                      |                              43 | 0.0797           |
| UK58           | Mar-12, Apr-09 |                     7 | B.1                                                      |                              60 | 0.0389           |
| UK151          | Mar-23, Apr-24 |                     7 | B.1                                                      |                              45 | 0.1185           |
| UK133          | Mar-22, Apr-25 |                     7 | B.1                                                      |                              44 | 0.0966           |
| UK51           | Mar-26, Jun-07 |                     7 | B.1.36                                                   |                               1 | 0.9873           |
| UK3692         | Mar-12, May-19 |                     6 | B.1.1                                                    |                              20 | 0.1268           |
| UK240          | Mar-22, May-08 |                     6 | B.2                                                      |                              31 | 0.0259           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | EDIN     |            11 |
|  1 | GLAS     |            23 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK36 |   UK5098 |   UK5 |   UK42 |   UK109 |   UK40 |   UK199 |   UK5676 |   UK2464 |   UK39 |
|:------------------|-------:|---------:|------:|-------:|--------:|-------:|--------:|---------:|---------:|-------:|
| 2020-02-23        |      0 |        0 |     1 |      0 |       0 |      0 |       0 |        0 |        0 |      0 |
| 2020-03-01        |      0 |        0 |     0 |      2 |       0 |      0 |       1 |        0 |        0 |      0 |
| 2020-03-08        |      0 |        0 |     7 |      8 |       1 |      1 |       0 |        3 |        0 |      1 |
| 2020-03-15        |      2 |        3 |     7 |      6 |       1 |      3 |       5 |        8 |        5 |      2 |
| 2020-03-22        |      8 |        7 |    10 |     13 |       1 |      6 |       7 |        9 |       10 |      5 |
| 2020-03-29        |     11 |        4 |    10 |     10 |       3 |      4 |       4 |        9 |        7 |      2 |
| 2020-04-05        |      7 |        5 |    14 |      8 |       4 |      3 |       3 |        4 |        6 |      3 |
| 2020-04-12        |     15 |        7 |    10 |     11 |       5 |      3 |       7 |        1 |        6 |      5 |
| 2020-04-19        |     16 |       15 |    14 |     12 |       5 |      8 |      10 |        7 |        8 |      4 |
| 2020-04-26        |     10 |        7 |     5 |      3 |       5 |      2 |       6 |        1 |        3 |      1 |
| 2020-05-03        |      7 |        5 |     6 |      4 |       4 |      1 |       3 |        4 |        5 |      2 |
| 2020-05-10        |      9 |       11 |     5 |      6 |       6 |      3 |       2 |        0 |        4 |      4 |
| 2020-05-17        |      6 |       10 |     5 |      2 |       4 |      1 |       2 |        1 |        0 |      1 |
| 2020-05-24        |      2 |        3 |     3 |      1 |       3 |      2 |       1 |        0 |        0 |      1 |
| 2020-05-31        |      0 |        0 |     0 |      0 |       3 |      0 |       1 |        0 |        1 |      0 |
| 2020-06-07        |      0 |        0 |     1 |      0 |       1 |      0 |       0 |        0 |        0 |      0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-01-27 |                            0 |                                1 |       1 |
| 2020-02-03 |                            0 |                                3 |       3 |
| 2020-02-05 |                            0 |                                1 |       1 |
| 2020-02-09 |                            0 |                                1 |       1 |
| 2020-02-13 |                            0 |                                1 |       1 |
| 2020-02-14 |                            0 |                                1 |       1 |
| 2020-02-23 |                            0 |                                2 |       2 |
| 2020-02-25 |                            0 |                                2 |       2 |
| 2020-02-26 |                            0 |                                1 |       1 |
| 2020-02-27 |                            0 |                                1 |       1 |
| 2020-02-28 |                            0 |                                3 |       3 |
| 2020-02-29 |                            0 |                                1 |       1 |
| 2020-03-02 |                            0 |                                3 |       3 |
| 2020-03-03 |                            0 |                                2 |       2 |
| 2020-03-04 |                            0 |                                5 |       5 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-06 |                            0 |                                7 |       7 |
| 2020-03-07 |                            1 |                                4 |       5 |
| 2020-03-09 |                            1 |                                8 |       9 |
| 2020-03-10 |                            0 |                                5 |       5 |
| 2020-03-11 |                            3 |                                6 |       9 |
| 2020-03-12 |                            1 |                               15 |      16 |
| 2020-03-13 |                            5 |                                3 |       8 |
| 2020-03-14 |                            0 |                                1 |       1 |
| 2020-03-15 |                            0 |                                2 |       2 |
| 2020-03-16 |                            1 |                                1 |       2 |
| 2020-03-17 |                            1 |                                6 |       7 |
| 2020-03-18 |                            0 |                                7 |       7 |
| 2020-03-19 |                            0 |                                3 |       3 |
| 2020-03-20 |                            1 |                                6 |       7 |
| 2020-03-21 |                            1 |                                2 |       3 |
| 2020-03-22 |                            2 |                                5 |       7 |
| 2020-03-23 |                            3 |                                7 |      10 |
| 2020-03-24 |                            4 |                                1 |       5 |
| 2020-03-25 |                            2 |                                2 |       4 |
| 2020-03-26 |                            0 |                                4 |       4 |
| 2020-03-27 |                            2 |                                4 |       6 |
| 2020-03-28 |                            0 |                                1 |       1 |
| 2020-03-29 |                            2 |                                1 |       3 |
| 2020-03-30 |                            3 |                                8 |      11 |
| 2020-03-31 |                            2 |                                3 |       5 |
| 2020-04-01 |                            2 |                                0 |       2 |
| 2020-04-02 |                            1 |                                4 |       5 |
| 2020-04-03 |                            0 |                                1 |       1 |
| 2020-04-04 |                            1 |                                1 |       2 |
| 2020-04-06 |                            1 |                                0 |       1 |
| 2020-04-07 |                            2 |                                0 |       2 |
| 2020-04-08 |                            3 |                                0 |       3 |
| 2020-04-09 |                            0 |                                1 |       1 |
| 2020-04-10 |                            0 |                                2 |       2 |
| 2020-04-11 |                            1 |                                1 |       2 |
| 2020-04-12 |                            0 |                                1 |       1 |
| 2020-04-13 |                            3 |                                0 |       3 |
| 2020-04-14 |                            0 |                                1 |       1 |
| 2020-04-16 |                            1 |                                1 |       2 |
| 2020-04-17 |                            1 |                                1 |       2 |
| 2020-04-20 |                            1 |                                2 |       3 |
| 2020-04-21 |                            1 |                                0 |       1 |
| 2020-04-22 |                            2 |                                3 |       5 |
| 2020-04-23 |                            1 |                                3 |       4 |
| 2020-04-24 |                            3 |                                0 |       3 |
| 2020-04-25 |                            0 |                                1 |       1 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-21 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   Scotland |
|:-----------|-----------:|
| 2020-02-28 |          1 |
| 2020-03-01 |          1 |
| 2020-03-02 |          1 |
| 2020-03-03 |          2 |
| 2020-03-04 |          5 |
| 2020-03-05 |          3 |
| 2020-03-06 |          7 |
| 2020-03-07 |          5 |
| 2020-03-08 |          1 |
| 2020-03-09 |         12 |
| 2020-03-10 |          5 |
| 2020-03-11 |         11 |
| 2020-03-12 |         32 |
| 2020-03-13 |         42 |
| 2020-03-14 |         13 |
| 2020-03-15 |          8 |
| 2020-03-16 |         14 |
| 2020-03-17 |         31 |
| 2020-03-18 |         24 |
| 2020-03-19 |         28 |
| 2020-03-20 |         32 |
| 2020-03-21 |         35 |
| 2020-03-22 |         32 |
| 2020-03-23 |         84 |
| 2020-03-24 |         87 |
| 2020-03-25 |         71 |
| 2020-03-26 |         91 |
| 2020-03-27 |         87 |
| 2020-03-28 |         40 |
| 2020-03-29 |         53 |
| 2020-03-30 |        120 |
| 2020-03-31 |         86 |
| 2020-04-01 |         71 |
| 2020-04-02 |         48 |
| 2020-04-03 |         57 |
| 2020-04-04 |         45 |
| 2020-04-05 |         50 |
| 2020-04-06 |         71 |
| 2020-04-07 |         70 |
| 2020-04-08 |         43 |
| 2020-04-09 |         25 |
| 2020-04-10 |         22 |
| 2020-04-11 |         46 |
| 2020-04-12 |         61 |
| 2020-04-13 |         55 |
| 2020-04-14 |         50 |
| 2020-04-15 |         51 |
| 2020-04-16 |         62 |
| 2020-04-17 |         24 |
| 2020-04-18 |         55 |
| 2020-04-19 |         30 |
| 2020-04-20 |         68 |
| 2020-04-21 |        104 |
| 2020-04-22 |         99 |
| 2020-04-23 |         76 |
| 2020-04-24 |         91 |
| 2020-04-25 |         70 |
| 2020-04-26 |         49 |
| 2020-04-27 |         61 |
| 2020-04-28 |         35 |
| 2020-04-29 |         23 |
| 2020-04-30 |         24 |
| 2020-05-01 |         25 |
| 2020-05-02 |         13 |
| 2020-05-03 |         16 |
| 2020-05-04 |          9 |
| 2020-05-05 |         17 |
| 2020-05-06 |         31 |
| 2020-05-07 |         33 |
| 2020-05-08 |         25 |
| 2020-05-09 |         17 |
| 2020-05-10 |         21 |
| 2020-05-11 |         16 |
| 2020-05-12 |         22 |
| 2020-05-13 |         29 |
| 2020-05-14 |         47 |
| 2020-05-15 |         22 |
| 2020-05-16 |         19 |
| 2020-05-17 |         16 |
| 2020-05-18 |         29 |
| 2020-05-19 |         29 |
| 2020-05-20 |         15 |
| 2020-05-21 |         13 |
| 2020-05-22 |          8 |
| 2020-05-23 |          7 |
| 2020-05-24 |          4 |
| 2020-05-25 |          8 |
| 2020-05-26 |          3 |
| 2020-05-27 |          5 |
| 2020-05-28 |          4 |
| 2020-05-29 |          1 |
| 2020-05-31 |          1 |
| 2020-06-01 |          3 |
| 2020-06-02 |         11 |
| 2020-06-03 |          1 |
| 2020-06-04 |          7 |
| 2020-06-05 |          1 |
| 2020-06-06 |          2 |
| 2020-06-07 |          1 |
| 2020-06-08 |          1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country   |   Number of sequences | Sequence group   |
|:-----------------------|:----------|----------------------:|:-----------------|
| ABERDEEN               | Scotland  |                    22 | 10-50            |
| ABERDEENSHIRE          | Scotland  |                     5 | 1-10             |
| ANGUS                  | Scotland  |                    38 | 10-50            |
| ARGYLL AND BUTE        | Scotland  |                     6 | 1-10             |
| CLACKMANNANSHIRE       | Scotland  |                     2 | 1-10             |
| DUMFRIES AND GALLOWAY  | Scotland  |                    68 | 50-100           |
| DUNDEE                 | Scotland  |                   140 | 100-150          |
| EAST AYRSHIRE          | Scotland  |                    84 | 50-100           |
| EAST DUNBARTONSHIRE    | Scotland  |                    36 | 10-50            |
| EAST LOTHIAN           | Scotland  |                    55 | 50-100           |
| EAST RENFREWSHIRE      | Scotland  |                    21 | 10-50            |
| EDINBURGH              | Scotland  |                   456 | 400-500          |
| EILEAN SIAR            | Scotland  |                     2 | 1-10             |
| FALKIRK                | Scotland  |                    92 | 50-100           |
| FIFE                   | Scotland  |                    45 | 10-50            |
| GLASGOW                | Scotland  |                   988 | >500             |
| HIGHLAND               | Scotland  |                     9 | 1-10             |
| INVERCLYDE             | Scotland  |                    15 | 10-50            |
| MIDLOTHIAN             | Scotland  |                   134 | 100-150          |
| MORAY                  | Scotland  |                     6 | 1-10             |
| NORTH AYRSHIRE         | Scotland  |                     5 | 1-10             |
| NORTH LANARKSHIRE      | Scotland  |                   200 | 200-250          |
| ORKNEY ISLANDS         | Scotland  |                     1 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland  |                    57 | 50-100           |
| RENFREWSHIRE           | Scotland  |                   272 | 250-300          |
| SCOTTISH BORDERS       | Scotland  |                   143 | 100-150          |
| SHETLAND ISLANDS       | Scotland  |                    14 | 10-50            |
| SOUTH AYRSHIRE         | Scotland  |                     3 | 1-10             |
| SOUTH LANARKSHIRE      | Scotland  |                    28 | 10-50            |
| STIRLING               | Scotland  |                    11 | 10-50            |
| WEST DUNBARTONSHIRE    | Scotland  |                    20 | 10-50            |
| WEST LOTHIAN           | Scotland  |                   119 | 100-150          |

\pagebreak






