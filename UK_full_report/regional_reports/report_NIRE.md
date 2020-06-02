
# UK lineages summary report








This report gives summaries of UK specific lineages sequenced by NIRE for week 2020-05-29. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-03-29. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
163 sequences in the UK from the sequencing centre NIRE have been included in this analysis.

A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6130 and the maximum is 9084


Sequences which were replicates or too error-prone were removed from this analysis.



83 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 4 that remain:
4 lineages have been continuously circulating.


The following table contains information about lineages and the number of sequences the dataset, in reverse size order. 

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Northern_Ireland   | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) |
|:---------------|:-------------------|:---------------|------------------:|:-----------------|--------------------------------:|
| UK72           | 42 (100.0%)        | Mar-11, Mar-26 |                42 | B.10             |                               3 |
| UK760          | 11 (100.0%)        | Mar-21, Mar-28 |                11 | B.1.1            |                               1 |
| UK295          | 8 (100.0%)         | Mar-11, Mar-24 |                 8 | B                |                               5 |
| UK701          | 7 (100.0%)         | Mar-20, Mar-29 |                 7 | B.1              |                               0 |


These data is represented in the stacked bar chart below. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 






![](UK_full_report/regional_reports/results/results_NIRE/figures/report_NIRE_stacked_bars_by_country_1.png)\


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown below. 
The raw data for the plot is shown below it, with each column representing a lineage, and the number of admin2 regions it is present in in each week.







![](UK_full_report/regional_reports/results/results_NIRE/figures/report_NIRE_geog_plot_1.png)\



| Week commencing   |   UK72 |   UK760 |   UK295 |   UK701 |
|:------------------|-------:|--------:|--------:|--------:|
| 2020-03-08        |      1 |       0 |       1 |       0 |
| 2020-03-15        |      3 |       1 |       2 |       1 |
| 2020-03-22        |      5 |       3 |       3 |       3 |
| 2020-03-29        |      0 |       0 |       0 |       1 |














The date of first sequence in the cluster is shown below for every cluster with date information. 









![](UK_full_report/regional_reports/results/results_NIRE/figures/report_NIRE_firsts_plot_1.png)\



| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-10 |                            2 |                                0 |       2 |
| 2020-03-11 |                            0 |                                3 |       3 |
| 2020-03-13 |                            1 |                                0 |       1 |
| 2020-03-14 |                            5 |                                0 |       5 |
| 2020-03-16 |                            0 |                                1 |       1 |
| 2020-03-17 |                            3 |                                0 |       3 |
| 2020-03-18 |                            4 |                                0 |       4 |
| 2020-03-19 |                            1 |                                0 |       1 |
| 2020-03-20 |                            2 |                                1 |       3 |
| 2020-03-21 |                            5 |                                1 |       6 |
| 2020-03-22 |                            3 |                                1 |       4 |
| 2020-03-23 |                           11 |                                2 |      13 |
| 2020-03-24 |                           12 |                                1 |      13 |
| 2020-03-25 |                           11 |                                1 |      12 |
| 2020-03-26 |                            6 |                                1 |       7 |
| 2020-03-28 |                            6 |                                0 |       6 |
| 2020-03-29 |                            2 |                                1 |       3 |

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.





![](UK_full_report/regional_reports/results/results_NIRE/figures/report_NIRE_seqs_over_time_1.png)\



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
| 2020-03-26 |                 19 |
| 2020-03-28 |                 11 |
| 2020-03-29 |                  5 |


These lineages are shown on the timeline below. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.








![](UK_full_report/regional_reports/results/results_NIRE/figures/report_NIRE_make_timeline_1.png)\


The map below shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.



All sequences have been assigned clean adm2 data this week.



![](UK_full_report/regional_reports/results/results_NIRE/figures/report_NIRE_map_1.png)\



| Admin2      | Country          |   Number of sequences | Sequence group   |
|:------------|:-----------------|----------------------:|:-----------------|
| ANTRIM      | Northern Ireland |                    83 | 50-100           |
| ARMAGH      | Northern Ireland |                    12 | 10-50            |
| DOWN        | Northern Ireland |                    46 | 10-50            |
| FERMANAGH   | Northern Ireland |                     3 | 1-10             |
| LONDONDERRY | Northern Ireland |                     8 | 1-10             |
| TYRONE      | Northern Ireland |                    11 | 10-50            |









Other results modules for UK lineage analysis can be added in here if required.

\pagebreak













