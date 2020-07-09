







# Lineages report for LIVE




This report gives summaries of UK specific lineages sequenced by LIVE for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-16. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
699 sequences in the UK from the sequencing centre LIVE have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 75 and the maximum is 262


Sequences which were replicates or too error-prone were removed from this analysis.



70 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 10 that remain:
2 are pending extinction, ie last seen three weeks ago.
4 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
3 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 315 (100.0%) | Mar-21, Jun-16 |               315 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK36           | 31 (100.0%)  | Mar-29, Jun-03 |                31 | B.1              |                              13 | 0.1692           |
| UK42           | 25 (100.0%)  | Mar-23, May-26 |                25 | B.1              |                              21 | 0.127            |
| UK233          | 21 (100.0%)  | May-25, Jun-15 |                21 | B.1              |                               1 | 1.05             |
| UK501          | 21 (100.0%)  | Mar-24, Jun-02 |                21 | B.1              |                              14 | 0.25             |
| UK5300         | 16 (100.0%)  | Apr-17, Jun-16 |                16 | B.1.1            |                               0 | active today     |
| UK186          | 15 (100.0%)  | Apr-08, Jun-09 |                15 | B                |                               7 | 0.6327           |
| UK109          | 15 (100.0%)  | Apr-03, Jun-04 |                15 | B.1.5            |                              12 | 0.369            |
| UK274          | 13 (100.0%)  | Mar-23, Apr-15 |                13 | B.3              |                              62 | 0.0309           |
| UK632          | 12 (100.0%)  | Mar-23, Jun-10 |                12 | B.1.1            |                               6 | 1.197            |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/LIVE/figures/report_LIVE_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 17 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/LIVE/figures/report_LIVE_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/LIVE/figures/report_LIVE_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/LIVE/figures/report_LIVE_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/LIVE/figures/report_LIVE_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 109 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/LIVE/figures/report_LIVE_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England      | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 315 (100.0%) | Mar-21, Jun-16 |               315 | B.1.1.1, B.1.1   |                               0 | active today     |
| UK36           | 31 (100.0%)  | Mar-29, Jun-03 |                31 | B.1              |                              13 | 0.1692           |
| UK42           | 25 (100.0%)  | Mar-23, May-26 |                25 | B.1              |                              21 | 0.127            |
| UK233          | 21 (100.0%)  | May-25, Jun-15 |                21 | B.1              |                               1 | 1.05             |
| UK501          | 21 (100.0%)  | Mar-24, Jun-02 |                21 | B.1              |                              14 | 0.25             |
| UK5300         | 16 (100.0%)  | Apr-17, Jun-16 |                16 | B.1.1            |                               0 | active today     |
| UK186          | 15 (100.0%)  | Apr-08, Jun-09 |                15 | B                |                               7 | 0.6327           |
| UK109          | 15 (100.0%)  | Apr-03, Jun-04 |                15 | B.1.5            |                              12 | 0.369            |
| UK274          | 13 (100.0%)  | Mar-23, Apr-15 |                13 | B.3              |                              62 | 0.0309           |
| UK632          | 12 (100.0%)  | Mar-23, Jun-10 |                12 | B.1.1            |                               6 | 1.197            |
| UK5180         | 9 (100.0%)   | Mar-27, Apr-19 |                 9 | B.1.1.7          |                              58 | 0.0496           |
| UK1207         | 9 (100.0%)   | Mar-23, Apr-19 |                 9 | B.1.1            |                              58 | 0.0582           |
| UK131          | 7 (100.0%)   | Mar-24, Apr-14 |                 7 | B.15             |                              63 | 0.0556           |
| UK40           | 6 (100.0%)   | Mar-31, Apr-20 |                 6 | B.16             |                              57 | 0.0702           |
| UK202          | 6 (100.0%)   | Apr-02, Jun-04 |                 6 | B.1.1            |                              12 | 1.05             |
| UK390          | 6 (100.0%)   | Mar-29, May-01 |                 6 | B.1.5            |                              46 | 0.1435           |
| UK490          | 6 (100.0%)   | Apr-03, May-02 |                 6 | B.1.1            |                              45 | 0.1289           |
| UK832          | 6 (100.0%)   | Apr-14, Apr-26 |                 6 | A.5              |                              51 | 0.0471           |
| UK15           | 6 (100.0%)   | Apr-13, Apr-22 |                 6 | B.1.1            |                              55 | 0.0327           |
| UK199          | 6 (100.0%)   | Mar-29, Apr-27 |                 6 | B.1, B.1.5       |                              50 | 0.116            |
| UK777          | 6 (100.0%)   | Apr-01, Apr-14 |                 6 | B.1              |                              63 | 0.0413           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | LIVE     |            17 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK36 |   UK42 |   UK501 |   UK233 |   UK5300 |   UK109 |   UK186 |   UK632 |   UK202 |
|:------------------|------:|-------:|-------:|--------:|--------:|---------:|--------:|--------:|--------:|--------:|
| 2020-03-15        |     1 |      0 |      0 |       0 |       0 |        0 |       0 |       0 |       0 |       0 |
| 2020-03-22        |     2 |      0 |      3 |       1 |       0 |        0 |       0 |       0 |       1 |       0 |
| 2020-03-29        |     3 |      1 |      1 |       1 |       0 |        0 |       1 |       0 |       1 |       1 |
| 2020-04-05        |     4 |      2 |      1 |       1 |       0 |        0 |       2 |       1 |       1 |       0 |
| 2020-04-12        |     3 |      1 |      1 |       2 |       0 |        1 |       2 |       1 |       1 |       1 |
| 2020-04-19        |     5 |      1 |      0 |       1 |       0 |        1 |       2 |       1 |       1 |       1 |
| 2020-04-26        |     3 |      1 |      1 |       1 |       0 |        0 |       1 |       1 |       0 |       1 |
| 2020-05-03        |     2 |      1 |      0 |       0 |       0 |        0 |       0 |       1 |       0 |       0 |
| 2020-05-10        |     0 |      1 |      0 |       0 |       0 |        0 |       0 |       1 |       0 |       0 |
| 2020-05-17        |     2 |      0 |      0 |       0 |       0 |        0 |       0 |       0 |       0 |       0 |
| 2020-05-24        |     4 |      1 |      1 |       0 |       2 |        0 |       0 |       0 |       0 |       0 |
| 2020-05-31        |     5 |      2 |      0 |       1 |       2 |        1 |       1 |       0 |       0 |       1 |
| 2020-06-07        |     4 |      0 |      0 |       0 |       1 |        3 |       0 |       2 |       1 |       0 |
| 2020-06-14        |     1 |      0 |      0 |       0 |       1 |        1 |       0 |       0 |       0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-20 |                            0 |                                1 |       1 |
| 2020-03-21 |                            2 |                                1 |       3 |
| 2020-03-23 |                            1 |                                4 |       5 |
| 2020-03-24 |                            2 |                                3 |       5 |
| 2020-03-25 |                            3 |                                1 |       4 |
| 2020-03-26 |                            0 |                                2 |       2 |
| 2020-03-27 |                            0 |                                2 |       2 |
| 2020-03-28 |                            0 |                                1 |       1 |
| 2020-03-29 |                            1 |                                4 |       5 |
| 2020-03-30 |                            1 |                                1 |       2 |
| 2020-03-31 |                            2 |                                1 |       3 |
| 2020-04-01 |                            1 |                                2 |       3 |
| 2020-04-02 |                            0 |                                2 |       2 |
| 2020-04-03 |                            1 |                                8 |       9 |
| 2020-04-04 |                            0 |                                1 |       1 |
| 2020-04-05 |                            0 |                                1 |       1 |
| 2020-04-07 |                            2 |                                1 |       3 |
| 2020-04-08 |                            2 |                                3 |       5 |
| 2020-04-09 |                            2 |                                4 |       6 |
| 2020-04-10 |                            1 |                                0 |       1 |
| 2020-04-11 |                            3 |                                1 |       4 |
| 2020-04-12 |                            1 |                                0 |       1 |
| 2020-04-13 |                            0 |                                1 |       1 |
| 2020-04-14 |                            0 |                                2 |       2 |
| 2020-04-15 |                            1 |                                0 |       1 |
| 2020-04-16 |                            2 |                                0 |       2 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            1 |                                1 |       2 |
| 2020-04-20 |                            1 |                                0 |       1 |
| 2020-04-25 |                            2 |                                0 |       2 |
| 2020-04-29 |                            1 |                                0 |       1 |
| 2020-05-01 |                            1 |                                1 |       2 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-25 |                            0 |                                2 |       2 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-05-27 |                            1 |                                0 |       1 |
| 2020-06-08 |                            1 |                                0 |       1 |
| 2020-06-12 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-20 |         1 |
| 2020-03-21 |         3 |
| 2020-03-22 |         1 |
| 2020-03-23 |        13 |
| 2020-03-24 |        11 |
| 2020-03-25 |        10 |
| 2020-03-26 |         7 |
| 2020-03-27 |         8 |
| 2020-03-28 |         4 |
| 2020-03-29 |         9 |
| 2020-03-30 |        13 |
| 2020-03-31 |        11 |
| 2020-04-01 |        15 |
| 2020-04-02 |        13 |
| 2020-04-03 |        31 |
| 2020-04-04 |        16 |
| 2020-04-05 |        17 |
| 2020-04-06 |         7 |
| 2020-04-07 |        24 |
| 2020-04-08 |        35 |
| 2020-04-09 |        40 |
| 2020-04-10 |        19 |
| 2020-04-11 |        14 |
| 2020-04-12 |        18 |
| 2020-04-13 |        19 |
| 2020-04-14 |        14 |
| 2020-04-15 |         9 |
| 2020-04-16 |        12 |
| 2020-04-17 |        17 |
| 2020-04-18 |        10 |
| 2020-04-19 |        12 |
| 2020-04-20 |        13 |
| 2020-04-21 |        21 |
| 2020-04-22 |        14 |
| 2020-04-23 |         8 |
| 2020-04-24 |         9 |
| 2020-04-25 |         8 |
| 2020-04-26 |         8 |
| 2020-04-27 |         8 |
| 2020-04-28 |         7 |
| 2020-04-29 |         5 |
| 2020-04-30 |         2 |
| 2020-05-01 |        12 |
| 2020-05-02 |         4 |
| 2020-05-03 |         4 |
| 2020-05-04 |         2 |
| 2020-05-05 |         2 |
| 2020-05-06 |         1 |
| 2020-05-07 |         3 |
| 2020-05-09 |         1 |
| 2020-05-11 |         1 |
| 2020-05-12 |         2 |
| 2020-05-13 |         1 |
| 2020-05-15 |         1 |
| 2020-05-23 |         2 |
| 2020-05-24 |         1 |
| 2020-05-25 |        11 |
| 2020-05-26 |        14 |
| 2020-05-27 |         5 |
| 2020-05-28 |         3 |
| 2020-05-31 |         7 |
| 2020-06-01 |        12 |
| 2020-06-02 |        14 |
| 2020-06-03 |        16 |
| 2020-06-04 |        11 |
| 2020-06-05 |         1 |
| 2020-06-06 |         3 |
| 2020-06-07 |         4 |
| 2020-06-08 |         6 |
| 2020-06-09 |         5 |
| 2020-06-10 |         3 |
| 2020-06-12 |         1 |
| 2020-06-13 |         1 |
| 2020-06-15 |         3 |
| 2020-06-16 |         6 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2     | Country   |   Number of sequences | Sequence group   |
|:-----------|:----------|----------------------:|:-----------------|
| CHESHIRE   | England   |                    32 | 10-50            |
| CUMBRIA    | England   |                    18 | 10-50            |
| DERBYSHIRE | England   |                     2 | 1-10             |
| GWYNEDD    | Wales     |                     2 | 1-10             |
| LANCASHIRE | England   |                    45 | 10-50            |
| MERSEYSIDE | England   |                   489 | 400-500          |

\pagebreak






