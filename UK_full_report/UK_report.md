







# UK Lineages report




This report gives summaries of UK specific lineages for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-14. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
23786 sequences in the UK have been included in this analysis.
1061 lineages have been recorded, 525 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 512 and the maximum is 10001


Sequences which were replicates or too error-prone were removed from this analysis.



815 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 83 that remain:
46 are pending extinction, ie last seen three weeks ago.
31 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
5 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England       | Wales        | Northern Ireland   | Scotland     | Date range     |   Total sequences | Global lineage                                                                                     |   Time since last sample (days) | Activity score   |
|:---------------|:--------------|:-------------|:-------------------|:-------------|:---------------|------------------:|:---------------------------------------------------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | 5390 (80.17%) | 821 (12.21%) | 210 (3.12%)        | 302 (4.49%)  | Feb-23, Jun-14 |              6723 | B.1.1.p16, B.1.1.13, B.1.1.16, B.1.1.1, B.1.1.p15, B.1.1.p11, B.1.1.p12, B.1.1.10, B.1.1, B.1.1.14 |                               0 | active today     |
| UK42           | 699 (53.4%)   | 371 (28.34%) | 2 (0.15%)          | 237 (18.11%) | Feb-03, Jun-04 |              1309 | B.1.67, B.1.35, B.1.5, B.1.p73, B.1.p11, B.1, B.1.71, B.1.72                                       |                              10 | 0.0093           |
| UK107          | 1183 (91.78%) | 55 (4.27%)   | 11 (0.85%)         | 40 (3.1%)    | Feb-09, Jun-02 |              1289 | B.2.5, B.2.1, B.2                                                                                  |                              12 | 0.0074           |
| UK5676         | 328 (62.24%)  | 57 (10.82%)  | 5 (0.95%)          | 137 (26.0%)  | Feb-14, May-22 |               527 | B.3, B.2                                                                                           |                              23 | 0.0081           |
| UK2464         | 283 (57.99%)  | 80 (16.39%)  | 0 (0%)             | 125 (25.61%) | Mar-09, Jun-07 |               488 | B.1.p11, B.1                                                                                       |                               7 | 0.0264           |
| UK61           | 41 (9.36%)    | 397 (90.64%) | 0 (0%)             | 0 (0%)       | Mar-08, May-27 |               438 | B.3                                                                                                |                              18 | 0.0102           |
| UK199          | 243 (56.25%)  | 37 (8.56%)   | 1 (0.23%)          | 151 (34.95%) | Feb-26, Jun-08 |               432 | B.1.p73, B.1, B.1.5.5, B.1.5                                                                       |                               6 | 0.0398           |
| UK36           | 59 (14.18%)   | 2 (0.48%)    | 2 (0.48%)          | 353 (84.86%) | Mar-18, Jun-03 |               416 | B.1                                                                                                |                              11 | 0.0169           |
| UK2913         | 307 (74.15%)  | 17 (4.11%)   | 11 (2.66%)         | 79 (19.08%)  | Mar-07, Jun-01 |               414 | B.1.p11, B.1                                                                                       |                              13 | 0.016            |
| UK167          | 241 (61.48%)  | 115 (29.34%) | 17 (4.34%)         | 19 (4.85%)   | Jan-27, Jun-07 |               392 | B.1.66, B.1                                                                                        |                               7 | 0.0482           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_geog_plot_1.png){#geog_plot }




The growth and decline of diversity of lineages over time for each country is shown in the ridge plot in figure four.
This is represented by the Shannon Diversity, calculated using the number of sequences from each country from each lineage.



![Shannon diversity of lineages in each adm1 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_diversity_plot_1.png){#diversity_plot }



These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix



The plot below shows the number of sequences from each country that don't have specific enough location data to plot on the map.




![](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/full_report/figures/UK_report_map_2.png)\


Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England       | Wales        | Northern Ireland   | Scotland     | Date range     |   Total sequences | Global lineage                                                                                     |   Time since last sample (days) | Activity score   |
|:---------------|:--------------|:-------------|:-------------------|:-------------|:---------------|------------------:|:---------------------------------------------------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | 5390 (80.17%) | 821 (12.21%) | 210 (3.12%)        | 302 (4.49%)  | Feb-23, Jun-14 |              6723 | B.1.1.p16, B.1.1.13, B.1.1.16, B.1.1.1, B.1.1.p15, B.1.1.p11, B.1.1.p12, B.1.1.10, B.1.1, B.1.1.14 |                               0 | active today     |
| UK42           | 699 (53.4%)   | 371 (28.34%) | 2 (0.15%)          | 237 (18.11%) | Feb-03, Jun-04 |              1309 | B.1.67, B.1.35, B.1.5, B.1.p73, B.1.p11, B.1, B.1.71, B.1.72                                       |                              10 | 0.0093           |
| UK107          | 1183 (91.78%) | 55 (4.27%)   | 11 (0.85%)         | 40 (3.1%)    | Feb-09, Jun-02 |              1289 | B.2.5, B.2.1, B.2                                                                                  |                              12 | 0.0074           |
| UK5676         | 328 (62.24%)  | 57 (10.82%)  | 5 (0.95%)          | 137 (26.0%)  | Feb-14, May-22 |               527 | B.3, B.2                                                                                           |                              23 | 0.0081           |
| UK2464         | 283 (57.99%)  | 80 (16.39%)  | 0 (0%)             | 125 (25.61%) | Mar-09, Jun-07 |               488 | B.1.p11, B.1                                                                                       |                               7 | 0.0264           |
| UK61           | 41 (9.36%)    | 397 (90.64%) | 0 (0%)             | 0 (0%)       | Mar-08, May-27 |               438 | B.3                                                                                                |                              18 | 0.0102           |
| UK199          | 243 (56.25%)  | 37 (8.56%)   | 1 (0.23%)          | 151 (34.95%) | Feb-26, Jun-08 |               432 | B.1.p73, B.1, B.1.5.5, B.1.5                                                                       |                               6 | 0.0398           |
| UK36           | 59 (14.18%)   | 2 (0.48%)    | 2 (0.48%)          | 353 (84.86%) | Mar-18, Jun-03 |               416 | B.1                                                                                                |                              11 | 0.0169           |
| UK2913         | 307 (74.15%)  | 17 (4.11%)   | 11 (2.66%)         | 79 (19.08%)  | Mar-07, Jun-01 |               414 | B.1.p11, B.1                                                                                       |                              13 | 0.016            |
| UK167          | 241 (61.48%)  | 115 (29.34%) | 17 (4.34%)         | 19 (4.85%)   | Jan-27, Jun-07 |               392 | B.1.66, B.1                                                                                        |                               7 | 0.0482           |
| UK5098         | 6 (1.78%)     | 0 (0%)       | 0 (0%)             | 332 (98.22%) | Mar-16, May-27 |               338 | B.1.p73, B.1.8, B.1                                                                                |                              18 | 0.0119           |
| UK158          | 33 (9.88%)    | 301 (90.12%) | 0 (0%)             | 0 (0%)       | Mar-20, Jun-03 |               334 | B.1.1.2, B.1.1                                                                                     |                              11 | 0.0205           |
| UK2916         | 252 (77.54%)  | 52 (16.0%)   | 9 (2.77%)          | 12 (3.69%)   | Feb-03, Jun-01 |               325 | B.1                                                                                                |                              13 | 0.0283           |
| UK72           | 251 (77.71%)  | 14 (4.33%)   | 12 (3.72%)         | 46 (14.24%)  | Feb-05, May-27 |               323 | B, B.2.2, B.2                                                                                      |                              18 | 0.0193           |
| UK109          | 46 (14.84%)   | 31 (10.0%)   | 4 (1.29%)          | 229 (73.87%) | Mar-12, Jun-08 |               310 | B.1.5.5, B.1.5                                                                                     |                               6 | 0.0475           |
| UK5741         | 161 (59.19%)  | 111 (40.81%) | 0 (0%)             | 0 (0%)       | Mar-09, Jun-02 |               272 | B.1.44, B.1                                                                                        |                              12 | 0.0261           |
| UK2735         | 142 (57.49%)  | 67 (27.13%)  | 15 (6.07%)         | 23 (9.31%)   | Mar-18, May-29 |               247 | B.1.1                                                                                              |                              16 | 0.0183           |
| UK632          | 38 (15.45%)   | 205 (83.33%) | 0 (0%)             | 3 (1.22%)    | Mar-23, Jun-04 |               246 | B.1.1                                                                                              |                              10 | 0.0298           |
| UK3021         | 23 (9.58%)    | 217 (90.42%) | 0 (0%)             | 0 (0%)       | Mar-12, Jun-06 |               240 | B.1                                                                                                |                               8 | 0.045            |
| UK9            | 213 (99.53%)  | 1 (0.47%)    | 0 (0%)             | 0 (0%)       | Mar-09, May-15 |               214 | B.1.13                                                                                             |                              30 | 0.0105           |
| UK3929         | 175 (82.94%)  | 3 (1.42%)    | 2 (0.95%)          | 31 (14.69%)  | Mar-06, Jun-03 |               211 | B.1.1.4, B.1.1.3, B.1.1                                                                            |                              11 | 0.0385           |
| UK370          | 81 (46.29%)   | 54 (30.86%)  | 8 (4.57%)          | 32 (18.29%)  | Mar-06, Jun-02 |               175 | B.1.1.10                                                                                           |                              12 | 0.0421           |
| UK40           | 6 (3.49%)     | 2 (1.16%)    | 0 (0%)             | 164 (95.35%) | Mar-13, May-26 |               172 | B, B.16                                                                                            |                              19 | 0.0228           |
| UK15           | 128 (76.19%)  | 11 (6.55%)   | 1 (0.6%)           | 28 (16.67%)  | Feb-27, May-06 |               168 | B.1.1                                                                                              |                              39 | 0.0106           |
| UK5561         | 119 (80.41%)  | 23 (15.54%)  | 1 (0.68%)          | 5 (3.38%)    | Feb-25, May-24 |               148 | B.2.2, B.2                                                                                         |                              21 | 0.0288           |
| UK6            | 133 (96.38%)  | 0 (0%)       | 0 (0%)             | 5 (3.62%)    | Mar-06, May-13 |               138 | B.1                                                                                                |                              32 | 0.0155           |
| UK4            | 124 (97.64%)  | 0 (0%)       | 1 (0.79%)          | 2 (1.57%)    | Feb-28, Apr-29 |               127 | B                                                                                                  |                              46 | 0.0105           |
| UK494          | 121 (97.58%)  | 1 (0.81%)    | 0 (0%)             | 2 (1.61%)    | Mar-19, May-05 |               124 | B.1.p11                                                                                            |                              40 | 0.0096           |
| UK63           | 121 (99.18%)  | 1 (0.82%)    | 0 (0%)             | 0 (0%)       | Mar-18, May-10 |               122 | B.1.1                                                                                              |                              35 | 0.0125           |
| UK565          | 102 (91.07%)  | 5 (4.46%)    | 1 (0.89%)          | 4 (3.57%)    | Mar-11, May-14 |               112 | B.1.1                                                                                              |                              31 | 0.0186           |
| UK66           | 92 (83.64%)   | 0 (0%)       | 1 (0.91%)          | 17 (15.45%)  | Mar-18, May-20 |               110 | B.1.1.8                                                                                            |                              25 | 0.0231           |
| UK39           | 2 (1.83%)     | 0 (0%)       | 0 (0%)             | 107 (98.17%) | Mar-12, May-24 |               109 | A.2                                                                                                |                              21 | 0.0322           |
| UK394          | 21 (20.39%)   | 79 (76.7%)   | 1 (0.97%)          | 2 (1.94%)    | Mar-17, May-24 |               103 | B.1.1.10, B.1.1                                                                                    |                              21 | 0.0317           |
| UK2200         | 22 (23.16%)   | 33 (34.74%)  | 5 (5.26%)          | 35 (36.84%)  | Feb-28, May-20 |                95 | B.1.5.6, B.1.5                                                                                     |                              25 | 0.0349           |
| UK601          | 21 (22.58%)   | 0 (0%)       | 64 (68.82%)        | 8 (8.6%)     | Mar-11, May-04 |                93 | B.10                                                                                               |                              41 | 0.0143           |
| UK240          | 84 (91.3%)    | 2 (2.17%)    | 0 (0%)             | 6 (6.52%)    | Feb-25, May-08 |                92 | B, B.3, B.2, B.2.5, B.2.1                                                                          |                              37 | 0.0217           |
| UK28           | 89 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-13, May-08 |                89 | B.1.1.10                                                                                           |                              37 | 0.0172           |
| UK5180         | 81 (91.01%)   | 4 (4.49%)    | 4 (4.49%)          | 0 (0%)       | Mar-07, May-09 |                89 | B.1.1.7                                                                                            |                              36 | 0.0199           |
| UK5498         | 66 (78.57%)   | 7 (8.33%)    | 0 (0%)             | 11 (13.1%)   | Mar-06, May-28 |                84 | B, B.2                                                                                             |                              17 | 0.0588           |
| UK829          | 80 (98.77%)   | 0 (0%)       | 0 (0%)             | 1 (1.23%)    | Mar-03, Apr-29 |                81 | B.2.5                                                                                              |                              46 | 0.0155           |
| UK51           | 72 (90.0%)    | 0 (0%)       | 1 (1.25%)          | 7 (8.75%)    | Mar-21, Jun-07 |                80 | B.1.36                                                                                             |                               7 | 0.141            |
| UK339          | 61 (76.25%)   | 15 (18.75%)  | 1 (1.25%)          | 3 (3.75%)    | Feb-23, Apr-16 |                80 | B.3                                                                                                |                              59 | 0.0114           |
| UK501          | 66 (84.62%)   | 1 (1.28%)    | 0 (0%)             | 11 (14.1%)   | Mar-02, Jun-02 |                78 | B.1                                                                                                |                              12 | 0.0996           |
| UK5322         | 1 (1.28%)     | 73 (93.59%)  | 0 (0%)             | 4 (5.13%)    | Mar-23, May-30 |                78 | B.1.1                                                                                              |                              15 | 0.0589           |
| UK2906         | 68 (91.89%)   | 2 (2.7%)     | 0 (0%)             | 4 (5.41%)    | Mar-04, Jun-02 |                74 | B.1                                                                                                |                              12 | 0.1027           |
| UK86           | 18 (24.32%)   | 56 (75.68%)  | 0 (0%)             | 0 (0%)       | Mar-05, May-28 |                74 | B.1, B.1.5                                                                                         |                              17 | 0.0677           |
| UK495          | 1 (1.35%)     | 73 (98.65%)  | 0 (0%)             | 0 (0%)       | Apr-01, May-30 |                74 | B.1.p11                                                                                            |                              15 | 0.0539           |
| UK77           | 67 (93.06%)   | 5 (6.94%)    | 0 (0%)             | 0 (0%)       | Mar-11, May-20 |                72 | B.2                                                                                                |                              25 | 0.0394           |
| UK319          | 71 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-28, Jun-01 |                71 | B.1                                                                                                |                              13 | 0.0714           |
| UK85           | 63 (90.0%)    | 5 (7.14%)    | 1 (1.43%)          | 1 (1.43%)    | Mar-09, Apr-27 |                70 | B, B.3                                                                                             |                              48 | 0.0148           |
| UK120          | 52 (78.79%)   | 0 (0%)       | 0 (0%)             | 14 (21.21%)  | Feb-03, May-05 |                66 | B, B.14                                                                                            |                              40 | 0.0354           |
| UK37           | 63 (96.92%)   | 1 (1.54%)    | 0 (0%)             | 1 (1.54%)    | Mar-17, May-04 |                65 | B.1.30, B.1                                                                                        |                              41 | 0.0183           |
| UK607          | 53 (81.54%)   | 12 (18.46%)  | 0 (0%)             | 0 (0%)       | Mar-02, May-18 |                65 | B                                                                                                  |                              27 | 0.0446           |
| UK31           | 60 (93.75%)   | 0 (0%)       | 0 (0%)             | 4 (6.25%)    | Mar-11, Apr-23 |                64 | B.3                                                                                                |                              52 | 0.0131           |
| UK274          | 60 (95.24%)   | 2 (3.17%)    | 0 (0%)             | 1 (1.59%)    | Mar-06, May-21 |                63 | B, B.3                                                                                             |                              24 | 0.0511           |
| UK384          | 60 (95.24%)   | 1 (1.59%)    | 0 (0%)             | 2 (3.17%)    | Feb-28, Apr-23 |                63 | B.2.1, B.2                                                                                         |                              52 | 0.0171           |
| UK366          | 63 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-04, Jun-03 |                63 | B.1.1                                                                                              |                              11 | 0.088            |
| UK509          | 62 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-07, May-29 |                62 | B.1.1                                                                                              |                              16 | 0.0533           |
| UK198          | 5 (8.33%)     | 15 (25.0%)   | 3 (5.0%)           | 37 (61.67%)  | Mar-17, May-07 |                60 | B.1, B.1.5                                                                                         |                              38 | 0.0227           |
| UK13           | 55 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-13, May-13 |                55 | B.1.1                                                                                              |                              32 | 0.0353           |
| UK476          | 55 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-30, May-06 |                55 | B.1.1                                                                                              |                              39 | 0.0176           |
| UK89           | 42 (77.78%)   | 12 (22.22%)  | 0 (0%)             | 0 (0%)       | Mar-21, Jun-05 |                54 | B.1.1.9, B.1.1                                                                                     |                               9 | 0.1593           |
| UK371          | 50 (98.04%)   | 1 (1.96%)    | 0 (0%)             | 0 (0%)       | Mar-12, May-09 |                51 | B.1.1                                                                                              |                              36 | 0.0322           |
| UK513          | 50 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-12, Apr-29 |                50 | B.1.p11                                                                                            |                              46 | 0.0213           |
| UK448          | 47 (97.92%)   | 1 (2.08%)    | 0 (0%)             | 0 (0%)       | Apr-04, May-26 |                48 | B.1.1                                                                                              |                              19 | 0.0582           |
| UK187          | 4 (8.51%)     | 29 (61.7%)   | 7 (14.89%)         | 7 (14.89%)   | Mar-23, Apr-30 |                47 | B.1                                                                                                |                              45 | 0.0184           |
| UK275          | 38 (80.85%)   | 8 (17.02%)   | 0 (0%)             | 1 (2.13%)    | Mar-09, Apr-27 |                47 | B.1.13                                                                                             |                              48 | 0.0222           |
| UK5523         | 46 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | May-01, Jun-01 |                46 | B.1                                                                                                |                              13 | 0.053            |
| UK517          | 43 (93.48%)   | 1 (2.17%)    | 0 (0%)             | 2 (4.35%)    | Mar-02, Apr-30 |                46 | B.1.1                                                                                              |                              45 | 0.0291           |
| UK41           | 30 (69.77%)   | 13 (30.23%)  | 0 (0%)             | 0 (0%)       | Feb-29, May-21 |                43 | B.1                                                                                                |                              24 | 0.0813           |
| UK105          | 1 (2.33%)     | 42 (97.67%)  | 0 (0%)             | 0 (0%)       | Mar-27, May-26 |                43 | B.1.p11                                                                                            |                              19 | 0.0752           |
| UK497          | 38 (90.48%)   | 4 (9.52%)    | 0 (0%)             | 0 (0%)       | Mar-13, Jun-03 |                42 | A.2                                                                                                |                              11 | 0.1818           |
| UK3126         | 41 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-06, May-19 |                41 | B.1.1                                                                                              |                              26 | 0.0413           |
| UK64           | 26 (65.0%)    | 12 (30.0%)   | 0 (0%)             | 2 (5.0%)     | Mar-12, May-05 |                40 | B.1.p73, B.1                                                                                       |                              40 | 0.0346           |
| UK276          | 37 (94.87%)   | 0 (0%)       | 1 (2.56%)          | 1 (2.56%)    | Mar-10, May-13 |                39 | B.1.1                                                                                              |                              32 | 0.0526           |
| UK179          | 16 (41.03%)   | 23 (58.97%)  | 0 (0%)             | 0 (0%)       | Mar-17, May-07 |                39 | B.1.1, B.1.1.p11                                                                                   |                              38 | 0.0353           |
| UK131          | 34 (89.47%)   | 4 (10.53%)   | 0 (0%)             | 0 (0%)       | Mar-11, Apr-14 |                38 | B.15                                                                                               |                              61 | 0.0151           |
| UK173          | 38 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-14, May-19 |                38 | B                                                                                                  |                              26 | 0.0686           |
| UK376          | 38 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-11, Apr-30 |                38 | B.1.1.9                                                                                            |                              45 | 0.03             |
| UK404          | 37 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-01, Apr-19 |                37 | B.1                                                                                                |                              56 | 0.0243           |
| UK12           | 36 (97.3%)    | 0 (0%)       | 1 (2.7%)           | 0 (0%)       | Mar-12, May-07 |                37 | B.1.p11                                                                                            |                              38 | 0.0409           |
| UK355          | 35 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-22, Jun-14 |                35 | B.1.1                                                                                              |                               0 | active today     |
| UK119          | 27 (77.14%)   | 7 (20.0%)    | 0 (0%)             | 1 (2.86%)    | Mar-11, Apr-24 |                35 | B.2.5                                                                                              |                              51 | 0.0254           |
| UK79           | 35 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-24, May-05 |                35 | B.1                                                                                                |                              40 | 0.0309           |
| UK304          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 34 (100.0%)  | Apr-16, Jun-02 |                34 | B.1.1.14                                                                                           |                              12 | 0.1187           |
| UK18           | 31 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-11, Apr-14 |                31 | B.1.1.7                                                                                            |                              61 | 0.0186           |
| UK1207         | 30 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-23, May-12 |                30 | B.1.1                                                                                              |                              33 | 0.0522           |
| UK14           | 2 (6.67%)     | 0 (0%)       | 0 (0%)             | 28 (93.33%)  | Mar-12, Apr-27 |                30 | B                                                                                                  |                              48 | 0.033            |
| UK241          | 30 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-22, Apr-16 |                30 | B.1.5.3                                                                                            |                              59 | 0.0146           |
| UK43           | 1 (3.45%)     | 0 (0%)       | 0 (0%)             | 28 (96.55%)  | Mar-12, Apr-26 |                29 | A.5                                                                                                |                              49 | 0.0328           |
| UK100          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 29 (100.0%)  | Mar-30, May-25 |                29 | B.1, B.1.5                                                                                         |                              20 | 0.1              |
| UK3692         | 22 (75.86%)   | 1 (3.45%)    | 0 (0%)             | 6 (20.69%)   | Mar-09, May-19 |                29 | B.1.1                                                                                              |                              26 | 0.0975           |
| UK44           | 0 (0%)        | 0 (0%)       | 1 (3.45%)          | 28 (96.55%)  | Mar-17, Apr-19 |                29 | B                                                                                                  |                              56 | 0.021            |
| UK5549         | 24 (88.89%)   | 0 (0%)       | 2 (7.41%)          | 1 (3.7%)     | Mar-04, May-18 |                27 | B.2.2                                                                                              |                              27 | 0.1068           |
| UK5649         | 24 (88.89%)   | 2 (7.41%)    | 0 (0%)             | 1 (3.7%)     | Mar-15, May-04 |                27 | B.2.6                                                                                              |                              41 | 0.0469           |
| UK567          | 4 (14.81%)    | 18 (66.67%)  | 1 (3.7%)           | 4 (14.81%)   | Mar-20, May-15 |                27 | B.2.2                                                                                              |                              30 | 0.0718           |
| UK1721         | 26 (96.3%)    | 1 (3.7%)     | 0 (0%)             | 0 (0%)       | Mar-19, May-08 |                27 | B.1                                                                                                |                              37 | 0.052            |
| UK101          | 26 (96.3%)    | 0 (0%)       | 0 (0%)             | 1 (3.7%)     | Mar-21, Apr-25 |                27 | B.1.5                                                                                              |                              50 | 0.0269           |
| UK5309         | 23 (88.46%)   | 3 (11.54%)   | 0 (0%)             | 0 (0%)       | Mar-20, May-30 |                26 | B.1.1.10, B.1.1                                                                                    |                              15 | 0.1893           |
| UK94           | 26 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-12, Apr-19 |                26 | B.2.1, B.2                                                                                         |                              56 | 0.0271           |
| UK326          | 24 (96.0%)    | 0 (0%)       | 0 (0%)             | 1 (4.0%)     | Mar-22, May-22 |                25 | B.1.1.10                                                                                           |                              23 | 0.1105           |
| UK23           | 25 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-21, May-09 |                25 | B.9                                                                                                |                              36 | 0.0567           |
| UK317          | 11 (44.0%)    | 12 (48.0%)   | 0 (0%)             | 2 (8.0%)     | Mar-13, Apr-20 |                25 | B.3                                                                                                |                              55 | 0.0288           |
| UK164          | 24 (96.0%)    | 1 (4.0%)     | 0 (0%)             | 0 (0%)       | Apr-08, May-28 |                25 | B.1                                                                                                |                              17 | 0.1225           |
| UK462          | 17 (70.83%)   | 7 (29.17%)   | 0 (0%)             | 0 (0%)       | Apr-01, May-18 |                24 | B.1                                                                                                |                              27 | 0.0757           |
| UK1667         | 4 (16.67%)    | 0 (0%)       | 0 (0%)             | 20 (83.33%)  | Mar-30, May-14 |                24 | B.1.9, B.1.p9                                                                                      |                              31 | 0.0631           |
| UK46           | 23 (95.83%)   | 1 (4.17%)    | 0 (0%)             | 0 (0%)       | Mar-02, May-08 |                24 | B.2.1                                                                                              |                              37 | 0.0787           |
| UK491          | 16 (66.67%)   | 8 (33.33%)   | 0 (0%)             | 0 (0%)       | Mar-03, Apr-14 |                24 | B, B.2.1, B.2                                                                                      |                              61 | 0.0299           |
| UK21           | 0 (0%)        | 0 (0%)       | 0 (0%)             | 24 (100.0%)  | Mar-18, May-23 |                24 | B.1.40                                                                                             |                              22 | 0.1304           |
| UK202          | 9 (39.13%)    | 13 (56.52%)  | 0 (0%)             | 1 (4.35%)    | Mar-10, Jun-04 |                23 | B.1.1                                                                                              |                              10 | 0.3909           |
| UK87           | 0 (0%)        | 0 (0%)       | 0 (0%)             | 23 (100.0%)  | Mar-13, Apr-24 |                23 | B.1.70                                                                                             |                              51 | 0.0374           |
| UK203          | 19 (86.36%)   | 2 (9.09%)    | 0 (0%)             | 1 (4.55%)    | Mar-22, May-30 |                22 | B.1.1                                                                                              |                              15 | 0.219            |
| UK116          | 8 (38.1%)     | 13 (61.9%)   | 0 (0%)             | 0 (0%)       | Mar-24, May-30 |                21 | B.1                                                                                                |                              15 | 0.2233           |
| UK2045         | 21 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-17, May-09 |                21 | B.1                                                                                                |                              36 | 0.0736           |
| UK335          | 16 (76.19%)   | 1 (4.76%)    | 0 (0%)             | 4 (19.05%)   | Mar-07, Jun-05 |                21 | B.1.1                                                                                              |                               9 | 0.5              |
| UK161          | 16 (76.19%)   | 5 (23.81%)   | 0 (0%)             | 0 (0%)       | Mar-10, May-25 |                21 | B.1.1                                                                                              |                              20 | 0.19             |
| UK27           | 18 (85.71%)   | 2 (9.52%)    | 0 (0%)             | 1 (4.76%)    | Mar-05, May-21 |                21 | B.1.1                                                                                              |                              24 | 0.1604           |
| UK480          | 19 (90.48%)   | 0 (0%)       | 0 (0%)             | 2 (9.52%)    | Mar-20, May-18 |                21 | B.1.1                                                                                              |                              27 | 0.1093           |
| UK174          | 21 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-19, May-22 |                21 | B.1.5                                                                                              |                              23 | 0.1391           |
| UK24           | 21 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-14, Apr-10 |                21 | B.2.1                                                                                              |                              65 | 0.0208           |
| UK75           | 20 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-17, Apr-26 |                20 | B.1.34, B.1                                                                                        |                              49 | 0.043            |
| UK5503         | 20 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-20, May-13 |                20 | B.1                                                                                                |                              32 | 0.0888           |
| UK233          | 20 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | May-25, Jun-08 |                20 | B.1                                                                                                |                               6 | 0.1228           |
| UK47           | 15 (75.0%)    | 5 (25.0%)    | 0 (0%)             | 0 (0%)       | Mar-17, May-18 |                20 | B.1.1                                                                                              |                              27 | 0.1209           |
| UK134          | 15 (78.95%)   | 0 (0%)       | 0 (0%)             | 4 (21.05%)   | Mar-04, Apr-07 |                19 | B.1                                                                                                |                              68 | 0.0278           |
| UK1703         | 19 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-02, May-01 |                19 | B.1                                                                                                |                              44 | 0.0366           |
| UK146          | 18 (94.74%)   | 0 (0%)       | 0 (0%)             | 1 (5.26%)    | Mar-24, May-07 |                19 | B.1.1                                                                                              |                              38 | 0.0643           |
| UK502          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 18 (100.0%)  | Mar-06, Mar-30 |                18 | B.1.69                                                                                             |                              76 | 0.0186           |
| UK4493         | 0 (0%)        | 0 (0%)       | 0 (0%)             | 18 (100.0%)  | Apr-23, May-19 |                18 | B.1                                                                                                |                              26 | 0.0588           |
| UK425          | 4 (22.22%)    | 14 (77.78%)  | 0 (0%)             | 0 (0%)       | Mar-28, May-15 |                18 | B.1.1                                                                                              |                              30 | 0.0941           |
| UK4237         | 18 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-02, Apr-20 |                18 | B.1.1                                                                                              |                              55 | 0.0193           |
| UK125          | 17 (94.44%)   | 0 (0%)       | 0 (0%)             | 1 (5.56%)    | Mar-30, May-29 |                18 | B.1.1                                                                                              |                              16 | 0.2206           |
| UK2539         | 18 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-24, May-14 |                18 | B.1.1.5                                                                                            |                              31 | 0.0968           |
| UK5300         | 16 (94.12%)   | 0 (0%)       | 0 (0%)             | 1 (5.88%)    | Apr-17, Jun-07 |                17 | B.1.1                                                                                              |                               7 | 0.4554           |
| UK71           | 16 (94.12%)   | 1 (5.88%)    | 0 (0%)             | 0 (0%)       | Mar-08, May-06 |                17 | B                                                                                                  |                              39 | 0.0946           |
| UK604          | 12 (70.59%)   | 2 (11.76%)   | 0 (0%)             | 3 (17.65%)   | Mar-06, Mar-17 |                17 | B.1.1                                                                                              |                              89 | 0.0077           |
| UK706          | 3 (18.75%)    | 0 (0%)       | 13 (81.25%)        | 0 (0%)       | Mar-26, Apr-29 |                16 | B.1.1                                                                                              |                              46 | 0.0493           |
| UK268          | 12 (75.0%)    | 4 (25.0%)    | 0 (0%)             | 0 (0%)       | Mar-23, Jun-04 |                16 | B.1.1                                                                                              |                              10 | 0.4867           |
| UK5660         | 16 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-25, May-08 |                16 | B.1.1                                                                                              |                              37 | 0.0234           |
| UK3781         | 16 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-09, May-08 |                16 | B.1.1                                                                                              |                              37 | 0.1081           |
| UK527          | 10 (62.5%)    | 5 (31.25%)   | 0 (0%)             | 1 (6.25%)    | Mar-19, Apr-18 |                16 | B.1                                                                                                |                              57 | 0.0351           |
| UK553          | 11 (68.75%)   | 5 (31.25%)   | 0 (0%)             | 0 (0%)       | Feb-28, Apr-29 |                16 | B.1                                                                                                |                              46 | 0.0884           |
| UK5715         | 14 (93.33%)   | 0 (0%)       | 0 (0%)             | 1 (6.67%)    | Feb-13, Apr-22 |                15 | B.2                                                                                                |                              53 | 0.093            |
| UK569          | 15 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-23, May-12 |                15 | B.1.1                                                                                              |                              33 | 0.1082           |
| UK1177         | 15 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-22, May-29 |                15 | B.1.1                                                                                              |                              16 | 0.1652           |
| UK1006         | 15 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-02, May-03 |                15 | B.1.1                                                                                              |                              42 | 0.0527           |
| UK70           | 12 (80.0%)    | 1 (6.67%)    | 2 (13.33%)         | 0 (0%)       | Mar-06, Apr-18 |                15 | B.2                                                                                                |                              57 | 0.0539           |
| UK34           | 15 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Feb-15, Apr-02 |                15 | B.4                                                                                                |                              73 | 0.046            |
| UK38           | 14 (93.33%)   | 0 (0%)       | 0 (0%)             | 1 (6.67%)    | Mar-04, Apr-20 |                15 | B.2.1                                                                                              |                              55 | 0.061            |
| UK186          | 13 (92.86%)   | 1 (7.14%)    | 0 (0%)             | 0 (0%)       | Mar-27, May-15 |                14 | B                                                                                                  |                              30 | 0.1256           |
| UK49           | 12 (85.71%)   | 0 (0%)       | 1 (7.14%)          | 1 (7.14%)    | Mar-12, May-01 |                14 | B.9                                                                                                |                              44 | 0.0874           |
| UK153          | 14 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-13, Apr-14 |                14 | B.2                                                                                                |                              61 | 0.0404           |
| UK408          | 12 (92.31%)   | 1 (7.69%)    | 0 (0%)             | 0 (0%)       | Apr-13, Jun-08 |                13 | B.1.1                                                                                              |                               6 | 0.7778           |
| UK58           | 6 (46.15%)    | 0 (0%)       | 0 (0%)             | 7 (53.85%)   | Mar-12, Apr-09 |                13 | B.1                                                                                                |                              66 | 0.0354           |
| UK137          | 1 (7.69%)     | 0 (0%)       | 1 (7.69%)          | 11 (84.62%)  | Mar-09, Mar-31 |                13 | B.1.1                                                                                              |                              75 | 0.0244           |
| UK832          | 12 (92.31%)   | 0 (0%)       | 0 (0%)             | 1 (7.69%)    | Mar-09, Apr-26 |                13 | A.5                                                                                                |                              49 | 0.0816           |
| UK378          | 13 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Feb-15, Mar-05 |                13 | B.1.1                                                                                              |                             101 | 0.0157           |
| UK436          | 0 (0%)        | 1 (8.33%)    | 0 (0%)             | 11 (91.67%)  | Mar-30, May-14 |                12 | B.1.5                                                                                              |                              31 | 0.132            |
| UK141          | 12 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-22, Apr-24 |                12 | B.1.1                                                                                              |                              51 | 0.0588           |
| UK261          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 12 (100.0%)  | Mar-15, Apr-08 |                12 | A.3                                                                                                |                              67 | 0.0326           |
| UK178          | 11 (91.67%)   | 0 (0%)       | 1 (8.33%)          | 0 (0%)       | Mar-14, Apr-29 |                12 | B.1.1                                                                                              |                              46 | 0.0909           |
| UK5663         | 12 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-11, May-02 |                12 | B.2                                                                                                |                              43 | 0.0444           |
| UK193          | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)             | 0 (0%)       | Mar-30, May-01 |                12 | B.1.1                                                                                              |                              44 | 0.0661           |
| UK759          | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)             | 0 (0%)       | Mar-28, Apr-27 |                12 | B.1.1                                                                                              |                              48 | 0.0568           |
| UK132          | 11 (91.67%)   | 0 (0%)       | 0 (0%)             | 1 (8.33%)    | Mar-27, Apr-30 |                12 | B.1                                                                                                |                              45 | 0.0687           |
| UK83           | 9 (75.0%)     | 1 (8.33%)    | 0 (0%)             | 2 (16.67%)   | Feb-29, Apr-08 |                12 | B.1.1                                                                                              |                              67 | 0.0529           |
| UK507          | 12 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-18, Apr-30 |                12 | B.1.1.10                                                                                           |                              45 | 0.0869           |
| UK287          | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)             | 0 (0%)       | Mar-28, Apr-24 |                12 | B.1                                                                                                |                              51 | 0.0481           |
| UK5446         | 12 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | May-05, May-16 |                12 | B.1.1                                                                                              |                              29 | 0.0345           |
| UK445          | 11 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-14, Apr-27 |                11 | B.1.1                                                                                              |                              48 | 0.0917           |
| UK5084         | 9 (81.82%)    | 2 (18.18%)   | 0 (0%)             | 0 (0%)       | Mar-29, Apr-16 |                11 | B.1                                                                                                |                              59 | 0.0305           |
| UK415          | 11 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-19, May-06 |                11 | B.1                                                                                                |                              39 | 0.0436           |
| UK566          | 11 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-02, Apr-21 |                11 | B.1.1.10, B.1.1                                                                                    |                              54 | 0.0352           |
| UK5307         | 9 (81.82%)    | 2 (18.18%)   | 0 (0%)             | 0 (0%)       | Mar-08, May-12 |                11 | B.1.1                                                                                              |                              33 | 0.197            |
| UK572          | 11 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-16, Apr-11 |                11 | B.2                                                                                                |                              64 | 0.0406           |
| UK523          | 11 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-14, May-14 |                11 | B.1.1                                                                                              |                              31 | 0.0968           |
| UK266          | 11 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-06, Apr-30 |                11 | B.1                                                                                                |                              45 | 0.0533           |
| UK801          | 0 (0%)        | 10 (100.0%)  | 0 (0%)             | 0 (0%)       | Apr-05, May-05 |                10 | B.1                                                                                                |                              40 | 0.0833           |
| UK291          | 10 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-29, May-14 |                10 | B.1.5                                                                                              |                              31 | 0.1649           |
| UK22           | 10 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-02, Apr-21 |                10 | B                                                                                                  |                              54 | 0.1029           |
| UK788          | 10 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Feb-28, Mar-05 |                10 | B.4                                                                                                |                             101 | 0.0066           |
| UK320          | 6 (60.0%)     | 0 (0%)       | 4 (40.0%)          | 0 (0%)       | Mar-22, Jun-02 |                10 | B.1                                                                                                |                              12 | 0.6667           |
| UK5653         | 9 (90.0%)     | 0 (0%)       | 0 (0%)             | 1 (10.0%)    | Mar-10, Apr-01 |                10 | B.2.6                                                                                              |                              74 | 0.033            |
| UK242          | 10 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-26, Apr-20 |                10 | B.1.5                                                                                              |                              55 | 0.0505           |
| UK113          | 10 (100.0%)   | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-22, Jun-02 |                10 | B.1.1                                                                                              |                              12 | 0.6667           |
| UK206          | 0 (0%)        | 9 (100.0%)   | 0 (0%)             | 0 (0%)       | Apr-02, May-20 |                 9 | B.1                                                                                                |                              25 | 0.24             |
| UK3509         | 4 (44.44%)    | 3 (33.33%)   | 0 (0%)             | 2 (22.22%)   | Mar-12, Apr-24 |                 9 | B.1.1.10                                                                                           |                              51 | 0.1054           |
| UK506          | 2 (22.22%)    | 7 (77.78%)   | 0 (0%)             | 0 (0%)       | Apr-02, Apr-20 |                 9 | B.1.1                                                                                              |                              55 | 0.0409           |
| UK696          | 0 (0%)        | 9 (100.0%)   | 0 (0%)             | 0 (0%)       | Apr-10, May-01 |                 9 | B.1, B.1.5                                                                                         |                              44 | 0.0597           |
| UK340          | 9 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-23, May-17 |                 9 | B.1.1                                                                                              |                              28 | 0.2455           |
| UK454          | 9 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-22, Apr-29 |                 9 | B.1.1                                                                                              |                              46 | 0.1033           |
| UK133          | 2 (22.22%)    | 0 (0%)       | 0 (0%)             | 7 (77.78%)   | Mar-22, Apr-25 |                 9 | B.1                                                                                                |                              50 | 0.085            |
| UK59           | 9 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-24, Apr-21 |                 9 | B.1                                                                                                |                              54 | 0.0648           |
| UK5348         | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-14, Apr-24 |                 8 | B.1.1                                                                                              |                              51 | 0.1148           |
| UK570          | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-24, Apr-29 |                 8 | B.1.1                                                                                              |                              46 | 0.1118           |
| UK244          | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)             | 0 (0%)       | Mar-12, Apr-06 |                 8 | B.1.1                                                                                              |                              69 | 0.0518           |
| UK739          | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-01, Mar-08 |                 8 | B.4                                                                                                |                              98 | 0.0102           |
| UK594          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 8 (100.0%)   | Apr-20, May-01 |                 8 | B                                                                                                  |                              44 | 0.0357           |
| UK55           | 4 (50.0%)     | 0 (0%)       | 0 (0%)             | 4 (50.0%)    | Mar-23, May-06 |                 8 | B.1.1                                                                                              |                              39 | 0.1612           |
| UK756          | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Feb-27, Mar-05 |                 8 | B.1.1                                                                                              |                             101 | 0.0099           |
| UK271          | 1 (12.5%)     | 0 (0%)       | 0 (0%)             | 7 (87.5%)    | Apr-02, Apr-26 |                 8 | B.1                                                                                                |                              49 | 0.07             |
| UK548          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 8 (100.0%)   | Mar-14, Mar-30 |                 8 | B.2.1                                                                                              |                              76 | 0.0301           |
| UK342          | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-02, Apr-23 |                 8 | B.1.1                                                                                              |                              52 | 0.0577           |
| UK5308         | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-29, May-01 |                 8 | B.1.1                                                                                              |                              44 | 0.0065           |
| UK584          | 7 (87.5%)     | 0 (0%)       | 0 (0%)             | 1 (12.5%)    | Mar-17, May-08 |                 8 | B.2.1, B.2                                                                                         |                              37 | 0.2008           |
| UK479          | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-01, Apr-27 |                 8 | B.1.1                                                                                              |                              48 | 0.0774           |
| UK284          | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-02, Apr-25 |                 8 | B.1.1                                                                                              |                              50 | 0.0657           |
| UK243          | 5 (62.5%)     | 0 (0%)       | 0 (0%)             | 3 (37.5%)    | Mar-18, Apr-15 |                 8 | B.1.p11, B.1, B.1.5                                                                                |                              60 | 0.0667           |
| UK633          | 0 (0%)        | 8 (100.0%)   | 0 (0%)             | 0 (0%)       | Apr-03, Apr-28 |                 8 | B.1.1.p16, B.1.1.16                                                                                |                              47 | 0.076            |
| UK65           | 7 (87.5%)     | 0 (0%)       | 0 (0%)             | 1 (12.5%)    | Mar-07, Apr-21 |                 8 | B.1.1                                                                                              |                              54 | 0.119            |
| UK2888         | 8 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-09, May-14 |                 8 | B.1.1                                                                                              |                              31 | 0.1613           |
| UK755          | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-06, May-21 |                 7 | B.1.1                                                                                              |                              24 | 0.5278           |
| UK490          | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-03, May-02 |                 7 | B.1.1                                                                                              |                              43 | 0.1124           |
| UK122          | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-23, May-07 |                 7 | B.1                                                                                                |                              38 | 0.1974           |
| UK232          | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-04, Mar-30 |                 7 | B.1.1                                                                                              |                              76 | 0.057            |
| UK151          | 0 (0%)        | 0 (0%)       | 0 (0%)             | 7 (100.0%)   | Mar-23, Apr-24 |                 7 | B.1                                                                                                |                              51 | 0.1046           |
| UK171          | 2 (28.57%)    | 0 (0%)       | 0 (0%)             | 5 (71.43%)   | Mar-31, Apr-21 |                 7 | B.1                                                                                                |                              54 | 0.0648           |
| UK3045         | 1 (14.29%)    | 6 (85.71%)   | 0 (0%)             | 0 (0%)       | Apr-15, May-27 |                 7 | B.1.1, B.1.1.p11                                                                                   |                              18 | 0.3889           |
| UK581          | 1 (14.29%)    | 0 (0%)       | 6 (85.71%)         | 0 (0%)       | Apr-06, May-01 |                 7 | B.1.1                                                                                              |                              44 | 0.0947           |
| UK32           | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-10, May-01 |                 7 | B.1.1                                                                                              |                              44 | 0.0795           |
| UK5501         | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Apr-16, Jun-01 |                 7 | B.1.12                                                                                             |                              13 | 0.5897           |
| UK323          | 2 (28.57%)    | 1 (14.29%)   | 0 (0%)             | 4 (57.14%)   | Mar-23, May-06 |                 7 | B.1.35, B.1, B.1.5                                                                                 |                              39 | 0.188            |
| UK520          | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-14, Apr-08 |                 7 | B.2.1, B.2                                                                                         |                              67 | 0.0622           |
| UK390          | 7 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-27, May-01 |                 7 | B.1.5                                                                                              |                              44 | 0.1326           |
| UK451          | 0 (0%)        | 6 (85.71%)   | 0 (0%)             | 1 (14.29%)   | Mar-20, Apr-05 |                 7 | B.2.1                                                                                              |                              70 | 0.0381           |
| UK80           | 4 (57.14%)    | 3 (42.86%)   | 0 (0%)             | 0 (0%)       | Mar-31, Apr-20 |                 7 | B.1.1.p15                                                                                          |                              55 | 0.0606           |
| UK5640         | 2 (28.57%)    | 0 (0%)       | 1 (14.29%)         | 4 (57.14%)   | Mar-20, Apr-27 |                 7 | B.1.1                                                                                              |                              48 | 0.1319           |
| UK433          | 4 (57.14%)    | 0 (0%)       | 0 (0%)             | 3 (42.86%)   | Mar-22, May-03 |                 7 | B                                                                                                  |                              42 | 0.1667           |
| UK263          | 6 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-20, Apr-13 |                 6 | B.1.p11                                                                                            |                              62 | 0.0774           |
| UK364          | 1 (16.67%)    | 4 (66.67%)   | 1 (16.67%)         | 0 (0%)       | Mar-19, May-14 |                 6 | B.1                                                                                                |                              31 | 0.3613           |
| UK485          | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)         | 0 (0%)       | Mar-02, Apr-06 |                 6 | B.1.1                                                                                              |                              69 | 0.1014           |
| UK521          | 2 (33.33%)    | 4 (66.67%)   | 0 (0%)             | 0 (0%)       | Mar-27, Apr-08 |                 6 | B.1.1                                                                                              |                              67 | 0.0358           |
| UK2014         | 2 (33.33%)    | 0 (0%)       | 0 (0%)             | 4 (66.67%)   | Apr-11, Jun-05 |                 6 | B.1                                                                                                |                               9 | 1.2222           |
| UK799          | 6 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-01, Mar-07 |                 6 | B.1                                                                                                |                              99 | 0.0121           |
| UK713          | 5 (83.33%)    | 1 (16.67%)   | 0 (0%)             | 0 (0%)       | Apr-03, May-27 |                 6 | B.1.1                                                                                              |                              18 | 0.6              |
| UK629          | 6 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-23, Apr-13 |                 6 | B.1                                                                                                |                              62 | 0.0677           |
| UK464          | 4 (66.67%)    | 2 (33.33%)   | 0 (0%)             | 0 (0%)       | Mar-25, Apr-19 |                 6 | B.1                                                                                                |                              56 | 0.0893           |
| UK185          | 4 (66.67%)    | 0 (0%)       | 1 (16.67%)         | 1 (16.67%)   | Mar-10, May-15 |                 6 | B.3                                                                                                |                              30 | 0.44             |
| UK5903         | 5 (83.33%)    | 0 (0%)       | 0 (0%)             | 1 (16.67%)   | Mar-25, Apr-18 |                 6 | B.2                                                                                                |                              57 | 0.0842           |
| UK270          | 5 (83.33%)    | 0 (0%)       | 0 (0%)             | 1 (16.67%)   | Mar-04, Apr-01 |                 6 | B                                                                                                  |                              74 | 0.0757           |
| UK552          | 1 (16.67%)    | 0 (0%)       | 0 (0%)             | 5 (83.33%)   | Mar-18, Mar-30 |                 6 | A.1                                                                                                |                              76 | 0.0316           |
| UK5215         | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)         | 0 (0%)       | Mar-29, May-13 |                 6 | B.1.1                                                                                              |                              32 | 0.2812           |
| UK269          | 6 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Mar-25, Jun-02 |                 6 | B.1.1                                                                                              |                              12 | 1.15             |
| UK574          | 4 (66.67%)    | 2 (33.33%)   | 0 (0%)             | 0 (0%)       | Mar-26, Apr-13 |                 6 | B.2.1                                                                                              |                              62 | 0.0581           |
| UK330          | 5 (83.33%)    | 1 (16.67%)   | 0 (0%)             | 0 (0%)       | Mar-23, Apr-08 |                 6 | B.1.1                                                                                              |                              67 | 0.0478           |
| UK654          | 6 (100.0%)    | 0 (0%)       | 0 (0%)             | 0 (0%)       | Feb-27, Mar-08 |                 6 | B.2.5                                                                                              |                              98 | 0.0204           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NOTT     |             5 |
|  1 | CAMB     |             5 |
|  2 | NORW     |            10 |
|  3 | PORT     |            11 |
|  4 | BIRM     |            11 |
|  5 | EDIN     |            11 |
|  6 | LIVE     |            11 |
|  7 | PHWC     |            13 |
|  8 | SANG     |            14 |
|  9 | EXET     |            16 |
| 10 | SHEF     |            18 |
| 11 | NORT     |            19 |
| 12 | GLAS     |            23 |
| 13 | PHEC     |            31 |
| 14 | LOND     |            36 |
| 15 | OXON     |            66 |
| 16 | NIRE     |            80 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK42 |   UK107 |   UK5676 |   UK2464 |   UK61 |   UK199 |   UK36 |   UK2913 |   UK167 |
|:------------------|------:|-------:|--------:|---------:|---------:|-------:|--------:|-------:|---------:|--------:|
| 2020-01-26        |     0 |      0 |       0 |        0 |        0 |      0 |       0 |      0 |        0 |       1 |
| 2020-02-02        |     0 |      1 |       0 |        0 |        0 |      0 |       0 |      0 |        0 |       0 |
| 2020-02-09        |     0 |      0 |       1 |        1 |        0 |      0 |       0 |      0 |        0 |       0 |
| 2020-02-16        |     0 |      0 |       1 |        0 |        0 |      0 |       0 |      0 |        0 |       0 |
| 2020-02-23        |     2 |      4 |       5 |        2 |        0 |      0 |       1 |      0 |        0 |       0 |
| 2020-03-01        |    10 |     12 |       6 |        6 |        0 |      0 |       2 |      0 |        1 |       1 |
| 2020-03-08        |    29 |     16 |      18 |       15 |        3 |      3 |       3 |      0 |        4 |       9 |
| 2020-03-15        |    33 |     22 |      26 |       28 |       12 |      2 |      10 |      4 |        6 |       4 |
| 2020-03-22        |    55 |     38 |      36 |       30 |       25 |      9 |      21 |      9 |       12 |      17 |
| 2020-03-29        |    63 |     50 |      39 |       38 |       30 |     14 |      26 |     18 |       19 |      23 |
| 2020-04-05        |    73 |     51 |      35 |       27 |       27 |     21 |      24 |     12 |       21 |      25 |
| 2020-04-12        |    69 |     41 |      21 |       13 |       23 |     14 |      20 |     20 |       18 |      19 |
| 2020-04-19        |    69 |     37 |      19 |       16 |       24 |      8 |      20 |     17 |       17 |      17 |
| 2020-04-26        |    66 |     26 |      11 |        6 |       15 |      7 |      15 |     12 |       15 |      15 |
| 2020-05-03        |    62 |     16 |       4 |        6 |       11 |      3 |       9 |      8 |        5 |      11 |
| 2020-05-10        |    57 |     15 |       2 |        3 |        7 |      6 |      10 |     11 |        7 |      11 |
| 2020-05-17        |    49 |      7 |       1 |        1 |        2 |      2 |       4 |      6 |        3 |      13 |
| 2020-05-24        |    38 |      4 |       0 |        0 |        1 |      4 |       4 |      4 |        4 |       6 |
| 2020-05-31        |    30 |      4 |       1 |        0 |        2 |      0 |       3 |      2 |        3 |       3 |
| 2020-06-07        |    13 |      0 |       0 |        0 |        1 |      0 |       1 |      0 |        0 |       1 |
| 2020-06-14        |     1 |      0 |       0 |        0 |        0 |      0 |       0 |      0 |        0 |       0 |

\pagebreak


**Table S4** Raw data for figure four showing the Shannon diversity per admin1 region over time



| Week       |   England |    Wales |   Scotland |   Northern Ireland |
|:-----------|----------:|---------:|-----------:|-------------------:|
| 2020-01-26 |  0        | -0       |   0        |            0       |
| 2020-02-02 |  1.25548  |  0       |   0        |            0       |
| 2020-02-09 |  1.66746  |  0       |   0        |            0       |
| 2020-02-16 |  0.796312 |  0       |   0        |            0       |
| 2020-02-23 |  2.80211  | -0       |  -0        |            0       |
| 2020-03-01 |  3.38983  |  1.33218 |   2.13833  |            0       |
| 2020-03-08 |  3.77071  |  1.84732 |   3.31772  |            1.9792  |
| 2020-03-15 |  3.56184  |  2.01829 |   3.36593  |            1.82452 |
| 2020-03-22 |  3.80546  |  2.53207 |   3.50744  |            2.78284 |
| 2020-03-29 |  3.76128  |  3.48345 |   3.45855  |            2.00866 |
| 2020-04-05 |  3.5745   |  3.26534 |   3.22123  |            2.02811 |
| 2020-04-12 |  3.44145  |  2.95106 |   3.06333  |            1.62747 |
| 2020-04-19 |  3.29698  |  3.01851 |   3.15986  |            1.06588 |
| 2020-04-26 |  3.19389  |  2.999   |   2.8534   |            1.58445 |
| 2020-05-03 |  3.1828   |  2.65735 |   2.70626  |            0       |
| 2020-05-10 |  2.71692  |  2.63827 |   2.65054  |            0       |
| 2020-05-17 |  1.9998   |  2.59537 |   2.22607  |            0       |
| 2020-05-24 |  1.94991  |  2.2692  |   2.12343  |            0       |
| 2020-05-31 |  2.12849  |  1.65076 |   1.24908  |            0       |
| 2020-06-07 |  1.17005  |  0       |   0.693147 |            0       |
| 2020-06-14 |  0.693147 |  0       |   0        |            0       |

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
| 2020-02-15 |                            0 |                                2 |       2 |
| 2020-02-16 |                            0 |                                1 |       1 |
| 2020-02-23 |                            0 |                                2 |       2 |
| 2020-02-25 |                            0 |                                2 |       2 |
| 2020-02-26 |                            1 |                                1 |       2 |
| 2020-02-27 |                            1 |                                3 |       4 |
| 2020-02-28 |                            0 |                                6 |       6 |
| 2020-02-29 |                            0 |                                2 |       2 |
| 2020-03-01 |                            3 |                                5 |       8 |
| 2020-03-02 |                            1 |                                8 |       9 |
| 2020-03-03 |                            1 |                                5 |       6 |
| 2020-03-04 |                            0 |                                9 |       9 |
| 2020-03-05 |                            0 |                                4 |       4 |
| 2020-03-06 |                            3 |                                9 |      12 |
| 2020-03-07 |                            3 |                                6 |       9 |
| 2020-03-08 |                            2 |                                5 |       7 |
| 2020-03-09 |                            6 |                               14 |      20 |
| 2020-03-10 |                            4 |                                6 |      10 |
| 2020-03-11 |                           10 |                               15 |      25 |
| 2020-03-12 |                           10 |                               21 |      31 |
| 2020-03-13 |                           12 |                                8 |      20 |
| 2020-03-14 |                            4 |                               10 |      14 |
| 2020-03-15 |                            3 |                                4 |       7 |
| 2020-03-16 |                            3 |                                6 |       9 |
| 2020-03-17 |                           10 |                               15 |      25 |
| 2020-03-18 |                            8 |                               17 |      25 |
| 2020-03-19 |                           10 |                               11 |      21 |
| 2020-03-20 |                           11 |                               18 |      29 |
| 2020-03-21 |                            6 |                                9 |      15 |
| 2020-03-22 |                           12 |                               16 |      28 |
| 2020-03-23 |                           13 |                               22 |      35 |
| 2020-03-24 |                           13 |                               14 |      27 |
| 2020-03-25 |                           16 |                               10 |      26 |
| 2020-03-26 |                           10 |                               17 |      27 |
| 2020-03-27 |                           10 |                               12 |      22 |
| 2020-03-28 |                            9 |                               13 |      22 |
| 2020-03-29 |                           16 |                               11 |      27 |
| 2020-03-30 |                           17 |                               24 |      41 |
| 2020-03-31 |                           24 |                               16 |      40 |
| 2020-04-01 |                           14 |                                9 |      23 |
| 2020-04-02 |                           14 |                               17 |      31 |
| 2020-04-03 |                           14 |                               11 |      25 |
| 2020-04-04 |                           11 |                                8 |      19 |
| 2020-04-05 |                           16 |                                5 |      21 |
| 2020-04-06 |                           14 |                               12 |      26 |
| 2020-04-07 |                           20 |                                9 |      29 |
| 2020-04-08 |                           12 |                                4 |      16 |
| 2020-04-09 |                            6 |                                6 |      12 |
| 2020-04-10 |                           11 |                                6 |      17 |
| 2020-04-11 |                            5 |                                6 |      11 |
| 2020-04-12 |                            6 |                                3 |       9 |
| 2020-04-13 |                           13 |                                2 |      15 |
| 2020-04-14 |                           10 |                                4 |      14 |
| 2020-04-15 |                            8 |                                2 |      10 |
| 2020-04-16 |                           14 |                                4 |      18 |
| 2020-04-17 |                            2 |                                3 |       5 |
| 2020-04-18 |                            5 |                                4 |       9 |
| 2020-04-19 |                            4 |                                1 |       5 |
| 2020-04-20 |                            3 |                                4 |       7 |
| 2020-04-21 |                           11 |                                2 |      13 |
| 2020-04-22 |                            3 |                                4 |       7 |
| 2020-04-23 |                            4 |                                4 |       8 |
| 2020-04-24 |                            6 |                                0 |       6 |
| 2020-04-25 |                            2 |                                3 |       5 |
| 2020-04-26 |                            0 |                                1 |       1 |
| 2020-04-27 |                            3 |                                0 |       3 |
| 2020-04-28 |                            5 |                                1 |       6 |
| 2020-04-29 |                            2 |                                1 |       3 |
| 2020-05-01 |                            2 |                                2 |       4 |
| 2020-05-02 |                            3 |                                2 |       5 |
| 2020-05-03 |                            3 |                                0 |       3 |
| 2020-05-04 |                            4 |                                3 |       7 |
| 2020-05-05 |                            1 |                                1 |       2 |
| 2020-05-06 |                            3 |                                0 |       3 |
| 2020-05-07 |                            0 |                                1 |       1 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-11 |                            2 |                                0 |       2 |
| 2020-05-12 |                            2 |                                0 |       2 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-14 |                            2 |                                2 |       4 |
| 2020-05-15 |                            2 |                                0 |       2 |
| 2020-05-17 |                            1 |                                0 |       1 |
| 2020-05-18 |                            0 |                                1 |       1 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-05-21 |                            1 |                                0 |       1 |
| 2020-05-23 |                            1 |                                0 |       1 |
| 2020-05-25 |                            0 |                                1 |       1 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-05-28 |                            1 |                                0 |       1 |
| 2020-06-03 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Scotland |   Wales |   Northern Ireland |
|:-----------|----------:|-----------:|--------:|-------------------:|
| 2020-01-27 |         0 |          0 |       1 |                  0 |
| 2020-02-03 |         5 |          0 |       0 |                  0 |
| 2020-02-05 |         1 |          0 |       0 |                  0 |
| 2020-02-08 |         2 |          0 |       0 |                  0 |
| 2020-02-09 |         2 |          0 |       0 |                  0 |
| 2020-02-13 |         2 |          0 |       0 |                  0 |
| 2020-02-14 |         2 |          0 |       0 |                  0 |
| 2020-02-15 |         2 |          0 |       0 |                  0 |
| 2020-02-16 |         4 |          0 |       0 |                  0 |
| 2020-02-18 |         1 |          0 |       0 |                  0 |
| 2020-02-19 |         1 |          0 |       0 |                  0 |
| 2020-02-20 |         1 |          0 |       0 |                  0 |
| 2020-02-23 |         2 |          0 |       0 |                  0 |
| 2020-02-24 |         4 |          0 |       0 |                  0 |
| 2020-02-25 |         7 |          0 |       0 |                  0 |
| 2020-02-26 |         6 |          0 |       0 |                  0 |
| 2020-02-27 |        19 |          0 |       1 |                  0 |
| 2020-02-28 |        24 |          1 |       0 |                  0 |
| 2020-02-29 |        22 |          0 |       0 |                  0 |
| 2020-03-01 |        51 |          1 |       2 |                  0 |
| 2020-03-02 |        73 |          1 |       0 |                  0 |
| 2020-03-03 |        91 |          2 |       0 |                  0 |
| 2020-03-04 |       103 |          5 |       1 |                  0 |
| 2020-03-05 |        81 |          3 |       0 |                  0 |
| 2020-03-06 |        74 |          7 |       0 |                  0 |
| 2020-03-07 |        44 |          5 |       2 |                  0 |
| 2020-03-08 |        51 |          1 |       2 |                  0 |
| 2020-03-09 |        71 |         12 |       1 |                  0 |
| 2020-03-10 |        92 |          5 |       5 |                  2 |
| 2020-03-11 |       145 |         11 |      10 |                  3 |
| 2020-03-12 |       180 |         32 |       7 |                  0 |
| 2020-03-13 |       104 |         42 |       8 |                  1 |
| 2020-03-14 |        84 |         13 |      10 |                  6 |
| 2020-03-15 |        65 |          8 |      15 |                  0 |
| 2020-03-16 |        79 |         14 |      22 |                  5 |
| 2020-03-17 |       119 |         31 |      32 |                  7 |
| 2020-03-18 |       185 |         24 |      25 |                  6 |
| 2020-03-19 |       151 |         28 |      30 |                  3 |
| 2020-03-20 |       199 |         32 |      12 |                  6 |
| 2020-03-21 |       206 |         35 |       0 |                 13 |
| 2020-03-22 |       199 |         32 |       0 |                  8 |
| 2020-03-23 |       345 |         84 |       1 |                 29 |
| 2020-03-24 |       292 |         87 |      22 |                 23 |
| 2020-03-25 |       290 |         71 |      94 |                 16 |
| 2020-03-26 |       305 |         91 |      18 |                 27 |
| 2020-03-27 |       302 |         87 |      29 |                  7 |
| 2020-03-28 |       309 |         40 |      17 |                 12 |
| 2020-03-29 |       348 |         53 |      22 |                 11 |
| 2020-03-30 |       498 |        120 |      75 |                  6 |
| 2020-03-31 |       455 |         86 |     144 |                  8 |
| 2020-04-01 |       429 |         71 |     136 |                  0 |
| 2020-04-02 |       429 |         48 |      99 |                  1 |
| 2020-04-03 |       422 |         57 |     112 |                  0 |
| 2020-04-04 |       345 |         45 |     139 |                  1 |
| 2020-04-05 |       356 |         50 |      65 |                  0 |
| 2020-04-06 |       439 |         71 |     167 |                 18 |
| 2020-04-07 |       406 |         70 |     185 |                  5 |
| 2020-04-08 |       379 |         43 |     126 |                 14 |
| 2020-04-09 |       359 |         25 |      83 |                  1 |
| 2020-04-10 |       328 |         22 |     120 |                 19 |
| 2020-04-11 |       259 |         46 |      73 |                 14 |
| 2020-04-12 |       211 |         61 |      87 |                 23 |
| 2020-04-13 |       242 |         55 |      77 |                 22 |
| 2020-04-14 |       311 |         50 |     123 |                 11 |
| 2020-04-15 |       310 |         51 |      80 |                 13 |
| 2020-04-16 |       354 |         62 |      73 |                  0 |
| 2020-04-17 |       315 |         24 |      47 |                  6 |
| 2020-04-18 |       235 |         55 |      43 |                  7 |
| 2020-04-19 |       203 |         30 |      36 |                  2 |
| 2020-04-20 |       266 |         68 |      68 |                  2 |
| 2020-04-21 |       220 |        104 |      31 |                 17 |
| 2020-04-22 |       170 |         99 |      18 |                 23 |
| 2020-04-23 |       154 |         76 |      31 |                 11 |
| 2020-04-24 |       110 |         91 |      70 |                  2 |
| 2020-04-25 |        76 |         70 |      40 |                  5 |
| 2020-04-26 |        97 |         49 |      19 |                  2 |
| 2020-04-27 |       164 |         61 |      70 |                  2 |
| 2020-04-28 |       126 |         35 |      51 |                  9 |
| 2020-04-29 |       216 |         23 |      52 |                 11 |
| 2020-04-30 |       183 |         24 |      50 |                 15 |
| 2020-05-01 |       218 |         25 |      46 |                  7 |
| 2020-05-02 |       118 |         13 |      51 |                  2 |
| 2020-05-03 |        94 |         16 |      19 |                  0 |
| 2020-05-04 |       179 |          9 |      40 |                  0 |
| 2020-05-05 |       119 |         17 |      34 |                  0 |
| 2020-05-06 |       143 |         31 |      53 |                  0 |
| 2020-05-07 |       123 |         33 |      53 |                  0 |
| 2020-05-08 |        79 |         25 |      30 |                  0 |
| 2020-05-09 |        65 |         17 |      41 |                  0 |
| 2020-05-10 |        73 |         21 |      38 |                  0 |
| 2020-05-11 |       114 |         16 |      63 |                  0 |
| 2020-05-12 |        77 |         22 |      44 |                  0 |
| 2020-05-13 |        77 |         29 |      53 |                  0 |
| 2020-05-14 |        54 |         47 |      28 |                  0 |
| 2020-05-15 |        60 |         22 |      31 |                  0 |
| 2020-05-16 |        44 |         19 |      14 |                  0 |
| 2020-05-17 |        26 |         16 |      11 |                  0 |
| 2020-05-18 |        69 |         29 |      18 |                  0 |
| 2020-05-19 |        52 |         29 |      27 |                  0 |
| 2020-05-20 |        32 |         15 |      38 |                  0 |
| 2020-05-21 |        39 |         13 |      24 |                  0 |
| 2020-05-22 |        35 |          8 |      24 |                  0 |
| 2020-05-23 |        21 |          7 |      21 |                  0 |
| 2020-05-24 |        20 |          4 |      18 |                  0 |
| 2020-05-25 |        39 |          8 |      16 |                  0 |
| 2020-05-26 |        43 |          3 |      25 |                  0 |
| 2020-05-27 |        30 |          5 |      29 |                  0 |
| 2020-05-28 |        35 |          4 |      19 |                  0 |
| 2020-05-29 |        16 |          1 |      20 |                  0 |
| 2020-05-30 |        11 |          0 |      14 |                  0 |
| 2020-05-31 |        26 |          1 |      10 |                  0 |
| 2020-06-01 |        41 |          3 |       6 |                  0 |
| 2020-06-02 |        34 |         11 |       1 |                  0 |
| 2020-06-03 |        27 |          1 |       7 |                  0 |
| 2020-06-04 |        26 |          7 |       6 |                  0 |
| 2020-06-05 |        13 |          1 |       1 |                  0 |
| 2020-06-06 |         9 |          2 |       1 |                  0 |
| 2020-06-07 |        12 |          1 |       0 |                  0 |
| 2020-06-08 |        14 |          1 |       0 |                  0 |
| 2020-06-09 |         2 |          0 |       0 |                  0 |
| 2020-06-10 |        10 |          0 |       0 |                  0 |
| 2020-06-11 |         1 |          0 |       0 |                  0 |
| 2020-06-12 |         2 |          0 |       0 |                  0 |
| 2020-06-13 |         1 |          0 |       0 |                  0 |
| 2020-06-14 |         2 |          0 |       0 |                  0 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                       | Country          |   Number of sequences | Sequence group   |
|:-----------------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN                     | Scotland         |                    22 | 10-50            |
| ABERDEENSHIRE                | Scotland         |                     5 | 1-10             |
| ANGLESEY                     | Wales            |                    71 | 50-100           |
| ANGUS                        | Scotland         |                    38 | 10-50            |
| ANTRIM                       | Northern Ireland |                   243 | 200-250          |
| ARGYLL AND BUTE              | Scotland         |                     6 | 1-10             |
| ARMAGH                       | Northern Ireland |                    15 | 10-50            |
| BATH AND NORTH EAST SOMERSET | England          |                     0 | 0                |
| BEDFORDSHIRE                 | England          |                   449 | 400-500          |
| BERKSHIRE                    | England          |                    10 | 10-50            |
| BLACKBURN WITH DARWEN        | England          |                     0 | 0                |
| BLACKPOOL                    | England          |                     0 | 0                |
| BLAENAU GWENT                | Wales            |                    60 | 50-100           |
| BOLTON                       | England          |                     0 | 0                |
| BOURNEMOUTH                  | England          |                     0 | 0                |
| BRIDGEND                     | Wales            |                   115 | 100-150          |
| BRIGHTON AND HOVE            | England          |                     0 | 0                |
| BRISTOL                      | England          |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England          |                   400 | 400-500          |
| BURY                         | England          |                     0 | 0                |
| CAERPHILLY                   | Wales            |                   142 | 100-150          |
| CAMBRIDGESHIRE               | England          |                   706 | >500             |
| CARDIFF                      | Wales            |                   563 | >500             |
| CARMARTHENSHIRE              | Wales            |                   144 | 100-150          |
| CENTRAL BEDFORDSHIRE         | England          |                     0 | 0                |
| CEREDIGION                   | Wales            |                    16 | 10-50            |
| CHESHIRE                     | England          |                    43 | 10-50            |
| CLACKMANNANSHIRE             | Scotland         |                     2 | 1-10             |
| CONWY                        | Wales            |                   143 | 100-150          |
| CORNWALL                     | England          |                    23 | 10-50            |
| CUMBRIA                      | England          |                    58 | 50-100           |
| DARLINGTON                   | England          |                     0 | 0                |
| DENBIGHSHIRE                 | Wales            |                   168 | 150-200          |
| DERBY                        | England          |                     0 | 0                |
| DERBYSHIRE                   | England          |                    28 | 10-50            |
| DEVON                        | England          |                   400 | 400-500          |
| DORSET                       | England          |                   183 | 150-200          |
| DOWN                         | Northern Ireland |                   161 | 150-200          |
| DUMFRIES AND GALLOWAY        | Scotland         |                    68 | 50-100           |
| DUNDEE                       | Scotland         |                   140 | 100-150          |
| DURHAM                       | England          |                    21 | 10-50            |
| EAST AYRSHIRE                | Scotland         |                    84 | 50-100           |
| EAST DUNBARTONSHIRE          | Scotland         |                    36 | 10-50            |
| EAST LOTHIAN                 | Scotland         |                    55 | 50-100           |
| EAST RENFREWSHIRE            | Scotland         |                    21 | 10-50            |
| EAST RIDING OF YORKSHIRE     | England          |                    33 | 10-50            |
| EDINBURGH                    | Scotland         |                   456 | 400-500          |
| EILEAN SIAR                  | Scotland         |                     2 | 1-10             |
| ESSEX                        | England          |                  1375 | >500             |
| FALKIRK                      | Scotland         |                    92 | 50-100           |
| FERMANAGH                    | Northern Ireland |                     4 | 1-10             |
| FIFE                         | Scotland         |                    45 | 10-50            |
| FLINTSHIRE                   | Wales            |                   120 | 100-150          |
| GATESHEAD                    | England          |                     0 | 0                |
| GLASGOW                      | Scotland         |                   988 | >500             |
| GLOUCESTERSHIRE              | England          |                   626 | >500             |
| GREATER LONDON               | England          |                  2368 | >500             |
| GUERNSEY                     | Channel_islands  |                    41 | 10-50            |
| GWYNEDD                      | Wales            |                   115 | 100-150          |
| HALTON                       | England          |                     0 | 0                |
| HAMPSHIRE                    | England          |                   226 | 200-250          |
| HARTLEPOOL                   | England          |                     0 | 0                |
| HEREFORDSHIRE                | England          |                    39 | 10-50            |
| HERTFORDSHIRE                | England          |                  1003 | >500             |
| HIGHLAND                     | Scotland         |                     9 | 1-10             |
| INVERCLYDE                   | Scotland         |                    15 | 10-50            |
| ISLE OF WIGHT                | England          |                     0 | 0                |
| ISLES OF SCILLY              | England          |                     0 | 0                |
| JERSEY                       | Channel_islands  |                    77 | 50-100           |
| KENT                         | England          |                    29 | 10-50            |
| KINGSTON UPON HULL           | England          |                     0 | 0                |
| LANCASHIRE                   | England          |                    53 | 50-100           |
| LEICESTER                    | England          |                     0 | 0                |
| LEICESTERSHIRE               | England          |                     5 | 1-10             |
| LINCOLNSHIRE                 | England          |                    37 | 10-50            |
| LONDONDERRY                  | Northern Ireland |                    22 | 10-50            |
| LUTON                        | England          |                     0 | 0                |
| MANCHESTER                   | England          |                    30 | 10-50            |
| MEDWAY                       | England          |                     0 | 0                |
| MERSEYSIDE                   | England          |                   541 | >500             |
| MERTHYR TYDFIL               | Wales            |                    91 | 50-100           |
| MIDDLESBROUGH                | England          |                     0 | 0                |
| MIDLOTHIAN                   | Scotland         |                   134 | 100-150          |
| MILTON KEYNES                | England          |                     0 | 0                |
| MONMOUTHSHIRE                | Wales            |                    77 | 50-100           |
| MORAY                        | Scotland         |                     6 | 1-10             |
| NEATH PORT TALBOT            | Wales            |                   114 | 100-150          |
| NEWPORT                      | Wales            |                   164 | 150-200          |
| NORFOLK                      | England          |                   607 | >500             |
| NORTH AYRSHIRE               | Scotland         |                     5 | 1-10             |
| NORTH LANARKSHIRE            | Scotland         |                   200 | 200-250          |
| NORTH LINCOLNSHIRE           | England          |                     0 | 0                |
| NORTH SOMERSET               | England          |                     0 | 0                |
| NORTH YORKSHIRE              | England          |                    96 | 50-100           |
| NORTHAMPTONSHIRE             | England          |                    24 | 10-50            |
| NORTHUMBERLAND               | England          |                    12 | 10-50            |
| NOTTINGHAM                   | England          |                   662 | >500             |
| NOTTINGHAMSHIRE              | England          |                    58 | 50-100           |
| OLDHAM                       | England          |                     0 | 0                |
| ORKNEY ISLANDS               | Scotland         |                     1 | 1-10             |
| OXFORDSHIRE                  | England          |                    98 | 50-100           |
| PEMBROKESHIRE                | Wales            |                    70 | 50-100           |
| PERTHSHIRE AND KINROSS       | Scotland         |                    57 | 50-100           |
| PETERBOROUGH                 | England          |                     0 | 0                |
| PLYMOUTH                     | England          |                     1 | 1-10             |
| POOLE                        | England          |                     0 | 0                |
| PORTSMOUTH                   | England          |                     0 | 0                |
| POWYS                        | Wales            |                    77 | 50-100           |
| REDCAR AND CLEVELAND         | England          |                     0 | 0                |
| RENFREWSHIRE                 | Scotland         |                   272 | 250-300          |
| RHONDDA, CYNON, TAFF         | Wales            |                     0 | 0                |
| ROCHDALE                     | England          |                     0 | 0                |
| RUTLAND                      | England          |                     0 | 0                |
| SALFORD                      | England          |                     0 | 0                |
| SCOTTISH BORDERS             | Scotland         |                   143 | 100-150          |
| SHETLAND ISLANDS             | Scotland         |                    14 | 10-50            |
| SHROPSHIRE                   | England          |                     6 | 1-10             |
| SOMERSET                     | England          |                   602 | >500             |
| SOUTH AYRSHIRE               | Scotland         |                     3 | 1-10             |
| SOUTH GLOUCESTERSHIRE        | England          |                     0 | 0                |
| SOUTH LANARKSHIRE            | Scotland         |                    28 | 10-50            |
| SOUTH YORKSHIRE              | England          |                  1425 | >500             |
| SOUTHAMPTON                  | England          |                     0 | 0                |
| SOUTHEND-ON-SEA              | England          |                     0 | 0                |
| STAFFORDSHIRE                | England          |                    59 | 50-100           |
| STIRLING                     | Scotland         |                    11 | 10-50            |
| STOCKPORT                    | England          |                     0 | 0                |
| STOCKTON-ON-TEES             | England          |                     0 | 0                |
| STOKE-ON-TRENT               | England          |                     0 | 0                |
| SUFFOLK                      | England          |                   569 | >500             |
| SURREY                       | England          |                    65 | 50-100           |
| SUSSEX                       | England          |                     1 | 1-10             |
| SWANSEA                      | Wales            |                   269 | 250-300          |
| SWINDON                      | England          |                     0 | 0                |
| TAMESIDE                     | England          |                     0 | 0                |
| TELFORD AND WREKIN           | England          |                     0 | 0                |
| THURROCK                     | England          |                     0 | 0                |
| TORBAY                       | England          |                     0 | 0                |
| TORFAEN                      | Wales            |                    91 | 50-100           |
| TRAFFORD                     | England          |                     0 | 0                |
| TYNE AND WEAR                | England          |                   106 | 100-150          |
| TYRONE                       | Northern Ireland |                    19 | 10-50            |
| VALE OF GLAMORGAN            | Wales            |                   187 | 150-200          |
| WARRINGTON                   | England          |                     0 | 0                |
| WARWICKSHIRE                 | England          |                    10 | 10-50            |
| WEST DUNBARTONSHIRE          | Scotland         |                    20 | 10-50            |
| WEST LOTHIAN                 | Scotland         |                   119 | 100-150          |
| WEST MIDLANDS                | England          |                   120 | 100-150          |
| WEST YORKSHIRE               | England          |                    20 | 10-50            |
| WIGAN                        | England          |                     0 | 0                |
| WILTSHIRE                    | England          |                   348 | 300-400          |
| WORCESTERSHIRE               | England          |                    12 | 10-50            |
| WREXHAM                      | Wales            |                   149 | 100-150          |
| YORK                         | England          |                     0 | 0                |

\pagebreak






