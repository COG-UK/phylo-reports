







# UK Lineages report




This report gives summaries of UK specific lineages for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-28. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
27611 sequences in the UK have been included in this analysis.
1167 lineages have been recorded, 565 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 937 and the maximum is 10919


Sequences which were replicates or too error-prone were removed from this analysis.



893 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 66 that remain:
43 are pending extinction, ie last seen three weeks ago.
16 lineages have gone quiet, ie haven't been seen this week.
3 lineages have reactivated.
4 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England       | Wales         | Scotland     | Northern Ireland   | Date range     |   Total sequences | Global lineage                                                                                                                         |   Time since last sample (days) |   Activity score |
|:---------------|:--------------|:--------------|:-------------|:-------------------|:---------------|------------------:|:---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------:|-----------------:|
| UK5            | 6696 (77.34%) | 1168 (13.49%) | 435 (5.02%)  | 359 (4.15%)        | Feb-16, Jun-27 |              8658 | B.1.1.16, B.1.1.p12, B.1.1.4, B.1.1.p16, B.1.1.10, B.1.1.14, B.1.1.13, B.1.1.p11, B.1.1.p15, B.1.1.2, B.1.1.5, B.1.1, B.1.1.3, B.1.1.1 |                               1 |           0.0152 |
| UK107          | 1293 (91.44%) | 61 (4.31%)    | 46 (3.25%)   | 14 (0.99%)         | Feb-09, Jun-02 |              1414 | B, B.2, B.2.5, B.2.1                                                                                                                   |                              26 |           0.0031 |
| UK42           | 794 (58.0%)   | 368 (26.88%)  | 205 (14.97%) | 2 (0.15%)          | Feb-24, Jun-21 |              1369 | B.1.35, B.1.72, B.1.p11, B.1.5, B.1.p73, B.1, B.1.71                                                                                   |                               7 |           0.0123 |
| UK36           | 68 (11.2%)    | 1 (0.16%)     | 536 (88.3%)  | 2 (0.33%)          | Mar-18, Jun-06 |               607 | B.1                                                                                                                                    |                              22 |           0.006  |
| UK5676         | 362 (63.4%)   | 54 (9.46%)    | 150 (26.27%) | 5 (0.88%)          | Feb-26, May-27 |               571 | B.2                                                                                                                                    |                              32 |           0.005  |
| UK2464         | 298 (53.6%)   | 78 (14.03%)   | 180 (32.37%) | 0 (0%)             | Mar-09, Jun-18 |               556 | B.1.p11, B.1                                                                                                                           |                              10 |           0.0182 |
| UK199          | 260 (47.62%)  | 55 (10.07%)   | 227 (41.58%) | 4 (0.73%)          | Feb-26, Jun-22 |               546 | B.1.5, B.1.5.5, B.1, B.1.p73                                                                                                           |                               6 |           0.0358 |
| UK2913         | 387 (72.74%)  | 18 (3.38%)    | 110 (20.68%) | 17 (3.2%)          | Mar-07, Jun-16 |               532 | B.1.p11, B.1                                                                                                                           |                              12 |           0.0159 |
| UK61           | 107 (20.19%)  | 419 (79.06%)  | 3 (0.57%)    | 1 (0.19%)          | Feb-23, May-27 |               530 | B, B.3                                                                                                                                 |                              32 |           0.0056 |
| UK5098         | 6 (1.36%)     | 1 (0.23%)     | 433 (98.41%) | 0 (0%)             | Mar-01, Jun-05 |               440 | B.1.8, B.1, B.1.p73                                                                                                                    |                              23 |           0.0095 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_geog_plot_1.png){#geog_plot }




The growth and decline of diversity of lineages over time for each country is shown in the ridge plot in figure four.
This is represented by the Shannon Diversity, calculated using the number of sequences from each country from each lineage.



![Shannon diversity of lineages in each adm1 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_diversity_plot_1.png){#diversity_plot }



These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix



The plot below shows the number of sequences from each country that don't have specific enough location data to plot on the map.




![](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/full_report/figures/UK_report_map_2.png)\


Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England       | Wales         | Scotland     | Northern Ireland   | Date range     |   Total sequences | Global lineage                                                                                                                         |   Time since last sample (days) | Activity score   |
|:---------------|:--------------|:--------------|:-------------|:-------------------|:---------------|------------------:|:---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | 6696 (77.34%) | 1168 (13.49%) | 435 (5.02%)  | 359 (4.15%)        | Feb-16, Jun-27 |              8658 | B.1.1.16, B.1.1.p12, B.1.1.4, B.1.1.p16, B.1.1.10, B.1.1.14, B.1.1.13, B.1.1.p11, B.1.1.p15, B.1.1.2, B.1.1.5, B.1.1, B.1.1.3, B.1.1.1 |                               1 | 0.0152           |
| UK107          | 1293 (91.44%) | 61 (4.31%)    | 46 (3.25%)   | 14 (0.99%)         | Feb-09, Jun-02 |              1414 | B, B.2, B.2.5, B.2.1                                                                                                                   |                              26 | 0.0031           |
| UK42           | 794 (58.0%)   | 368 (26.88%)  | 205 (14.97%) | 2 (0.15%)          | Feb-24, Jun-21 |              1369 | B.1.35, B.1.72, B.1.p11, B.1.5, B.1.p73, B.1, B.1.71                                                                                   |                               7 | 0.0123           |
| UK36           | 68 (11.2%)    | 1 (0.16%)     | 536 (88.3%)  | 2 (0.33%)          | Mar-18, Jun-06 |               607 | B.1                                                                                                                                    |                              22 | 0.006            |
| UK5676         | 362 (63.4%)   | 54 (9.46%)    | 150 (26.27%) | 5 (0.88%)          | Feb-26, May-27 |               571 | B.2                                                                                                                                    |                              32 | 0.005            |
| UK2464         | 298 (53.6%)   | 78 (14.03%)   | 180 (32.37%) | 0 (0%)             | Mar-09, Jun-18 |               556 | B.1.p11, B.1                                                                                                                           |                              10 | 0.0182           |
| UK199          | 260 (47.62%)  | 55 (10.07%)   | 227 (41.58%) | 4 (0.73%)          | Feb-26, Jun-22 |               546 | B.1.5, B.1.5.5, B.1, B.1.p73                                                                                                           |                               6 | 0.0358           |
| UK2913         | 387 (72.74%)  | 18 (3.38%)    | 110 (20.68%) | 17 (3.2%)          | Mar-07, Jun-16 |               532 | B.1.p11, B.1                                                                                                                           |                              12 | 0.0159           |
| UK61           | 107 (20.19%)  | 419 (79.06%)  | 3 (0.57%)    | 1 (0.19%)          | Feb-23, May-27 |               530 | B, B.3                                                                                                                                 |                              32 | 0.0056           |
| UK5098         | 6 (1.36%)     | 1 (0.23%)     | 433 (98.41%) | 0 (0%)             | Mar-01, Jun-05 |               440 | B.1.8, B.1, B.1.p73                                                                                                                    |                              23 | 0.0095           |
| UK109          | 111 (27.89%)  | 35 (8.79%)    | 244 (61.31%) | 8 (2.01%)          | Mar-12, Jun-12 |               398 | B.1.5, B.1.5.5                                                                                                                         |                              16 | 0.0145           |
| UK2916         | 301 (79.84%)  | 54 (14.32%)   | 13 (3.45%)   | 9 (2.39%)          | Feb-03, Jun-10 |               377 | B.1                                                                                                                                    |                              18 | 0.0189           |
| UK72           | 265 (77.71%)  | 15 (4.4%)     | 49 (14.37%)  | 12 (3.52%)         | Feb-05, Jun-02 |               341 | B.2.2, B                                                                                                                               |                              26 | 0.0133           |
| UK167          | 240 (75.24%)  | 21 (6.58%)    | 32 (10.03%)  | 26 (8.15%)         | Mar-06, Jun-07 |               319 | B.1.66, B.1                                                                                                                            |                              21 | 0.0139           |
| UK5741         | 191 (64.53%)  | 104 (35.14%)  | 1 (0.34%)    | 0 (0%)             | Mar-09, Jun-12 |               296 | B.1.44, B.1                                                                                                                            |                              16 | 0.0201           |
| UK632          | 42 (15.33%)   | 232 (84.67%)  | 0 (0%)       | 0 (0%)             | Mar-23, Jun-10 |               274 | B.1.1                                                                                                                                  |                              18 | 0.0161           |
| UK2735         | 150 (55.15%)  | 76 (27.94%)   | 32 (11.76%)  | 14 (5.15%)         | Mar-18, Jun-10 |               272 | B.1.1                                                                                                                                  |                              18 | 0.0172           |
| UK3021         | 23 (9.27%)    | 225 (90.73%)  | 0 (0%)       | 0 (0%)             | Mar-12, Jun-09 |               248 | B.1                                                                                                                                    |                              19 | 0.019            |
| UK9            | 226 (99.56%)  | 1 (0.44%)     | 0 (0%)       | 0 (0%)             | Mar-09, May-15 |               227 | B.1.13                                                                                                                                 |                              44 | 0.0067           |
| UK40           | 6 (2.69%)     | 2 (0.9%)      | 215 (96.41%) | 0 (0%)             | Mar-13, Jun-08 |               223 | B.16, B                                                                                                                                |                              20 | 0.0196           |
| UK5561         | 169 (84.5%)   | 23 (11.5%)    | 7 (3.5%)     | 1 (0.5%)           | Feb-25, May-24 |               200 | B.2.2, B.2                                                                                                                             |                              35 | 0.0128           |
| UK15           | 141 (73.82%)  | 11 (5.76%)    | 36 (18.85%)  | 3 (1.57%)          | Feb-27, May-06 |               191 | B.1.1                                                                                                                                  |                              53 | 0.0069           |
| UK370          | 93 (48.69%)   | 50 (26.18%)   | 40 (20.94%)  | 8 (4.19%)          | Mar-06, Jun-16 |               191 | B.1.1.10                                                                                                                               |                              12 | 0.0447           |
| UK240          | 169 (91.85%)  | 2 (1.09%)     | 13 (7.07%)   | 0 (0%)             | Feb-25, May-27 |               184 | B, B.2, B.2.5, B.2.1                                                                                                                   |                              32 | 0.0157           |
| UK39           | 3 (2.03%)     | 0 (0%)        | 145 (97.97%) | 0 (0%)             | Mar-12, May-29 |               148 | A.2                                                                                                                                    |                              30 | 0.0177           |
| UK6            | 135 (96.43%)  | 0 (0%)        | 5 (3.57%)    | 0 (0%)             | Mar-06, Jun-16 |               140 | B.1                                                                                                                                    |                              12 | 0.0612           |
| UK63           | 128 (95.52%)  | 2 (1.49%)     | 4 (2.99%)    | 0 (0%)             | Mar-18, May-10 |               134 | B.1.1                                                                                                                                  |                              49 | 0.0081           |
| UK4            | 124 (95.38%)  | 2 (1.54%)     | 3 (2.31%)    | 1 (0.77%)          | Feb-28, Apr-29 |               130 | B                                                                                                                                      |                              60 | 0.0079           |
| UK494          | 125 (97.66%)  | 1 (0.78%)     | 2 (1.56%)    | 0 (0%)             | Mar-19, May-05 |               128 | B.1.p11, B.1                                                                                                                           |                              54 | 0.0069           |
| UK495          | 1 (0.79%)     | 124 (98.41%)  | 1 (0.79%)    | 0 (0%)             | Mar-28, Jun-03 |               126 | B.1.p11                                                                                                                                |                              25 | 0.0214           |
| UK66           | 105 (85.37%)  | 0 (0%)        | 17 (13.82%)  | 1 (0.81%)          | Mar-18, May-20 |               123 | B.1.1.8                                                                                                                                |                              39 | 0.0132           |
| UK668          | 28 (24.14%)   | 1 (0.86%)     | 87 (75.0%)   | 0 (0%)             | Mar-20, Jun-10 |               116 | B.1                                                                                                                                    |                              18 | 0.0396           |
| UK2200         | 37 (34.26%)   | 35 (32.41%)   | 30 (27.78%)  | 6 (5.56%)          | Feb-28, Jun-06 |               108 | B.1.5, B.1.5.6                                                                                                                         |                              22 | 0.0421           |
| UK605          | 24 (22.22%)   | 79 (73.15%)   | 4 (3.7%)     | 1 (0.93%)          | Mar-17, May-24 |               108 | B.1.1, B.1.1.10                                                                                                                        |                              35 | 0.0182           |
| UK822          | 1 (0.97%)     | 102 (99.03%)  | 0 (0%)       | 0 (0%)             | Apr-14, Jun-11 |               103 | B.1                                                                                                                                    |                              17 | 0.0334           |
| UK5180         | 93 (92.08%)   | 4 (3.96%)     | 0 (0%)       | 4 (3.96%)          | Mar-07, May-09 |               101 | B.1.1.7                                                                                                                                |                              50 | 0.0126           |
| UK28           | 99 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-13, May-08 |                99 | B.1.1.10                                                                                                                               |                              51 | 0.0112           |
| UK601          | 23 (23.47%)   | 0 (0%)        | 9 (9.18%)    | 66 (67.35%)        | Mar-11, May-11 |                98 | B.10                                                                                                                                   |                              48 | 0.0131           |
| UK51           | 88 (91.67%)   | 0 (0%)        | 7 (7.29%)    | 1 (1.04%)          | Mar-21, Jun-20 |                96 | B.1.36                                                                                                                                 |                               8 | 0.1197           |
| UK5322         | 2 (2.11%)     | 86 (90.53%)   | 7 (7.37%)    | 0 (0%)             | Mar-22, Jun-04 |                95 | B.1.1                                                                                                                                  |                              24 | 0.0328           |
| UK77           | 88 (95.65%)   | 4 (4.35%)     | 0 (0%)       | 0 (0%)             | Mar-11, May-20 |                92 | B.2                                                                                                                                    |                              39 | 0.0197           |
| UK5498         | 72 (79.12%)   | 7 (7.69%)     | 12 (13.19%)  | 0 (0%)             | Mar-06, May-28 |                91 | B, B.2                                                                                                                                 |                              31 | 0.0297           |
| UK501          | 66 (75.86%)   | 1 (1.15%)     | 20 (22.99%)  | 0 (0%)             | Mar-11, Jun-18 |                87 | B.1                                                                                                                                    |                              10 | 0.1151           |
| UK829          | 84 (98.82%)   | 0 (0%)        | 1 (1.18%)    | 0 (0%)             | Mar-03, Apr-29 |                85 | B.2.5                                                                                                                                  |                              60 | 0.0113           |
| UK31           | 78 (95.12%)   | 0 (0%)        | 4 (4.88%)    | 0 (0%)             | Mar-12, Jun-27 |                82 | B.3                                                                                                                                    |                               1 | 1.321            |
| UK2906         | 72 (92.31%)   | 2 (2.56%)     | 4 (5.13%)    | 0 (0%)             | Mar-03, Jun-02 |                78 | B.1                                                                                                                                    |                              26 | 0.0455           |
| UK319          | 77 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-28, Jun-03 |                77 | B.1                                                                                                                                    |                              25 | 0.0353           |
| UK339          | 70 (92.11%)   | 4 (5.26%)     | 1 (1.32%)    | 1 (1.32%)          | Mar-09, Jun-18 |                76 | B.3                                                                                                                                    |                              10 | 0.1347           |
| UK384          | 70 (95.89%)   | 1 (1.37%)     | 2 (2.74%)    | 0 (0%)             | Feb-28, Apr-23 |                73 | B.2, B.2.1                                                                                                                             |                              66 | 0.0116           |
| UK120          | 58 (79.45%)   | 0 (0%)        | 15 (20.55%)  | 0 (0%)             | Feb-27, Jun-07 |                73 | B.14, B                                                                                                                                |                              21 | 0.0668           |
| UK86           | 9 (12.68%)    | 61 (85.92%)   | 1 (1.41%)    | 0 (0%)             | Mar-05, May-30 |                71 | B.1                                                                                                                                    |                              29 | 0.0424           |
| UK335          | 58 (81.69%)   | 1 (1.41%)     | 12 (16.9%)   | 0 (0%)             | Mar-07, Jun-22 |                71 | B.1.1                                                                                                                                  |                               6 | 0.2548           |
| UK607          | 58 (82.86%)   | 12 (17.14%)   | 0 (0%)       | 0 (0%)             | Mar-02, May-18 |                70 | B                                                                                                                                      |                              41 | 0.0272           |
| UK89           | 58 (82.86%)   | 12 (17.14%)   | 0 (0%)       | 0 (0%)             | Mar-21, Jun-22 |                70 | B.1.1, B.1.1.9                                                                                                                         |                               6 | 0.2246           |
| UK37           | 67 (97.1%)    | 1 (1.45%)     | 1 (1.45%)    | 0 (0%)             | Mar-17, May-04 |                69 | B.1, B.1.30                                                                                                                            |                              55 | 0.0128           |
| UK274          | 63 (95.45%)   | 2 (3.03%)     | 1 (1.52%)    | 0 (0%)             | Mar-06, May-19 |                66 | B, B.3                                                                                                                                 |                              40 | 0.0285           |
| UK13           | 64 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-13, May-21 |                64 | B.1.1                                                                                                                                  |                              38 | 0.0288           |
| UK509          | 63 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-07, May-29 |                63 | B.1.1                                                                                                                                  |                              30 | 0.028            |
| UK476          | 56 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-14, May-06 |                56 | B.1.1                                                                                                                                  |                              53 | 0.0182           |
| UK371          | 54 (98.18%)   | 1 (1.82%)     | 0 (0%)       | 0 (0%)             | Mar-12, May-06 |                55 | B.1.1                                                                                                                                  |                              53 | 0.0192           |
| UK376          | 55 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-11, May-03 |                55 | B.1.1.9                                                                                                                                |                              56 | 0.0175           |
| UK275          | 44 (83.02%)   | 8 (15.09%)    | 1 (1.89%)    | 0 (0%)             | Mar-09, Apr-27 |                53 | B.1.13                                                                                                                                 |                              62 | 0.0152           |
| UK187          | 5 (9.62%)     | 29 (55.77%)   | 9 (17.31%)   | 9 (17.31%)         | Mar-21, Apr-30 |                52 | B.1                                                                                                                                    |                              59 | 0.0133           |
| UK448          | 50 (98.04%)   | 1 (1.96%)     | 0 (0%)       | 0 (0%)             | Apr-04, May-26 |                51 | B.1.1                                                                                                                                  |                              33 | 0.0315           |
| UK5523         | 51 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-16, Jun-01 |                51 | B.1                                                                                                                                    |                              27 | 0.0341           |
| UK517          | 47 (94.0%)    | 1 (2.0%)      | 2 (4.0%)     | 0 (0%)             | Mar-02, Apr-30 |                50 | B.1.1                                                                                                                                  |                              59 | 0.0204           |
| UK641          | 47 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-25, Jun-17 |                47 | B.1.1                                                                                                                                  |                              11 | 0.166            |
| UK276          | 46 (97.87%)   | 0 (0%)        | 1 (2.13%)    | 0 (0%)             | Mar-15, May-13 |                47 | B.1.1                                                                                                                                  |                              46 | 0.0279           |
| UK478          | 46 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-20, May-19 |                46 | B.1.1                                                                                                                                  |                              40 | 0.0333           |
| UK497          | 39 (88.64%)   | 4 (9.09%)     | 1 (2.27%)    | 0 (0%)             | Mar-13, Jun-03 |                44 | A.2                                                                                                                                    |                              25 | 0.0763           |
| UK100          | 0 (0%)        | 0 (0%)        | 43 (100.0%)  | 0 (0%)             | Mar-22, Jun-01 |                43 | B.1.5, B.1                                                                                                                             |                              27 | 0.0626           |
| UK64           | 31 (72.09%)   | 12 (27.91%)   | 0 (0%)       | 0 (0%)             | Mar-12, May-05 |                43 | B.1                                                                                                                                    |                              54 | 0.0238           |
| UK44           | 3 (7.14%)     | 0 (0%)        | 37 (88.1%)   | 2 (4.76%)          | Mar-17, Apr-23 |                42 | B                                                                                                                                      |                              66 | 0.0137           |
| UK5309         | 38 (92.68%)   | 3 (7.32%)     | 0 (0%)       | 0 (0%)             | Mar-20, Jun-18 |                41 | B.1.1, B.1.1.10                                                                                                                        |                              10 | 0.225            |
| UK3126         | 41 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-06, May-19 |                41 | B.1.1                                                                                                                                  |                              40 | 0.0269           |
| UK623          | 40 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | May-10, Jun-11 |                40 | B.1.1                                                                                                                                  |                              17 | 0.0483           |
| UK12           | 39 (97.5%)    | 0 (0%)        | 0 (0%)       | 1 (2.5%)           | Mar-12, May-07 |                40 | B.1.p11, B.1                                                                                                                           |                              52 | 0.0276           |
| UK304          | 0 (0%)        | 0 (0%)        | 40 (100.0%)  | 0 (0%)             | Apr-16, Jun-02 |                40 | B.1.1.14                                                                                                                               |                              26 | 0.0464           |
| UK131          | 34 (89.47%)   | 4 (10.53%)    | 0 (0%)       | 0 (0%)             | Mar-11, Apr-14 |                38 | B.15                                                                                                                                   |                              75 | 0.0123           |
| UK1207         | 37 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, Jun-01 |                37 | B.1.1                                                                                                                                  |                              27 | 0.072            |
| UK179          | 17 (45.95%)   | 20 (54.05%)   | 0 (0%)       | 0 (0%)             | Mar-17, May-07 |                37 | B.1.1, B.1.1.p11                                                                                                                       |                              52 | 0.0272           |
| UK119          | 29 (78.38%)   | 7 (18.92%)    | 1 (2.7%)     | 0 (0%)             | Mar-11, Apr-24 |                37 | B.2.5                                                                                                                                  |                              65 | 0.0188           |
| UK5549         | 31 (86.11%)   | 0 (0%)        | 3 (8.33%)    | 2 (5.56%)          | Mar-04, May-18 |                36 | B.2.2                                                                                                                                  |                              41 | 0.0523           |
| UK27           | 31 (86.11%)   | 4 (11.11%)    | 1 (2.78%)    | 0 (0%)             | Mar-05, May-21 |                36 | B.1.1                                                                                                                                  |                              38 | 0.0579           |
| UK14           | 3 (8.33%)     | 0 (0%)        | 33 (91.67%)  | 0 (0%)             | Mar-12, May-21 |                36 | B                                                                                                                                      |                              38 | 0.0526           |
| UK79           | 35 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-24, May-05 |                35 | B.1                                                                                                                                    |                              54 | 0.0229           |
| UK636          | 34 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-16, May-25 |                34 | B.1.1                                                                                                                                  |                              34 | 0.0624           |
| UK43           | 1 (2.94%)     | 0 (0%)        | 33 (97.06%)  | 0 (0%)             | Mar-12, Apr-26 |                34 | A.5                                                                                                                                    |                              63 | 0.0216           |
| UK479          | 6 (17.65%)    | 28 (82.35%)   | 0 (0%)       | 0 (0%)             | Apr-05, Jun-12 |                34 | B.1.1                                                                                                                                  |                              16 | 0.1288           |
| UK87           | 0 (0%)        | 0 (0%)        | 33 (100.0%)  | 0 (0%)             | Mar-13, Apr-24 |                33 | B.1.70                                                                                                                                 |                              65 | 0.0202           |
| UK462          | 25 (78.12%)   | 7 (21.88%)    | 0 (0%)       | 0 (0%)             | Apr-01, Jun-09 |                32 | B.1                                                                                                                                    |                              19 | 0.1171           |
| UK404          | 32 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-01, Apr-19 |                32 | B.1                                                                                                                                    |                              70 | 0.0226           |
| UK5649         | 29 (90.62%)   | 2 (6.25%)     | 1 (3.12%)    | 0 (0%)             | Mar-15, May-04 |                32 | B.2.6                                                                                                                                  |                              55 | 0.0293           |
| UK18           | 31 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-11, Apr-14 |                31 | B.1.1.7                                                                                                                                |                              75 | 0.0151           |
| UK241          | 31 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-22, Apr-16 |                31 | B.1.5.3                                                                                                                                |                              73 | 0.0114           |
| UK21           | 0 (0%)        | 0 (0%)        | 31 (100.0%)  | 0 (0%)             | Mar-18, May-23 |                31 | B.1.40                                                                                                                                 |                              36 | 0.0611           |
| UK23           | 30 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-18, May-09 |                30 | B.9                                                                                                                                    |                              50 | 0.0359           |
| UK1667         | 5 (16.67%)    | 0 (0%)        | 25 (83.33%)  | 0 (0%)             | Mar-30, May-18 |                30 | B.1.9, B.1.p9                                                                                                                          |                              41 | 0.0412           |
| UK567          | 4 (13.33%)    | 20 (66.67%)   | 5 (16.67%)   | 1 (3.33%)          | Mar-20, May-15 |                30 | B.2.2                                                                                                                                  |                              44 | 0.0439           |
| UK158          | 29 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, Apr-24 |                29 | B.1.1                                                                                                                                  |                              65 | 0.0176           |
| UK482          | 2 (6.9%)      | 0 (0%)        | 0 (0%)       | 27 (93.1%)         | Apr-03, May-05 |                29 | B.1.1                                                                                                                                  |                              54 | 0.0212           |
| UK1721         | 27 (96.43%)   | 1 (3.57%)     | 0 (0%)       | 0 (0%)             | Mar-19, May-08 |                28 | B.1                                                                                                                                    |                              51 | 0.0363           |
| UK101          | 26 (96.3%)    | 0 (0%)        | 1 (3.7%)     | 0 (0%)             | Mar-21, Apr-25 |                27 | B.1.5                                                                                                                                  |                              64 | 0.021            |
| UK46           | 25 (92.59%)   | 1 (3.7%)      | 1 (3.7%)     | 0 (0%)             | Mar-02, May-08 |                27 | B.2.1                                                                                                                                  |                              51 | 0.0505           |
| UK94           | 26 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-12, Apr-19 |                26 | B.2, B.2.1                                                                                                                             |                              70 | 0.0217           |
| UK317          | 11 (42.31%)   | 12 (46.15%)   | 3 (11.54%)   | 0 (0%)             | Mar-13, Apr-20 |                26 | B.3                                                                                                                                    |                              69 | 0.022            |
| UK615          | 26 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-15, May-15 |                26 | B.1.1                                                                                                                                  |                              44 | 0.0555           |
| UK600          | 4 (15.38%)    | 22 (84.62%)   | 0 (0%)       | 0 (0%)             | Apr-01, May-26 |                26 | B.1.1                                                                                                                                  |                              33 | 0.0667           |
| UK173          | 26 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-14, Apr-20 |                26 | B                                                                                                                                      |                              69 | 0.0214           |
| UK4493         | 0 (0%)        | 0 (0%)        | 26 (100.0%)  | 0 (0%)             | Apr-23, May-19 |                26 | B.1                                                                                                                                    |                              40 | 0.026            |
| UK1177         | 25 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-22, Jun-09 |                25 | B.1.1                                                                                                                                  |                              19 | 0.1053           |
| UK202          | 10 (40.0%)    | 14 (56.0%)    | 1 (4.0%)     | 0 (0%)             | Mar-10, Jun-04 |                25 | B.1.1                                                                                                                                  |                              24 | 0.1493           |
| UK47           | 20 (80.0%)    | 5 (20.0%)     | 0 (0%)       | 0 (0%)             | Mar-17, May-18 |                25 | B.1.1                                                                                                                                  |                              41 | 0.063            |
| UK684          | 24 (96.0%)    | 1 (4.0%)      | 0 (0%)       | 0 (0%)             | Apr-08, May-21 |                25 | B.1                                                                                                                                    |                              38 | 0.0471           |
| UK116          | 9 (36.0%)     | 16 (64.0%)    | 0 (0%)       | 0 (0%)             | Mar-24, Jun-02 |                25 | B.1                                                                                                                                    |                              26 | 0.1122           |
| UK326          | 24 (96.0%)    | 0 (0%)        | 1 (4.0%)     | 0 (0%)             | Mar-22, May-22 |                25 | B.1.1.10                                                                                                                               |                              37 | 0.0687           |
| UK617          | 25 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-29, Apr-28 |                25 | B.1.1                                                                                                                                  |                              61 | 0.0205           |
| UK161          | 21 (84.0%)    | 4 (16.0%)     | 0 (0%)       | 0 (0%)             | Mar-10, May-25 |                25 | B.1.1                                                                                                                                  |                              34 | 0.0931           |
| UK712          | 24 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-08, Jun-18 |                24 | B.1.5, B.1                                                                                                                             |                              10 | 0.3087           |
| UK2787         | 23 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-07, Jun-26 |                23 | B.1.1                                                                                                                                  |                               2 | 1.8182           |
| UK5300         | 22 (95.65%)   | 0 (0%)        | 1 (4.35%)    | 0 (0%)             | Apr-17, Jun-16 |                23 | B.1.1                                                                                                                                  |                              12 | 0.2273           |
| UK2045         | 23 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-17, May-09 |                23 | B.1                                                                                                                                    |                              50 | 0.0482           |
| UK58           | 6 (26.09%)    | 0 (0%)        | 17 (73.91%)  | 0 (0%)             | Mar-12, Apr-24 |                23 | B.1                                                                                                                                    |                              65 | 0.0301           |
| UK4237         | 22 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-28, Jun-10 |                22 | B.1.1                                                                                                                                  |                              18 | 0.1958           |
| UK5503         | 21 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-20, Jun-12 |                21 | B.1                                                                                                                                    |                              16 | 0.2625           |
| UK329          | 21 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-17, Apr-26 |                21 | B.1.34, B.1                                                                                                                            |                              63 | 0.0317           |
| UK203          | 20 (95.24%)   | 1 (4.76%)     | 0 (0%)       | 0 (0%)             | Mar-22, Jun-03 |                21 | B.1.1                                                                                                                                  |                              25 | 0.146            |
| UK174          | 21 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-19, May-22 |                21 | B.1.5                                                                                                                                  |                              37 | 0.0865           |
| UK24           | 21 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-14, Apr-10 |                21 | B.2.1                                                                                                                                  |                              79 | 0.0171           |
| UK233          | 21 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | May-25, Jun-15 |                21 | B.1                                                                                                                                    |                              13 | 0.0808           |
| UK134          | 16 (80.0%)    | 0 (0%)        | 4 (20.0%)    | 0 (0%)             | Mar-04, Apr-07 |                20 | B.1                                                                                                                                    |                              82 | 0.0218           |
| UK125          | 19 (95.0%)    | 0 (0%)        | 1 (5.0%)     | 0 (0%)             | Mar-30, May-29 |                20 | B.1.1                                                                                                                                  |                              30 | 0.1053           |
| UK604          | 15 (75.0%)    | 2 (10.0%)     | 3 (15.0%)    | 0 (0%)             | Mar-06, Mar-17 |                20 | B.1.1                                                                                                                                  |                             103 | 0.0056           |
| UK1703         | 20 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-16, May-01 |                20 | B.1                                                                                                                                    |                              58 | 0.0417           |
| UK146          | 18 (94.74%)   | 0 (0%)        | 1 (5.26%)    | 0 (0%)             | Mar-24, May-07 |                19 | B.1.1                                                                                                                                  |                              52 | 0.047            |
| UK3692         | 15 (78.95%)   | 1 (5.26%)     | 2 (10.53%)   | 1 (5.26%)          | Mar-12, May-19 |                19 | B.1.1                                                                                                                                  |                              40 | 0.0944           |
| UK70           | 16 (84.21%)   | 1 (5.26%)     | 0 (0%)       | 2 (10.53%)         | Mar-06, Apr-22 |                19 | B.2                                                                                                                                    |                              67 | 0.039            |
| UK206          | 0 (0%)        | 19 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-02, May-20 |                19 | B.1                                                                                                                                    |                              39 | 0.0684           |
| UK425          | 4 (22.22%)    | 14 (77.78%)   | 0 (0%)       | 0 (0%)             | Mar-28, May-15 |                18 | B.1.1                                                                                                                                  |                              44 | 0.0642           |
| UK502          | 0 (0%)        | 0 (0%)        | 18 (100.0%)  | 0 (0%)             | Mar-06, Mar-30 |                18 | B.1.69                                                                                                                                 |                              90 | 0.0157           |
| UK706          | 3 (17.65%)    | 0 (0%)        | 0 (0%)       | 14 (82.35%)        | Mar-26, Apr-29 |                17 | B.1.1                                                                                                                                  |                              60 | 0.0354           |
| UK268          | 13 (76.47%)   | 4 (23.53%)    | 0 (0%)       | 0 (0%)             | Mar-23, Jun-03 |                17 | B.1.1                                                                                                                                  |                              25 | 0.18             |
| UK71           | 16 (94.12%)   | 1 (5.88%)     | 0 (0%)       | 0 (0%)             | Mar-08, May-06 |                17 | B                                                                                                                                      |                              53 | 0.0696           |
| UK83           | 13 (81.25%)   | 1 (6.25%)     | 2 (12.5%)    | 0 (0%)             | Feb-29, Apr-13 |                16 | B.1.1                                                                                                                                  |                              76 | 0.0386           |
| UK3045         | 2 (12.5%)     | 14 (87.5%)    | 0 (0%)       | 0 (0%)             | Apr-15, Jun-28 |                16 | B.1.1, B.1.1.p11                                                                                                                       |                               0 | active today     |
| UK186          | 15 (93.75%)   | 1 (6.25%)     | 0 (0%)       | 0 (0%)             | Mar-27, Jun-09 |                16 | B                                                                                                                                      |                              19 | 0.2596           |
| UK695          | 0 (0%)        | 16 (100.0%)   | 0 (0%)       | 0 (0%)             | Mar-25, Apr-12 |                16 | B.1.67                                                                                                                                 |                              77 | 0.0156           |
| UK5660         | 16 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-25, May-08 |                16 | B.1.1                                                                                                                                  |                              51 | 0.017            |
| UK569          | 16 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, Jun-16 |                16 | B.1.1                                                                                                                                  |                              12 | 0.4722           |
| UK38           | 14 (93.33%)   | 0 (0%)        | 1 (6.67%)    | 0 (0%)             | Mar-04, Apr-20 |                15 | B.2.1                                                                                                                                  |                              69 | 0.0487           |
| UK832          | 14 (93.33%)   | 0 (0%)        | 1 (6.67%)    | 0 (0%)             | Mar-09, May-10 |                15 | A.5                                                                                                                                    |                              49 | 0.0904           |
| UK722          | 0 (0%)        | 0 (0%)        | 15 (100.0%)  | 0 (0%)             | Mar-23, May-27 |                15 | B.1.5                                                                                                                                  |                              32 | 0.1451           |
| UK153          | 15 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-13, Apr-14 |                15 | B.2, B.3                                                                                                                               |                              75 | 0.0305           |
| UK49           | 12 (85.71%)   | 0 (0%)        | 1 (7.14%)    | 1 (7.14%)          | Mar-12, May-01 |                14 | B.9                                                                                                                                    |                              58 | 0.0663           |
| UK137          | 1 (7.14%)     | 0 (0%)        | 13 (92.86%)  | 0 (0%)             | Mar-09, Mar-31 |                14 | B.1.1                                                                                                                                  |                              89 | 0.019            |
| UK3509         | 9 (64.29%)    | 3 (21.43%)    | 2 (14.29%)   | 0 (0%)             | Mar-23, Apr-21 |                14 | B.1.1.10                                                                                                                               |                              68 | 0.0328           |
| UK261          | 0 (0%)        | 0 (0%)        | 14 (100.0%)  | 0 (0%)             | Mar-15, Apr-10 |                14 | A.3                                                                                                                                    |                              79 | 0.0253           |
| UK5715         | 13 (92.86%)   | 0 (0%)        | 1 (7.14%)    | 0 (0%)             | Feb-29, Apr-22 |                14 | B.2                                                                                                                                    |                              67 | 0.0608           |
| UK32           | 14 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-29, May-03 |                14 | B.1.1                                                                                                                                  |                              56 | 0.0481           |
| UK565          | 14 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-14, May-14 |                14 | B.1.1                                                                                                                                  |                              45 | 0.0513           |
| UK436          | 0 (0%)        | 1 (7.14%)     | 13 (92.86%)  | 0 (0%)             | Mar-28, May-14 |                14 | B.1.5                                                                                                                                  |                              45 | 0.0803           |
| UK527          | 10 (71.43%)   | 4 (28.57%)    | 0 (0%)       | 0 (0%)             | Mar-22, Apr-18 |                14 | B.1                                                                                                                                    |                              71 | 0.0293           |
| UK602          | 13 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-20, Apr-02 |                13 | B.1.1                                                                                                                                  |                              87 | 0.0125           |
| UK165          | 13 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-13, May-19 |                13 | B                                                                                                                                      |                              40 | 0.075            |
| UK5663         | 13 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, May-02 |                13 | B.2                                                                                                                                    |                              57 | 0.0585           |
| UK132          | 12 (92.31%)   | 0 (0%)        | 1 (7.69%)    | 0 (0%)             | Mar-27, Apr-30 |                13 | B.1                                                                                                                                    |                              59 | 0.048            |
| UK328          | 13 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-13, Apr-23 |                13 | B.1                                                                                                                                    |                              66 | 0.0126           |
| UK34           | 13 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Feb-27, Apr-02 |                13 | B.4                                                                                                                                    |                              87 | 0.0335           |
| UK5307         | 10 (76.92%)   | 2 (15.38%)    | 1 (7.69%)    | 0 (0%)             | Mar-08, May-12 |                13 | B.1.1                                                                                                                                  |                              47 | 0.1152           |
| UK141          | 13 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-22, Apr-24 |                13 | B.1.1                                                                                                                                  |                              65 | 0.0423           |
| UK320          | 6 (46.15%)    | 0 (0%)        | 0 (0%)       | 7 (53.85%)         | Mar-22, Jun-02 |                13 | B.1                                                                                                                                    |                              26 | 0.2308           |
| UK287          | 11 (91.67%)   | 1 (8.33%)     | 0 (0%)       | 0 (0%)             | Mar-28, Apr-24 |                12 | B.1                                                                                                                                    |                              65 | 0.0378           |
| UK566          | 11 (91.67%)   | 0 (0%)        | 1 (8.33%)    | 0 (0%)             | Apr-02, Apr-21 |                12 | B.1.1, B.1.1.10                                                                                                                        |                              68 | 0.0254           |
| UK507          | 12 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-18, Apr-30 |                12 | B.1.1.10                                                                                                                               |                              59 | 0.0663           |
| UK5084         | 10 (83.33%)   | 2 (16.67%)    | 0 (0%)       | 0 (0%)             | Mar-28, Apr-16 |                12 | B.1                                                                                                                                    |                              73 | 0.0237           |
| UK193          | 11 (91.67%)   | 1 (8.33%)     | 0 (0%)       | 0 (0%)             | Mar-30, May-01 |                12 | B.1.1                                                                                                                                  |                              58 | 0.0502           |
| UK291          | 12 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-29, May-14 |                12 | B.1.5                                                                                                                                  |                              45 | 0.0929           |
| UK467          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, Jun-05 |                11 | B.1.1                                                                                                                                  |                              23 | 0.3217           |
| UK178          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-14, Apr-13 |                11 | B.1.1                                                                                                                                  |                              76 | 0.0395           |
| UK215          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-16, Apr-11 |                11 | B.2                                                                                                                                    |                              78 | 0.0333           |
| UK759          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-28, Apr-04 |                11 | B.1.1                                                                                                                                  |                              85 | 0.0082           |
| UK2888         | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-09, May-14 |                11 | B.1.1                                                                                                                                  |                              45 | 0.0778           |
| UK415          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-19, May-06 |                11 | B.1                                                                                                                                    |                              53 | 0.0321           |
| UK340          | 10 (90.91%)   | 1 (9.09%)     | 0 (0%)       | 0 (0%)             | Mar-17, May-17 |                11 | B.1.1                                                                                                                                  |                              42 | 0.1452           |
| UK653          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-07, May-19 |                11 | B.1.1                                                                                                                                  |                              40 | 0.105            |
| UK22           | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-02, Apr-21 |                11 | B                                                                                                                                      |                              68 | 0.0735           |
| UK266          | 11 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-06, Apr-30 |                11 | B.1                                                                                                                                    |                              59 | 0.0407           |
| UK788          | 10 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Feb-28, Mar-05 |                10 | B.4                                                                                                                                    |                             115 | 0.0058           |
| UK584          | 9 (90.0%)     | 0 (0%)        | 1 (10.0%)    | 0 (0%)             | Mar-17, Apr-02 |                10 | B.2, B.2.1                                                                                                                             |                              87 | 0.0204           |
| UK327          | 0 (0%)        | 10 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-05, May-05 |                10 | B.1                                                                                                                                    |                              54 | 0.0617           |
| UK433          | 5 (50.0%)     | 0 (0%)        | 5 (50.0%)    | 0 (0%)             | Mar-22, May-03 |                10 | B                                                                                                                                      |                              56 | 0.0833           |
| UK133          | 3 (30.0%)     | 0 (0%)        | 7 (70.0%)    | 0 (0%)             | Mar-22, Apr-25 |                10 | B.1                                                                                                                                    |                              64 | 0.059            |
| UK5653         | 9 (90.0%)     | 0 (0%)        | 1 (10.0%)    | 0 (0%)             | Mar-10, Apr-01 |                10 | B.2.6                                                                                                                                  |                              88 | 0.0278           |
| UK5525         | 10 (100.0%)   | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-31, Apr-29 |                10 | B.1                                                                                                                                    |                              60 | 0.0537           |
| UK581          | 1 (10.0%)     | 0 (0%)        | 0 (0%)       | 9 (90.0%)          | Apr-06, May-01 |                10 | B.1.1                                                                                                                                  |                              58 | 0.0479           |
| UK55           | 6 (60.0%)     | 0 (0%)        | 4 (40.0%)    | 0 (0%)             | Mar-13, May-06 |                10 | B.1.1                                                                                                                                  |                              53 | 0.1132           |
| UK263          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-20, Apr-13 |                 9 | B.1.p11                                                                                                                                |                              76 | 0.0395           |
| UK284          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-02, Apr-25 |                 9 | B.1.1                                                                                                                                  |                              64 | 0.0449           |
| UK113          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-22, Jun-02 |                 9 | B.1.1                                                                                                                                  |                              26 | 0.3462           |
| UK454          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-22, Apr-29 |                 9 | B.1.1                                                                                                                                  |                              60 | 0.0792           |
| UK121          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-21, May-27 |                 9 | B.1.1.7                                                                                                                                |                              32 | 0.1406           |
| UK91           | 8 (88.89%)    | 1 (11.11%)    | 0 (0%)       | 0 (0%)             | Mar-01, Apr-01 |                 9 | B.1                                                                                                                                    |                              88 | 0.044            |
| UK244          | 8 (88.89%)    | 1 (11.11%)    | 0 (0%)       | 0 (0%)             | Mar-10, Apr-06 |                 9 | B.1.1                                                                                                                                  |                              83 | 0.0407           |
| UK563          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-11, May-01 |                 9 | B.1.1                                                                                                                                  |                              58 | 0.1099           |
| UK5501         | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-16, Jun-01 |                 9 | B.1.12                                                                                                                                 |                              27 | 0.213            |
| UK629          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, May-05 |                 9 | B.1                                                                                                                                    |                              54 | 0.0995           |
| UK575          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-14, Apr-16 |                 9 | B.2.1                                                                                                                                  |                              73 | 0.0565           |
| UK819          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-01, May-15 |                 9 | B.1                                                                                                                                    |                              44 | 0.125            |
| UK756          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Feb-27, Mar-05 |                 9 | B.1.1                                                                                                                                  |                             115 | 0.0076           |
| UK65           | 8 (88.89%)    | 0 (0%)        | 1 (11.11%)   | 0 (0%)             | Mar-07, Apr-21 |                 9 | B.1.1                                                                                                                                  |                              68 | 0.0827           |
| UK698          | 8 (88.89%)    | 0 (0%)        | 1 (11.11%)   | 0 (0%)             | Mar-23, Apr-12 |                 9 | B.1.p73, B.1                                                                                                                           |                              77 | 0.0325           |
| UK1810         | 8 (88.89%)    | 0 (0%)        | 1 (11.11%)   | 0 (0%)             | Mar-21, Apr-20 |                 9 | B.1.5, B.1                                                                                                                             |                              69 | 0.0543           |
| UK491          | 9 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-03, Apr-03 |                 9 | B, B.2                                                                                                                                 |                              86 | 0.0451           |
| UK80           | 5 (62.5%)     | 3 (37.5%)     | 0 (0%)       | 0 (0%)             | Mar-31, Jun-17 |                 8 | B.1.1.p15                                                                                                                              |                              11 | 1.013            |
| UK271          | 1 (12.5%)     | 0 (0%)        | 7 (87.5%)    | 0 (0%)             | Apr-02, Apr-26 |                 8 | B.1                                                                                                                                    |                              63 | 0.0544           |
| UK195          | 7 (87.5%)     | 1 (12.5%)     | 0 (0%)       | 0 (0%)             | May-19, Jun-15 |                 8 | B.1                                                                                                                                    |                              13 | 0.2967           |
| UK633          | 0 (0%)        | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | Apr-03, Apr-28 |                 8 | B.1.1.16, B.1.1.p16                                                                                                                    |                              61 | 0.0585           |
| UK594          | 0 (0%)        | 0 (0%)        | 8 (100.0%)   | 0 (0%)             | Apr-20, May-01 |                 8 | B                                                                                                                                      |                              58 | 0.0271           |
| UK548          | 0 (0%)        | 0 (0%)        | 8 (100.0%)   | 0 (0%)             | Mar-14, Mar-30 |                 8 | B.2.1                                                                                                                                  |                              90 | 0.0254           |
| UK151          | 0 (0%)        | 0 (0%)        | 8 (100.0%)   | 0 (0%)             | Mar-23, Apr-24 |                 8 | B.1                                                                                                                                    |                              65 | 0.0703           |
| UK342          | 8 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-02, Apr-22 |                 8 | B.1.1                                                                                                                                  |                              67 | 0.0426           |
| UK4658         | 8 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-13, Apr-10 |                 8 | B.2.1                                                                                                                                  |                              79 | 0.0506           |
| UK5308         | 8 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-29, May-01 |                 8 | B.1.1                                                                                                                                  |                              58 | 0.0049           |
| UK598          | 7 (87.5%)     | 1 (12.5%)     | 0 (0%)       | 0 (0%)             | Mar-22, Apr-14 |                 8 | B.1.1                                                                                                                                  |                              75 | 0.0438           |
| UK323          | 2 (25.0%)     | 2 (25.0%)     | 4 (50.0%)    | 0 (0%)             | Mar-12, May-06 |                 8 | B.1.35, B.1.5, B.1                                                                                                                     |                              53 | 0.1482           |
| UK570          | 8 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-24, Apr-29 |                 8 | B.1.1                                                                                                                                  |                              60 | 0.0857           |
| UK696          | 0 (0%)        | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | Apr-10, May-01 |                 8 | B.1.5, B.1                                                                                                                             |                              58 | 0.0517           |
| UK369          | 7 (87.5%)     | 0 (0%)        | 1 (12.5%)    | 0 (0%)             | Mar-22, Apr-11 |                 8 | B.1.1                                                                                                                                  |                              78 | 0.0366           |
| UK755          | 8 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-06, May-21 |                 8 | B.1.1                                                                                                                                  |                              38 | 0.2857           |
| UK739          | 8 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-01, Mar-08 |                 8 | B.4                                                                                                                                    |                             112 | 0.0089           |
| UK656          | 3 (42.86%)    | 4 (57.14%)    | 0 (0%)       | 0 (0%)             | Mar-13, Apr-24 |                 7 | B.1.1.10                                                                                                                               |                              65 | 0.1077           |
| UK490          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-03, May-02 |                 7 | B.1.1                                                                                                                                  |                              57 | 0.0848           |
| UK75           | 6 (85.71%)    | 0 (0%)        | 1 (14.29%)   | 0 (0%)             | Mar-28, Apr-12 |                 7 | B                                                                                                                                      |                              77 | 0.0325           |
| UK451          | 0 (0%)        | 6 (85.71%)    | 1 (14.29%)   | 0 (0%)             | Mar-20, Apr-05 |                 7 | B.2.1                                                                                                                                  |                              84 | 0.0317           |
| UK767          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-05, Apr-19 |                 7 | B.1                                                                                                                                    |                              70 | 0.0333           |
| UK232          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-04, Mar-30 |                 7 | B.1.1                                                                                                                                  |                              90 | 0.0481           |
| UK464          | 4 (57.14%)    | 2 (28.57%)    | 0 (0%)       | 1 (14.29%)         | Mar-25, May-04 |                 7 | B.1                                                                                                                                    |                              55 | 0.1212           |
| UK171          | 2 (28.57%)    | 0 (0%)        | 5 (71.43%)   | 0 (0%)             | Mar-31, Apr-21 |                 7 | B.1                                                                                                                                    |                              68 | 0.0515           |
| UK437          | 5 (71.43%)    | 2 (28.57%)    | 0 (0%)       | 0 (0%)             | Mar-23, Apr-11 |                 7 | B.1                                                                                                                                    |                              78 | 0.0406           |
| UK98           | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-24, Jun-08 |                 7 | B.6                                                                                                                                    |                              20 | 0.6333           |
| UK269          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-25, Jun-02 |                 7 | B.1.1                                                                                                                                  |                              26 | 0.4423           |
| UK957          | 6 (85.71%)    | 0 (0%)        | 0 (0%)       | 1 (14.29%)         | Mar-24, May-26 |                 7 | B.1.1                                                                                                                                  |                              33 | 0.3182           |
| UK799          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-01, Mar-07 |                 7 | B.1                                                                                                                                    |                             113 | 0.0088           |
| UK390          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-27, May-01 |                 7 | B.1.5                                                                                                                                  |                              58 | 0.1006           |
| UK1003         | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-02, Apr-22 |                 7 | B.1.1                                                                                                                                  |                              67 | 0.0498           |
| UK54           | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-11, Apr-02 |                 7 | B.2.4                                                                                                                                  |                              87 | 0.0421           |
| UK671          | 0 (0%)        | 0 (0%)        | 7 (100.0%)   | 0 (0%)             | Apr-17, May-31 |                 7 | B.1.p73                                                                                                                                |                              28 | 0.2619           |
| UK414          | 5 (71.43%)    | 0 (0%)        | 0 (0%)       | 2 (28.57%)         | Mar-30, May-09 |                 7 | B.1.1                                                                                                                                  |                              50 | 0.1333           |
| UK728          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-19, Apr-01 |                 7 | B.2, B.2.1                                                                                                                             |                              88 | 0.0246           |
| UK520          | 7 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-14, Apr-08 |                 7 | B.2.1                                                                                                                                  |                              81 | 0.0514           |
| UK270          | 6 (85.71%)    | 0 (0%)        | 1 (14.29%)   | 0 (0%)             | Mar-04, Apr-03 |                 7 | B                                                                                                                                      |                              86 | 0.0581           |
| UK521          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-31, May-01 |                 6 | B.1.1                                                                                                                                  |                              58 | 0.1069           |
| UK552          | 1 (16.67%)    | 0 (0%)        | 5 (83.33%)   | 0 (0%)             | Mar-18, Mar-30 |                 6 | A.1                                                                                                                                    |                              90 | 0.0267           |
| UK743          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Feb-24, Jun-14 |                 6 | B.1.5.1                                                                                                                                |                              14 | 1.5857           |
| UK106          | 3 (50.0%)     | 1 (16.67%)    | 2 (33.33%)   | 0 (0%)             | Mar-09, Apr-18 |                 6 | B, B.3                                                                                                                                 |                              71 | 0.1127           |
| UK419          | 0 (0%)        | 0 (0%)        | 5 (83.33%)   | 1 (16.67%)         | Mar-30, May-07 |                 6 | B.1.1                                                                                                                                  |                              52 | 0.1462           |
| UK5648         | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-08, Apr-02 |                 6 | B.2                                                                                                                                    |                              87 | 0.0575           |
| UK364          | 1 (16.67%)    | 4 (66.67%)    | 0 (0%)       | 1 (16.67%)         | Mar-19, May-14 |                 6 | B.1                                                                                                                                    |                              45 | 0.2489           |
| UK185          | 4 (66.67%)    | 0 (0%)        | 1 (16.67%)   | 1 (16.67%)         | Mar-10, May-15 |                 6 | B.3                                                                                                                                    |                              44 | 0.3              |
| UK676          | 5 (83.33%)    | 0 (0%)        | 1 (16.67%)   | 0 (0%)             | Mar-03, Mar-12 |                 6 | B.1.1                                                                                                                                  |                             108 | 0.0167           |
| UK403          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-23, Apr-14 |                 6 | B.1.1                                                                                                                                  |                              75 | 0.0587           |
| UK56           | 5 (83.33%)    | 1 (16.67%)    | 0 (0%)       | 0 (0%)             | Mar-18, Apr-04 |                 6 | B.2                                                                                                                                    |                              85 | 0.04             |
| UK456          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-03, Apr-23 |                 6 | B.1.1                                                                                                                                  |                              66 | 0.0606           |
| UK654          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Feb-27, Mar-08 |                 6 | B.2.5                                                                                                                                  |                             112 | 0.0179           |
| UK60           | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-21, Mar-30 |                 6 | B                                                                                                                                      |                              90 | 0.02             |
| UK1867         | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-18, Apr-30 |                 6 | B.1.1                                                                                                                                  |                              59 | 0.1458           |
| UK697          | 0 (0%)        | 0 (0%)        | 6 (100.0%)   | 0 (0%)             | Mar-31, Apr-24 |                 6 | B.1                                                                                                                                    |                              65 | 0.0738           |
| UK330          | 5 (83.33%)    | 1 (16.67%)    | 0 (0%)       | 0 (0%)             | Mar-23, Apr-08 |                 6 | B.1.1                                                                                                                                  |                              81 | 0.0395           |
| UK293          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-13, Apr-16 |                 6 | B.3                                                                                                                                    |                              73 | 0.0932           |
| UK777          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Apr-01, Apr-14 |                 6 | B.1                                                                                                                                    |                              75 | 0.0347           |
| UK4735         | 0 (0%)        | 0 (0%)        | 6 (100.0%)   | 0 (0%)             | Apr-22, May-27 |                 6 | B.1.1                                                                                                                                  |                              32 | 0.2188           |
| UK288          | 3 (50.0%)     | 0 (0%)        | 2 (33.33%)   | 1 (16.67%)         | Mar-12, Apr-04 |                 6 | B.2.1                                                                                                                                  |                              85 | 0.0541           |
| UK196          | 6 (100.0%)    | 0 (0%)        | 0 (0%)       | 0 (0%)             | Mar-15, Mar-31 |                 6 | B.2.1                                                                                                                                  |                              89 | 0.036            |
| UK243          | 3 (50.0%)     | 0 (0%)        | 3 (50.0%)    | 0 (0%)             | Mar-18, Apr-12 |                 6 | B.1.5                                                                                                                                  |                              77 | 0.0649           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | PHWC     |             5 |
|  1 | NOTT     |             6 |
|  2 | BIRM     |             8 |
|  3 | SHEF     |             9 |
|  4 | CAMB     |            10 |
|  5 | EDIN     |            11 |
|  6 | NORW     |            15 |
|  7 | GLAS     |            15 |
|  8 | PHEC     |            16 |
|  9 | LIVE     |            17 |
| 10 | SANG     |            24 |
| 11 | PORT     |            24 |
| 12 | EXET     |            30 |
| 13 | NORT     |            33 |
| 14 | OXON     |            45 |
| 15 | LOND     |            50 |
| 16 | NIRE     |            94 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK107 |   UK42 |   UK36 |   UK2464 |   UK199 |   UK2913 |   UK5098 |   UK109 |   UK2916 |
|:------------------|------:|--------:|-------:|-------:|---------:|--------:|---------:|---------:|--------:|---------:|
| 2020-02-02        |     0 |       0 |      0 |      0 |        0 |       0 |        0 |        0 |       0 |        1 |
| 2020-02-09        |     0 |       1 |      0 |      0 |        0 |       0 |        0 |        0 |       0 |        0 |
| 2020-02-16        |     1 |       0 |      0 |      0 |        0 |       0 |        0 |        0 |       0 |        0 |
| 2020-02-23        |     2 |       5 |      5 |      0 |        0 |       1 |        0 |        0 |       0 |       10 |
| 2020-03-01        |    11 |       6 |     15 |      0 |        0 |       2 |        1 |        1 |       0 |       16 |
| 2020-03-08        |    31 |      19 |     18 |      0 |        4 |       3 |        4 |        1 |       3 |        8 |
| 2020-03-15        |    36 |      28 |     23 |      6 |       13 |      13 |        9 |        4 |       6 |       10 |
| 2020-03-22        |    63 |      36 |     40 |      9 |       28 |      27 |       19 |        8 |       7 |       17 |
| 2020-03-29        |    71 |      41 |     49 |     20 |       33 |      29 |       26 |        5 |      18 |       20 |
| 2020-04-05        |    81 |      37 |     53 |     18 |       29 |      34 |       27 |       13 |      22 |       18 |
| 2020-04-12        |    78 |      28 |     41 |     26 |       31 |      27 |       27 |       14 |      19 |       16 |
| 2020-04-19        |    87 |      19 |     35 |     17 |       24 |      25 |       21 |       15 |      16 |       14 |
| 2020-04-26        |    78 |      12 |     27 |     13 |       15 |      19 |       16 |        7 |      10 |       13 |
| 2020-05-03        |    79 |       4 |     16 |     12 |       11 |      12 |        6 |        6 |       9 |        4 |
| 2020-05-10        |    70 |       2 |     11 |     14 |        8 |      11 |        7 |       11 |      12 |        3 |
| 2020-05-17        |    57 |       1 |      8 |      9 |        3 |       5 |        3 |       10 |       5 |        1 |
| 2020-05-24        |    46 |       0 |      4 |      5 |        1 |       4 |        4 |        8 |       3 |        0 |
| 2020-05-31        |    35 |       1 |      6 |      7 |        3 |       3 |        4 |        4 |       4 |        3 |
| 2020-06-07        |    28 |       0 |      0 |      0 |        1 |       2 |        0 |        0 |       2 |        1 |
| 2020-06-14        |    14 |       0 |      0 |      0 |        2 |       0 |        1 |        0 |       0 |        0 |
| 2020-06-21        |     7 |       0 |      1 |      0 |        0 |       1 |        0 |        0 |       0 |        0 |

\pagebreak


**Table S4** Raw data for figure four showing the Shannon diversity per admin1 region over time



| Week       |   England |     Wales |   Scotland |   Northern Ireland |
|:-----------|----------:|----------:|-----------:|-------------------:|
| 2020-02-02 |  0.562335 |  0        |    0       |           0        |
| 2020-02-09 | -0        |  0        |    0       |           0        |
| 2020-02-16 | -0        |  0        |    0       |           0        |
| 2020-02-23 |  2.69812  | -0        |   -0       |           0        |
| 2020-03-01 |  3.27542  |  1.03972  |    2.1961  |           0        |
| 2020-03-08 |  3.73035  |  1.82175  |    3.30629 |           2.13833  |
| 2020-03-15 |  3.5986   |  1.90111  |    3.38952 |           1.65948  |
| 2020-03-22 |  3.82189  |  2.35921  |    3.58468 |           2.73527  |
| 2020-03-29 |  3.79534  |  3.31791  |    3.45432 |           1.71147  |
| 2020-04-05 |  3.51223  |  3.04127  |    3.24663 |           2.19792  |
| 2020-04-12 |  3.32701  |  2.77082  |    3.14563 |           1.56957  |
| 2020-04-19 |  3.19203  |  2.87373  |    3.10626 |           1.7272   |
| 2020-04-26 |  2.98946  |  2.83926  |    2.79133 |           1.55027  |
| 2020-05-03 |  2.8654   |  2.61705  |    2.66917 |           0.979229 |
| 2020-05-10 |  2.46193  |  2.45208  |    2.58735 |          -0        |
| 2020-05-17 |  2.13989  |  2.38265  |    2.32646 |          -0        |
| 2020-05-24 |  2.328    |  2.11254  |    2.46267 |          -0        |
| 2020-05-31 |  2.515    |  1.8823   |    2.10997 |          -0        |
| 2020-06-07 |  1.90464  |  1.61473  |    1.58326 |           0        |
| 2020-06-14 |  1.67341  | -0        |    1.27703 |           0        |
| 2020-06-21 |  1.51715  |  0.636514 |   -0       |           0        |
| 2020-06-28 |  0        | -0        |    0       |           0        |

\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-02-03 |                            0 |                                1 |       1 |
| 2020-02-05 |                            0 |                                1 |       1 |
| 2020-02-09 |                            0 |                                1 |       1 |
| 2020-02-16 |                            0 |                                1 |       1 |
| 2020-02-23 |                            0 |                                1 |       1 |
| 2020-02-24 |                            0 |                                2 |       2 |
| 2020-02-25 |                            0 |                                2 |       2 |
| 2020-02-26 |                            1 |                                2 |       3 |
| 2020-02-27 |                            1 |                                5 |       6 |
| 2020-02-28 |                            0 |                                5 |       5 |
| 2020-02-29 |                            0 |                                2 |       2 |
| 2020-03-01 |                            2 |                                5 |       7 |
| 2020-03-02 |                            1 |                                6 |       7 |
| 2020-03-03 |                            0 |                                7 |       7 |
| 2020-03-04 |                            3 |                                8 |      11 |
| 2020-03-05 |                            0 |                                5 |       5 |
| 2020-03-06 |                            4 |                                9 |      13 |
| 2020-03-07 |                            5 |                                6 |      11 |
| 2020-03-08 |                            1 |                                4 |       5 |
| 2020-03-09 |                            4 |                               12 |      16 |
| 2020-03-10 |                            5 |                                8 |      13 |
| 2020-03-11 |                            9 |                               15 |      24 |
| 2020-03-12 |                            6 |                               24 |      30 |
| 2020-03-13 |                           12 |                               12 |      24 |
| 2020-03-14 |                            6 |                                9 |      15 |
| 2020-03-15 |                            6 |                                6 |      12 |
| 2020-03-16 |                            3 |                                5 |       8 |
| 2020-03-17 |                            7 |                               16 |      23 |
| 2020-03-18 |                            8 |                               20 |      28 |
| 2020-03-19 |                            9 |                               11 |      20 |
| 2020-03-20 |                            9 |                               22 |      31 |
| 2020-03-21 |                            8 |                               12 |      20 |
| 2020-03-22 |                           11 |                               20 |      31 |
| 2020-03-23 |                           11 |                               25 |      36 |
| 2020-03-24 |                           15 |                               18 |      33 |
| 2020-03-25 |                           19 |                               17 |      36 |
| 2020-03-26 |                           12 |                               18 |      30 |
| 2020-03-27 |                           17 |                               15 |      32 |
| 2020-03-28 |                           11 |                               16 |      27 |
| 2020-03-29 |                           18 |                               11 |      29 |
| 2020-03-30 |                           20 |                               22 |      42 |
| 2020-03-31 |                           27 |                               21 |      48 |
| 2020-04-01 |                           20 |                               10 |      30 |
| 2020-04-02 |                           14 |                               18 |      32 |
| 2020-04-03 |                           18 |                               12 |      30 |
| 2020-04-04 |                           12 |                                5 |      17 |
| 2020-04-05 |                           14 |                                9 |      23 |
| 2020-04-06 |                           11 |                               12 |      23 |
| 2020-04-07 |                            9 |                               11 |      20 |
| 2020-04-08 |                           15 |                                6 |      21 |
| 2020-04-09 |                            8 |                                3 |      11 |
| 2020-04-10 |                           10 |                                5 |      15 |
| 2020-04-11 |                            8 |                                4 |      12 |
| 2020-04-12 |                            7 |                                5 |      12 |
| 2020-04-13 |                           17 |                                6 |      23 |
| 2020-04-14 |                            9 |                                4 |      13 |
| 2020-04-15 |                            2 |                                4 |       6 |
| 2020-04-16 |                           16 |                                7 |      23 |
| 2020-04-17 |                            5 |                                4 |       9 |
| 2020-04-18 |                            8 |                                4 |      12 |
| 2020-04-19 |                            4 |                                2 |       6 |
| 2020-04-20 |                            6 |                                4 |      10 |
| 2020-04-21 |                           12 |                                2 |      14 |
| 2020-04-22 |                            5 |                                6 |      11 |
| 2020-04-23 |                            2 |                                6 |       8 |
| 2020-04-24 |                            5 |                                2 |       7 |
| 2020-04-25 |                            2 |                                3 |       5 |
| 2020-04-26 |                            2 |                                0 |       2 |
| 2020-04-27 |                            4 |                                2 |       6 |
| 2020-04-28 |                            6 |                                3 |       9 |
| 2020-04-29 |                            3 |                                1 |       4 |
| 2020-04-30 |                            3 |                                0 |       3 |
| 2020-05-01 |                            2 |                                1 |       3 |
| 2020-05-02 |                            1 |                                1 |       2 |
| 2020-05-03 |                            3 |                                0 |       3 |
| 2020-05-04 |                            4 |                                3 |       7 |
| 2020-05-05 |                            1 |                                0 |       1 |
| 2020-05-06 |                            2 |                                0 |       2 |
| 2020-05-07 |                            0 |                                2 |       2 |
| 2020-05-08 |                            3 |                                0 |       3 |
| 2020-05-10 |                            0 |                                1 |       1 |
| 2020-05-11 |                            3 |                                0 |       3 |
| 2020-05-12 |                            2 |                                0 |       2 |
| 2020-05-14 |                            3 |                                1 |       4 |
| 2020-05-17 |                            2 |                                0 |       2 |
| 2020-05-18 |                            0 |                                1 |       1 |
| 2020-05-19 |                            0 |                                1 |       1 |
| 2020-05-20 |                            0 |                                1 |       1 |
| 2020-05-22 |                            2 |                                0 |       2 |
| 2020-05-23 |                            1 |                                0 |       1 |
| 2020-05-25 |                            1 |                                1 |       2 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-06-03 |                            1 |                                0 |       1 |
| 2020-06-04 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-06 |                            0 |                                1 |       1 |
| 2020-06-08 |                            1 |                                0 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |
| 2020-06-15 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Scotland |   Wales |   Northern Ireland |
|:-----------|----------:|-----------:|--------:|-------------------:|
| 2020-02-03 |         1 |          0 |       0 |                  0 |
| 2020-02-05 |         1 |          0 |       0 |                  0 |
| 2020-02-08 |         2 |          0 |       0 |                  0 |
| 2020-02-09 |         1 |          0 |       0 |                  0 |
| 2020-02-13 |         1 |          0 |       0 |                  0 |
| 2020-02-16 |         1 |          0 |       0 |                  0 |
| 2020-02-23 |         2 |          0 |       0 |                  0 |
| 2020-02-24 |         5 |          0 |       0 |                  0 |
| 2020-02-25 |         7 |          0 |       0 |                  0 |
| 2020-02-26 |         6 |          0 |       0 |                  0 |
| 2020-02-27 |        19 |          0 |       1 |                  0 |
| 2020-02-28 |        24 |          1 |       0 |                  0 |
| 2020-02-29 |        23 |          0 |       0 |                  0 |
| 2020-03-01 |        51 |          1 |       1 |                  0 |
| 2020-03-02 |        76 |          1 |       0 |                  0 |
| 2020-03-03 |        97 |          2 |       0 |                  0 |
| 2020-03-04 |       107 |          5 |       1 |                  0 |
| 2020-03-05 |        85 |          3 |       0 |                  0 |
| 2020-03-06 |        81 |          7 |       0 |                  0 |
| 2020-03-07 |        46 |          5 |       2 |                  0 |
| 2020-03-08 |        53 |          1 |       2 |                  0 |
| 2020-03-09 |        75 |         12 |       1 |                  0 |
| 2020-03-10 |        98 |          5 |       5 |                  2 |
| 2020-03-11 |       151 |         11 |      10 |                  3 |
| 2020-03-12 |       193 |         32 |       7 |                  0 |
| 2020-03-13 |       113 |         42 |       8 |                  1 |
| 2020-03-14 |        95 |         13 |      10 |                  6 |
| 2020-03-15 |        86 |          8 |      15 |                  0 |
| 2020-03-16 |        95 |         14 |      22 |                  5 |
| 2020-03-17 |       136 |         33 |      32 |                  7 |
| 2020-03-18 |       209 |         27 |      24 |                  6 |
| 2020-03-19 |       172 |         31 |      30 |                  3 |
| 2020-03-20 |       225 |         40 |      12 |                  6 |
| 2020-03-21 |       232 |         44 |       0 |                 13 |
| 2020-03-22 |       213 |         50 |       0 |                  8 |
| 2020-03-23 |       385 |         96 |       1 |                 29 |
| 2020-03-24 |       347 |         87 |      25 |                 23 |
| 2020-03-25 |       341 |         78 |      91 |                 16 |
| 2020-03-26 |       367 |        111 |      18 |                 27 |
| 2020-03-27 |       356 |        130 |      29 |                  7 |
| 2020-03-28 |       372 |         82 |      17 |                 12 |
| 2020-03-29 |       407 |         63 |      22 |                 11 |
| 2020-03-30 |       573 |        134 |      75 |                  6 |
| 2020-03-31 |       562 |         98 |     141 |                  8 |
| 2020-04-01 |       467 |         84 |     131 |                  0 |
| 2020-04-02 |       461 |         61 |      99 |                  1 |
| 2020-04-03 |       507 |         83 |     111 |                  0 |
| 2020-04-04 |       382 |         58 |     128 |                  1 |
| 2020-04-05 |       374 |         55 |      65 |                  0 |
| 2020-04-06 |       447 |        103 |     167 |                 18 |
| 2020-04-07 |       407 |         97 |     185 |                  5 |
| 2020-04-08 |       397 |         91 |     126 |                 14 |
| 2020-04-09 |       372 |         41 |      83 |                  1 |
| 2020-04-10 |       350 |         53 |     120 |                 19 |
| 2020-04-11 |       277 |         62 |      73 |                 14 |
| 2020-04-12 |       233 |         85 |      87 |                 23 |
| 2020-04-13 |       296 |         92 |      77 |                 22 |
| 2020-04-14 |       335 |         84 |     123 |                 14 |
| 2020-04-15 |       336 |         85 |      80 |                 23 |
| 2020-04-16 |       376 |        101 |      74 |                 32 |
| 2020-04-17 |       349 |         70 |      47 |                 28 |
| 2020-04-18 |       262 |         73 |      43 |                  7 |
| 2020-04-19 |       236 |         30 |      37 |                  9 |
| 2020-04-20 |       318 |         76 |      71 |                 25 |
| 2020-04-21 |       272 |        107 |      41 |                 23 |
| 2020-04-22 |       284 |        107 |      21 |                 23 |
| 2020-04-23 |       268 |         81 |      31 |                 11 |
| 2020-04-24 |       175 |         91 |      70 |                 10 |
| 2020-04-25 |       120 |         70 |      41 |                 14 |
| 2020-04-26 |       119 |         49 |      19 |                  4 |
| 2020-04-27 |       193 |         61 |      75 |                 11 |
| 2020-04-28 |       169 |         36 |      51 |                 15 |
| 2020-04-29 |       240 |         23 |      52 |                 11 |
| 2020-04-30 |       202 |         24 |      56 |                 15 |
| 2020-05-01 |       229 |         25 |      46 |                 16 |
| 2020-05-02 |       123 |         13 |      51 |                  9 |
| 2020-05-03 |       104 |         16 |      20 |                 12 |
| 2020-05-04 |       194 |          9 |      40 |                 20 |
| 2020-05-05 |       133 |         18 |      34 |                  4 |
| 2020-05-06 |       158 |         32 |      53 |                  2 |
| 2020-05-07 |       143 |         39 |      53 |                  3 |
| 2020-05-08 |        90 |         40 |      32 |                  7 |
| 2020-05-09 |        66 |         29 |      41 |                 10 |
| 2020-05-10 |        92 |         30 |      38 |                  1 |
| 2020-05-11 |       132 |         34 |      70 |                  3 |
| 2020-05-12 |        92 |         50 |      44 |                  4 |
| 2020-05-13 |        87 |         40 |      53 |                  0 |
| 2020-05-14 |        61 |         50 |      28 |                  0 |
| 2020-05-15 |        70 |         22 |      33 |                  0 |
| 2020-05-16 |        49 |         21 |      18 |                  0 |
| 2020-05-17 |        34 |         16 |      19 |                  0 |
| 2020-05-18 |        76 |         35 |      36 |                  1 |
| 2020-05-19 |        64 |         38 |      40 |                  1 |
| 2020-05-20 |        36 |         18 |      42 |                  0 |
| 2020-05-21 |        47 |         28 |      26 |                  0 |
| 2020-05-22 |        40 |         17 |      32 |                  0 |
| 2020-05-23 |        21 |          8 |      25 |                  0 |
| 2020-05-24 |        21 |          8 |      18 |                  0 |
| 2020-05-25 |        42 |         13 |      23 |                  0 |
| 2020-05-26 |        46 |          6 |      31 |                  0 |
| 2020-05-27 |        34 |         12 |      35 |                  1 |
| 2020-05-28 |        35 |          7 |      25 |                  0 |
| 2020-05-29 |        21 |          2 |      25 |                  0 |
| 2020-05-30 |        29 |          5 |      15 |                  0 |
| 2020-05-31 |        39 |          7 |      11 |                  0 |
| 2020-06-01 |        49 |          7 |      13 |                  1 |
| 2020-06-02 |        51 |         14 |       6 |                  0 |
| 2020-06-03 |        49 |          4 |      16 |                  0 |
| 2020-06-04 |        41 |          9 |      10 |                  0 |
| 2020-06-05 |        30 |          3 |       3 |                  0 |
| 2020-06-06 |        21 |          4 |       2 |                  0 |
| 2020-06-07 |        26 |          1 |       1 |                  0 |
| 2020-06-08 |        32 |          2 |       3 |                  0 |
| 2020-06-09 |        31 |          1 |       8 |                  0 |
| 2020-06-10 |        29 |          2 |       8 |                  0 |
| 2020-06-11 |        19 |          3 |       4 |                  0 |
| 2020-06-12 |        16 |          2 |       3 |                  0 |
| 2020-06-13 |        12 |          1 |       0 |                  0 |
| 2020-06-14 |        11 |          1 |       0 |                  0 |
| 2020-06-15 |        21 |          3 |       0 |                  0 |
| 2020-06-16 |        18 |          1 |       0 |                  0 |
| 2020-06-17 |        14 |          1 |       0 |                  0 |
| 2020-06-18 |        26 |          1 |       0 |                  0 |
| 2020-06-19 |         7 |          0 |       1 |                  0 |
| 2020-06-20 |         4 |          0 |       1 |                  0 |
| 2020-06-21 |         3 |          0 |       0 |                  0 |
| 2020-06-22 |         2 |          3 |       0 |                  0 |
| 2020-06-23 |         4 |          0 |       0 |                  0 |
| 2020-06-24 |         1 |          0 |       0 |                  0 |
| 2020-06-25 |         1 |          0 |       0 |                  0 |
| 2020-06-26 |         1 |          0 |       2 |                  0 |
| 2020-06-27 |         1 |          0 |       4 |                  0 |
| 2020-06-28 |         0 |          0 |       1 |                  0 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                       | Country          |   Number of sequences | Sequence group   |
|:-----------------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN                     | Scotland         |                    23 | 10-50            |
| ABERDEENSHIRE                | Scotland         |                    12 | 10-50            |
| ANGLESEY                     | Wales            |                    80 | 50-100           |
| ANGUS                        | Scotland         |                    69 | 50-100           |
| ANTRIM                       | Northern Ireland |                   325 | 300-400          |
| ARGYLL AND BUTE              | Scotland         |                    14 | 10-50            |
| ARMAGH                       | Northern Ireland |                    29 | 10-50            |
| BATH AND NORTH EAST SOMERSET | England          |                     0 | 0                |
| BEDFORDSHIRE                 | England          |                   452 | 400-500          |
| BERKSHIRE                    | England          |                    21 | 10-50            |
| BLACKBURN WITH DARWEN        | England          |                     0 | 0                |
| BLACKPOOL                    | England          |                     0 | 0                |
| BLAENAU GWENT                | Wales            |                    59 | 50-100           |
| BOLTON                       | England          |                     0 | 0                |
| BOURNEMOUTH                  | England          |                     0 | 0                |
| BRIDGEND                     | Wales            |                   114 | 100-150          |
| BRIGHTON AND HOVE            | England          |                     0 | 0                |
| BRISTOL                      | England          |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England          |                   413 | 400-500          |
| BURY                         | England          |                     0 | 0                |
| CAERPHILLY                   | Wales            |                   142 | 100-150          |
| CAMBRIDGESHIRE               | England          |                   727 | >500             |
| CARDIFF                      | Wales            |                   586 | >500             |
| CARMARTHENSHIRE              | Wales            |                   148 | 100-150          |
| CENTRAL BEDFORDSHIRE         | England          |                     0 | 0                |
| CEREDIGION                   | Wales            |                    16 | 10-50            |
| CHESHIRE                     | England          |                    44 | 10-50            |
| CLACKMANNANSHIRE             | Scotland         |                     4 | 1-10             |
| CONWY                        | Wales            |                   162 | 150-200          |
| CORNWALL                     | England          |                    27 | 10-50            |
| CUMBRIA                      | England          |                    78 | 50-100           |
| DARLINGTON                   | England          |                     0 | 0                |
| DENBIGHSHIRE                 | Wales            |                   194 | 150-200          |
| DERBY                        | England          |                     0 | 0                |
| DERBYSHIRE                   | England          |                    30 | 10-50            |
| DEVON                        | England          |                   421 | 400-500          |
| DORSET                       | England          |                   192 | 150-200          |
| DOWN                         | Northern Ireland |                   272 | 250-300          |
| DUMFRIES AND GALLOWAY        | Scotland         |                    88 | 50-100           |
| DUNDEE                       | Scotland         |                   278 | 250-300          |
| DURHAM                       | England          |                   161 | 150-200          |
| EAST AYRSHIRE                | Scotland         |                    93 | 50-100           |
| EAST DUNBARTONSHIRE          | Scotland         |                    73 | 50-100           |
| EAST LOTHIAN                 | Scotland         |                    57 | 50-100           |
| EAST RENFREWSHIRE            | Scotland         |                    40 | 10-50            |
| EAST RIDING OF YORKSHIRE     | England          |                    35 | 10-50            |
| EDINBURGH                    | Scotland         |                   478 | 400-500          |
| EILEAN SIAR                  | Scotland         |                     2 | 1-10             |
| ESSEX                        | England          |                  1432 | >500             |
| FALKIRK                      | Scotland         |                   102 | 100-150          |
| FERMANAGH                    | Northern Ireland |                     5 | 1-10             |
| FIFE                         | Scotland         |                    51 | 50-100           |
| FLINTSHIRE                   | Wales            |                   131 | 100-150          |
| GATESHEAD                    | England          |                     0 | 0                |
| GLASGOW                      | Scotland         |                  1246 | >500             |
| GLOUCESTERSHIRE              | England          |                   708 | >500             |
| GREATER LONDON               | England          |                  2654 | >500             |
| GUERNSEY                     | Channel_islands  |                    41 | 10-50            |
| GWYNEDD                      | Wales            |                   125 | 100-150          |
| HALTON                       | England          |                     0 | 0                |
| HAMPSHIRE                    | England          |                   347 | 300-400          |
| HARTLEPOOL                   | England          |                     0 | 0                |
| HEREFORDSHIRE                | England          |                    59 | 50-100           |
| HERTFORDSHIRE                | England          |                  1031 | >500             |
| HIGHLAND                     | Scotland         |                    10 | 10-50            |
| INVERCLYDE                   | Scotland         |                    42 | 10-50            |
| ISLE OF WIGHT                | England          |                     1 | 1-10             |
| ISLES OF SCILLY              | England          |                     0 | 0                |
| JERSEY                       | Channel_islands  |                    77 | 50-100           |
| KENT                         | England          |                    38 | 10-50            |
| KINGSTON UPON HULL           | England          |                     0 | 0                |
| LANCASHIRE                   | England          |                    53 | 50-100           |
| LEICESTER                    | England          |                     0 | 0                |
| LEICESTERSHIRE               | England          |                   109 | 100-150          |
| LINCOLNSHIRE                 | England          |                    73 | 50-100           |
| LONDONDERRY                  | Northern Ireland |                    32 | 10-50            |
| LUTON                        | England          |                     0 | 0                |
| MANCHESTER                   | England          |                    30 | 10-50            |
| MEDWAY                       | England          |                     0 | 0                |
| MERSEYSIDE                   | England          |                   549 | >500             |
| MERTHYR TYDFIL               | Wales            |                   103 | 100-150          |
| MIDDLESBROUGH                | England          |                     0 | 0                |
| MIDLOTHIAN                   | Scotland         |                   146 | 100-150          |
| MILTON KEYNES                | England          |                     0 | 0                |
| MONMOUTHSHIRE                | Wales            |                    88 | 50-100           |
| MORAY                        | Scotland         |                    10 | 10-50            |
| NEATH PORT TALBOT            | Wales            |                   119 | 100-150          |
| NEWPORT                      | Wales            |                   165 | 150-200          |
| NORFOLK                      | England          |                   626 | >500             |
| NORTH AYRSHIRE               | Scotland         |                    18 | 10-50            |
| NORTH LANARKSHIRE            | Scotland         |                   273 | 250-300          |
| NORTH LINCOLNSHIRE           | England          |                     0 | 0                |
| NORTH SOMERSET               | England          |                     0 | 0                |
| NORTH YORKSHIRE              | England          |                   123 | 100-150          |
| NORTHAMPTONSHIRE             | England          |                    28 | 10-50            |
| NORTHUMBERLAND               | England          |                   172 | 150-200          |
| NOTTINGHAM                   | England          |                   685 | >500             |
| NOTTINGHAMSHIRE              | England          |                    59 | 50-100           |
| OLDHAM                       | England          |                     0 | 0                |
| ORKNEY ISLANDS               | Scotland         |                     1 | 1-10             |
| OXFORDSHIRE                  | England          |                    98 | 50-100           |
| PEMBROKESHIRE                | Wales            |                    73 | 50-100           |
| PERTHSHIRE AND KINROSS       | Scotland         |                   118 | 100-150          |
| PETERBOROUGH                 | England          |                     0 | 0                |
| PLYMOUTH                     | England          |                     1 | 1-10             |
| POOLE                        | England          |                     0 | 0                |
| PORTSMOUTH                   | England          |                     0 | 0                |
| POWYS                        | Wales            |                    77 | 50-100           |
| REDCAR AND CLEVELAND         | England          |                     0 | 0                |
| RENFREWSHIRE                 | Scotland         |                   317 | 300-400          |
| RHONDDA, CYNON, TAFF         | Wales            |                     0 | 0                |
| ROCHDALE                     | England          |                     0 | 0                |
| RUTLAND                      | England          |                     0 | 0                |
| SALFORD                      | England          |                     0 | 0                |
| SCOTTISH BORDERS             | Scotland         |                   143 | 100-150          |
| SHETLAND ISLANDS             | Scotland         |                    14 | 10-50            |
| SHROPSHIRE                   | England          |                     6 | 1-10             |
| SOMERSET                     | England          |                   652 | >500             |
| SOUTH AYRSHIRE               | Scotland         |                     7 | 1-10             |
| SOUTH GLOUCESTERSHIRE        | England          |                     0 | 0                |
| SOUTH LANARKSHIRE            | Scotland         |                    70 | 50-100           |
| SOUTH YORKSHIRE              | England          |                  1594 | >500             |
| SOUTHAMPTON                  | England          |                     0 | 0                |
| SOUTHEND-ON-SEA              | England          |                     0 | 0                |
| STAFFORDSHIRE                | England          |                    62 | 50-100           |
| STIRLING                     | Scotland         |                    18 | 10-50            |
| STOCKPORT                    | England          |                     0 | 0                |
| STOCKTON-ON-TEES             | England          |                     0 | 0                |
| STOKE-ON-TRENT               | England          |                     0 | 0                |
| SUFFOLK                      | England          |                   596 | >500             |
| SURREY                       | England          |                    73 | 50-100           |
| SUSSEX                       | England          |                     1 | 1-10             |
| SWANSEA                      | Wales            |                   276 | 250-300          |
| SWINDON                      | England          |                     0 | 0                |
| TAMESIDE                     | England          |                     0 | 0                |
| TELFORD AND WREKIN           | England          |                     0 | 0                |
| THURROCK                     | England          |                     0 | 0                |
| TORBAY                       | England          |                     0 | 0                |
| TORFAEN                      | Wales            |                    91 | 50-100           |
| TRAFFORD                     | England          |                     0 | 0                |
| TYNE AND WEAR                | England          |                   496 | 400-500          |
| TYRONE                       | Northern Ireland |                    25 | 10-50            |
| VALE OF GLAMORGAN            | Wales            |                   191 | 150-200          |
| WARRINGTON                   | England          |                     0 | 0                |
| WARWICKSHIRE                 | England          |                    11 | 10-50            |
| WEST DUNBARTONSHIRE          | Scotland         |                    49 | 10-50            |
| WEST LOTHIAN                 | Scotland         |                   131 | 100-150          |
| WEST MIDLANDS                | England          |                   167 | 150-200          |
| WEST YORKSHIRE               | England          |                    22 | 10-50            |
| WIGAN                        | England          |                     0 | 0                |
| WILTSHIRE                    | England          |                   386 | 300-400          |
| WORCESTERSHIRE               | England          |                    13 | 10-50            |
| WREXHAM                      | Wales            |                   166 | 150-200          |
| YORK                         | England          |                     0 | 0                |

\pagebreak






