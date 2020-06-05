
# UK lineages summary report








This report gives summaries of UK specific lineages for week 2020-05-29. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-24. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
19040 sequences in the UK have been included in this analysis.
5903 lineages have been recorded, 4457 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6130 and the maximum is 9084


Sequences which were replicates or too error-prone were removed from this analysis.



5464 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 242 that remain:
169 are pending extinction, ie last seen three weeks ago.
47 lineages have gone quiet, ie haven't been seen this week.
5 lineages have reactivated.
21 lineages have been continuously circulating.


The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lienages is found in the appendix, along with the raw data for all of the other figures.

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England       | Wales        | Scotland     | Northern Ireland   | Date range     |   Total sequences | Global lineage      |   Time since last sample (days) |   Activity score |
|:---------------|:--------------|:-------------|:-------------|:-------------------|:---------------|------------------:|:--------------------|--------------------------------:|-----------------:|
| UK5            | 1000 (83.47%) | 125 (10.43%) | 70 (5.84%)   | 3 (0.25%)          | Mar-03, May-22 |              1198 | B.1, B.1.1, B.1.1.1 |                               2 |           0.0334 |
| UK2464         | 240 (59.7%)   | 70 (17.41%)  | 92 (22.89%)  | 0 (0%)             | Mar-09, May-12 |               402 | B.1.p11             |                              12 |           0.0133 |
| UK61           | 22 (6.08%)    | 340 (93.92%) | 0 (0%)       | 0 (0%)             | Mar-10, May-01 |               362 | B.3                 |                              23 |           0.0063 |
| UK701          | 244 (80.79%)  | 43 (14.24%)  | 7 (2.32%)    | 8 (2.65%)          | Feb-03, May-10 |               302 | B.1, B.1.p11        |                              14 |           0.023  |
| UK36           | 81 (26.91%)   | 2 (0.66%)    | 216 (71.76%) | 2 (0.66%)          | Mar-18, May-12 |               301 | B.1                 |                              12 |           0.0153 |
| UK19           | 137 (62.84%)  | 81 (37.16%)  | 0 (0%)       | 0 (0%)             | Mar-09, May-10 |               218 | B.1, B.1.44         |                              14 |           0.0204 |
| UK9            | 199 (99.5%)   | 1 (0.5%)     | 0 (0%)       | 0 (0%)             | Mar-09, May-05 |               200 | B.1.13              |                              19 |           0.0151 |
| UK52           | 3 (1.69%)     | 0 (0%)       | 175 (98.31%) | 0 (0%)             | Mar-16, May-12 |               178 | B.1.p73, B.1        |                              12 |           0.0268 |
| UK158          | 25 (14.97%)   | 142 (85.03%) | 0 (0%)       | 0 (0%)             | Mar-20, May-02 |               167 | B.1.1, B.1.1.2      |                              22 |           0.0118 |
| UK4            | 138 (90.79%)  | 13 (8.55%)   | 1 (0.66%)    | 0 (0%)             | Feb-28, May-01 |               152 | B                   |                              23 |           0.0181 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 


![Number of sequences sampled in a lineage by country](UK_full_report/results/figures/UK_report_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](UK_full_report/results/figures/UK_report_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](UK_full_report/results/figures/UK_report_geog_plot_1.png){#geog_plot }




The growth and decline of diversity of lineages over time for each country is shown in the ridge plot in figure four.
This is represented by the Shannon Diversity, calculated using the number of sequences from each country from each lineage.
![Shannon diversity of lineages in each adm1 region](UK_full_report/results/figures/UK_report_diversity_plot_1.png){#diversity_plot }



These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](UK_full_report/results/figures/UK_report_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](UK_full_report/results/figures/UK_report_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](UK_full_report/results/figures/UK_report_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.



![Map showing the number of sequences sampled by adm2 region](UK_full_report/results/figures/UK_report_map_1.png){#map }




There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix



The plot below shows the number of sequences from each country that don't have specific enough location data to plot on the map.




![](UK_full_report/results/figures/UK_report_map_2.png)\


Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England       | Wales        | Scotland     | Northern Ireland   | Date range     |   Total sequences | Global lineage      |   Time since last sample (days) | Activity score   |
|:---------------|:--------------|:-------------|:-------------|:-------------------|:---------------|------------------:|:--------------------|--------------------------------:|:-----------------|
| UK5            | 1000 (83.47%) | 125 (10.43%) | 70 (5.84%)   | 3 (0.25%)          | Mar-03, May-22 |              1198 | B.1, B.1.1, B.1.1.1 |                               2 | 0.0334           |
| UK2464         | 240 (59.7%)   | 70 (17.41%)  | 92 (22.89%)  | 0 (0%)             | Mar-09, May-12 |               402 | B.1.p11             |                              12 | 0.0133           |
| UK61           | 22 (6.08%)    | 340 (93.92%) | 0 (0%)       | 0 (0%)             | Mar-10, May-01 |               362 | B.3                 |                              23 | 0.0063           |
| UK701          | 244 (80.79%)  | 43 (14.24%)  | 7 (2.32%)    | 8 (2.65%)          | Feb-03, May-10 |               302 | B.1, B.1.p11        |                              14 | 0.023            |
| UK36           | 81 (26.91%)   | 2 (0.66%)    | 216 (71.76%) | 2 (0.66%)          | Mar-18, May-12 |               301 | B.1                 |                              12 | 0.0153           |
| UK19           | 137 (62.84%)  | 81 (37.16%)  | 0 (0%)       | 0 (0%)             | Mar-09, May-10 |               218 | B.1, B.1.44         |                              14 | 0.0204           |
| UK9            | 199 (99.5%)   | 1 (0.5%)     | 0 (0%)       | 0 (0%)             | Mar-09, May-05 |               200 | B.1.13              |                              19 | 0.0151           |
| UK52           | 3 (1.69%)     | 0 (0%)       | 175 (98.31%) | 0 (0%)             | Mar-16, May-12 |               178 | B.1.p73, B.1        |                              12 | 0.0268           |
| UK158          | 25 (14.97%)   | 142 (85.03%) | 0 (0%)       | 0 (0%)             | Mar-20, May-02 |               167 | B.1.1, B.1.1.2      |                              22 | 0.0118           |
| UK4            | 138 (90.79%)  | 13 (8.55%)   | 1 (0.66%)    | 0 (0%)             | Feb-28, May-01 |               152 | B                   |                              23 | 0.0181           |
| UK632          | 54 (35.76%)   | 97 (64.24%)  | 0 (0%)       | 0 (0%)             | Mar-23, May-17 |               151 | B.1.1               |                               7 | 0.0524           |
| UK40           | 6 (4.48%)     | 2 (1.49%)    | 126 (94.03%) | 0 (0%)             | Mar-13, May-12 |               134 | B.16, B             |                              12 | 0.0376           |
| UK42           | 10 (8.0%)     | 112 (89.6%)  | 3 (2.4%)     | 0 (0%)             | Mar-07, May-07 |               125 | B.1, B.1.35         |                              17 | 0.0289           |
| UK74           | 21 (17.95%)   | 96 (82.05%)  | 0 (0%)       | 0 (0%)             | Mar-12, May-03 |               117 | B.1                 |                              21 | 0.0213           |
| UK6            | 112 (96.55%)  | 0 (0%)       | 4 (3.45%)    | 0 (0%)             | Mar-06, May-13 |               116 | B.1                 |                              11 | 0.0538           |
| UK494          | 105 (98.13%)  | 1 (0.93%)    | 1 (0.93%)    | 0 (0%)             | Mar-20, May-05 |               107 | B.1.p11             |                              19 | 0.0228           |
| UK63           | 103 (97.17%)  | 2 (1.89%)    | 1 (0.94%)    | 0 (0%)             | Mar-18, May-05 |               106 | B.1.1               |                              19 | 0.0241           |
| UK2200         | 22 (24.44%)   | 33 (36.67%)  | 32 (35.56%)  | 3 (3.33%)          | Feb-28, May-05 |                90 | B.1.5, B.1.5.6      |                              19 | 0.0396           |
| UK66           | 68 (80.0%)    | 0 (0%)       | 16 (18.82%)  | 1 (1.18%)          | Mar-18, May-20 |                85 | B.1.1.8             |                               4 | 0.1875           |
| UK39           | 0 (0%)        | 0 (0%)       | 80 (100.0%)  | 0 (0%)             | Mar-12, May-10 |                80 | A.2                 |                              14 | 0.0533           |
| UK371          | 79 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-12, May-19 |                79 | B.1.1               |                               5 | 0.1744           |
| UK77           | 74 (94.87%)   | 4 (5.13%)    | 0 (0%)       | 0 (0%)             | Mar-11, May-20 |                78 | B.2.4, B.2          |                               4 | 0.2273           |
| UK72           | 18 (23.38%)   | 0 (0%)       | 7 (9.09%)    | 52 (67.53%)        | Mar-11, May-04 |                77 | B.10                |                              20 | 0.0355           |
| UK5322         | 53 (70.67%)   | 16 (21.33%)  | 5 (6.67%)    | 1 (1.33%)          | Mar-23, May-13 |                75 | B.1.1               |                              11 | 0.0627           |
| UK26           | 73 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, May-18 |                73 | B.1.1.3             |                               6 | 0.1412           |
| UK177          | 73 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, May-02 |                73 | B.1.1               |                              22 | 0.0227           |
| UK31           | 71 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, May-08 |                71 | B.1                 |                              16 | 0.0429           |
| UK107          | 68 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-15, Apr-21 |                68 | B.2, B.2.5, B.2.1   |                              33 | 0.0167           |
| UK175          | 0 (0%)        | 0 (0%)       | 67 (100.0%)  | 0 (0%)             | Mar-22, May-04 |                67 | B.1                 |                              20 | 0.0326           |
| UK495          | 2 (2.99%)     | 65 (97.01%)  | 0 (0%)       | 0 (0%)             | Mar-27, May-02 |                67 | B.1.p11             |                              22 | 0.0248           |
| UK89           | 64 (96.97%)   | 2 (3.03%)    | 0 (0%)       | 0 (0%)             | Mar-11, May-17 |                66 | B.1.1.9             |                               7 | 0.1473           |
| UK37           | 60 (96.77%)   | 1 (1.61%)    | 1 (1.61%)    | 0 (0%)             | Mar-17, May-04 |                62 | B.1, B.1.30         |                              20 | 0.0393           |
| UK274          | 59 (95.16%)   | 2 (3.23%)    | 1 (1.61%)    | 0 (0%)             | Mar-06, May-11 |                62 | B.3, B              |                              13 | 0.0832           |
| UK200          | 62 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-08, May-14 |                62 | B.1.p11             |                              10 | 0.059            |
| UK194          | 61 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-19, Apr-24 |                61 | B.1.1               |                              30 | 0.02             |
| UK343          | 60 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, Apr-24 |                60 | B.1                 |                              30 | 0.0153           |
| UK115          | 58 (98.31%)   | 1 (1.69%)    | 0 (0%)       | 0 (0%)             | Mar-15, Apr-20 |                59 | B.2.1               |                              34 | 0.0183           |
| UK233          | 59 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-08, May-13 |                59 | B.1.1               |                              11 | 0.0549           |
| UK51           | 50 (87.72%)   | 0 (0%)       | 6 (10.53%)   | 1 (1.75%)          | Mar-21, May-19 |                57 | B.1.36              |                               5 | 0.2107           |
| UK476          | 56 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, May-06 |                56 | B.1.1               |                              18 | 0.0364           |
| UK225          | 1 (1.79%)     | 2 (3.57%)    | 50 (89.29%)  | 3 (5.36%)          | Mar-14, Apr-10 |                56 | B.2                 |                              44 | 0.0112           |
| UK112          | 55 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-15, May-04 |                55 | B.1.1, B.1.1.p11    |                              20 | 0.0463           |
| UK62           | 52 (94.55%)   | 0 (0%)       | 3 (5.45%)    | 0 (0%)             | Mar-12, Apr-23 |                55 | B.3                 |                              31 | 0.0251           |
| UK12           | 36 (65.45%)   | 0 (0%)       | 18 (32.73%)  | 1 (1.82%)          | Mar-12, May-13 |                55 | B.1.p11             |                              11 | 0.1044           |
| UK204          | 54 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-07, May-12 |                54 | B.1.1               |                              12 | 0.055            |
| UK33           | 50 (96.15%)   | 0 (0%)       | 2 (3.85%)    | 0 (0%)             | Mar-21, May-15 |                52 | B.1.1               |                               9 | 0.1198           |
| UK199          | 52 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-08, May-17 |                52 | B.1.5.5             |                               7 | 0.1092           |
| UK11           | 46 (90.2%)    | 3 (5.88%)    | 2 (3.92%)    | 0 (0%)             | Mar-04, Apr-11 |                51 | B.1                 |                              43 | 0.0177           |
| UK53           | 26 (52.0%)    | 0 (0%)       | 24 (48.0%)   | 0 (0%)             | Mar-26, May-22 |                50 | B.1.1.4             |                               2 | 0.5816           |
| UK3            | 48 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-24, May-10 |                48 | B.1                 |                              14 | 0.1155           |
| UK94           | 47 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-12, Apr-19 |                47 | B.2, B.2.1          |                              35 | 0.0236           |
| UK13           | 46 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, May-13 |                46 | B.1.1               |                              11 | 0.1232           |
| UK28           | 45 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, May-01 |                45 | B.1.1.10            |                              23 | 0.0484           |
| UK760          | 1 (2.27%)     | 0 (0%)       | 0 (0%)       | 43 (97.73%)        | Mar-21, Apr-22 |                44 | B.1.1               |                              32 | 0.0233           |
| UK238          | 44 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-19, May-03 |                44 | B.1.1               |                              21 | 0.0498           |
| UK513          | 43 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-12, Apr-29 |                43 | B.1.p11             |                              25 | 0.0457           |
| UK8            | 38 (90.48%)   | 2 (4.76%)    | 2 (4.76%)    | 0 (0%)             | Mar-03, May-01 |                42 | B                   |                              23 | 0.0626           |
| UK88           | 0 (0%)        | 1 (2.44%)    | 40 (97.56%)  | 0 (0%)             | Mar-22, May-12 |                41 | B.1                 |                              12 | 0.1062           |
| UK187          | 4 (10.0%)     | 26 (65.0%)   | 5 (12.5%)    | 5 (12.5%)          | Mar-23, Apr-28 |                40 | B.1                 |                              26 | 0.0355           |
| UK44           | 0 (0%)        | 0 (0%)       | 39 (97.5%)   | 1 (2.5%)           | Mar-17, May-01 |                40 | B                   |                              23 | 0.0502           |
| UK86           | 16 (41.03%)   | 23 (58.97%)  | 0 (0%)       | 0 (0%)             | Mar-05, Apr-28 |                39 | B.1                 |                              26 | 0.0547           |
| UK2240         | 37 (94.87%)   | 0 (0%)       | 2 (5.13%)    | 0 (0%)             | Mar-01, Apr-19 |                39 | B.1                 |                              35 | 0.0368           |
| UK131          | 34 (87.18%)   | 5 (12.82%)   | 0 (0%)       | 0 (0%)             | Mar-11, Apr-14 |                39 | B, B.15             |                              40 | 0.0224           |
| UK23           | 37 (97.37%)   | 0 (0%)       | 1 (2.63%)    | 0 (0%)             | Mar-12, May-02 |                38 | B.9, B              |                              22 | 0.0627           |
| UK214          | 37 (97.37%)   | 0 (0%)       | 1 (2.63%)    | 0 (0%)             | Mar-14, May-13 |                38 | B.1.1               |                              11 | 0.1474           |
| UK5098         | 1 (2.7%)      | 0 (0%)       | 36 (97.3%)   | 0 (0%)             | Mar-21, May-09 |                37 | B.1.p73, B.2.1      |                              15 | 0.0907           |
| UK128          | 37 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-03, May-23 |                37 | B.1.1               |                               1 | 1.3889           |
| UK346          | 36 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-16, Apr-19 |                36 | B.1, B.1.72         |                              35 | 0.0278           |
| UK283          | 36 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-25, May-04 |                36 | B.1.1               |                              20 | 0.0571           |
| UK179          | 14 (38.89%)   | 22 (61.11%)  | 0 (0%)       | 0 (0%)             | Mar-17, May-01 |                36 | B.1.1.p11           |                              23 | 0.0559           |
| UK57           | 35 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, May-04 |                35 | B.1.1               |                              20 | 0.0662           |
| UK147          | 34 (97.14%)   | 0 (0%)       | 1 (2.86%)    | 0 (0%)             | Apr-04, May-22 |                35 | B.1.1               |                               2 | 0.7059           |
| UK1845         | 30 (88.24%)   | 2 (5.88%)    | 1 (2.94%)    | 1 (2.94%)          | Mar-01, Apr-11 |                34 | B                   |                              43 | 0.0289           |
| UK18           | 34 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-11, May-03 |                34 | B.1.1.7             |                              21 | 0.0765           |
| UK41           | 25 (73.53%)   | 9 (26.47%)   | 0 (0%)       | 0 (0%)             | Mar-01, Apr-27 |                34 | B.1                 |                              27 | 0.064            |
| UK138          | 33 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-26 |                33 | B.2.1               |                              28 | 0.0379           |
| UK64           | 24 (72.73%)   | 9 (27.27%)   | 0 (0%)       | 0 (0%)             | Mar-12, Apr-20 |                33 | B.1                 |                              34 | 0.0358           |
| UK14           | 7 (21.88%)    | 0 (0%)       | 25 (78.12%)  | 0 (0%)             | Mar-04, Apr-27 |                32 | B                   |                              27 | 0.0645           |
| UK167          | 31 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-21 |                31 | B.1.66, B.1         |                               3 | 0.5889           |
| UK119          | 23 (74.19%)   | 7 (22.58%)   | 1 (3.23%)    | 0 (0%)             | Mar-11, Apr-16 |                31 | B.2.5               |                              38 | 0.0316           |
| UK173          | 31 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-16, May-06 |                31 | B                   |                              18 | 0.0944           |
| UK300          | 30 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, May-04 |                30 | B.1.1               |                              20 | 0.0638           |
| UK79           | 30 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, May-05 |                30 | B.1                 |                              19 | 0.0762           |
| UK5672         | 30 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, May-13 |                30 | B.2                 |                              11 | 0.1693           |
| UK43           | 1 (3.45%)     | 0 (0%)       | 28 (96.55%)  | 0 (0%)             | Mar-12, Apr-26 |                29 | A.5                 |                              28 | 0.0574           |
| UK241          | 29 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-22, Apr-16 |                29 | B.1.5.3             |                              38 | 0.0235           |
| UK95           | 28 (96.55%)   | 0 (0%)       | 1 (3.45%)    | 0 (0%)             | Mar-10, May-03 |                29 | B.2.1               |                              21 | 0.0918           |
| UK183          | 28 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, Apr-28 |                28 | B.1.1               |                              26 | 0.0427           |
| UK116          | 28 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-25, Apr-01 |                28 | B.2.1               |                              53 | 0.0252           |
| UK193          | 18 (64.29%)   | 10 (35.71%)  | 0 (0%)       | 0 (0%)             | Apr-01, May-01 |                28 | B.1.1               |                              23 | 0.0483           |
| UK82           | 1 (3.57%)     | 0 (0%)       | 27 (96.43%)  | 0 (0%)             | Mar-25, May-06 |                28 | B.1.1, B.1.1.p11    |                              18 | 0.0864           |
| UK5675         | 25 (89.29%)   | 1 (3.57%)    | 1 (3.57%)    | 1 (3.57%)          | Mar-03, Apr-10 |                28 | B.2                 |                              44 | 0.032            |
| UK45           | 14 (53.85%)   | 10 (38.46%)  | 2 (7.69%)    | 0 (0%)             | Mar-01, Apr-20 |                26 | B.1.1               |                              34 | 0.0588           |
| UK46           | 25 (96.15%)   | 1 (3.85%)    | 0 (0%)       | 0 (0%)             | Mar-02, May-08 |                26 | B.2.1               |                              16 | 0.1675           |
| UK351          | 26 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-13, May-17 |                26 | B.1.1.10, B.1.1     |                               7 | 0.1943           |
| UK565          | 26 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, May-13 |                26 | B.1.1               |                              11 | 0.1564           |
| UK144          | 26 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-05, Apr-07 |                26 | B.2.1               |                              47 | 0.0281           |
| UK109          | 23 (88.46%)   | 1 (3.85%)    | 2 (7.69%)    | 0 (0%)             | Mar-21, May-01 |                26 | B.1.5               |                              23 | 0.0713           |
| UK92           | 25 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-28 |                25 | B.1.1               |                              26 | 0.0577           |
| UK296          | 0 (0%)        | 0 (0%)       | 25 (100.0%)  | 0 (0%)             | Apr-08, May-13 |                25 | B.1.5               |                              11 | 0.1326           |
| UK81           | 24 (96.0%)    | 0 (0%)       | 1 (4.0%)     | 0 (0%)             | Mar-19, Apr-27 |                25 | B.1.1               |                              27 | 0.0602           |
| UK5649         | 22 (88.0%)    | 2 (8.0%)     | 1 (4.0%)     | 0 (0%)             | Mar-15, May-01 |                25 | B.2.6               |                              23 | 0.0851           |
| UK5549         | 21 (87.5%)    | 0 (0%)       | 1 (4.17%)    | 2 (8.33%)          | Mar-04, May-10 |                24 | B.2.2               |                              14 | 0.2081           |
| UK56           | 24 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, May-06 |                24 | B.1.1               |                              18 | 0.1135           |
| UK21           | 0 (0%)        | 0 (0%)       | 24 (100.0%)  | 0 (0%)             | Mar-18, May-23 |                24 | B.1.40              |                               1 | 2.8696           |
| UK473          | 0 (0%)        | 24 (100.0%)  | 0 (0%)       | 0 (0%)             | Apr-02, Apr-29 |                24 | B.1.1               |                              25 | 0.047            |
| UK633          | 0 (0%)        | 24 (100.0%)  | 0 (0%)       | 0 (0%)             | Apr-03, May-01 |                24 | B.1.1.16, B.1.1.p16 |                              23 | 0.0529           |
| UK101          | 22 (95.65%)   | 0 (0%)       | 1 (4.35%)    | 0 (0%)             | Mar-21, Apr-27 |                23 | B.1.5               |                              27 | 0.0623           |
| UK235          | 23 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, May-04 |                23 | B.1.1               |                              20 | 0.1              |
| UK322          | 3 (13.04%)    | 15 (65.22%)  | 5 (21.74%)   | 0 (0%)             | Mar-16, Apr-26 |                23 | B.1, B.1.5          |                              28 | 0.0666           |
| UK156          | 0 (0%)        | 9 (39.13%)   | 14 (60.87%)  | 0 (0%)             | Mar-18, Apr-30 |                23 | B.1.71              |                              24 | 0.0814           |
| UK326          | 23 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-22, May-22 |                23 | B.1.1.10            |                               2 | 1.3864           |
| UK103          | 23 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, May-20 |                23 | B.1.1               |                               4 | 0.6932           |
| UK30           | 22 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-15, May-15 |                22 | B.1.1               |                               9 | 0.3228           |
| UK4507         | 0 (0%)        | 22 (100.0%)  | 0 (0%)       | 0 (0%)             | Apr-14, May-03 |                22 | B.1                 |                              21 | 0.0431           |
| UK279          | 22 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-26, Apr-25 |                22 | B.1.1               |                              29 | 0.0493           |
| UK114          | 22 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-16, Apr-21 |                22 | B.1.1               |                              33 | 0.0519           |
| UK394          | 5 (23.81%)    | 16 (76.19%)  | 0 (0%)       | 0 (0%)             | Mar-24, Apr-24 |                21 | B.1.1.10, B.1.1     |                              30 | 0.0517           |
| UK5309         | 18 (85.71%)   | 3 (14.29%)   | 0 (0%)       | 0 (0%)             | Mar-20, Apr-29 |                21 | B.1.1.10, B.1.1     |                              25 | 0.08             |
| UK5561         | 4 (19.05%)    | 12 (57.14%)  | 4 (19.05%)   | 1 (4.76%)          | Mar-20, Apr-27 |                21 | B.2.2               |                              27 | 0.0704           |
| UK174          | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-19, May-22 |                21 | B.1.5               |                               2 | 1.6              |
| UK113          | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-22, May-19 |                21 | B.1.1               |                               5 | 0.58             |
| UK5668         | 0 (0%)        | 0 (0%)       | 21 (100.0%)  | 0 (0%)             | Mar-13, May-09 |                21 | B.2                 |                              15 | 0.19             |
| UK291          | 20 (95.24%)   | 1 (4.76%)    | 0 (0%)       | 0 (0%)             | Mar-13, Apr-05 |                21 | B.2.1               |                              49 | 0.0235           |
| UK384          | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-14, Apr-02 |                21 | B.2.1               |                              52 | 0.0183           |
| UK135          | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-01, May-14 |                21 | B.1.p11             |                              10 | 0.215            |
| UK293          | 20 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, Apr-28 |                20 | B.1                 |                              26 | 0.0709           |
| UK24           | 20 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, Apr-30 |                20 | B.1.1.10, B.1.1     |                              24 | 0.0943           |
| UK298          | 0 (0%)        | 20 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-27, Apr-29 |                20 | B.1.1               |                              25 | 0.0695           |
| UK75           | 20 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-17, Apr-26 |                20 | B.1, B.1.34         |                              28 | 0.0752           |
| UK87           | 0 (0%)        | 0 (0%)       | 20 (100.0%)  | 0 (0%)             | Mar-13, Apr-20 |                20 | B.1.70              |                              34 | 0.0588           |
| UK514          | 19 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, Apr-13 |                19 | B.1.1               |                              41 | 0.019            |
| UK419          | 19 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, May-02 |                19 | B.1.1               |                              22 | 0.0833           |
| UK150          | 0 (0%)        | 0 (0%)       | 19 (100.0%)  | 0 (0%)             | Mar-21, Apr-22 |                19 | B.1.1.p12           |                              32 | 0.0556           |
| UK403          | 19 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, May-04 |                19 | B.1.1               |                              20 | 0.1167           |
| UK307          | 19 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, May-04 |                19 | B.1.1               |                              20 | 0.1028           |
| UK461          | 0 (0%)        | 0 (0%)       | 19 (100.0%)  | 0 (0%)             | Apr-18, May-19 |                19 | B.1.5               |                               5 | 0.3444           |
| UK134          | 15 (78.95%)   | 0 (0%)       | 4 (21.05%)   | 0 (0%)             | Mar-04, Apr-07 |                19 | B.1                 |                              47 | 0.0402           |
| UK155          | 10 (52.63%)   | 7 (36.84%)   | 1 (5.26%)    | 1 (5.26%)          | Feb-27, May-03 |                19 | B.1                 |                              21 | 0.1746           |
| UK304          | 0 (0%)        | 0 (0%)       | 18 (100.0%)  | 0 (0%)             | Apr-16, May-20 |                18 | B.1.1.14            |                               4 | 0.5              |
| UK5378         | 6 (33.33%)    | 12 (66.67%)  | 0 (0%)       | 0 (0%)             | Mar-23, May-01 |                18 | B.1.1               |                              23 | 0.0997           |
| UK248          | 18 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-08, May-11 |                18 | B.1.1               |                              13 | 0.1493           |
| UK472          | 0 (0%)        | 18 (100.0%)  | 0 (0%)       | 0 (0%)             | Apr-04, Apr-27 |                18 | B.1.1, B.1.1.p11    |                              27 | 0.0501           |
| UK117          | 18 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-28, Apr-04 |                18 | B.2.1               |                              50 | 0.0424           |
| UK502          | 0 (0%)        | 0 (0%)       | 18 (100.0%)  | 0 (0%)             | Mar-06, Mar-30 |                18 | B.1.69              |                              55 | 0.0257           |
| UK143          | 18 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-14, Apr-16 |                18 | B.2.1               |                              38 | 0.0511           |
| UK5084         | 15 (88.24%)   | 2 (11.76%)   | 0 (0%)       | 0 (0%)             | Mar-23, Apr-16 |                17 | B.1, B.1.p11, B.2.1 |                              38 | 0.0395           |
| UK604          | 12 (70.59%)   | 2 (11.76%)   | 3 (17.65%)   | 0 (0%)             | Mar-06, Mar-17 |                17 | B.1.1               |                              68 | 0.0101           |
| UK444          | 16 (94.12%)   | 1 (5.88%)    | 0 (0%)       | 0 (0%)             | Mar-24, May-02 |                17 | B.1.1               |                              22 | 0.1108           |
| UK277          | 3 (17.65%)    | 14 (82.35%)  | 0 (0%)       | 0 (0%)             | Mar-28, May-07 |                17 | B.1.1               |                              17 | 0.1471           |
| UK163          | 11 (64.71%)   | 1 (5.88%)    | 5 (29.41%)   | 0 (0%)             | Mar-27, May-03 |                17 | B.1.1               |                              21 | 0.1101           |
| UK2557         | 7 (41.18%)    | 5 (29.41%)   | 5 (29.41%)   | 0 (0%)             | Mar-22, May-13 |                17 | B.1.p11             |                              11 | 0.2955           |
| UK38           | 10 (58.82%)   | 0 (0%)       | 7 (41.18%)   | 0 (0%)             | Mar-04, May-01 |                17 | B.2.1               |                              23 | 0.1576           |
| UK47           | 11 (68.75%)   | 5 (31.25%)   | 0 (0%)       | 0 (0%)             | Mar-17, Apr-13 |                16 | B.1.1               |                              41 | 0.0439           |
| UK392          | 0 (0%)        | 16 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-25, Apr-12 |                16 | B.1.67              |                              42 | 0.0286           |
| UK195          | 16 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-03 |                16 | B.1.1               |                              21 | 0.1111           |
| UK203          | 12 (75.0%)    | 4 (25.0%)    | 0 (0%)       | 0 (0%)             | Mar-31, May-17 |                16 | B.1.1               |                               7 | 0.4476           |
| UK888          | 16 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-05, May-01 |                16 | B.1.1               |                              23 | 0.0754           |
| UK67           | 16 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-25, May-21 |                16 | B.1.1               |                               3 | 1.2667           |
| UK146          | 14 (93.33%)   | 0 (0%)       | 1 (6.67%)    | 0 (0%)             | Mar-24, May-07 |                15 | B.1.1               |                              17 | 0.1849           |
| UK236          | 14 (93.33%)   | 1 (6.67%)    | 0 (0%)       | 0 (0%)             | Mar-27, Apr-22 |                15 | B.1.1               |                              32 | 0.058            |
| UK5556         | 0 (0%)        | 15 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-18, Apr-16 |                15 | B.2.2               |                              38 | 0.0545           |
| UK2045         | 15 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-17, Apr-29 |                15 | B.1, B              |                              25 | 0.1229           |
| UK397          | 13 (86.67%)   | 0 (0%)       | 2 (13.33%)   | 0 (0%)             | Mar-28, Apr-14 |                15 | B.1.1.13            |                              40 | 0.0304           |
| UK269          | 12 (80.0%)    | 3 (20.0%)    | 0 (0%)       | 0 (0%)             | Mar-31, May-06 |                15 | B.1.1               |                              18 | 0.1429           |
| UK374          | 15 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-01, Apr-20 |                15 | B.1.1               |                              34 | 0.0399           |
| UK264          | 0 (0%)        | 0 (0%)       | 15 (100.0%)  | 0 (0%)             | Mar-29, Apr-22 |                15 | B.1.p11             |                              32 | 0.0536           |
| UK295          | 1 (6.67%)     | 1 (6.67%)    | 3 (20.0%)    | 10 (66.67%)        | Mar-11, Apr-22 |                15 | B                   |                              32 | 0.0938           |
| UK5669         | 0 (0%)        | 0 (0%)       | 15 (100.0%)  | 0 (0%)             | Mar-24, May-07 |                15 | B.2                 |                              17 | 0.1849           |
| UK249          | 14 (93.33%)   | 1 (6.67%)    | 0 (0%)       | 0 (0%)             | Mar-31, Apr-25 |                15 | B.1.1               |                              29 | 0.0616           |
| UK5409         | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-22, Apr-19 |                14 | B.1.1               |                              35 | 0.0615           |
| UK726          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, May-04 |                14 | B.1                 |                              20 | 0.1346           |
| UK370          | 0 (0%)        | 0 (0%)       | 14 (100.0%)  | 0 (0%)             | Apr-06, Apr-27 |                14 | B.1.1.10            |                              27 | 0.0598           |
| UK376          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-08, May-08 |                14 | B.1.1               |                              16 | 0.1442           |
| UK253          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-03, May-03 |                14 | B.1.1               |                              21 | 0.1099           |
| UK303          | 4 (28.57%)    | 10 (71.43%)  | 0 (0%)       | 0 (0%)             | Mar-23, Apr-14 |                14 | B.1.1               |                              40 | 0.0423           |
| UK71           | 13 (92.86%)   | 1 (7.14%)    | 0 (0%)       | 0 (0%)             | Mar-08, Apr-30 |                14 | B                   |                              24 | 0.1699           |
| UK5498         | 13 (92.86%)   | 0 (0%)       | 1 (7.14%)    | 0 (0%)             | Mar-23, Apr-20 |                14 | B.1.1, B.2          |                              34 | 0.0633           |
| UK5180         | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, Apr-24 |                14 | B.1.1.7             |                              30 | 0.0513           |
| UK276          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, May-04 |                14 | B.1.1               |                              20 | 0.1808           |
| UK441          | 11 (78.57%)   | 3 (21.43%)   | 0 (0%)       | 0 (0%)             | Apr-04, May-01 |                14 | B.1.1               |                              23 | 0.0903           |
| UK635          | 5 (35.71%)    | 9 (64.29%)   | 0 (0%)       | 0 (0%)             | Apr-05, May-13 |                14 | B.1.1               |                              11 | 0.2657           |
| UK722          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, May-05 |                14 | B.1.1               |                              19 | 0.1417           |
| UK153          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, Apr-14 |                14 | B.2                 |                              40 | 0.0615           |
| UK254          | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, Apr-14 |                14 | B.1.1               |                              40 | 0.0481           |
| UK186          | 12 (92.31%)   | 1 (7.69%)    | 0 (0%)       | 0 (0%)             | Mar-27, May-15 |                13 | B                   |                               9 | 0.4537           |
| UK637          | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, May-01 |                13 | B.1.1               |                              23 | 0.1232           |
| UK5260         | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-02 |                13 | B.1.1               |                              22 | 0.1288           |
| UK58           | 6 (46.15%)    | 0 (0%)       | 7 (53.85%)   | 0 (0%)             | Mar-12, Apr-09 |                13 | B.1                 |                              45 | 0.0519           |
| UK603          | 0 (0%)        | 13 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-29, Apr-09 |                13 | B.1.1               |                              45 | 0.0204           |
| UK219          | 10 (76.92%)   | 0 (0%)       | 3 (23.08%)   | 0 (0%)             | Mar-26, May-02 |                13 | B.1.1               |                              22 | 0.1402           |
| UK34           | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-15, Apr-02 |                13 | B.4                 |                              52 | 0.0753           |
| UK278          | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-10, May-07 |                13 | B.1.1               |                              17 | 0.1324           |
| UK378          | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-15, Mar-05 |                13 | B.1.1               |                              80 | 0.0198           |
| UK354          | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, Apr-07 |                13 | B.1.1               |                              47 | 0.0355           |
| UK308          | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-09, May-18 |                13 | B.1.1               |                               6 | 0.5417           |
| UK5715         | 12 (92.31%)   | 0 (0%)       | 1 (7.69%)    | 0 (0%)             | Feb-13, Apr-22 |                13 | B.2                 |                              32 | 0.1797           |
| UK558          | 0 (0%)        | 0 (0%)       | 13 (100.0%)  | 0 (0%)             | Apr-24, May-22 |                13 | B.1.5               |                               2 | 1.1667           |
| UK132          | 10 (76.92%)   | 1 (7.69%)    | 2 (15.38%)   | 0 (0%)             | Mar-27, Apr-30 |                13 | B.1                 |                              24 | 0.1181           |
| UK501          | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-03, Apr-22 |                13 | B.1, B              |                              32 | 0.0495           |
| UK126          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-03 |                12 | B.1.1               |                              21 | 0.1515           |
| UK73           | 0 (0%)        | 0 (0%)       | 12 (100.0%)  | 0 (0%)             | Apr-01, May-10 |                12 | B.1.p11             |                              14 | 0.2532           |
| UK694          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-06, Mar-14 |                12 | B                   |                              71 | 0.0102           |
| UK479          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, May-12 |                12 | B.1.1               |                              12 | 0.3258           |
| UK499          | 0 (0%)        | 0 (0%)       | 12 (100.0%)  | 0 (0%)             | Apr-24, May-15 |                12 | B.1.5               |                               9 | 0.2121           |
| UK347          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, Apr-02 |                12 | B.1                 |                              52 | 0.035            |
| UK180          | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)       | 0 (0%)             | Mar-30, May-01 |                12 | B.1.1               |                              23 | 0.1265           |
| UK137          | 2 (16.67%)    | 0 (0%)       | 10 (83.33%)  | 0 (0%)             | Mar-10, Apr-13 |                12 | B.1.1               |                              41 | 0.0754           |
| UK504          | 0 (0%)        | 12 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-30, Apr-13 |                12 | B.1.1               |                              41 | 0.031            |
| UK100          | 1 (8.33%)     | 0 (0%)       | 11 (91.67%)  | 0 (0%)             | Mar-22, May-12 |                12 | B.1.5               |                              12 | 0.3864           |
| UK261          | 0 (0%)        | 0 (0%)       | 12 (100.0%)  | 0 (0%)             | Mar-15, Apr-08 |                12 | A.3                 |                              46 | 0.0474           |
| UK511          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-05, May-06 |                12 | B.1.1               |                              18 | 0.1566           |
| UK168          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-16, Apr-16 |                12 | B.2.1               |                              38 | 0.0742           |
| UK148          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-02, May-13 |                12 | B.1.1               |                              11 | 0.3388           |
| UK202          | 6 (50.0%)     | 5 (41.67%)   | 1 (8.33%)    | 0 (0%)             | Mar-10, May-01 |                12 | B.1.1               |                              23 | 0.2055           |
| UK111          | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)       | 0 (0%)             | Mar-25, May-01 |                12 | B.1.1               |                              23 | 0.1462           |
| UK251          | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)       | 0 (0%)             | Mar-17, May-02 |                12 | B.1.1               |                              22 | 0.1901           |
| UK5685         | 9 (75.0%)     | 1 (8.33%)    | 2 (16.67%)   | 0 (0%)             | Mar-17, Apr-13 |                12 | B.2                 |                              41 | 0.0599           |
| UK329          | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-11, May-09 |                12 | B.1.1               |                              15 | 0.1697           |
| UK160          | 0 (0%)        | 0 (0%)       | 12 (100.0%)  | 0 (0%)             | Mar-31, May-02 |                12 | B.1.1               |                              22 | 0.1322           |
| UK5339         | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-15, Apr-29 |                11 | B.1.1               |                              25 | 0.056            |
| UK266          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-06, Apr-30 |                11 | B.1                 |                              24 | 0.1              |
| UK211          | 0 (0%)        | 11 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-24, Apr-30 |                11 | B.1.5               |                              24 | 0.1542           |
| UK530          | 0 (0%)        | 11 (100.0%)  | 0 (0%)       | 0 (0%)             | Mar-31, Apr-13 |                11 | B.1.1               |                              41 | 0.0317           |
| UK83           | 8 (72.73%)    | 1 (9.09%)    | 2 (18.18%)   | 0 (0%)             | Feb-29, Apr-08 |                11 | B.1.1               |                              46 | 0.0848           |
| UK70           | 8 (72.73%)    | 1 (9.09%)    | 0 (0%)       | 2 (18.18%)         | Mar-06, Apr-16 |                11 | B.2                 |                              38 | 0.1079           |
| UK415          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-19, May-06 |                11 | B.1                 |                              18 | 0.0944           |
| UK161          | 6 (54.55%)    | 5 (45.45%)   | 0 (0%)       | 0 (0%)             | Mar-10, May-03 |                11 | B.1.1               |                              21 | 0.2571           |
| UK759          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, Apr-04 |                11 | B.1.1               |                              50 | 0.014            |
| UK141          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-22, Apr-24 |                11 | B.1.1               |                              30 | 0.11             |
| UK287          | 8 (72.73%)    | 2 (18.18%)   | 1 (9.09%)    | 0 (0%)             | Mar-26, Apr-18 |                11 | B.1                 |                              36 | 0.0639           |
| UK255          | 10 (90.91%)   | 0 (0%)       | 1 (9.09%)    | 0 (0%)             | Mar-26, Apr-20 |                11 | B.1.1               |                              34 | 0.0735           |
| UK240          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-16, Apr-11 |                11 | B.2                 |                              43 | 0.0605           |
| UK268          | 7 (63.64%)    | 4 (36.36%)   | 0 (0%)       | 0 (0%)             | Mar-23, Apr-16 |                11 | B.1.1               |                              38 | 0.0632           |
| UK1018         | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-20, Apr-21 |                11 | B.1.1               |                              33 | 0.003            |
| UK562          | 0 (0%)        | 0 (0%)       | 11 (100.0%)  | 0 (0%)             | Mar-27, Apr-25 |                11 | B.1                 |                              29 | 0.1              |
| UK1539         | 0 (0%)        | 0 (0%)       | 11 (100.0%)  | 0 (0%)             | May-09, May-24 |                11 | B.1.5               |                               0 | active today     |
| UK54           | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, Apr-30 |                11 | B.1.1.10            |                              24 | 0.1792           |
| UK532          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, May-09 |                11 | B.1.1               |                              15 | 0.2333           |
| UK368          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, May-01 |                11 | B.1                 |                              23 | 0.1913           |
| UK428          | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, Apr-06 |                11 | B.2, B.2.1          |                              48 | 0.0354           |
| UK436          | 0 (0%)        | 0 (0%)       | 11 (100.0%)  | 0 (0%)             | Apr-13, May-14 |                11 | B.1.5               |                              10 | 0.31             |
| UK909          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-13, Apr-20 |                10 | B.1                 |                              34 | 0.0229           |
| UK125          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, May-10 |                10 | B.1.1               |                              14 | 0.3492           |
| UK198          | 0 (0%)        | 2 (20.0%)    | 6 (60.0%)    | 2 (20.0%)          | Mar-18, Apr-15 |                10 | B.1.5, A            |                              39 | 0.0798           |
| UK1737         | 9 (90.0%)     | 0 (0%)       | 1 (10.0%)    | 0 (0%)             | Mar-11, Apr-14 |                10 | B.1                 |                              40 | 0.0944           |
| UK22           | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-02, Apr-21 |                10 | B                   |                              33 | 0.1684           |
| UK123          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, May-01 |                10 | B.1                 |                              23 | 0.1884           |
| UK242          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-26, Apr-20 |                10 | B.1.5               |                              34 | 0.0817           |
| UK171          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, Apr-13 |                10 | B.2, B.2.1          |                              41 | 0.084            |
| UK5681         | 0 (0%)        | 10 (100.0%)  | 0 (0%)       | 0 (0%)             | Apr-03, Apr-27 |                10 | B.2                 |                              27 | 0.0988           |
| UK571          | 0 (0%)        | 10 (100.0%)  | 0 (0%)       | 0 (0%)             | Apr-06, Apr-29 |                10 | B.1.1               |                              25 | 0.1022           |
| UK5557         | 8 (80.0%)     | 1 (10.0%)    | 1 (10.0%)    | 0 (0%)             | Mar-10, May-07 |                10 | B.2.2, B.2          |                              17 | 0.3791           |
| UK15           | 6 (60.0%)     | 4 (40.0%)    | 0 (0%)       | 0 (0%)             | Mar-06, Apr-30 |                10 | B.1.1               |                              24 | 0.2546           |
| UK687          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-28, Mar-08 |                10 | B.2, B.2.1          |                              77 | 0.013            |
| UK201          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-03 |                10 | B.1                 |                              21 | 0.1852           |
| UK78           | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-14 |                10 | B.1.5               |                              10 | 0.5111           |
| UK220          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, Apr-22 |                10 | B.1.1               |                              32 | 0.0903           |
| UK178          | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-14, Apr-13 |                10 | B.1.1               |                              41 | 0.0813           |
| UK414          | 0 (0%)        | 0 (0%)       | 10 (100.0%)  | 0 (0%)             | Apr-05, Apr-22 |                10 | B.1.5               |                              32 | 0.059            |
| UK2891         | 3 (30.0%)     | 7 (70.0%)    | 0 (0%)       | 0 (0%)             | Mar-23, Apr-24 |                10 | B.1.1               |                              30 | 0.1185           |
| UK142          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-15, Apr-17 |                 9 | B.2.1               |                              37 | 0.1115           |
| UK471          | 0 (0%)        | 9 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-02, Apr-24 |                 9 | B.1.1               |                              30 | 0.0917           |
| UK91           | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, May-06 |                 9 | B.1.1               |                              18 | 0.2708           |
| UK802          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, Apr-22 |                 9 | B.1                 |                              32 | 0.125            |
| UK564          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-03, May-02 |                 9 | B.1.1               |                              22 | 0.1648           |
| UK5307         | 7 (77.78%)    | 2 (22.22%)   | 0 (0%)       | 0 (0%)             | Mar-08, May-12 |                 9 | B.1.1               |                              12 | 0.6771           |
| UK80           | 3 (33.33%)    | 6 (66.67%)   | 0 (0%)       | 0 (0%)             | Mar-09, Apr-27 |                 9 | B.1.1.p15           |                              27 | 0.2269           |
| UK750          | 0 (0%)        | 9 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-07, Apr-15 |                 9 | B.1                 |                              39 | 0.0256           |
| UK1667         | 3 (33.33%)    | 0 (0%)       | 6 (66.67%)   | 0 (0%)             | Mar-30, May-07 |                 9 | B.1.9, B.1.p9       |                              17 | 0.2794           |
| UK5673         | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-19, May-01 |                 9 | B.2                 |                              23 | 0.2337           |
| UK297          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-09, May-15 |                 9 | B.1.p11             |                               9 | 0.5              |
| UK190          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-01, Mar-30 |                 9 | B.1                 |                              55 | 0.0659           |
| UK306          | 8 (88.89%)    | 0 (0%)       | 1 (11.11%)   | 0 (0%)             | Mar-26, Apr-10 |                 9 | B.1.1               |                              44 | 0.0426           |
| UK5423         | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-23, May-04 |                 9 | B.1.1               |                              20 | 0.0688           |
| UK1548         | 0 (0%)        | 0 (0%)       | 9 (100.0%)   | 0 (0%)             | Apr-13, Apr-24 |                 9 | B.1.5.5, B.1.5      |                              30 | 0.0458           |
| UK237          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, May-16 |                 9 | B.1.1               |                               8 | 0.7188           |
| UK5663         | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-11, Apr-30 |                 9 | B.2                 |                              24 | 0.099            |
| UK129          | 8 (88.89%)    | 1 (11.11%)   | 0 (0%)       | 0 (0%)             | Mar-23, Apr-29 |                 9 | B.1.1               |                              25 | 0.185            |
| UK339          | 2 (22.22%)    | 7 (77.78%)   | 0 (0%)       | 0 (0%)             | Mar-25, Apr-14 |                 9 | B.3                 |                              40 | 0.0625           |
| UK2258         | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-25, May-07 |                 9 | B.1, B.1.5          |                              17 | 0.3162           |
| UK696          | 0 (0%)        | 8 (88.89%)   | 1 (11.11%)   | 0 (0%)             | Apr-10, May-03 |                 9 | B.1, B.1.5          |                              21 | 0.1369           |
| UK541          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-01, May-02 |                 9 | B.1.1               |                              22 | 0.1761           |
| UK569          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-10 |                 9 | B.1.1               |                              44 | 0.0511           |
| UK165          | 4 (44.44%)    | 5 (55.56%)   | 0 (0%)       | 0 (0%)             | Mar-20, Apr-11 |                 9 | B.1.1               |                              43 | 0.064            |
| UK3075         | 1 (11.11%)    | 8 (88.89%)   | 0 (0%)       | 0 (0%)             | Apr-16, May-01 |                 9 | B.1.1               |                              23 | 0.0815           |
| UK5338         | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-29, May-02 |                 9 | B.1.1               |                              22 | 0.017            |
| UK432          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, Apr-09 |                 9 | B.3                 |                              45 | 0.0444           |
| UK312          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-01, Mar-23 |                 9 | B.1.1               |                              62 | 0.0444           |
| UK244          | 8 (88.89%)    | 1 (11.11%)   | 0 (0%)       | 0 (0%)             | Mar-12, Apr-30 |                 9 | B.1.1               |                              24 | 0.2552           |
| UK133          | 2 (22.22%)    | 0 (0%)       | 7 (77.78%)   | 0 (0%)             | Mar-22, Apr-25 |                 9 | B.1                 |                              29 | 0.1466           |
| UK462          | 3 (33.33%)    | 6 (66.67%)   | 0 (0%)       | 0 (0%)             | Apr-01, May-11 |                 9 | B.1                 |                              13 | 0.3846           |
| UK90           | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-06 |                 9 | B.1.1               |                              18 | 0.2639           |
| UK645          | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, Apr-08 |                 9 | B.2.1               |                              46 | 0.0272           |
| UK352          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-11, May-03 |                 8 | B.1.1               |                              21 | 0.1497           |
| UK271          | 1 (12.5%)     | 0 (0%)       | 7 (87.5%)    | 0 (0%)             | Apr-02, Apr-26 |                 8 | B.1                 |                              28 | 0.1224           |
| UK5505         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-21 |                 8 | B.1, B.2            |                              33 | 0.1255           |
| UK223          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-10, Apr-06 |                 8 | B.2.1               |                              48 | 0.0804           |
| UK69           | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | 0 (0%)             | Mar-04, Apr-14 |                 8 | B.2.1               |                              40 | 0.1464           |
| UK3875         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-08, May-12 |                 8 | B.1.1               |                              12 | 0.4048           |
| UK188          | 7 (87.5%)     | 0 (0%)       | 1 (12.5%)    | 0 (0%)             | Mar-07, Apr-15 |                 8 | B.1                 |                              39 | 0.1429           |
| UK358          | 2 (25.0%)     | 6 (75.0%)    | 0 (0%)       | 0 (0%)             | Mar-20, Apr-09 |                 8 | B.2.1               |                              45 | 0.0635           |
| UK5178         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, Apr-17 |                 8 | B.1.1.7             |                              37 | 0.1042           |
| UK1013         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-15, Apr-16 |                 8 | B.1.1               |                              38 | 0.0038           |
| UK5308         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-29, May-01 |                 8 | B.1.1               |                              23 | 0.0124           |
| UK324          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, Apr-21 |                 8 | B.1.1               |                              33 | 0.0909           |
| UK788          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-28, Mar-05 |                 8 | B.4                 |                              80 | 0.0107           |
| UK5174         | 7 (87.5%)     | 0 (0%)       | 0 (0%)       | 1 (12.5%)          | Mar-26, Apr-07 |                 8 | B.1.1.7             |                              47 | 0.0365           |
| UK733          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-10, Apr-22 |                 8 | B.2.1               |                              32 | 0.192            |
| UK311          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, Apr-11 |                 8 | B.1.1               |                              43 | 0.0731           |
| UK739          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-01, Mar-08 |                 8 | B.4                 |                              77 | 0.013            |
| UK480          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, May-19 |                 8 | B.1.1.10, B.1.1     |                               5 | 1.5143           |
| UK5670         | 2 (25.0%)     | 6 (75.0%)    | 0 (0%)       | 0 (0%)             | Mar-22, Apr-30 |                 8 | B.2                 |                              24 | 0.2321           |
| UK341          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-12 |                 8 | B.1                 |                              42 | 0.068            |
| UK574          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, Apr-29 |                 8 | B.1.1               |                              25 | 0.1714           |
| UK182          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-02 |                 8 | B.1.1               |                              22 | 0.2208           |
| UK252          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, Apr-29 |                 8 | B.1.1               |                              25 | 0.1429           |
| UK335          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-25, Apr-15 |                 8 | B.2.1               |                              39 | 0.0769           |
| UK474          | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-01, Apr-16 |                 8 | B.1.1               |                              38 | 0.0564           |
| UK756          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-27, Mar-05 |                 8 | B.1.1               |                              80 | 0.0125           |
| UK2904         | 0 (0%)        | 0 (0%)       | 0 (0%)       | 8 (100.0%)         | Apr-06, Apr-22 |                 8 | B.1.p11             |                              32 | 0.0714           |
| UK367          | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | 0 (0%)             | Mar-25, Apr-27 |                 8 | B.1                 |                              27 | 0.1746           |
| UK65           | 7 (87.5%)     | 0 (0%)       | 1 (12.5%)    | 0 (0%)             | Mar-07, Apr-17 |                 8 | B.1.1               |                              37 | 0.1583           |
| UK318          | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, Apr-10 |                 8 | B                   |                              44 | 0.0682           |
| UK5563         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-11, Apr-22 |                 8 | B.2.2               |                              32 | 0.0491           |
| UK350          | 2 (25.0%)     | 6 (75.0%)    | 0 (0%)       | 0 (0%)             | Mar-31, Apr-20 |                 8 | B.1.1               |                              34 | 0.084            |
| UK5707         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, Apr-14 |                 8 | B.2                 |                              40 | 0.0964           |
| UK1849         | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-11, Apr-29 |                 8 | B.1.1               |                              25 | 0.1029           |
| UK560          | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | 0 (0%)             | Apr-15, Apr-27 |                 7 | B.1.5               |                              27 | 0.0741           |
| UK540          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-09, Apr-22 |                 7 | B.1.1, B.1.1.p15    |                              32 | 0.0677           |
| UK292          | 4 (57.14%)    | 3 (42.86%)   | 0 (0%)       | 0 (0%)             | Mar-21, Apr-13 |                 7 | B.2.1               |                              41 | 0.0935           |
| UK5112         | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, May-08 |                 7 | B.1, B.2.1          |                              16 | 0.5104           |
| UK213          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-18, Apr-17 |                 7 | B.1.1               |                              37 | 0.1351           |
| UK647          | 6 (85.71%)    | 0 (0%)       | 1 (14.29%)   | 0 (0%)             | Mar-17, Mar-27 |                 7 | B.2, B.2.1          |                              58 | 0.0287           |
| UK309          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-01, May-17 |                 7 | B.1.1               |                               7 | 1.0952           |
| UK331          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, May-01 |                 7 | B.1.1               |                              23 | 0.2246           |
| UK49           | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-19, May-11 |                 7 | B.2.1               |                              13 | 0.6795           |
| UK874          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-06, Apr-24 |                 7 | B.1                 |                              30 | 0.1              |
| UK32           | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-11, May-01 |                 7 | B.1.1               |                              23 | 0.3696           |
| UK692          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-04, Apr-03 |                 7 | B.2, B.2.1, B       |                              51 | 0.098            |
| UK5177         | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, Apr-11 |                 7 | B.1.1.7             |                              43 | 0.0581           |
| UK323          | 2 (28.57%)    | 0 (0%)       | 5 (71.43%)   | 0 (0%)             | Mar-31, Apr-21 |                 7 | B.1                 |                              33 | 0.1061           |
| UK629          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-13 |                 7 | B.1                 |                              41 | 0.0854           |
| UK29           | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-09, Apr-30 |                 7 | B.1.1               |                              24 | 0.3611           |
| UK5261         | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-01 |                 7 | B.1.1               |                              23 | 0.2391           |
| UK510          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-02, Apr-16 |                 7 | B.1.1               |                              38 | 0.0614           |
| UK634          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, Apr-18 |                 7 | B.1.1               |                              36 | 0.088            |
| UK451          | 0 (0%)        | 6 (85.71%)   | 1 (14.29%)   | 0 (0%)             | Mar-20, Apr-05 |                 7 | B.2.1               |                              49 | 0.0544           |
| UK536          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Mar-27, Apr-09 |                 7 | B.1.1               |                              45 | 0.0481           |
| UK1174         | 6 (85.71%)    | 0 (0%)       | 1 (14.29%)   | 0 (0%)             | Apr-02, May-13 |                 7 | B.1.1               |                              11 | 0.6212           |
| UK320          | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | 0 (0%)             | Mar-24, Apr-21 |                 7 | B.1, B.1.5          |                              33 | 0.1414           |
| UK612          | 1 (14.29%)    | 6 (85.71%)   | 0 (0%)       | 0 (0%)             | Mar-31, Apr-11 |                 7 | B.2.1               |                              43 | 0.0426           |
| UK487          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, Apr-08 |                 7 | B.1.1               |                              46 | 0.0543           |
| UK572          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-07, May-01 |                 7 | B.1.1               |                              23 | 0.1739           |
| UK330          | 6 (85.71%)    | 1 (14.29%)   | 0 (0%)       | 0 (0%)             | Mar-23, Apr-13 |                 7 | B.1.1               |                              41 | 0.0854           |
| UK1006         | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, Apr-29 |                 7 | B.1.1               |                              25 | 0.1667           |
| UK217          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, May-18 |                 7 | B.1.1               |                               6 | 1.2222           |
| UK206          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-22, Apr-19 |                 7 | B.2.1               |                              35 | 0.1333           |
| UK762          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-11, Apr-30 |                 7 | B.1.1               |                              24 | 0.1319           |
| UK439          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-02, Apr-20 |                 7 | B.1.1               |                              34 | 0.0882           |
| UK390          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, May-01 |                 7 | B.1.5               |                              23 | 0.2536           |
| UK5703         | 6 (85.71%)    | 1 (14.29%)   | 0 (0%)       | 0 (0%)             | Mar-06, Apr-11 |                 7 | B.2                 |                              43 | 0.1395           |
| UK806          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, Apr-27 |                 7 | B.1.1.10            |                              27 | 0.142            |
| UK699          | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | 0 (0%)             | Mar-23, Apr-24 |                 7 | B.1.5               |                              30 | 0.1778           |
| UK317          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-26, Apr-16 |                 7 | B.3                 |                              38 | 0.0921           |
| UK232          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-04, Mar-30 |                 7 | B.1.1               |                              55 | 0.0788           |
| UK913          | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-03, Apr-29 |                 7 | B.1                 |                              25 | 0.1733           |
| UK418          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-03, Apr-20 |                 7 | B.1.1.10            |                              34 | 0.0833           |
| UK282          | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | 0 (0%)             | Mar-23, Apr-22 |                 7 | B.1.1               |                              32 | 0.1562           |
| UK434          | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | 0 (0%)             | Apr-20, May-03 |                 7 | B.1.5               |                              21 | 0.1032           |
| UK563          | 4 (57.14%)    | 0 (0%)       | 3 (42.86%)   | 0 (0%)             | Mar-20, May-12 |                 7 | B.1                 |                              12 | 0.7361           |
| UK554          | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | 0 (0%)             | Apr-23, May-05 |                 7 | B.1.5               |                              19 | 0.1053           |
| UK801          | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-05, May-02 |                 7 | B.1                 |                              22 | 0.2045           |
| UK247          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-04, May-15 |                 6 | B.1.1               |                               9 | 0.9111           |
| UK157          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, May-16 |                 6 | B.1                 |                               8 | 1.2              |
| UK5667         | 3 (50.0%)     | 3 (50.0%)    | 0 (0%)       | 0 (0%)             | Mar-27, Apr-08 |                 6 | B.2                 |                              46 | 0.0522           |
| UK857          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, Mar-29 |                 6 | B.2.1               |                              56 | 0.0179           |
| UK716          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, Apr-08 |                 6 | B.1.1               |                              46 | 0.0348           |
| UK440          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, Apr-13 |                 6 | B.1.1.10            |                              41 | 0.078            |
| UK849          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-16, May-07 |                 6 | B.1.1               |                              17 | 0.2471           |
| UK481          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, Apr-14 |                 6 | B.1.1               |                              40 | 0.075            |
| UK552          | 1 (16.67%)    | 0 (0%)       | 5 (83.33%)   | 0 (0%)             | Mar-18, Mar-30 |                 6 | A.1                 |                              55 | 0.0436           |
| UK735          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, Apr-16 |                 6 | B.3                 |                              38 | 0.1789           |
| UK761          | 0 (0%)        | 6 (100.0%)   | 0 (0%)       | 0 (0%)             | Apr-12, Apr-28 |                 6 | B.1.1               |                              26 | 0.1231           |
| UK870          | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | 0 (0%)             | Mar-18, Mar-25 |                 6 | B.1.5               |                              60 | 0.0233           |
| UK680          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-05, Apr-14 |                 6 | B.1                 |                              40 | 0.045            |
| UK1023         | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-07, Apr-16 |                 6 | B.1.1               |                              38 | 0.0474           |
| UK433          | 3 (50.0%)     | 0 (0%)       | 3 (50.0%)    | 0 (0%)             | Mar-22, Apr-07 |                 6 | B                   |                              47 | 0.0681           |
| UK627          | 0 (0%)        | 6 (100.0%)   | 0 (0%)       | 0 (0%)             | Mar-31, Apr-10 |                 6 | B.1                 |                              44 | 0.0455           |
| UK989          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, Apr-19 |                 6 | B.1                 |                              35 | 0.1657           |
| UK313          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-14 |                 6 | B.1.1               |                              40 | 0.11             |
| UK799          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-01, Mar-07 |                 6 | B.1                 |                              78 | 0.0154           |
| UK654          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Feb-27, Mar-08 |                 6 | B.2.5               |                              77 | 0.026            |
| UK16           | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-16, May-06 |                 6 | B.1.1               |                              18 | 0.2222           |
| UK5486         | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-11, May-20 |                 6 | B.1.1, B.2          |                               4 | 3.5              |
| UK325          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-10, May-01 |                 6 | B.1.1               |                              23 | 0.1826           |
| UK372          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-16, May-05 |                 6 | B.1.1               |                              19 | 0.2              |
| UK1793         | 2 (33.33%)    | 1 (16.67%)   | 3 (50.0%)    | 0 (0%)             | Mar-30, Apr-30 |                 6 | B.1.5               |                              24 | 0.2583           |
| UK263          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, Apr-13 |                 6 | B.1.p11             |                              41 | 0.1171           |
| UK673          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-28, May-18 |                 6 | B.1.1               |                               6 | 1.7              |
| UK497          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-27, Apr-27 |                 6 | A.2                 |                              27 | 0.2296           |
| UK3432         | 1 (16.67%)    | 0 (0%)       | 5 (83.33%)   | 0 (0%)             | Apr-07, May-10 |                 6 | B.1.1               |                              14 | 0.4714           |
| UK93           | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | 0 (0%)             | Mar-21, May-06 |                 6 | B.1.1               |                              18 | 0.5111           |
| UK682          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, Mar-30 |                 6 | B.2, B.2.1          |                              55 | 0.0327           |
| UK2911         | 1 (16.67%)    | 0 (0%)       | 5 (83.33%)   | 0 (0%)             | Mar-31, May-02 |                 6 | B.1.p11             |                              22 | 0.2909           |
| UK489          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-23, Apr-07 |                 6 | B.2.1               |                              47 | 0.0638           |
| UK5352         | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | 0 (0%)             | Apr-22, Apr-27 |                 6 | B.1.1.14            |                              27 | 0.037            |
| UK491          | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)   | 0 (0%)             | Mar-23, Apr-02 |                 6 | B.2.1               |                              52 | 0.0385           |
| UK544          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, Apr-06 |                 6 | B.2.1               |                              48 | 0.0542           |
| UK5570         | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)   | 0 (0%)             | Mar-05, Apr-17 |                 6 | B.2.2               |                              37 | 0.2324           |
| UK110          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-24, Apr-29 |                 6 | B.1                 |                              25 | 0.288            |
| UK68           | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-20, Apr-30 |                 6 | B.1.1               |                              24 | 0.3417           |
| UK596          | 2 (33.33%)    | 0 (0%)       | 4 (66.67%)   | 0 (0%)             | Mar-22, Apr-05 |                 6 | B                   |                              49 | 0.0571           |
| UK102          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-10, Apr-16 |                 6 | B.1                 |                              38 | 0.1947           |
| UK570          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-05, Apr-17 |                 6 | B.1.1               |                              37 | 0.0649           |
| UK746          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-31, Apr-14 |                 6 | B.1.5               |                              40 | 0.07             |
| UK555          | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | 0 (0%)             | Apr-13, Apr-25 |                 6 | B.1.5               |                              29 | 0.0828           |
| UK755          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-06, May-21 |                 6 | B.1.1               |                               3 | 5.0667           |
| UK5581         | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-11, Apr-08 |                 6 | B.2.2               |                              46 | 0.1217           |
| UK27           | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-08, Apr-26 |                 6 | B.1.1               |                              28 | 0.35             |
| UK181          | 3 (50.0%)     | 3 (50.0%)    | 0 (0%)       | 0 (0%)             | Apr-07, Apr-26 |                 6 | B.1.1               |                              28 | 0.1357           |
| UK3126         | 4 (66.67%)    | 0 (0%)       | 0 (0%)       | 2 (33.33%)         | Apr-06, May-04 |                 6 | B.1.1               |                              20 | 0.28             |
| UK270          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, Apr-09 |                 6 | B.3                 |                              45 | 0.12             |
| UK302          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-25, May-03 |                 6 | B.1.1               |                              21 | 0.3714           |
| UK280          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, Apr-15 |                 6 | B.1.1               |                              39 | 0.0821           |
| UK5666         | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-13, Apr-05 |                 6 | B.2                 |                              49 | 0.0939           |
| UK512          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-30, Apr-13 |                 6 | B.1.1               |                              41 | 0.0683           |
| UK517          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-29, Apr-12 |                 6 | B.1.1               |                              42 | 0.0667           |
| UK284          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-02, Apr-25 |                 6 | B.1.1               |                              29 | 0.1586           |
| UK447          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-05, Apr-21 |                 6 | B.1.1               |                              33 | 0.097            |
| UK437          | 3 (50.0%)     | 3 (50.0%)    | 0 (0%)       | 0 (0%)             | Mar-23, Apr-08 |                 6 | B.1                 |                              46 | 0.0696           |
| UK506          | 4 (66.67%)    | 0 (0%)       | 2 (33.33%)   | 0 (0%)             | Mar-20, Apr-03 |                 6 | B.1.1               |                              51 | 0.0549           |
| UK185          | 4 (66.67%)    | 0 (0%)       | 1 (16.67%)   | 1 (16.67%)         | Mar-10, May-15 |                 6 | B.3                 |                               9 | 1.4667           |
| UK435          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-03, Apr-23 |                 6 | B.1.5               |                              31 | 0.129            |
| UK659          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Mar-21, Mar-30 |                 6 | B                   |                              55 | 0.0327           |
| UK542          | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-01, Apr-14 |                 6 | B.1                 |                              40 | 0.065            |
| UK706          | 3 (50.0%)     | 0 (0%)       | 0 (0%)       | 3 (50.0%)          | Mar-26, Apr-11 |                 6 | B.1.1               |                              43 | 0.0744           |
| UK464          | 4 (66.67%)    | 2 (33.33%)   | 0 (0%)       | 0 (0%)             | Mar-25, Apr-19 |                 6 | B.1                 |                              35 | 0.1429           |
| UK1344         | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | 0 (0%)             | Apr-20, May-08 |                 6 | B                   |                              16 | 0.225            |

\pagebreak

**Table S2** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2464 |   UK61 |   UK701 |   UK36 |   UK19 |   UK9 |   UK52 |   UK158 |   UK4 |
|:------------------|------:|---------:|-------:|--------:|-------:|-------:|------:|-------:|--------:|------:|
| 2020-02-02        |     0 |        0 |      0 |       2 |      0 |      0 |     0 |      0 |       0 |     0 |
| 2020-02-09        |     0 |        0 |      0 |       1 |      0 |      0 |     0 |      0 |       0 |     0 |
| 2020-02-23        |     0 |        0 |      0 |      10 |      0 |      0 |     0 |      0 |       0 |     1 |
| 2020-03-01        |     3 |        0 |      0 |      15 |      0 |      0 |     0 |      0 |       0 |     6 |
| 2020-03-08        |    15 |        3 |      2 |       8 |      0 |      2 |     2 |      0 |       0 |     4 |
| 2020-03-15        |    15 |       12 |      2 |      10 |      4 |      3 |     4 |      2 |       1 |     9 |
| 2020-03-22        |    26 |       23 |      8 |      16 |      9 |      7 |     7 |      8 |       2 |    12 |
| 2020-03-29        |    37 |       26 |     15 |      12 |     15 |     17 |    13 |      4 |      15 |    12 |
| 2020-04-05        |    40 |       26 |     21 |      17 |     12 |     15 |    10 |      4 |      17 |     6 |
| 2020-04-12        |    36 |       18 |     13 |      17 |     16 |     14 |     9 |      5 |      10 |     3 |
| 2020-04-19        |    29 |       14 |      4 |       8 |     11 |      8 |     1 |      4 |       5 |     3 |
| 2020-04-26        |    37 |       14 |      6 |      10 |      8 |      9 |     2 |      4 |      11 |     1 |
| 2020-05-03        |    15 |        6 |      0 |       1 |      6 |      1 |     1 |      4 |       0 |     0 |
| 2020-05-10        |     7 |        3 |      0 |       1 |      3 |      1 |     0 |      3 |       0 |     0 |
| 2020-05-17        |     6 |        0 |      0 |       0 |      0 |      0 |     0 |      0 |       0 |     0 |

\pagebreak


**Table S3** Raw data for figure four showing the Shannon diversity per admin1 region over time



| Week       |   England |    Wales |   Scotland |   Northern Ireland |
|:-----------|----------:|---------:|-----------:|-------------------:|
| 2020-01-26 |   0       | -0       |   0        |            0       |
| 2020-02-02 |   1.66746 |  0       |   0        |            0       |
| 2020-02-09 |   2.07944 |  0       |   0        |            0       |
| 2020-02-16 |   1.94591 |  0       |   0        |            0       |
| 2020-02-23 |   3.55301 | -0       |  -0        |            0       |
| 2020-03-01 |   5.04248 |  1.60944 |   2.88924  |            0       |
| 2020-03-08 |   5.97165 |  1.86729 |   4.10615  |            2.36938 |
| 2020-03-15 |   6.04596 |  2.16536 |   4.29377  |            2.28424 |
| 2020-03-22 |   6.41628 |  3.12241 |   4.40799  |            3.55151 |
| 2020-03-29 |   6.42902 |  4.91359 |   4.35062  |            2.8571  |
| 2020-04-05 |   6.14426 |  4.80981 |   4.15876  |            2.79956 |
| 2020-04-12 |   5.7636  |  4.31555 |   3.92759  |            1.86835 |
| 2020-04-19 |   4.95923 |  4.02483 |   3.9971   |            1.86597 |
| 2020-04-26 |   5.01118 |  3.70568 |   3.93112  |            0       |
| 2020-05-03 |   4.40305 |  1.56071 |   3.34264  |            0       |
| 2020-05-10 |   3.78485 |  0       |   3.06272  |            0       |
| 2020-05-17 |   3.01928 |  0       |   2.94776  |            0       |
| 2020-05-24 |   0       |  0       |   0.693147 |            0       |

\pagebreak

**Table S4** Raw data for figure six showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-01-27 |                            1 |                                0 |       1 |
| 2020-02-03 |                            2 |                                1 |       3 |
| 2020-02-05 |                            1 |                                0 |       1 |
| 2020-02-08 |                            2 |                                0 |       2 |
| 2020-02-09 |                            1 |                                1 |       2 |
| 2020-02-13 |                            1 |                                1 |       2 |
| 2020-02-14 |                            1 |                                0 |       1 |
| 2020-02-15 |                            0 |                                2 |       2 |
| 2020-02-16 |                            3 |                                0 |       3 |
| 2020-02-18 |                            1 |                                0 |       1 |
| 2020-02-19 |                            1 |                                0 |       1 |
| 2020-02-20 |                            1 |                                0 |       1 |
| 2020-02-23 |                            2 |                                0 |       2 |
| 2020-02-24 |                            2 |                                1 |       3 |
| 2020-02-25 |                            4 |                                3 |       7 |
| 2020-02-26 |                            6 |                                0 |       6 |
| 2020-02-27 |                            7 |                                3 |      10 |
| 2020-02-28 |                            5 |                                6 |      11 |
| 2020-02-29 |                            9 |                                1 |      10 |
| 2020-03-01 |                           17 |                               10 |      27 |
| 2020-03-02 |                           40 |                                3 |      43 |
| 2020-03-03 |                           34 |                               11 |      45 |
| 2020-03-04 |                           37 |                               15 |      52 |
| 2020-03-05 |                           44 |                                6 |      50 |
| 2020-03-06 |                           39 |                               17 |      56 |
| 2020-03-07 |                           22 |                                7 |      29 |
| 2020-03-08 |                           24 |                               10 |      34 |
| 2020-03-09 |                           40 |                               15 |      55 |
| 2020-03-10 |                           48 |                               23 |      71 |
| 2020-03-11 |                           81 |                               32 |     113 |
| 2020-03-12 |                          113 |                               31 |     144 |
| 2020-03-13 |                           49 |                               31 |      80 |
| 2020-03-14 |                           47 |                               22 |      69 |
| 2020-03-15 |                           34 |                               13 |      47 |
| 2020-03-16 |                           35 |                               23 |      58 |
| 2020-03-17 |                           56 |                               34 |      90 |
| 2020-03-18 |                           76 |                               51 |     127 |
| 2020-03-19 |                           68 |                               37 |     105 |
| 2020-03-20 |                           84 |                               48 |     132 |
| 2020-03-21 |                           88 |                               42 |     130 |
| 2020-03-22 |                           79 |                               33 |     112 |
| 2020-03-23 |                          141 |                               62 |     203 |
| 2020-03-24 |                          139 |                               43 |     182 |
| 2020-03-25 |                          126 |                               48 |     174 |
| 2020-03-26 |                          123 |                               51 |     174 |
| 2020-03-27 |                          110 |                               57 |     167 |
| 2020-03-28 |                          111 |                               38 |     149 |
| 2020-03-29 |                          114 |                               44 |     158 |
| 2020-03-30 |                          179 |                               57 |     236 |
| 2020-03-31 |                          166 |                               53 |     219 |
| 2020-04-01 |                          167 |                               44 |     211 |
| 2020-04-02 |                          136 |                               44 |     180 |
| 2020-04-03 |                          142 |                               39 |     181 |
| 2020-04-04 |                          126 |                               47 |     173 |
| 2020-04-05 |                          115 |                               22 |     137 |
| 2020-04-06 |                          161 |                               24 |     185 |
| 2020-04-07 |                          155 |                               28 |     183 |
| 2020-04-08 |                           97 |                               28 |     125 |
| 2020-04-09 |                           69 |                               14 |      83 |
| 2020-04-10 |                           90 |                               14 |     104 |
| 2020-04-11 |                           67 |                               17 |      84 |
| 2020-04-12 |                           58 |                               10 |      68 |
| 2020-04-13 |                           63 |                               13 |      76 |
| 2020-04-14 |                           70 |                               16 |      86 |
| 2020-04-15 |                           63 |                               14 |      77 |
| 2020-04-16 |                           57 |                               13 |      70 |
| 2020-04-17 |                           53 |                                9 |      62 |
| 2020-04-18 |                           26 |                                5 |      31 |
| 2020-04-19 |                           30 |                                5 |      35 |
| 2020-04-20 |                           39 |                                7 |      46 |
| 2020-04-21 |                           29 |                                2 |      31 |
| 2020-04-22 |                           12 |                                9 |      21 |
| 2020-04-23 |                           14 |                                4 |      18 |
| 2020-04-24 |                           17 |                                4 |      21 |
| 2020-04-25 |                           11 |                                3 |      14 |
| 2020-04-26 |                           11 |                                1 |      12 |
| 2020-04-27 |                           23 |                                3 |      26 |
| 2020-04-28 |                           13 |                                1 |      14 |
| 2020-04-29 |                           18 |                                3 |      21 |
| 2020-04-30 |                           14 |                                3 |      17 |
| 2020-05-01 |                           21 |                                1 |      22 |
| 2020-05-02 |                            4 |                                2 |       6 |
| 2020-05-03 |                            6 |                                1 |       7 |
| 2020-05-04 |                            8 |                                1 |       9 |
| 2020-05-05 |                           10 |                                2 |      12 |
| 2020-05-06 |                            4 |                                0 |       4 |
| 2020-05-07 |                            3 |                                1 |       4 |
| 2020-05-08 |                            6 |                                0 |       6 |
| 2020-05-09 |                            2 |                                3 |       5 |
| 2020-05-10 |                            5 |                                0 |       5 |
| 2020-05-11 |                            6 |                                2 |       8 |
| 2020-05-12 |                            2 |                                0 |       2 |
| 2020-05-13 |                            4 |                                1 |       5 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            4 |                                0 |       4 |
| 2020-05-18 |                            2 |                                0 |       2 |
| 2020-05-19 |                            2 |                                0 |       2 |
| 2020-05-21 |                            3 |                                0 |       3 |
| 2020-05-22 |                            1 |                                0 |       1 |
| 2020-05-23 |                            2 |                                0 |       2 |
| 2020-05-24 |                            1 |                                0 |       1 |

\pagebreak

**Table S5** Raw data for figure seven showing the number of sequences taken over time.


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
| 2020-03-02 |        72 |          1 |       0 |                  0 |
| 2020-03-03 |        91 |          2 |       0 |                  0 |
| 2020-03-04 |       102 |          5 |       1 |                  0 |
| 2020-03-05 |        81 |          3 |       0 |                  0 |
| 2020-03-06 |        74 |          7 |       0 |                  0 |
| 2020-03-07 |        43 |          5 |       2 |                  0 |
| 2020-03-08 |        50 |          1 |       1 |                  0 |
| 2020-03-09 |        71 |         11 |       1 |                  0 |
| 2020-03-10 |        89 |          5 |       5 |                  2 |
| 2020-03-11 |       145 |         11 |      10 |                  3 |
| 2020-03-12 |       179 |         32 |       7 |                  0 |
| 2020-03-13 |       102 |         42 |       8 |                  1 |
| 2020-03-14 |        83 |         13 |      10 |                  6 |
| 2020-03-15 |        64 |          8 |      15 |                  0 |
| 2020-03-16 |        79 |         14 |      22 |                  5 |
| 2020-03-17 |       118 |         31 |      32 |                  7 |
| 2020-03-18 |       184 |         24 |      25 |                  6 |
| 2020-03-19 |       141 |         28 |      30 |                  3 |
| 2020-03-20 |       194 |         32 |      12 |                  6 |
| 2020-03-21 |       203 |         35 |       0 |                 13 |
| 2020-03-22 |       193 |         32 |       0 |                  8 |
| 2020-03-23 |       332 |         84 |       1 |                 29 |
| 2020-03-24 |       285 |         87 |      22 |                 23 |
| 2020-03-25 |       276 |         71 |      93 |                 16 |
| 2020-03-26 |       299 |         91 |       6 |                 27 |
| 2020-03-27 |       292 |         83 |      19 |                  7 |
| 2020-03-28 |       299 |         37 |      14 |                 11 |
| 2020-03-29 |       339 |         46 |      13 |                  5 |
| 2020-03-30 |       481 |         58 |      67 |                  6 |
| 2020-03-31 |       442 |         70 |     119 |                  7 |
| 2020-04-01 |       402 |         71 |     130 |                  0 |
| 2020-04-02 |       413 |         44 |      99 |                  1 |
| 2020-04-03 |       416 |         54 |     111 |                  0 |
| 2020-04-04 |       336 |         45 |     137 |                  1 |
| 2020-04-05 |       346 |         50 |      65 |                  0 |
| 2020-04-06 |       428 |         70 |     152 |                 13 |
| 2020-04-07 |       396 |         70 |     183 |                  0 |
| 2020-04-08 |       344 |         41 |     118 |                  0 |
| 2020-04-09 |       293 |         20 |      78 |                  0 |
| 2020-04-10 |       303 |         18 |     118 |                 11 |
| 2020-04-11 |       256 |         38 |      67 |                  8 |
| 2020-04-12 |       206 |         48 |      86 |                  7 |
| 2020-04-13 |       239 |         53 |      65 |                  5 |
| 2020-04-14 |       309 |         50 |     119 |                  0 |
| 2020-04-15 |       302 |         44 |      79 |                  8 |
| 2020-04-16 |       283 |         48 |      71 |                  0 |
| 2020-04-17 |       213 |         19 |      42 |                  0 |
| 2020-04-18 |       109 |         37 |      36 |                  0 |
| 2020-04-19 |       139 |         30 |      16 |                  1 |
| 2020-04-20 |       151 |         45 |      52 |                  2 |
| 2020-04-21 |       111 |         59 |      14 |                 12 |
| 2020-04-22 |       121 |         63 |       3 |                 14 |
| 2020-04-23 |        82 |         40 |      17 |                  0 |
| 2020-04-24 |        48 |         48 |      53 |                  0 |
| 2020-04-25 |        48 |         34 |      26 |                  0 |
| 2020-04-26 |        77 |         37 |      13 |                  0 |
| 2020-04-27 |       127 |         53 |      63 |                  0 |
| 2020-04-28 |        81 |         31 |      46 |                  0 |
| 2020-04-29 |       163 |         17 |      28 |                  0 |
| 2020-04-30 |       156 |         23 |      35 |                  0 |
| 2020-05-01 |       200 |         23 |      35 |                  0 |
| 2020-05-02 |        98 |         13 |      22 |                  0 |
| 2020-05-03 |        61 |         16 |       6 |                  0 |
| 2020-05-04 |       111 |          8 |       0 |                  0 |
| 2020-05-05 |        68 |         12 |       0 |                  0 |
| 2020-05-06 |        77 |         17 |       0 |                  0 |
| 2020-05-07 |        75 |         30 |       0 |                  0 |
| 2020-05-08 |        41 |         20 |       0 |                  0 |
| 2020-05-09 |        40 |         13 |       0 |                  0 |
| 2020-05-10 |        36 |         17 |       0 |                  0 |
| 2020-05-11 |        66 |         11 |       0 |                  0 |
| 2020-05-12 |        38 |         14 |       0 |                  0 |
| 2020-05-13 |        39 |          8 |       0 |                  0 |
| 2020-05-14 |        14 |          1 |       0 |                  0 |
| 2020-05-15 |        16 |          7 |       0 |                  0 |
| 2020-05-16 |         7 |          1 |       0 |                  0 |
| 2020-05-17 |        10 |          7 |       0 |                  0 |
| 2020-05-18 |        21 |          3 |       0 |                  0 |
| 2020-05-19 |        21 |          8 |       0 |                  0 |
| 2020-05-20 |         7 |          8 |       0 |                  0 |
| 2020-05-21 |         7 |          4 |       0 |                  0 |
| 2020-05-22 |         8 |          2 |       0 |                  0 |
| 2020-05-23 |         2 |          4 |       0 |                  0 |
| 2020-05-24 |         0 |          2 |       0 |                  0 |

\pagebreak

**Table S6** Raw data for the map with the number of sequences assigned to each admin2 region.


| Admin2                       | Country          |   Number of sequences | Sequence group   |
|:-----------------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN                     | Scotland         |                    22 | 10-50            |
| ABERDEENSHIRE                | Scotland         |                     5 | 1-10             |
| ANGLESEY                     | Wales            |                    23 | 10-50            |
| ANGUS                        | Scotland         |                    13 | 10-50            |
| ANTRIM                       | Northern Ireland |                   140 | 100-150          |
| ARGYLL AND BUTE              | Scotland         |                     0 | 0                |
| ARMAGH                       | Northern Ireland |                    12 | 10-50            |
| BATH AND NORTH EAST SOMERSET | England          |                     0 | 0                |
| BEDFORDSHIRE                 | England          |                   417 | 400-500          |
| BERKSHIRE                    | England          |                     7 | 1-10             |
| BLACKBURN WITH DARWEN        | England          |                     0 | 0                |
| BLACKPOOL                    | England          |                     0 | 0                |
| BLAENAU GWENT                | Wales            |                    46 | 10-50            |
| BOLTON                       | England          |                     0 | 0                |
| BOURNEMOUTH                  | England          |                     0 | 0                |
| BRIDGEND                     | Wales            |                    96 | 50-100           |
| BRIGHTON AND HOVE            | England          |                     0 | 0                |
| BRISTOL                      | England          |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England          |                   348 | 300-400          |
| BURY                         | England          |                     0 | 0                |
| CAERPHILLY                   | Wales            |                   108 | 100-150          |
| CAMBRIDGESHIRE               | England          |                   656 | >500             |
| CARDIFF                      | Wales            |                   368 | 300-400          |
| CARMARTHENSHIRE              | Wales            |                    80 | 50-100           |
| CENTRAL BEDFORDSHIRE         | England          |                     0 | 0                |
| CEREDIGION                   | Wales            |                    16 | 10-50            |
| CHESHIRE                     | England          |                    10 | 10-50            |
| CLACKMANNANSHIRE             | Scotland         |                     2 | 1-10             |
| CONWY                        | Wales            |                    57 | 50-100           |
| CORNWALL                     | England          |                    20 | 10-50            |
| CUMBRIA                      | England          |                    31 | 10-50            |
| DARLINGTON                   | England          |                     0 | 0                |
| DENBIGHSHIRE                 | Wales            |                    86 | 50-100           |
| DERBY                        | England          |                     0 | 0                |
| DERBYSHIRE                   | England          |                    25 | 10-50            |
| DEVON                        | England          |                   283 | 250-300          |
| DORSET                       | England          |                   159 | 150-200          |
| DOWN                         | Northern Ireland |                    90 | 50-100           |
| DUMFRIES AND GALLOWAY        | Scotland         |                    54 | 50-100           |
| DUNDEE                       | Scotland         |                    93 | 50-100           |
| DURHAM                       | England          |                     3 | 1-10             |
| EAST AYRSHIRE                | Scotland         |                    75 | 50-100           |
| EAST DUNBARTONSHIRE          | Scotland         |                     0 | 0                |
| EAST LOTHIAN                 | Scotland         |                    54 | 50-100           |
| EAST RENFREWSHIRE            | Scotland         |                     0 | 0                |
| EAST RIDING OF YORKSHIRE     | England          |                    31 | 10-50            |
| EDINBURGH                    | Scotland         |                   412 | 400-500          |
| EILEAN SIAR                  | Scotland         |                     2 | 1-10             |
| ESSEX                        | England          |                  1189 | >500             |
| FALKIRK                      | Scotland         |                    92 | 50-100           |
| FERMANAGH                    | Northern Ireland |                     3 | 1-10             |
| FIFE                         | Scotland         |                    42 | 10-50            |
| FLINTSHIRE                   | Wales            |                    55 | 50-100           |
| GATESHEAD                    | England          |                     0 | 0                |
| GLASGOW                      | Scotland         |                   791 | >500             |
| GLOUCESTERSHIRE              | England          |                   452 | 400-500          |
| GREATER LONDON               | England          |                  2273 | >500             |
| GUERNSEY                     | Channel_islands  |                    41 | 10-50            |
| GWYNEDD                      | Wales            |                    51 | 50-100           |
| HALTON                       | England          |                     0 | 0                |
| HAMPSHIRE                    | England          |                    95 | 50-100           |
| HARTLEPOOL                   | England          |                     0 | 0                |
| HEREFORDSHIRE                | England          |                     4 | 1-10             |
| HERTFORDSHIRE                | England          |                   928 | >500             |
| HIGHLAND                     | Scotland         |                     9 | 1-10             |
| INVERCLYDE                   | Scotland         |                     0 | 0                |
| ISLE OF WIGHT                | England          |                     0 | 0                |
| ISLES OF SCILLY              | England          |                     0 | 0                |
| JERSEY                       | Channel_islands  |                    77 | 50-100           |
| KENT                         | England          |                    28 | 10-50            |
| KINGSTON UPON HULL           | England          |                     0 | 0                |
| LANCASHIRE                   | England          |                     6 | 1-10             |
| LEICESTER                    | England          |                     0 | 0                |
| LEICESTERSHIRE               | England          |                     5 | 1-10             |
| LINCOLNSHIRE                 | England          |                    16 | 10-50            |
| LONDONDERRY                  | Northern Ireland |                    15 | 10-50            |
| LUTON                        | England          |                     0 | 0                |
| MANCHESTER                   | England          |                    30 | 10-50            |
| MEDWAY                       | England          |                     0 | 0                |
| MERSEYSIDE                   | England          |                    59 | 50-100           |
| MERTHYR TYDFIL               | Wales            |                    52 | 50-100           |
| MIDDLESBROUGH                | England          |                     0 | 0                |
| MIDLOTHIAN                   | Scotland         |                   127 | 100-150          |
| MILTON KEYNES                | England          |                     0 | 0                |
| MONMOUTHSHIRE                | Wales            |                    53 | 50-100           |
| MORAY                        | Scotland         |                     0 | 0                |
| NEATH PORT TALBOT            | Wales            |                    94 | 50-100           |
| NEWPORT                      | Wales            |                   121 | 100-150          |
| NORFOLK                      | England          |                   498 | 400-500          |
| NORTH AYRSHIRE               | Scotland         |                     0 | 0                |
| NORTH LANARKSHIRE            | Scotland         |                   158 | 150-200          |
| NORTH LINCOLNSHIRE           | England          |                     0 | 0                |
| NORTH SOMERSET               | England          |                     0 | 0                |
| NORTH YORKSHIRE              | England          |                    53 | 50-100           |
| NORTHAMPTONSHIRE             | England          |                    22 | 10-50            |
| NORTHUMBERLAND               | England          |                     2 | 1-10             |
| NOTTINGHAM                   | England          |                   559 | >500             |
| NOTTINGHAMSHIRE              | England          |                    58 | 50-100           |
| OLDHAM                       | England          |                     0 | 0                |
| ORKNEY ISLANDS               | Scotland         |                     1 | 1-10             |
| OXFORDSHIRE                  | England          |                    97 | 50-100           |
| PEMBROKESHIRE                | Wales            |                    62 | 50-100           |
| PERTHSHIRE AND KINROSS       | Scotland         |                    48 | 10-50            |
| PETERBOROUGH                 | England          |                     0 | 0                |
| PLYMOUTH                     | England          |                     1 | 1-10             |
| POOLE                        | England          |                     0 | 0                |
| PORTSMOUTH                   | England          |                     0 | 0                |
| POWYS                        | Wales            |                    46 | 10-50            |
| REDCAR AND CLEVELAND         | England          |                     0 | 0                |
| RENFREWSHIRE                 | Scotland         |                   209 | 200-250          |
| RHONDDA, CYNON, TAFF         | Wales            |                     0 | 0                |
| ROCHDALE                     | England          |                     0 | 0                |
| RUTLAND                      | England          |                     0 | 0                |
| SALFORD                      | England          |                     0 | 0                |
| SCOTTISH BORDERS             | Scotland         |                   128 | 100-150          |
| SHETLAND ISLANDS             | Scotland         |                    14 | 10-50            |
| SHROPSHIRE                   | England          |                     1 | 1-10             |
| SOMERSET                     | England          |                   338 | 300-400          |
| SOUTH AYRSHIRE               | Scotland         |                     0 | 0                |
| SOUTH GLOUCESTERSHIRE        | England          |                     0 | 0                |
| SOUTH LANARKSHIRE            | Scotland         |                     4 | 1-10             |
| SOUTH YORKSHIRE              | England          |                  1165 | >500             |
| SOUTHAMPTON                  | England          |                     0 | 0                |
| SOUTHEND-ON-SEA              | England          |                     0 | 0                |
| STAFFORDSHIRE                | England          |                    28 | 10-50            |
| STIRLING                     | Scotland         |                     0 | 0                |
| STOCKPORT                    | England          |                     0 | 0                |
| STOCKTON-ON-TEES             | England          |                     0 | 0                |
| STOKE-ON-TRENT               | England          |                     0 | 0                |
| SUFFOLK                      | England          |                   484 | 400-500          |
| SURREY                       | England          |                    60 | 50-100           |
| SUSSEX                       | England          |                     1 | 1-10             |
| SWANSEA                      | Wales            |                   223 | 200-250          |
| SWINDON                      | England          |                     0 | 0                |
| TAMESIDE                     | England          |                     0 | 0                |
| TELFORD AND WREKIN           | England          |                     0 | 0                |
| THURROCK                     | England          |                     0 | 0                |
| TORBAY                       | England          |                     0 | 0                |
| TORFAEN                      | Wales            |                    76 | 50-100           |
| TRAFFORD                     | England          |                     0 | 0                |
| TYNE AND WEAR                | England          |                    38 | 10-50            |
| TYRONE                       | Northern Ireland |                    15 | 10-50            |
| VALE OF GLAMORGAN            | Wales            |                   137 | 100-150          |
| WARRINGTON                   | England          |                     0 | 0                |
| WARWICKSHIRE                 | England          |                    10 | 10-50            |
| WEST DUNBARTONSHIRE          | Scotland         |                     0 | 0                |
| WEST LOTHIAN                 | Scotland         |                    92 | 50-100           |
| WEST MIDLANDS                | England          |                    89 | 50-100           |
| WEST YORKSHIRE               | England          |                    20 | 10-50            |
| WIGAN                        | England          |                     0 | 0                |
| WILTSHIRE                    | England          |                   243 | 200-250          |
| WORCESTERSHIRE               | England          |                     7 | 1-10             |
| WREXHAM                      | Wales            |                    73 | 50-100           |
| YORK                         | England          |                     0 | 0                |

\pagebreak






