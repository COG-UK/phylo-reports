







# Lineages report for Northern Ireland




This report gives summaries of lineages sampled in Northern Ireland for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-01. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
687 sequences from Northern_Ireland have been included in this analysis.
72 lineages have been recorded, 41 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 63 and the maximum is 243


Sequences which were replicates or too error-prone were removed from this analysis.



59 are lineages which were sampled less than five times in Northern_Ireland, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 13 that remain:
4 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
2 lineages have reactivated.
6 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Date range     |   Number of sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | Mar-10, Jun-01 |                   359 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK601          | Mar-11, May-11 |                    66 | B.10             |                              21 | 0.0299           |
| UK482          | Apr-10, May-05 |                    27 | B.1.1            |                              27 | 0.0423           |
| UK167          | Mar-14, Jun-01 |                    26 | B.1              |                               0 | active today     |
| UK2913         | Apr-06, Jun-01 |                    17 | B.1.p11          |                               0 | active today     |
| UK2735         | Mar-26, May-31 |                    14 | B.1.1            |                               1 | 0.31             |
| UK107          | Mar-17, May-19 |                    14 | B.2.1            |                              13 | 0.0062           |
| UK706          | Mar-28, Apr-29 |                    14 | B.1.1            |                              33 | 0.0644           |
| UK72           | Mar-11, May-27 |                    12 | B                |                               5 | 0.0694           |
| UK2916         | Mar-20, Jun-01 |                     9 | B.1              |                               0 | active today     |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/Northern_Ireland/figures/Northern_Ireland_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.




The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/Northern_Ireland/figures/Northern_Ireland_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/Northern_Ireland/figures/Northern_Ireland_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 



NB the lineage may have started anywhere in the UK, but has been recorded at least once in Northern_Ireland



![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/Northern_Ireland/figures/Northern_Ireland_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/Northern_Ireland/figures/Northern_Ireland_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/Northern_Ireland/figures/Northern_Ireland_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Date range     |   Number of sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | Mar-10, Jun-01 |                   359 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK601          | Mar-11, May-11 |                    66 | B.10             |                              21 | 0.0299           |
| UK482          | Apr-10, May-05 |                    27 | B.1.1            |                              27 | 0.0423           |
| UK167          | Mar-14, Jun-01 |                    26 | B.1              |                               0 | active today     |
| UK2913         | Apr-06, Jun-01 |                    17 | B.1.p11          |                               0 | active today     |
| UK2735         | Mar-26, May-31 |                    14 | B.1.1            |                               1 | 0.31             |
| UK107          | Mar-17, May-19 |                    14 | B.2.1            |                              13 | 0.0062           |
| UK706          | Mar-28, Apr-29 |                    14 | B.1.1            |                              33 | 0.0644           |
| UK72           | Mar-11, May-27 |                    12 | B                |                               5 | 0.0694           |
| UK2916         | Mar-20, Jun-01 |                     9 | B.1              |                               0 | active today     |
| UK187          | Mar-26, Apr-30 |                     9 | B.1              |                              32 | 0.0245           |
| UK581          | Apr-06, May-01 |                     9 | B.1.1            |                              31 | 0.0896           |
| UK109          | Apr-13, May-31 |                     8 | B.1.5            |                               1 | 0.2317           |
| UK370          | Mar-24, May-30 |                     8 | B.1.1.10         |                               2 | 0.2684           |
| UK320          | Mar-22, May-16 |                     7 | B.1              |                              16 | 0.375            |
| UK2200         | Mar-23, May-05 |                     6 | B.1.5            |                              27 | 0.0343           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NIRE     |            94 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK601 |   UK482 |   UK167 |   UK2913 |   UK107 |   UK2735 |   UK72 |   UK2916 |   UK370 |
|:------------------|------:|--------:|--------:|--------:|---------:|--------:|---------:|-------:|---------:|--------:|
| 2020-03-08        |     2 |       1 |       0 |       2 |        0 |       0 |        0 |      1 |        0 |       0 |
| 2020-03-15        |     3 |       3 |       0 |       0 |        0 |       1 |        0 |      2 |        1 |       0 |
| 2020-03-22        |     4 |       5 |       0 |       1 |        0 |       2 |        1 |      3 |        4 |       2 |
| 2020-03-29        |     3 |       2 |       0 |       1 |        0 |       0 |        0 |      1 |        1 |       1 |
| 2020-04-05        |     4 |       2 |       1 |       1 |        2 |       1 |        2 |      0 |        0 |       1 |
| 2020-04-12        |     5 |       2 |       2 |       2 |        1 |       1 |        1 |      0 |        0 |       1 |
| 2020-04-19        |     5 |       1 |       3 |       1 |        2 |       0 |        1 |      1 |        0 |       0 |
| 2020-04-26        |     4 |       1 |       2 |       1 |        1 |       0 |        3 |      0 |        0 |       0 |
| 2020-05-03        |     5 |       0 |       2 |       2 |        1 |       0 |        1 |      0 |        0 |       0 |
| 2020-05-10        |     2 |       0 |       0 |       0 |        0 |       0 |        0 |      0 |        0 |       0 |
| 2020-05-17        |     2 |       0 |       0 |       0 |        0 |       0 |        0 |      0 |        0 |       0 |
| 2020-05-24        |     1 |       0 |       0 |       0 |        0 |       0 |        0 |      0 |        0 |       0 |
| 2020-05-31        |     1 |       0 |       0 |       0 |        0 |       0 |        0 |      0 |        0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-02-03 |                            0 |                                1 |       1 |
| 2020-02-05 |                            0 |                                1 |       1 |
| 2020-02-09 |                            0 |                                1 |       1 |
| 2020-02-16 |                            0 |                                1 |       1 |
| 2020-02-23 |                            0 |                                1 |       1 |
| 2020-02-24 |                            0 |                                1 |       1 |
| 2020-02-25 |                            0 |                                1 |       1 |
| 2020-02-26 |                            0 |                                2 |       2 |
| 2020-02-27 |                            0 |                                1 |       1 |
| 2020-02-28 |                            0 |                                2 |       2 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-06 |                            0 |                                3 |       3 |
| 2020-03-07 |                            0 |                                2 |       2 |
| 2020-03-09 |                            0 |                                2 |       2 |
| 2020-03-10 |                            0 |                                1 |       1 |
| 2020-03-11 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                5 |       5 |
| 2020-03-14 |                            3 |                                0 |       3 |
| 2020-03-17 |                            0 |                                2 |       2 |
| 2020-03-18 |                            0 |                                4 |       4 |
| 2020-03-19 |                            0 |                                1 |       1 |
| 2020-03-20 |                            1 |                                1 |       2 |
| 2020-03-21 |                            0 |                                2 |       2 |
| 2020-03-22 |                            0 |                                1 |       1 |
| 2020-03-23 |                            1 |                                1 |       2 |
| 2020-03-24 |                            1 |                                2 |       3 |
| 2020-03-25 |                            2 |                                3 |       5 |
| 2020-03-26 |                            2 |                                2 |       4 |
| 2020-03-27 |                            0 |                                1 |       1 |
| 2020-03-30 |                            0 |                                2 |       2 |
| 2020-04-03 |                            0 |                                1 |       1 |
| 2020-04-06 |                            0 |                                1 |       1 |
| 2020-04-08 |                            0 |                                1 |       1 |
| 2020-04-10 |                            1 |                                0 |       1 |
| 2020-04-11 |                            0 |                                1 |       1 |
| 2020-04-12 |                            0 |                                1 |       1 |
| 2020-04-13 |                            0 |                                1 |       1 |
| 2020-04-15 |                            1 |                                1 |       2 |
| 2020-04-16 |                            1 |                                1 |       2 |
| 2020-04-20 |                            1 |                                0 |       1 |
| 2020-04-25 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   Northern Ireland |
|:-----------|-------------------:|
| 2020-03-10 |                  2 |
| 2020-03-11 |                  3 |
| 2020-03-13 |                  1 |
| 2020-03-14 |                  6 |
| 2020-03-16 |                  5 |
| 2020-03-17 |                  7 |
| 2020-03-18 |                  6 |
| 2020-03-19 |                  3 |
| 2020-03-20 |                  6 |
| 2020-03-21 |                 13 |
| 2020-03-22 |                  8 |
| 2020-03-23 |                 29 |
| 2020-03-24 |                 23 |
| 2020-03-25 |                 16 |
| 2020-03-26 |                 27 |
| 2020-03-27 |                  7 |
| 2020-03-28 |                 12 |
| 2020-03-29 |                 11 |
| 2020-03-30 |                  6 |
| 2020-03-31 |                  8 |
| 2020-04-02 |                  1 |
| 2020-04-04 |                  1 |
| 2020-04-06 |                 18 |
| 2020-04-07 |                  5 |
| 2020-04-08 |                 14 |
| 2020-04-09 |                  1 |
| 2020-04-10 |                 19 |
| 2020-04-11 |                 14 |
| 2020-04-12 |                 23 |
| 2020-04-13 |                 22 |
| 2020-04-14 |                 14 |
| 2020-04-15 |                 23 |
| 2020-04-16 |                 32 |
| 2020-04-17 |                 28 |
| 2020-04-18 |                  7 |
| 2020-04-19 |                  9 |
| 2020-04-20 |                 25 |
| 2020-04-21 |                 23 |
| 2020-04-22 |                 23 |
| 2020-04-23 |                 11 |
| 2020-04-24 |                 10 |
| 2020-04-25 |                 14 |
| 2020-04-26 |                  4 |
| 2020-04-27 |                 11 |
| 2020-04-28 |                 15 |
| 2020-04-29 |                 11 |
| 2020-04-30 |                 15 |
| 2020-05-01 |                 16 |
| 2020-05-02 |                  9 |
| 2020-05-03 |                 12 |
| 2020-05-04 |                 20 |
| 2020-05-05 |                  4 |
| 2020-05-06 |                  2 |
| 2020-05-07 |                  3 |
| 2020-05-08 |                  7 |
| 2020-05-09 |                 10 |
| 2020-05-10 |                  1 |
| 2020-05-11 |                  3 |
| 2020-05-12 |                  4 |
| 2020-05-18 |                  1 |
| 2020-05-19 |                  1 |
| 2020-05-27 |                  1 |
| 2020-06-01 |                  1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2      | Country          |   Number of sequences | Sequence group   |
|:------------|:-----------------|----------------------:|:-----------------|
| ANTRIM      | Northern Ireland |                   325 | 300-400          |
| ARMAGH      | Northern Ireland |                    29 | 10-50            |
| DOWN        | Northern Ireland |                   272 | 250-300          |
| FERMANAGH   | Northern Ireland |                     5 | 1-10             |
| LONDONDERRY | Northern Ireland |                    32 | 10-50            |
| TYRONE      | Northern Ireland |                    25 | 10-50            |

\pagebreak






