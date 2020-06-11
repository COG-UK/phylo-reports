







# UK Lineages report




This report gives summaries of UK specific lineages for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-02. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
20166 sequences in the UK have been included in this analysis.
5928 lineages have been recorded, 4450 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6210 and the maximum is 8985


Sequences which were replicates or too error-prone were removed from this analysis.



5472 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 169 that remain:
120 are pending extinction, ie last seen three weeks ago.
36 lineages have gone quiet, ie haven't been seen this week.
4 lineages have reactivated.
9 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Northern Ireland   | England       | Wales        | Scotland     | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:-------------------|:--------------|:-------------|:-------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 4 (0.3%)           | 1096 (83.35%) | 140 (10.65%) | 75 (5.7%)    | Mar-03, May-31 |              1315 | B.1.1, B.1.1.1   |                               2 | 0.0339           |
| UK2464         | 0 (0%)             | 255 (58.62%)  | 77 (17.7%)   | 103 (23.68%) | Mar-09, May-25 |               435 | B.1.p11          |                               8 | 0.0222           |
| UK61           | 0 (0%)             | 22 (5.57%)    | 373 (94.43%) | 0 (0%)       | Mar-10, May-15 |               395 | B.3              |                              18 | 0.0093           |
| UK36           | 2 (0.6%)           | 83 (25.0%)    | 10 (3.01%)   | 237 (71.39%) | Mar-18, May-21 |               332 | B.1              |                              12 | 0.0161           |
| UK2916         | 9 (2.8%)           | 253 (78.82%)  | 52 (16.2%)   | 7 (2.18%)    | Feb-03, May-10 |               321 | B.1, B.1.p11     |                              23 | 0.0132           |
| UK5098         | 0 (0%)             | 1 (0.41%)     | 0 (0%)       | 240 (99.59%) | Mar-16, May-12 |               241 | B.1.p73          |                              21 | 0.0113           |
| UK158          | 0 (0%)             | 24 (11.06%)   | 193 (88.94%) | 0 (0%)       | Mar-20, May-17 |               217 | B.1.1.2, B.1.1   |                              16 | 0.0168           |
| UK632          | 0 (0%)             | 71 (32.87%)   | 145 (67.13%) | 0 (0%)       | Mar-23, Jun-02 |               216 | B.1.1            |                               0 | active today     |
| UK9            | 0 (0%)             | 201 (99.5%)   | 1 (0.5%)     | 0 (0%)       | Mar-09, May-15 |               202 | B.1.13           |                              18 | 0.0185           |
| UK19           | 0 (0%)             | 93 (49.47%)   | 95 (50.53%)  | 0 (0%)       | Mar-09, May-15 |               188 | B.1, B.1.44      |                              18 | 0.0199           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_geog_plot_1.png){#geog_plot }




The growth and decline of diversity of lineages over time for each country is shown in the ridge plot in figure four.
This is represented by the Shannon Diversity, calculated using the number of sequences from each country from each lineage.



![Shannon diversity of lineages in each adm1 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_diversity_plot_1.png){#diversity_plot }



These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix



The plot below shows the number of sequences from each country that don't have specific enough location data to plot on the map.




![](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/full_report/figures/UK_report_map_2.png)\


Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Northern Ireland   | England       | Wales        | Scotland     | Date range     |   Total sequences | Global lineage      |   Time since last sample (days) | Activity score   |
|:---------------|:-------------------|:--------------|:-------------|:-------------|:---------------|------------------:|:--------------------|--------------------------------:|:-----------------|
| UK5            | 4 (0.3%)           | 1096 (83.35%) | 140 (10.65%) | 75 (5.7%)    | Mar-03, May-31 |              1315 | B.1.1, B.1.1.1      |                               2 | 0.0339           |
| UK2464         | 0 (0%)             | 255 (58.62%)  | 77 (17.7%)   | 103 (23.68%) | Mar-09, May-25 |               435 | B.1.p11             |                               8 | 0.0222           |
| UK61           | 0 (0%)             | 22 (5.57%)    | 373 (94.43%) | 0 (0%)       | Mar-10, May-15 |               395 | B.3                 |                              18 | 0.0093           |
| UK36           | 2 (0.6%)           | 83 (25.0%)    | 10 (3.01%)   | 237 (71.39%) | Mar-18, May-21 |               332 | B.1                 |                              12 | 0.0161           |
| UK2916         | 9 (2.8%)           | 253 (78.82%)  | 52 (16.2%)   | 7 (2.18%)    | Feb-03, May-10 |               321 | B.1, B.1.p11        |                              23 | 0.0132           |
| UK5098         | 0 (0%)             | 1 (0.41%)     | 0 (0%)       | 240 (99.59%) | Mar-16, May-12 |               241 | B.1.p73             |                              21 | 0.0113           |
| UK158          | 0 (0%)             | 24 (11.06%)   | 193 (88.94%) | 0 (0%)       | Mar-20, May-17 |               217 | B.1.1.2, B.1.1      |                              16 | 0.0168           |
| UK632          | 0 (0%)             | 71 (32.87%)   | 145 (67.13%) | 0 (0%)       | Mar-23, Jun-02 |               216 | B.1.1               |                               0 | active today     |
| UK9            | 0 (0%)             | 201 (99.5%)   | 1 (0.5%)     | 0 (0%)       | Mar-09, May-15 |               202 | B.1.13              |                              18 | 0.0185           |
| UK19           | 0 (0%)             | 93 (49.47%)   | 95 (50.53%)  | 0 (0%)       | Mar-09, May-15 |               188 | B.1, B.1.44         |                              18 | 0.0199           |
| UK4            | 1 (0.53%)          | 169 (90.37%)  | 15 (8.02%)   | 2 (1.07%)    | Feb-28, May-18 |               187 | B                   |                              15 | 0.0287           |
| UK3021         | 0 (0%)             | 23 (14.2%)    | 139 (85.8%)  | 0 (0%)       | Mar-12, May-16 |               162 | B.1                 |                              17 | 0.0237           |
| UK42           | 0 (0%)             | 10 (6.76%)    | 135 (91.22%) | 3 (2.03%)    | Mar-07, May-16 |               148 | B.1, B.1.35         |                              17 | 0.028            |
| UK40           | 0 (0%)             | 6 (4.2%)      | 2 (1.4%)     | 135 (94.41%) | Mar-13, May-12 |               143 | B, B.16             |                              21 | 0.0201           |
| UK2913         | 0 (0%)             | 99 (75.57%)   | 29 (22.14%)  | 3 (2.29%)    | Mar-10, May-12 |               131 | B.1.p11             |                              21 | 0.0231           |
| UK494          | 0 (0%)             | 106 (97.25%)  | 1 (0.92%)    | 2 (1.83%)    | Mar-20, May-05 |               109 | B.1.p11             |                              28 | 0.0152           |
| UK6            | 0 (0%)             | 94 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-17, May-13 |                94 | B.1                 |                              20 | 0.0306           |
| UK2200         | 3 (3.26%)          | 22 (23.91%)   | 34 (36.96%)  | 33 (35.87%)  | Feb-28, May-05 |                92 | B.1.5.6, B.1.5      |                              28 | 0.0263           |
| UK2735         | 7 (7.69%)          | 57 (62.64%)   | 6 (6.59%)    | 21 (23.08%)  | Mar-18, May-15 |                91 | B.1.1               |                              18 | 0.0358           |
| UK63           | 0 (0%)             | 90 (98.9%)    | 1 (1.1%)     | 0 (0%)       | Mar-18, May-05 |                91 | B.1.1               |                              28 | 0.019            |
| UK39           | 0 (0%)             | 0 (0%)        | 0 (0%)       | 86 (100.0%)  | Mar-12, May-10 |                86 | A.2                 |                              23 | 0.0302           |
| UK66           | 1 (1.18%)          | 68 (80.0%)    | 0 (0%)       | 16 (18.82%)  | Mar-18, May-20 |                85 | B.1.1.8             |                              13 | 0.0577           |
| UK72           | 55 (67.07%)        | 20 (24.39%)   | 0 (0%)       | 7 (8.54%)    | Mar-11, May-04 |                82 | B.10                |                              29 | 0.023            |
| UK177          | 0 (0%)             | 79 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-27, May-12 |                79 | B.1.1               |                              21 | 0.0281           |
| UK77           | 0 (0%)             | 74 (93.67%)   | 5 (6.33%)    | 0 (0%)       | Mar-11, May-20 |                79 | B.2.4, B.2          |                              13 | 0.069            |
| UK371          | 0 (0%)             | 77 (98.72%)   | 0 (0%)       | 1 (1.28%)    | Mar-12, May-19 |                78 | B.1.1               |                              14 | 0.0631           |
| UK339          | 1 (1.32%)          | 59 (77.63%)   | 13 (17.11%)  | 3 (3.95%)    | Feb-23, Apr-16 |                76 | B.3                 |                              47 | 0.015            |
| UK200          | 0 (0%)             | 76 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-08, May-18 |                76 | B.1.p11             |                              15 | 0.0356           |
| UK89           | 0 (0%)             | 72 (96.0%)    | 3 (4.0%)     | 0 (0%)       | Mar-11, May-28 |                75 | B.1.1.9             |                               5 | 0.2108           |
| UK26           | 0 (0%)             | 74 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-18, May-20 |                74 | B.1.1.3             |                              13 | 0.0664           |
| UK107          | 0 (0%)             | 68 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-15, Apr-21 |                68 | B.2.5, B.2, B.2.1   |                              42 | 0.0131           |
| UK274          | 0 (0%)             | 62 (95.38%)   | 2 (3.08%)    | 1 (1.54%)    | Mar-06, May-21 |                65 | B, B.3              |                              12 | 0.099            |
| UK51           | 1 (1.56%)          | 57 (89.06%)   | 0 (0%)       | 6 (9.38%)    | Mar-21, May-26 |                64 | B.1.36              |                               7 | 0.1497           |
| UK343          | 0 (0%)             | 64 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-28, May-15 |                64 | B.1                 |                              18 | 0.0423           |
| UK194          | 0 (0%)             | 64 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-19, Apr-24 |                64 | B.1.1               |                              39 | 0.0147           |
| UK37           | 0 (0%)             | 60 (96.77%)   | 1 (1.61%)    | 1 (1.61%)    | Mar-17, May-04 |                62 | B.1, B.1.30         |                              29 | 0.0271           |
| UK495          | 0 (0%)             | 2 (3.33%)     | 58 (96.67%)  | 0 (0%)       | Mar-27, May-14 |                60 | B.1.p11             |                              19 | 0.0428           |
| UK204          | 0 (0%)             | 60 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-07, May-12 |                60 | B.1.1               |                              21 | 0.0282           |
| UK199          | 0 (0%)             | 59 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-08, May-21 |                59 | B.1.5.5             |                              12 | 0.0618           |
| UK115          | 0 (0%)             | 58 (98.31%)   | 1 (1.69%)    | 0 (0%)       | Mar-15, Apr-20 |                59 | B.2.1               |                              43 | 0.0144           |
| UK225          | 3 (5.26%)          | 1 (1.75%)     | 2 (3.51%)    | 51 (89.47%)  | Mar-14, Apr-10 |                57 | B.2                 |                              53 | 0.0091           |
| UK112          | 0 (0%)             | 56 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-15, May-04 |                56 | B.1.1, B.1.1.p11    |                              29 | 0.0313           |
| UK476          | 0 (0%)             | 56 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-31, May-06 |                56 | B.1.1               |                              27 | 0.0242           |
| UK53           | 0 (0%)             | 27 (49.09%)   | 0 (0%)       | 28 (50.91%)  | Mar-26, May-22 |                55 | B.1.1.4             |                              11 | 0.096            |
| UK214          | 1 (1.85%)          | 52 (96.3%)    | 0 (0%)       | 1 (1.85%)    | Mar-06, May-21 |                54 | B.1.1               |                              12 | 0.1195           |
| UK86           | 0 (0%)             | 16 (30.77%)   | 36 (69.23%)  | 0 (0%)       | Mar-05, May-14 |                52 | B.1                 |                              19 | 0.0722           |
| UK56           | 0 (0%)             | 52 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-20, Jun-02 |                52 | B.1.1               |                               0 | active today     |
| UK3            | 0 (0%)             | 49 (100.0%)   | 0 (0%)       | 0 (0%)       | Feb-24, May-25 |                49 | B.1                 |                               8 | 0.237            |
| UK88           | 0 (0%)             | 0 (0%)        | 1 (2.08%)    | 47 (97.92%)  | Mar-22, May-12 |                48 | B.1                 |                              21 | 0.0517           |
| UK44           | 1 (2.13%)          | 0 (0%)        | 0 (0%)       | 46 (97.87%)  | Mar-17, May-01 |                47 | B                   |                              32 | 0.0306           |
| UK238          | 0 (0%)             | 47 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-19, May-07 |                47 | B.1.1               |                              26 | 0.041            |
| UK13           | 0 (0%)             | 47 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-13, May-13 |                47 | B.1.1               |                              20 | 0.0663           |
| UK94           | 0 (0%)             | 47 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-12, Apr-19 |                47 | B.2, B.2.1          |                              44 | 0.0188           |
| UK28           | 0 (0%)             | 45 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-13, May-01 |                45 | B.1.1.10            |                              32 | 0.0348           |
| UK187          | 5 (11.36%)         | 4 (9.09%)     | 28 (63.64%)  | 7 (15.91%)   | Mar-23, Apr-28 |                44 | B.1                 |                              35 | 0.0239           |
| UK4507         | 0 (0%)             | 0 (0%)        | 44 (100.0%)  | 0 (0%)       | Apr-14, May-14 |                44 | B.1                 |                              19 | 0.0367           |
| UK5672         | 0 (0%)             | 43 (97.73%)   | 1 (2.27%)    | 0 (0%)       | Mar-19, May-13 |                44 | B.1.1, B.2          |                              20 | 0.064            |
| UK5322         | 0 (0%)             | 3 (6.98%)     | 35 (81.4%)   | 5 (11.63%)   | Mar-23, May-15 |                43 | B.1.1               |                              18 | 0.0701           |
| UK513          | 0 (0%)             | 43 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-12, Apr-29 |                43 | B.1.p11             |                              34 | 0.0336           |
| UK760          | 43 (100.0%)        | 0 (0%)        | 0 (0%)       | 0 (0%)       | Mar-21, Apr-22 |                43 | B.1.1               |                              41 | 0.0186           |
| UK8            | 0 (0%)             | 38 (90.48%)   | 2 (4.76%)    | 2 (4.76%)    | Mar-03, May-01 |                42 | B                   |                              32 | 0.045            |
| UK62           | 0 (0%)             | 38 (92.68%)   | 0 (0%)       | 3 (7.32%)    | Mar-12, Apr-23 |                41 | B.3                 |                              40 | 0.0262           |
| UK233          | 0 (0%)             | 41 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-08, May-21 |                41 | B.1.1               |                              12 | 0.0896           |
| UK128          | 0 (0%)             | 40 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-03, May-27 |                40 | B.1.1               |                               6 | 0.2308           |
| UK82           | 0 (0%)             | 1 (2.5%)      | 0 (0%)       | 39 (97.5%)   | Mar-25, May-13 |                40 | B.1.1, B.1.1.p11    |                              20 | 0.0628           |
| UK131          | 0 (0%)             | 34 (87.18%)   | 5 (12.82%)   | 0 (0%)       | Mar-11, Apr-14 |                39 | B, B.15             |                              49 | 0.0183           |
| UK23           | 0 (0%)             | 37 (97.37%)   | 0 (0%)       | 1 (2.63%)    | Mar-12, May-02 |                38 | B, B.9              |                              31 | 0.0445           |
| UK179          | 0 (0%)             | 14 (36.84%)   | 24 (63.16%)  | 0 (0%)       | Mar-17, May-07 |                38 | B.1.1.p11           |                              26 | 0.053            |
| UK3019         | 0 (0%)             | 33 (89.19%)   | 0 (0%)       | 4 (10.81%)   | Mar-06, May-07 |                37 | B.1                 |                              26 | 0.0662           |
| UK31           | 0 (0%)             | 37 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-21, May-06 |                37 | B.1                 |                              27 | 0.0473           |
| UK64           | 0 (0%)             | 25 (67.57%)   | 12 (32.43%)  | 0 (0%)       | Mar-12, May-05 |                37 | B.1                 |                              28 | 0.0536           |
| UK346          | 0 (0%)             | 36 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-16, Apr-19 |                36 | B.1, B.1.72         |                              44 | 0.0221           |
| UK147          | 0 (0%)             | 36 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-04, May-26 |                36 | B.1.1               |                               7 | 0.2122           |
| UK190          | 0 (0%)             | 36 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-01, Apr-19 |                36 | B.1                 |                              44 | 0.0318           |
| UK12           | 1 (2.78%)          | 35 (97.22%)   | 0 (0%)       | 0 (0%)       | Mar-12, May-07 |                36 | B.1.p11             |                              26 | 0.0615           |
| UK276          | 0 (0%)             | 36 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-18, May-01 |                36 | B.1.1               |                              32 | 0.0393           |
| UK18           | 0 (0%)             | 35 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-11, May-27 |                35 | B.1.1.7             |                               6 | 0.3775           |
| UK283          | 0 (0%)             | 35 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-25, May-04 |                35 | B.1.1               |                              29 | 0.0406           |
| UK3035         | 0 (0%)             | 35 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-24, May-18 |                35 | B.1                 |                              15 | 0.1078           |
| UK5660         | 0 (0%)             | 33 (97.06%)   | 0 (0%)       | 1 (2.94%)    | Mar-13, May-10 |                34 | B.1.1, B.2          |                              23 | 0.0764           |
| UK138          | 0 (0%)             | 33 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-23, Apr-26 |                33 | B.2.1               |                              37 | 0.0287           |
| UK173          | 0 (0%)             | 32 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-16, May-19 |                32 | B                   |                              14 | 0.1475           |
| UK119          | 0 (0%)             | 24 (75.0%)    | 7 (21.88%)   | 1 (3.12%)    | Mar-11, Apr-16 |                32 | B.2.5               |                              47 | 0.0247           |
| UK95           | 0 (0%)             | 30 (96.77%)   | 0 (0%)       | 1 (3.23%)    | Mar-10, May-07 |                31 | B.2.1               |                              26 | 0.0744           |
| UK167          | 0 (0%)             | 31 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-21 |                31 | B.1.66, B.1         |                              12 | 0.1472           |
| UK79           | 0 (0%)             | 30 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-24, May-05 |                30 | B.1                 |                              28 | 0.0517           |
| UK5675         | 1 (3.45%)          | 25 (86.21%)   | 2 (6.9%)     | 1 (3.45%)    | Mar-03, May-06 |                29 | B.1.1, B.2          |                              27 | 0.0847           |
| UK43           | 0 (0%)             | 1 (3.45%)     | 0 (0%)       | 28 (96.55%)  | Mar-12, Apr-26 |                29 | A.5                 |                              37 | 0.0434           |
| UK635          | 0 (0%)             | 5 (17.24%)    | 24 (82.76%)  | 0 (0%)       | Apr-05, May-25 |                29 | B.1.1               |                               8 | 0.2232           |
| UK394          | 0 (0%)             | 6 (20.69%)    | 23 (79.31%)  | 0 (0%)       | Mar-17, May-24 |                29 | B.1.1               |                               9 | 0.2698           |
| UK5741         | 0 (0%)             | 27 (93.1%)    | 2 (6.9%)     | 0 (0%)       | Mar-01, Apr-19 |                29 | B.1, B.2            |                              44 | 0.0398           |
| UK633          | 0 (0%)             | 0 (0%)        | 29 (100.0%)  | 0 (0%)       | Apr-03, May-11 |                29 | B.1.1.16, B.1.1.p16 |                              22 | 0.0617           |
| UK298          | 0 (0%)             | 0 (0%)        | 29 (100.0%)  | 0 (0%)       | Mar-27, May-15 |                29 | B.1.1               |                              18 | 0.0972           |
| UK116          | 0 (0%)             | 28 (100.0%)   | 0 (0%)       | 0 (0%)       | Feb-25, Apr-01 |                28 | B.2.1               |                              62 | 0.0215           |
| UK113          | 0 (0%)             | 28 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-22, May-30 |                28 | B.1.1               |                               3 | 0.8519           |
| UK241          | 0 (0%)             | 28 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-22, Apr-16 |                28 | B.1.5.3             |                              47 | 0.0197           |
| UK14           | 0 (0%)             | 2 (7.14%)     | 0 (0%)       | 26 (92.86%)  | Mar-12, Apr-27 |                28 | B                   |                              36 | 0.0473           |
| UK248          | 0 (0%)             | 24 (88.89%)   | 3 (11.11%)   | 0 (0%)       | Apr-08, May-16 |                27 | B.1.1               |                              17 | 0.086            |
| UK304          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 27 (100.0%)  | Apr-16, May-26 |                27 | B.1.1.14            |                               7 | 0.2198           |
| UK300          | 0 (0%)             | 27 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-28, May-04 |                27 | B.1.1               |                              29 | 0.0491           |
| UK351          | 0 (0%)             | 27 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-13, May-21 |                27 | B.1.1, B.1.1.10     |                              12 | 0.1218           |
| UK5649         | 0 (0%)             | 23 (88.46%)   | 2 (7.69%)    | 1 (3.85%)    | Mar-15, May-11 |                26 | B.1.1, B.2.6        |                              22 | 0.1036           |
| UK183          | 0 (0%)             | 26 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, Apr-23 |                26 | B.1.1               |                              40 | 0.025            |
| UK109          | 0 (0%)             | 23 (88.46%)   | 1 (3.85%)    | 2 (7.69%)    | Mar-21, May-01 |                26 | B.1.5               |                              32 | 0.0512           |
| UK5668         | 0 (0%)             | 1 (3.85%)     | 0 (0%)       | 25 (96.15%)  | Mar-13, May-09 |                26 | B.1.1, B.2          |                              24 | 0.095            |
| UK5549         | 2 (7.69%)          | 22 (84.62%)   | 1 (3.85%)    | 1 (3.85%)    | Mar-04, May-18 |                26 | B.2.2               |                              15 | 0.2              |
| UK565          | 0 (0%)             | 26 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-31, May-13 |                26 | B.1.1               |                              20 | 0.086            |
| UK144          | 0 (0%)             | 26 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-05, Apr-07 |                26 | B.2.1               |                              56 | 0.0236           |
| UK81           | 0 (0%)             | 24 (96.0%)    | 0 (0%)       | 1 (4.0%)     | Mar-19, Apr-27 |                25 | B.1.1               |                              36 | 0.0451           |
| UK33           | 0 (0%)             | 25 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-30, May-12 |                25 | B.1.1               |                              21 | 0.0853           |
| UK57           | 0 (0%)             | 25 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-05, Apr-28 |                25 | B.1.1               |                              35 | 0.0274           |
| UK296          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 25 (100.0%)  | Apr-08, May-13 |                25 | B.1.5               |                              20 | 0.0729           |
| UK235          | 0 (0%)             | 25 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-21, May-04 |                25 | B.1.1               |                              29 | 0.0632           |
| UK5561         | 1 (4.0%)           | 4 (16.0%)     | 16 (64.0%)   | 4 (16.0%)    | Mar-20, May-15 |                25 | B.2.2               |                              18 | 0.1296           |
| UK114          | 0 (0%)             | 25 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-16, May-25 |                25 | B.1.1               |                               8 | 0.3646           |
| UK193          | 0 (0%)             | 8 (33.33%)    | 16 (66.67%)  | 0 (0%)       | Apr-01, May-13 |                24 | B.1.1               |                              20 | 0.0913           |
| UK92           | 0 (0%)             | 23 (95.83%)   | 0 (0%)       | 1 (4.17%)    | Mar-23, Apr-30 |                24 | B.1.1               |                              33 | 0.0501           |
| UK101          | 0 (0%)             | 23 (95.83%)   | 0 (0%)       | 1 (4.17%)    | Mar-21, Apr-27 |                24 | B.1.5               |                              36 | 0.0447           |
| UK21           | 0 (0%)             | 0 (0%)        | 0 (0%)       | 24 (100.0%)  | Mar-18, May-23 |                24 | B.1.40              |                              10 | 0.287            |
| UK103          | 0 (0%)             | 24 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-20, May-27 |                24 | B.1.1               |                               6 | 0.4928           |
| UK326          | 0 (0%)             | 23 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-22, May-22 |                23 | B.1.1.10            |                              11 | 0.2521           |
| UK473          | 0 (0%)             | 0 (0%)        | 23 (100.0%)  | 0 (0%)       | Apr-02, Apr-29 |                23 | B.1.1               |                              34 | 0.0361           |
| UK156          | 0 (0%)             | 0 (0%)        | 9 (39.13%)   | 14 (60.87%)  | Mar-18, Apr-30 |                23 | B.1.71              |                              33 | 0.0592           |
| UK30           | 0 (0%)             | 22 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-15, May-15 |                22 | B.1.1               |                              18 | 0.1614           |
| UK24           | 0 (0%)             | 22 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-18, May-04 |                22 | B.1.1, B.1.1.10     |                              29 | 0.0772           |
| UK279          | 0 (0%)             | 22 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-26, Apr-25 |                22 | B.1.1               |                              38 | 0.0376           |
| UK174          | 0 (0%)             | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-19, May-22 |                21 | B.1.5               |                              11 | 0.2909           |
| UK384          | 0 (0%)             | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-14, Apr-02 |                21 | B.2.1               |                              61 | 0.0156           |
| UK722          | 0 (0%)             | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-23, May-18 |                21 | B.1.1               |                              15 | 0.1867           |
| UK135          | 0 (0%)             | 21 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-01, May-14 |                21 | B.1.p11             |                              19 | 0.1132           |
| UK307          | 0 (0%)             | 20 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-28, May-04 |                20 | B.1.1               |                              29 | 0.0672           |
| UK2912         | 0 (0%)             | 1 (5.0%)      | 0 (0%)       | 19 (95.0%)   | Apr-06, May-13 |                20 | B.1.p11             |                              20 | 0.0974           |
| UK293          | 0 (0%)             | 20 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-24, Apr-28 |                20 | B.1                 |                              35 | 0.0526           |
| UK5309         | 0 (0%)             | 17 (85.0%)    | 3 (15.0%)    | 0 (0%)       | Mar-20, Apr-29 |                20 | B.1.1, B.1.1.10     |                              34 | 0.0619           |
| UK461          | 0 (0%)             | 1 (5.0%)      | 0 (0%)       | 19 (95.0%)   | Apr-18, May-19 |                20 | B.1.5               |                              14 | 0.1165           |
| UK2013         | 0 (0%)             | 19 (95.0%)    | 1 (5.0%)     | 0 (0%)       | Mar-15, Apr-26 |                20 | B.1                 |                              37 | 0.0597           |
| UK41           | 0 (0%)             | 17 (85.0%)    | 3 (15.0%)    | 0 (0%)       | Mar-01, Apr-24 |                20 | B.1                 |                              39 | 0.0729           |
| UK75           | 0 (0%)             | 20 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-17, Apr-26 |                20 | B.1, B.1.34         |                              37 | 0.0569           |
| UK291          | 0 (0%)             | 19 (95.0%)    | 1 (5.0%)     | 0 (0%)       | Mar-13, Apr-05 |                20 | B.2.1               |                              58 | 0.0209           |
| UK38           | 0 (0%)             | 10 (50.0%)    | 0 (0%)       | 10 (50.0%)   | Mar-04, May-11 |                20 | B.2.1               |                              22 | 0.1627           |
| UK219          | 0 (0%)             | 19 (95.0%)    | 0 (0%)       | 1 (5.0%)     | Mar-26, May-02 |                20 | B.1.1               |                              31 | 0.0628           |
| UK514          | 0 (0%)             | 19 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-30, Apr-13 |                19 | B.1.1               |                              50 | 0.0156           |
| UK87           | 0 (0%)             | 0 (0%)        | 0 (0%)       | 19 (100.0%)  | Mar-17, Apr-24 |                19 | B.1.70              |                              39 | 0.0541           |
| UK134          | 0 (0%)             | 15 (78.95%)   | 0 (0%)       | 4 (21.05%)   | Mar-04, Apr-07 |                19 | B.1                 |                              56 | 0.0337           |
| UK419          | 0 (0%)             | 19 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-30, May-02 |                19 | B.1.1               |                              31 | 0.0591           |
| UK269          | 0 (0%)             | 12 (66.67%)   | 6 (33.33%)   | 0 (0%)       | Mar-31, May-06 |                18 | B.1.1               |                              27 | 0.0784           |
| UK888          | 1 (5.56%)          | 17 (94.44%)   | 0 (0%)       | 0 (0%)       | Apr-05, May-04 |                18 | B.1.1               |                              29 | 0.0588           |
| UK472          | 0 (0%)             | 0 (0%)        | 18 (100.0%)  | 0 (0%)       | Apr-04, Apr-27 |                18 | B.1.1, B.1.1.p11    |                              36 | 0.0376           |
| UK1764         | 0 (0%)             | 18 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-14, Apr-19 |                18 | B.3                 |                              44 | 0.0481           |
| UK117          | 0 (0%)             | 18 (100.0%)   | 0 (0%)       | 0 (0%)       | Feb-28, Apr-04 |                18 | B.2.1               |                              59 | 0.0359           |
| UK502          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 18 (100.0%)  | Mar-06, Mar-30 |                18 | B.1.69              |                              64 | 0.0221           |
| UK5084         | 0 (0%)             | 16 (88.89%)   | 2 (11.11%)   | 0 (0%)       | Mar-29, Apr-18 |                18 | B.1                 |                              45 | 0.0261           |
| UK47           | 0 (0%)             | 12 (66.67%)   | 5 (27.78%)   | 1 (5.56%)    | Mar-17, May-18 |                18 | B.1.1               |                              15 | 0.2431           |
| UK126          | 0 (0%)             | 18 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-03 |                18 | B.1.1               |                              30 | 0.0686           |
| UK45           | 0 (0%)             | 13 (72.22%)   | 3 (16.67%)   | 2 (11.11%)   | Mar-02, Apr-16 |                18 | B.1.1               |                              47 | 0.0563           |
| UK46           | 0 (0%)             | 16 (94.12%)   | 1 (5.88%)    | 0 (0%)       | Mar-02, May-08 |                17 | B.2.1               |                              25 | 0.1675           |
| UK143          | 0 (0%)             | 17 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-14, Apr-16 |                17 | B.2.1               |                              47 | 0.0439           |
| UK277          | 0 (0%)             | 2 (11.76%)    | 15 (88.24%)  | 0 (0%)       | Mar-28, May-05 |                17 | B.1.1               |                              28 | 0.0848           |
| UK558          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 17 (100.0%)  | Apr-24, May-22 |                17 | B.1.5               |                              11 | 0.1591           |
| UK604          | 0 (0%)             | 12 (70.59%)   | 2 (11.76%)   | 3 (17.65%)   | Mar-06, Mar-17 |                17 | B.1.1               |                              77 | 0.0089           |
| UK5556         | 0 (0%)             | 0 (0%)        | 17 (100.0%)  | 0 (0%)       | Mar-18, Apr-16 |                17 | B.2.2               |                              47 | 0.0386           |
| UK403          | 0 (0%)             | 17 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-23, Apr-15 |                17 | B.1.1               |                              48 | 0.0299           |
| UK29           | 0 (0%)             | 17 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-09, May-08 |                17 | B.1.1               |                              25 | 0.15             |
| UK2045         | 0 (0%)             | 17 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-17, May-09 |                17 | B.1, B              |                              24 | 0.138            |
| UK5669         | 0 (0%)             | 1 (5.88%)     | 0 (0%)       | 16 (94.12%)  | Mar-24, May-19 |                17 | B.1.1, B.2          |                              14 | 0.25             |
| UK376          | 0 (0%)             | 17 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-04, May-08 |                17 | B.1.1               |                              25 | 0.085            |
| UK58           | 0 (0%)             | 6 (35.29%)    | 0 (0%)       | 11 (64.71%)  | Mar-12, Apr-24 |                17 | B.1                 |                              39 | 0.0689           |
| UK73           | 0 (0%)             | 0 (0%)        | 0 (0%)       | 17 (100.0%)  | Apr-01, May-13 |                17 | B.1.p11             |                              20 | 0.1312           |
| UK4442         | 0 (0%)             | 17 (100.0%)   | 0 (0%)       | 0 (0%)       | May-10, May-24 |                17 | B.1.1               |                               9 | 0.0972           |
| UK150          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 16 (100.0%)  | Mar-21, Apr-22 |                16 | B.1.1.p12           |                              41 | 0.052            |
| UK322          | 0 (0%)             | 0 (0%)        | 16 (100.0%)  | 0 (0%)       | Mar-29, Apr-26 |                16 | B.1                 |                              37 | 0.0505           |
| UK195          | 0 (0%)             | 16 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-03 |                16 | B.1.1               |                              30 | 0.0778           |
| UK1667         | 0 (0%)             | 3 (18.75%)    | 0 (0%)       | 13 (81.25%)  | Mar-30, May-07 |                16 | B.1.p9, B.1.9       |                              26 | 0.0974           |
| UK397          | 0 (0%)             | 16 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-28, Apr-18 |                16 | B.1.1, B.1.1.13     |                              45 | 0.0311           |
| UK5715         | 0 (0%)             | 15 (93.75%)   | 0 (0%)       | 1 (6.25%)    | Feb-13, Apr-22 |                16 | B.1.1, B.2          |                              41 | 0.1122           |
| UK249          | 0 (0%)             | 14 (87.5%)    | 2 (12.5%)    | 0 (0%)       | Mar-31, Apr-25 |                16 | B.1.1               |                              38 | 0.0439           |
| UK392          | 0 (0%)             | 0 (0%)        | 16 (100.0%)  | 0 (0%)       | Mar-25, Apr-12 |                16 | B.1.67              |                              51 | 0.0235           |
| UK67           | 0 (0%)             | 16 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-25, May-21 |                16 | B.1.1               |                              12 | 0.3167           |
| UK2918         | 0 (0%)             | 8 (53.33%)    | 7 (46.67%)   | 0 (0%)       | Mar-02, Apr-27 |                15 | B.1                 |                              36 | 0.1111           |
| UK504          | 0 (0%)             | 0 (0%)        | 15 (100.0%)  | 0 (0%)       | Mar-30, May-12 |                15 | B.1.1               |                              21 | 0.1463           |
| UK236          | 0 (0%)             | 14 (93.33%)   | 1 (6.67%)    | 0 (0%)       | Mar-27, Apr-22 |                15 | B.1.1               |                              41 | 0.0453           |
| UK295          | 10 (66.67%)        | 1 (6.67%)     | 1 (6.67%)    | 3 (20.0%)    | Mar-11, Apr-22 |                15 | B                   |                              41 | 0.0732           |
| UK374          | 0 (0%)             | 15 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-01, Apr-20 |                15 | B.1.1               |                              43 | 0.0316           |
| UK264          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 15 (100.0%)  | Mar-29, Apr-22 |                15 | B.1.p11             |                              41 | 0.0418           |
| UK161          | 0 (0%)             | 10 (66.67%)   | 5 (33.33%)   | 0 (0%)       | Mar-10, May-25 |                15 | B.1.1               |                               8 | 0.6786           |
| UK1849         | 0 (0%)             | 15 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-07, Apr-20 |                15 | B.1.1               |                              43 | 0.0216           |
| UK354          | 1 (6.67%)          | 14 (93.33%)   | 0 (0%)       | 0 (0%)       | Mar-18, Apr-11 |                15 | B.1.1               |                              52 | 0.033            |
| UK146          | 0 (0%)             | 14 (93.33%)   | 0 (0%)       | 1 (6.67%)    | Mar-24, May-07 |                15 | B.1.1               |                              26 | 0.1209           |
| UK278          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-10, May-06 |                14 | B.1.1               |                              27 | 0.0741           |
| UK303          | 0 (0%)             | 4 (28.57%)    | 10 (71.43%)  | 0 (0%)       | Mar-23, Apr-14 |                14 | B.1.1               |                              49 | 0.0345           |
| UK5713         | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-26, Apr-14 |                14 | B.1.1, B.2          |                              49 | 0.0298           |
| UK5180         | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-04, Apr-24 |                14 | B.1.1.7             |                              39 | 0.0394           |
| UK254          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-20, Apr-14 |                14 | B.1.1               |                              49 | 0.0392           |
| UK370          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 14 (100.0%)  | Apr-06, Apr-27 |                14 | B.1.1.10            |                              36 | 0.0449           |
| UK153          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-13, Apr-14 |                14 | B.2                 |                              49 | 0.0502           |
| UK569          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-23, May-12 |                14 | B.1.1               |                              21 | 0.1832           |
| UK5214         | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-20, May-04 |                14 | B.1.1               |                              29 | 0.1194           |
| UK441          | 0 (0%)             | 11 (78.57%)   | 3 (21.43%)   | 0 (0%)       | Apr-04, May-01 |                14 | B.1.1               |                              32 | 0.0649           |
| UK253          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-03, May-03 |                14 | B.1.1               |                              30 | 0.0769           |
| UK501          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-03, Apr-29 |                14 | B.1, B              |                              34 | 0.0588           |
| UK202          | 0 (0%)             | 6 (42.86%)    | 7 (50.0%)    | 1 (7.14%)    | Mar-10, May-05 |                14 | B.1.1               |                              28 | 0.1538           |
| UK163          | 0 (0%)             | 11 (78.57%)   | 1 (7.14%)    | 2 (14.29%)   | Mar-27, May-03 |                14 | B.1.1               |                              30 | 0.0949           |
| UK726          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-30, May-04 |                14 | B.1                 |                              29 | 0.0928           |
| UK505          | 0 (0%)             | 14 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-21, May-15 |                14 | B.1.1, B.1.1.p11    |                              18 | 0.235            |
| UK186          | 0 (0%)             | 12 (92.31%)   | 1 (7.69%)    | 0 (0%)       | Mar-27, May-15 |                13 | B                   |                              18 | 0.2269           |
| UK247          | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-04, May-27 |                13 | B.1.1               |                               6 | 0.7361           |
| UK100          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 13 (100.0%)  | Apr-06, May-12 |                13 | B.1.5               |                              21 | 0.1429           |
| UK5663         | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-11, May-02 |                13 | B.1.1, B.2          |                              31 | 0.0565           |
| UK5685         | 0 (0%)             | 9 (69.23%)    | 2 (15.38%)   | 2 (15.38%)   | Mar-17, May-03 |                13 | B.1.1, B.2          |                              30 | 0.1306           |
| UK308          | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-09, May-18 |                13 | B.1.1               |                              15 | 0.2167           |
| UK34           | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Feb-15, Apr-02 |                13 | B.4                 |                              61 | 0.0642           |
| UK378          | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Feb-15, Mar-05 |                13 | B.1.1               |                              89 | 0.0178           |
| UK132          | 0 (0%)             | 10 (76.92%)   | 1 (7.69%)    | 2 (15.38%)   | Mar-27, Apr-30 |                13 | B.1                 |                              33 | 0.0859           |
| UK499          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 13 (100.0%)  | Apr-24, May-15 |                13 | B.1.5               |                              18 | 0.0972           |
| UK329          | 0 (0%)             | 11 (84.62%)   | 0 (0%)       | 2 (15.38%)   | Mar-20, May-09 |                13 | B.1.1               |                              24 | 0.1736           |
| UK689          | 0 (0%)             | 12 (92.31%)   | 0 (0%)       | 1 (7.69%)    | Mar-05, Apr-07 |                13 | B.2, B.2.1          |                              56 | 0.0491           |
| UK637          | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-28, May-01 |                13 | B.1.1               |                              32 | 0.0885           |
| UK5260         | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-02 |                13 | B.1.1               |                              31 | 0.0914           |
| UK571          | 0 (0%)             | 0 (0%)        | 13 (100.0%)  | 0 (0%)       | Apr-06, May-13 |                13 | B.1.1               |                              20 | 0.1542           |
| UK603          | 0 (0%)             | 0 (0%)        | 13 (100.0%)  | 0 (0%)       | Mar-29, Apr-09 |                13 | B.1.1               |                              54 | 0.017            |
| UK203          | 0 (0%)             | 9 (69.23%)    | 4 (30.77%)   | 0 (0%)       | Mar-31, May-17 |                13 | B.1.1               |                              16 | 0.2448           |
| UK1539         | 0 (0%)             | 0 (0%)        | 0 (0%)       | 13 (100.0%)  | May-09, May-25 |                13 | B.1.5               |                               8 | 0.1667           |
| UK759          | 0 (0%)             | 11 (84.62%)   | 2 (15.38%)   | 0 (0%)       | Mar-28, Apr-27 |                13 | B.1.1               |                              36 | 0.0694           |
| UK71           | 0 (0%)             | 12 (92.31%)   | 1 (7.69%)    | 0 (0%)       | Mar-08, Apr-30 |                13 | B                   |                              33 | 0.1338           |
| UK5498         | 0 (0%)             | 13 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-01, Apr-20 |                13 | B.2                 |                              43 | 0.0368           |
| UK694          | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-06, Mar-14 |                12 | B                   |                              80 | 0.0091           |
| UK211          | 0 (0%)             | 0 (0%)        | 12 (100.0%)  | 0 (0%)       | Mar-24, Apr-30 |                12 | B.1.5               |                              33 | 0.1019           |
| UK148          | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-02, May-13 |                12 | B.1.1               |                              20 | 0.1864           |
| UK266          | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-06, Apr-30 |                12 | B.1                 |                              33 | 0.0661           |
| UK251          | 0 (0%)             | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)       | Mar-17, May-02 |                12 | B.1.1               |                              31 | 0.1349           |
| UK474          | 0 (0%)             | 0 (0%)        | 12 (100.0%)  | 0 (0%)       | Apr-01, May-02 |                12 | B.1.1               |                              31 | 0.0909           |
| UK5703         | 0 (0%)             | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)       | Mar-06, Apr-15 |                12 | B.1.1, B.2          |                              48 | 0.0758           |
| UK111          | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-25, May-18 |                12 | B.1.1               |                              15 | 0.3273           |
| UK806          | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-04, May-08 |                12 | B.1.1.10            |                              25 | 0.1236           |
| UK137          | 0 (0%)             | 3 (25.0%)     | 3 (25.0%)    | 6 (50.0%)    | Mar-04, Apr-11 |                12 | B.1.1               |                              52 | 0.0664           |
| UK347          | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-13, Apr-02 |                12 | B.1                 |                              61 | 0.0298           |
| UK180          | 0 (0%)             | 11 (91.67%)   | 1 (8.33%)    | 0 (0%)       | Mar-30, May-01 |                12 | B.1.1               |                              32 | 0.0909           |
| UK261          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 12 (100.0%)  | Mar-15, Apr-08 |                12 | A.3                 |                              55 | 0.0397           |
| UK436          | 0 (0%)             | 0 (0%)        | 1 (8.33%)    | 11 (91.67%)  | Mar-30, May-14 |                12 | B.1.5               |                              19 | 0.2153           |
| UK5505         | 0 (0%)             | 12 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-01 |                12 | B.1                 |                              32 | 0.0938           |
| UK1018         | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-20, Apr-21 |                11 | B.1.1               |                              42 | 0.0024           |
| UK141          | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-22, Apr-24 |                11 | B.1.1               |                              39 | 0.0846           |
| UK268          | 0 (0%)             | 7 (63.64%)    | 4 (36.36%)   | 0 (0%)       | Mar-23, Apr-16 |                11 | B.1.1               |                              47 | 0.0511           |
| UK83           | 0 (0%)             | 8 (72.73%)    | 1 (9.09%)    | 2 (18.18%)   | Feb-29, Apr-08 |                11 | B.1.1               |                              55 | 0.0709           |
| UK70           | 2 (18.18%)         | 8 (72.73%)    | 1 (9.09%)    | 0 (0%)       | Mar-06, Apr-16 |                11 | B.2                 |                              47 | 0.0872           |
| UK287          | 0 (0%)             | 8 (72.73%)    | 2 (18.18%)   | 1 (9.09%)    | Mar-26, Apr-18 |                11 | B.1                 |                              45 | 0.0511           |
| UK5409         | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-27, Apr-19 |                11 | B.1.1               |                              44 | 0.0523           |
| UK54           | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-18, Apr-30 |                11 | B.1.1.10            |                              33 | 0.1303           |
| UK240          | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-16, Apr-11 |                11 | B.2                 |                              52 | 0.05             |
| UK368          | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-18, May-01 |                11 | B.1                 |                              32 | 0.1375           |
| UK415          | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-19, May-06 |                11 | B.1                 |                              27 | 0.063            |
| UK5332         | 0 (0%)             | 5 (45.45%)    | 6 (54.55%)   | 0 (0%)       | Mar-01, Apr-20 |                11 | B.1.1               |                              43 | 0.1163           |
| UK15           | 0 (0%)             | 7 (63.64%)    | 4 (36.36%)   | 0 (0%)       | Mar-06, May-06 |                11 | B.1.1               |                              27 | 0.2259           |
| UK2906         | 0 (0%)             | 10 (90.91%)   | 1 (9.09%)    | 0 (0%)       | Apr-02, May-22 |                11 | B.1                 |                              11 | 0.4545           |
| UK255          | 0 (0%)             | 10 (90.91%)   | 0 (0%)       | 1 (9.09%)    | Mar-26, Apr-20 |                11 | B.1.1               |                              43 | 0.0581           |
| UK471          | 0 (0%)             | 0 (0%)        | 11 (100.0%)  | 0 (0%)       | Mar-26, Apr-24 |                11 | B.1.1               |                              39 | 0.0744           |
| UK428          | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-20, Apr-06 |                11 | B.2, B.2.1          |                              57 | 0.0298           |
| UK511          | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-05, May-06 |                11 | B.1.1               |                              27 | 0.1148           |
| UK5339         | 0 (0%)             | 11 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-15, Apr-29 |                11 | B.1.1               |                              34 | 0.0412           |
| UK5707         | 2 (18.18%)         | 9 (81.82%)    | 0 (0%)       | 0 (0%)       | Mar-18, Apr-16 |                11 | B.1.1, B.2          |                              47 | 0.0617           |
| UK5681         | 0 (0%)             | 0 (0%)        | 11 (100.0%)  | 0 (0%)       | Apr-03, Apr-27 |                11 | B.1.1, B.2          |                              36 | 0.0667           |
| UK3075         | 0 (0%)             | 1 (9.09%)     | 10 (90.91%)  | 0 (0%)       | Apr-16, May-04 |                11 | B.1.1               |                              29 | 0.0621           |
| UK562          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 10 (100.0%)  | Mar-27, Apr-25 |                10 | B.1                 |                              38 | 0.0848           |
| UK125          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-22, May-20 |                10 | B.1.1               |                              13 | 0.2393           |
| UK5670         | 0 (0%)             | 2 (20.0%)     | 5 (50.0%)    | 3 (30.0%)    | Mar-22, Apr-26 |                10 | B.1.1, B.2          |                              37 | 0.1051           |
| UK123          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-23, May-01 |                10 | B.1                 |                              32 | 0.1354           |
| UK552          | 0 (0%)             | 5 (50.0%)     | 0 (0%)       | 5 (50.0%)    | Mar-18, Apr-04 |                10 | A.1                 |                              59 | 0.032            |
| UK91           | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-28, May-06 |                10 | B.1.1               |                              27 | 0.1605           |
| UK414          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 10 (100.0%)  | Apr-05, Apr-22 |                10 | B.1.5               |                              41 | 0.0461           |
| UK198          | 2 (20.0%)          | 0 (0%)        | 2 (20.0%)    | 6 (60.0%)    | Mar-18, Apr-15 |                10 | A, B.1.5            |                              48 | 0.0648           |
| UK78           | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-14 |                10 | B.1.5               |                              19 | 0.269            |
| UK5557         | 0 (0%)             | 8 (80.0%)     | 2 (20.0%)    | 0 (0%)       | Mar-11, May-13 |                10 | B.2.2               |                              20 | 0.35             |
| UK297          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-09, May-26 |                10 | B.1.p11             |                               7 | 0.746            |
| UK541          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Apr-01, May-20 |                10 | B.1.1               |                              13 | 0.4188           |
| UK462          | 0 (0%)             | 3 (30.0%)     | 7 (70.0%)    | 0 (0%)       | Apr-01, May-11 |                10 | B.1                 |                              22 | 0.202            |
| UK5543         | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-10, Apr-29 |                10 | B.2.1               |                              34 | 0.1634           |
| UK22           | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-02, Apr-21 |                10 | B                   |                              42 | 0.1323           |
| UK687          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Feb-28, Mar-08 |                10 | B.2, B.2.1          |                              86 | 0.0116           |
| UK2904         | 8 (80.0%)          | 1 (10.0%)     | 1 (10.0%)    | 0 (0%)       | Apr-06, Apr-22 |                10 | B.1, B.1.p11        |                              41 | 0.0434           |
| UK201          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-29, May-13 |                10 | B.1                 |                              20 | 0.25             |
| UK171          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-13, Apr-13 |                10 | B.2, B.2.1          |                              50 | 0.0689           |
| UK5423         | 0 (0%)             | 9 (90.0%)     | 1 (10.0%)    | 0 (0%)       | Apr-06, May-04 |                10 | B.1.1               |                              29 | 0.1073           |
| UK242          | 0 (0%)             | 10 (100.0%)   | 0 (0%)       | 0 (0%)       | Mar-26, Apr-20 |                10 | B.1.5               |                              43 | 0.0646           |
| UK306          | 0 (0%)             | 8 (88.89%)    | 0 (0%)       | 1 (11.11%)   | Mar-26, Apr-10 |                 9 | B.1.1               |                              53 | 0.0354           |
| UK244          | 0 (0%)             | 8 (88.89%)    | 1 (11.11%)   | 0 (0%)       | Mar-12, Apr-30 |                 9 | B.1.1               |                              33 | 0.1856           |
| UK312          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-01, Mar-23 |                 9 | B.1.1               |                              71 | 0.0387           |
| UK432          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-24, Apr-09 |                 9 | B.3                 |                              54 | 0.037            |
| UK564          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-03, May-02 |                 9 | B.1.1               |                              31 | 0.1169           |
| UK5338         | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-29, May-02 |                 9 | B.1.1               |                              31 | 0.0121           |
| UK750          | 0 (0%)             | 0 (0%)        | 9 (100.0%)   | 0 (0%)       | Apr-07, Apr-15 |                 9 | B.1                 |                              48 | 0.0208           |
| UK913          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-03, May-04 |                 9 | B.1                 |                              29 | 0.1336           |
| UK1548         | 0 (0%)             | 0 (0%)        | 0 (0%)       | 9 (100.0%)   | Apr-13, Apr-24 |                 9 | B.1.5.5, B.1.5      |                              39 | 0.0353           |
| UK237          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-31, May-16 |                 9 | B.1.1               |                              17 | 0.3382           |
| UK168          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-16, Apr-16 |                 9 | B.2.1               |                              47 | 0.0824           |
| UK5308         | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-29, May-01 |                 9 | B.1.1               |                              32 | 0.0078           |
| UK434          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 9 (100.0%)   | Apr-20, May-07 |                 9 | B.1.5               |                              26 | 0.0817           |
| UK49           | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-19, Jun-02 |                 9 | B.2.1               |                               0 | active today     |
| UK645          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-29, Apr-08 |                 9 | B.2.1               |                              55 | 0.0227           |
| UK178          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-14, Apr-13 |                 9 | B.1.1               |                              50 | 0.075            |
| UK699          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 9 (100.0%)   | Mar-23, Apr-24 |                 9 | B.1.5               |                              39 | 0.1026           |
| UK188          | 0 (0%)             | 6 (66.67%)    | 0 (0%)       | 3 (33.33%)   | Mar-07, Apr-08 |                 9 | B.1                 |                              55 | 0.0727           |
| UK80           | 0 (0%)             | 3 (33.33%)    | 6 (66.67%)   | 0 (0%)       | Mar-09, Apr-27 |                 9 | B.1.1.p15           |                              36 | 0.1701           |
| UK802          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-21, Apr-22 |                 9 | B.1                 |                              41 | 0.0976           |
| UK761          | 0 (0%)             | 0 (0%)        | 9 (100.0%)   | 0 (0%)       | Apr-12, May-10 |                 9 | B.1.1               |                              23 | 0.1522           |
| UK311          | 0 (0%)             | 9 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-20, Apr-11 |                 9 | B.1.1               |                              52 | 0.0529           |
| UK133          | 0 (0%)             | 2 (22.22%)    | 0 (0%)       | 7 (77.78%)   | Mar-22, Apr-25 |                 9 | B.1                 |                              38 | 0.1118           |
| UK5307         | 0 (0%)             | 8 (88.89%)    | 1 (11.11%)   | 0 (0%)       | Mar-08, May-12 |                 9 | B.1.1               |                              21 | 0.3869           |
| UK444          | 3 (37.5%)          | 5 (62.5%)     | 0 (0%)       | 0 (0%)       | Mar-31, Apr-21 |                 8 | B.1.1               |                              42 | 0.0714           |
| UK181          | 0 (0%)             | 5 (62.5%)     | 3 (37.5%)    | 0 (0%)       | Mar-28, Apr-27 |                 8 | B.1.1               |                              36 | 0.119            |
| UK341          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-23, Apr-12 |                 8 | B.1                 |                              51 | 0.056            |
| UK367          | 0 (0%)             | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | Mar-25, Apr-27 |                 8 | B.1                 |                              36 | 0.131            |
| UK5682         | 0 (0%)             | 1 (12.5%)     | 7 (87.5%)    | 0 (0%)       | Apr-08, May-06 |                 8 | B.1.1, B.2          |                              27 | 0.1481           |
| UK532          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-04, Apr-17 |                 8 | B.1.1               |                              46 | 0.0404           |
| UK762          | 0 (0%)             | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | Apr-11, May-04 |                 8 | B.1.1               |                              29 | 0.1133           |
| UK5261         | 0 (0%)             | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | Mar-29, May-01 |                 8 | B.1.1               |                              32 | 0.1473           |
| UK801          | 0 (0%)             | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | Apr-05, May-05 |                 8 | B.1                 |                              28 | 0.1531           |
| UK285          | 0 (0%)             | 5 (62.5%)     | 0 (0%)       | 3 (37.5%)    | Mar-30, Apr-22 |                 8 | B.1.1, B.1.1.p12    |                              41 | 0.0801           |
| UK733          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-10, Apr-22 |                 8 | B.2.1               |                              41 | 0.1498           |
| UK788          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Feb-28, Mar-05 |                 8 | B.4                 |                              89 | 0.0096           |
| UK1013         | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-15, Apr-16 |                 8 | B.1.1               |                              47 | 0.003            |
| UK874          | 0 (0%)             | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | Mar-26, Apr-24 |                 8 | B.1                 |                              39 | 0.1062           |
| UK5708         | 0 (0%)             | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | Mar-30, May-01 |                 8 | B.1.1, B.2          |                              32 | 0.1429           |
| UK252          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-04, Apr-29 |                 8 | B.1.1               |                              34 | 0.105            |
| UK157          | 2 (25.0%)          | 6 (75.0%)     | 0 (0%)       | 0 (0%)       | Mar-22, Jun-02 |                 8 | B.1                 |                               0 | active today     |
| UK292          | 0 (0%)             | 5 (62.5%)     | 3 (37.5%)    | 0 (0%)       | Mar-21, May-01 |                 8 | B.2.1, B.2          |                              32 | 0.183            |
| UK271          | 0 (0%)             | 1 (12.5%)     | 0 (0%)       | 7 (87.5%)    | Apr-02, Apr-26 |                 8 | B.1                 |                              37 | 0.0927           |
| UK574          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-30, Apr-29 |                 8 | B.1.1               |                              34 | 0.1261           |
| UK739          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-01, Mar-08 |                 8 | B.4                 |                              86 | 0.0116           |
| UK696          | 0 (0%)             | 1 (12.5%)     | 7 (87.5%)    | 0 (0%)       | Apr-08, May-01 |                 8 | B.1, B.1.5          |                              32 | 0.1027           |
| UK318          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-20, Apr-10 |                 8 | B                   |                              53 | 0.0566           |
| UK3875         | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-08, May-12 |                 8 | B.1.1               |                              21 | 0.2313           |
| UK480          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-02, May-27 |                 8 | B.1.1               |                               6 | 1.3095           |
| UK554          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 8 (100.0%)   | Apr-23, May-06 |                 8 | B.1.5               |                              27 | 0.0688           |
| UK534          | 0 (0%)             | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | Apr-13, May-13 |                 8 | B.1.1               |                              20 | 0.2143           |
| UK142          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-15, Apr-01 |                 8 | B.2.1               |                              62 | 0.0392           |
| UK5563         | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-11, Apr-22 |                 8 | B.2.2               |                              41 | 0.0383           |
| UK335          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-25, Apr-15 |                 8 | B.2.1               |                              48 | 0.0625           |
| UK350          | 0 (0%)             | 2 (25.0%)     | 6 (75.0%)    | 0 (0%)       | Mar-31, Apr-20 |                 8 | B.1.1               |                              43 | 0.0664           |
| UK93           | 0 (0%)             | 0 (0%)        | 0 (0%)       | 8 (100.0%)   | Mar-21, May-06 |                 8 | B.1.1               |                              27 | 0.2434           |
| UK129          | 0 (0%)             | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | Mar-23, Apr-29 |                 8 | B.1.1               |                              34 | 0.1555           |
| UK223          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-10, Apr-06 |                 8 | B.2.1               |                              57 | 0.0677           |
| UK572          | 0 (0%)             | 0 (0%)        | 8 (100.0%)   | 0 (0%)       | Apr-07, May-01 |                 8 | B.1.1               |                              32 | 0.1071           |
| UK756          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Feb-27, Mar-05 |                 8 | B.1.1               |                              89 | 0.0112           |
| UK220          | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-27, Apr-11 |                 8 | B.1.1               |                              52 | 0.0412           |
| UK5174         | 1 (12.5%)          | 7 (87.5%)     | 0 (0%)       | 0 (0%)       | Mar-26, Apr-07 |                 8 | B.1.1.7             |                              56 | 0.0306           |
| UK69           | 0 (0%)             | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | Mar-04, Apr-14 |                 8 | B.2.1               |                              49 | 0.1195           |
| UK487          | 0 (0%)             | 7 (87.5%)     | 1 (12.5%)    | 0 (0%)       | Mar-24, Apr-08 |                 8 | B.1.1               |                              55 | 0.039            |
| UK5178         | 0 (0%)             | 8 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-21, Apr-17 |                 8 | B.1.1.7             |                              46 | 0.0839           |
| UK65           | 0 (0%)             | 7 (87.5%)     | 0 (0%)       | 1 (12.5%)    | Mar-07, Apr-17 |                 8 | B.1.1               |                              46 | 0.1273           |
| UK282          | 0 (0%)             | 1 (12.5%)     | 0 (0%)       | 7 (87.5%)    | Mar-23, Apr-22 |                 8 | B.1.1               |                              41 | 0.1045           |
| UK232          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-04, Mar-30 |                 7 | B.1.1               |                              64 | 0.0677           |
| UK634          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-30, Apr-18 |                 7 | B.1.1               |                              45 | 0.0704           |
| UK537          | 0 (0%)             | 1 (14.29%)    | 6 (85.71%)   | 0 (0%)       | Mar-27, May-17 |                 7 | B.1.1               |                              16 | 0.5312           |
| UK3673         | 0 (0%)             | 2 (28.57%)    | 5 (71.43%)   | 0 (0%)       | Mar-27, Apr-13 |                 7 | B.1.1               |                              50 | 0.0567           |
| UK647          | 0 (0%)             | 6 (85.71%)    | 0 (0%)       | 1 (14.29%)   | Mar-17, Mar-27 |                 7 | B.2, B.2.1          |                              67 | 0.0249           |
| UK182          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-03, May-02 |                 7 | B.1.1               |                              31 | 0.1559           |
| UK280          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-31, May-06 |                 7 | B.1.1               |                              27 | 0.2222           |
| UK5300         | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-17, May-06 |                 7 | B.1.1               |                              27 | 0.1173           |
| UK352          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-11, May-03 |                 7 | B.1.1               |                              30 | 0.1222           |
| UK289          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-25, Apr-16 |                 7 | B.2.1               |                              47 | 0.078            |
| UK317          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-26, Apr-16 |                 7 | B.3                 |                              47 | 0.0745           |
| UK563          | 0 (0%)             | 4 (57.14%)    | 0 (0%)       | 3 (42.86%)   | Mar-20, May-12 |                 7 | B.1                 |                              21 | 0.4206           |
| UK5177         | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-27, Apr-11 |                 7 | B.1.1.7             |                              52 | 0.0481           |
| UK390          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-27, May-01 |                 7 | B.1.5               |                              32 | 0.1823           |
| UK4399         | 0 (0%)             | 6 (85.71%)    | 0 (0%)       | 1 (14.29%)   | Mar-08, Apr-16 |                 7 | B.1.1               |                              47 | 0.1383           |
| UK5640         | 0 (0%)             | 3 (42.86%)    | 0 (0%)       | 4 (57.14%)   | Apr-11, May-09 |                 7 | B.1.1, B.2          |                              24 | 0.1944           |
| UK510          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-02, Apr-16 |                 7 | B.1.1               |                              47 | 0.0496           |
| UK560          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 7 (100.0%)   | Apr-15, Apr-27 |                 7 | B.1.5               |                              36 | 0.0556           |
| UK5667         | 0 (0%)             | 3 (42.86%)    | 4 (57.14%)   | 0 (0%)       | Mar-27, May-14 |                 7 | B.1.1, B.2          |                              19 | 0.4211           |
| UK5666         | 0 (0%)             | 6 (85.71%)    | 1 (14.29%)   | 0 (0%)       | Mar-13, May-10 |                 7 | B.1.1, B.2          |                              23 | 0.4203           |
| UK5523         | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | May-01, May-23 |                 7 | B.1                 |                              10 | 0.3667           |
| UK692          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-04, Apr-03 |                 7 | B, B.2.1, B.2       |                              60 | 0.0833           |
| UK612          | 0 (0%)             | 1 (14.29%)    | 6 (85.71%)   | 0 (0%)       | Mar-31, Apr-11 |                 7 | B.2.1               |                              52 | 0.0353           |
| UK1006         | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-04, Apr-29 |                 7 | B.1.1               |                              34 | 0.1225           |
| UK418          | 0 (0%)             | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | Apr-03, Apr-20 |                 7 | B.1.1.10            |                              43 | 0.0659           |
| UK629          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-23, Apr-13 |                 7 | B.1                 |                              50 | 0.07             |
| UK206          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-22, Apr-19 |                 7 | B.2.1               |                              44 | 0.1061           |
| UK451          | 0 (0%)             | 0 (0%)        | 6 (85.71%)   | 1 (14.29%)   | Mar-20, Apr-05 |                 7 | B.2.1               |                              58 | 0.046            |
| UK540          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-09, Apr-22 |                 7 | B.1.1, B.1.1.p15    |                              41 | 0.0528           |
| UK2258         | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-23, May-07 |                 7 | B.1                 |                              26 | 0.2885           |
| UK682          | 0 (0%)             | 6 (85.71%)    | 1 (14.29%)   | 0 (0%)       | Mar-21, Mar-31 |                 7 | B.2, B.2.1          |                              63 | 0.0265           |
| UK309          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-01, May-17 |                 7 | B.1.1               |                              16 | 0.4792           |
| UK670          | 0 (0%)             | 6 (85.71%)    | 0 (0%)       | 1 (14.29%)   | Mar-28, May-07 |                 7 | B.1.1               |                              26 | 0.2564           |
| UK323          | 0 (0%)             | 2 (28.57%)    | 0 (0%)       | 5 (71.43%)   | Mar-31, Apr-21 |                 7 | B.1                 |                              42 | 0.0833           |
| UK3323         | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-26, Apr-28 |                 7 | B.1.1               |                              35 | 0.1571           |
| UK536          | 0 (0%)             | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | Mar-27, Apr-09 |                 7 | B.1.1               |                              54 | 0.0401           |
| UK372          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-16, May-13 |                 7 | B.1.1               |                              20 | 0.225            |
| UK439          | 0 (0%)             | 0 (0%)        | 7 (100.0%)   | 0 (0%)       | Apr-02, Apr-20 |                 7 | B.1.1               |                              43 | 0.0698           |
| UK213          | 0 (0%)             | 7 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-18, Apr-17 |                 7 | B.1.1               |                              46 | 0.1087           |
| UK3126         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-06, May-04 |                 6 | B.1.1               |                              29 | 0.1931           |
| UK5780         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-14, Mar-29 |                 6 | B.2.1, B.2          |                              65 | 0.0462           |
| UK512          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-30, Apr-13 |                 6 | B.1.1               |                              50 | 0.056            |
| UK491          | 0 (0%)             | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)   | Mar-23, Apr-02 |                 6 | B.2.1               |                              61 | 0.0328           |
| UK5297         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-30, Apr-04 |                 6 | B.1.1               |                              59 | 0.0169           |
| UK5903         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-25, Apr-18 |                 6 | B.2                 |                              45 | 0.1067           |
| UK102          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-10, Apr-16 |                 6 | B.1                 |                              47 | 0.1574           |
| UK27           | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-08, Apr-26 |                 6 | B.1.1               |                              37 | 0.2649           |
| UK3432         | 0 (0%)             | 1 (16.67%)    | 0 (0%)       | 5 (83.33%)   | Apr-07, May-10 |                 6 | B.1.1               |                              23 | 0.287            |
| UK5699         | 0 (0%)             | 1 (16.67%)    | 0 (0%)       | 5 (83.33%)   | Mar-24, May-02 |                 6 | B.1.1, B.2          |                              31 | 0.2516           |
| UK358          | 0 (0%)             | 0 (0%)        | 6 (100.0%)   | 0 (0%)       | Mar-31, Apr-09 |                 6 | B.2.1               |                              54 | 0.0333           |
| UK5570         | 0 (0%)             | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)   | Mar-05, Apr-17 |                 6 | B.2.2               |                              46 | 0.187            |
| UK2911         | 0 (0%)             | 1 (16.67%)    | 0 (0%)       | 5 (83.33%)   | Mar-31, May-02 |                 6 | B.1.p11             |                              31 | 0.2065           |
| UK313          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-23, Apr-14 |                 6 | B.1.1               |                              49 | 0.0898           |
| UK284          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-02, Apr-25 |                 6 | B.1.1               |                              38 | 0.1211           |
| UK857          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-24, Mar-29 |                 6 | B.2.1               |                              65 | 0.0154           |
| UK331          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-31, May-01 |                 6 | B.1.1               |                              32 | 0.1938           |
| UK447          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-05, Apr-21 |                 6 | B.1.1               |                              42 | 0.0762           |
| UK68           | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-20, Apr-30 |                 6 | B.1.1               |                              33 | 0.2485           |
| UK488          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-31, Apr-15 |                 6 | B.1                 |                              48 | 0.0625           |
| UK755          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-06, May-21 |                 6 | B.1.1               |                              12 | 1.2667           |
| UK799          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-01, Mar-07 |                 6 | B.1                 |                              87 | 0.0138           |
| UK793          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-08, May-21 |                 6 | B.1, B.1.5          |                              12 | 0.7167           |
| UK5788         | 0 (0%)             | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)   | Mar-13, Mar-23 |                 6 | B.2.1, B.2          |                              71 | 0.0282           |
| UK746          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-31, Apr-14 |                 6 | B.1.5               |                              49 | 0.0571           |
| UK654          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Feb-27, Mar-08 |                 6 | B.2.5               |                              86 | 0.0233           |
| UK706          | 3 (50.0%)          | 3 (50.0%)     | 0 (0%)       | 0 (0%)       | Mar-26, Apr-11 |                 6 | B.1.1               |                              52 | 0.0615           |
| UK659          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-21, Mar-30 |                 6 | B                   |                              64 | 0.0281           |
| UK443          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-31, May-14 |                 6 | B.1.1               |                              19 | 0.4632           |
| UK5486         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | May-01, May-28 |                 6 | B.2                 |                               5 | 1.08             |
| UK5650         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-08, May-22 |                 6 | B.1.1, B.2.6        |                              11 | 1.3636           |
| UK489          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-23, Apr-07 |                 6 | B.2.1               |                              56 | 0.0536           |
| UK5648         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-08, May-19 |                 6 | B.1.1, B.2          |                              14 | 1.0286           |
| UK520          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-14, Mar-28 |                 6 | B.2.1, B.2          |                              66 | 0.0424           |
| UK870          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | Mar-18, Mar-25 |                 6 | B.1.5               |                              69 | 0.0203           |
| UK517          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-29, Apr-12 |                 6 | B.1.1               |                              51 | 0.0549           |
| UK530          | 0 (0%)             | 0 (0%)        | 6 (100.0%)   | 0 (0%)       | Mar-31, Apr-08 |                 6 | B.1.1               |                              55 | 0.0291           |
| UK1244         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | May-01, May-11 |                 6 | B.1.1               |                              22 | 0.0909           |
| UK1344         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-20, May-08 |                 6 | B                   |                              25 | 0.144            |
| UK4297         | 0 (0%)             | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | Mar-26, May-08 |                 6 | B.1.1               |                              25 | 0.344            |
| UK464          | 0 (0%)             | 4 (66.67%)    | 2 (33.33%)   | 0 (0%)       | Mar-25, Apr-19 |                 6 | B.1                 |                              44 | 0.1136           |
| UK185          | 1 (16.67%)         | 4 (66.67%)    | 0 (0%)       | 1 (16.67%)   | Mar-10, May-15 |                 6 | B.3                 |                              18 | 0.7333           |
| UK673          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-28, May-18 |                 6 | B.1.1               |                              15 | 0.68             |
| UK196          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-18, Apr-17 |                 6 | B.2.1               |                              46 | 0.1304           |
| UK413          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-06, Apr-03 |                 6 | B                   |                              60 | 0.0933           |
| UK263          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-20, Apr-13 |                 6 | B.1.p11             |                              50 | 0.096            |
| UK555          | 0 (0%)             | 0 (0%)        | 0 (0%)       | 6 (100.0%)   | Apr-13, Apr-25 |                 6 | B.1.5               |                              38 | 0.0632           |
| UK570          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-05, Apr-17 |                 6 | B.1.1               |                              46 | 0.0522           |
| UK330          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-23, Apr-13 |                 6 | B.1.1               |                              50 | 0.084            |
| UK435          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-03, Apr-23 |                 6 | B.1.5               |                              40 | 0.1              |
| UK5581         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-11, Apr-08 |                 6 | B.2.2               |                              55 | 0.1018           |
| UK5671         | 0 (0%)             | 0 (0%)        | 6 (100.0%)   | 0 (0%)       | Mar-31, May-09 |                 6 | B.1.1, B.2          |                              24 | 0.325            |
| UK680          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-05, Apr-14 |                 6 | B.1                 |                              49 | 0.0367           |
| UK110          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-24, Apr-29 |                 6 | B.1                 |                              34 | 0.2118           |
| UK433          | 0 (0%)             | 3 (50.0%)     | 0 (0%)       | 3 (50.0%)    | Mar-22, Apr-07 |                 6 | B                   |                              56 | 0.0571           |
| UK566          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-03, Apr-15 |                 6 | B.1.1.10            |                              48 | 0.05             |
| UK1023         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-07, Apr-16 |                 6 | B.1.1               |                              47 | 0.0383           |
| UK4237         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-15, Apr-15 |                 6 | B.1.1               |                              48 | 0.0              |
| UK16           | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-16, May-06 |                 6 | B.1.1               |                              27 | 0.1481           |
| UK542          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Apr-01, Apr-14 |                 6 | B.1                 |                              49 | 0.0531           |
| UK2891         | 0 (0%)             | 0 (0%)        | 6 (100.0%)   | 0 (0%)       | Mar-27, May-06 |                 6 | B.1.1               |                              27 | 0.2963           |
| UK440          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-28, Apr-13 |                 6 | B.1.1.10            |                              50 | 0.064            |
| UK5700         | 0 (0%)             | 5 (83.33%)    | 0 (0%)       | 1 (16.67%)   | Mar-20, May-21 |                 6 | B.1.1, B.2          |                              12 | 1.0333           |
| UK5743         | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-21, Apr-06 |                 6 | B.1, B.2            |                              57 | 0.0561           |
| UK481          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-30, Apr-14 |                 6 | B.1.1               |                              49 | 0.0612           |
| UK544          | 0 (0%)             | 6 (100.0%)    | 0 (0%)       | 0 (0%)       | Mar-24, Apr-06 |                 6 | B.2.1               |                              57 | 0.0456           |
| UK5208         | 0 (0%)             | 5 (83.33%)    | 1 (16.67%)   | 0 (0%)       | Mar-31, May-14 |                 6 | B.1.1               |                              19 | 0.4632           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NOTT     |             3 |
|  1 | CAMB     |             6 |
|  2 | EDIN     |            10 |
|  3 | PORT     |            11 |
|  4 | SANG     |            11 |
|  5 | BIRM     |            12 |
|  6 | SHEF     |            14 |
|  7 | NORW     |            15 |
|  8 | PHEC     |            17 |
|  9 | PHWC     |            19 |
| 10 | LIVE     |            21 |
| 11 | LOND     |            22 |
| 12 | NORT     |            22 |
| 13 | GLAS     |            23 |
| 14 | EXET     |            23 |
| 15 | OXON     |            52 |
| 16 | NIRE     |            66 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2464 |   UK61 |   UK36 |   UK2916 |   UK5098 |   UK158 |   UK632 |   UK9 |   UK19 |
|:------------------|------:|---------:|-------:|-------:|---------:|---------:|--------:|--------:|------:|-------:|
| 2020-02-02        |     0 |        0 |      0 |      0 |        2 |        0 |       0 |       0 |     0 |      0 |
| 2020-02-09        |     0 |        0 |      0 |      0 |        1 |        0 |       0 |       0 |     0 |      0 |
| 2020-02-23        |     0 |        0 |      0 |      0 |       10 |        0 |       0 |       0 |     0 |      0 |
| 2020-03-01        |     3 |        0 |      0 |      0 |       16 |        0 |       0 |       0 |     0 |      0 |
| 2020-03-08        |    15 |        3 |      2 |      0 |        8 |        0 |       0 |       0 |     2 |      2 |
| 2020-03-15        |    15 |       12 |      2 |      4 |       10 |        3 |       1 |       0 |     4 |      3 |
| 2020-03-22        |    26 |       24 |      9 |     10 |       16 |        7 |       5 |       7 |     7 |      7 |
| 2020-03-29        |    37 |       27 |     15 |     15 |       14 |        4 |      15 |      16 |    13 |     13 |
| 2020-04-05        |    40 |       27 |     21 |     12 |       19 |        4 |      17 |      15 |    10 |     14 |
| 2020-04-12        |    37 |       18 |     13 |     16 |       16 |        5 |      10 |      10 |     9 |     11 |
| 2020-04-19        |    31 |       19 |      4 |     16 |        9 |       10 |       6 |       7 |     1 |      8 |
| 2020-04-26        |    36 |       14 |      6 |      9 |       10 |        7 |      11 |      11 |     2 |      8 |
| 2020-05-03        |    20 |        9 |      2 |      6 |        3 |        4 |       3 |       5 |     1 |      5 |
| 2020-05-10        |    13 |        5 |      5 |      7 |        2 |        3 |       5 |       6 |     1 |      3 |
| 2020-05-17        |    14 |        1 |      0 |      1 |        0 |        0 |       1 |       1 |     0 |      0 |
| 2020-05-24        |     6 |        1 |      0 |      0 |        0 |        0 |       0 |       1 |     0 |      0 |
| 2020-05-31        |     1 |        0 |      0 |      0 |        0 |        0 |       0 |       1 |     0 |      0 |

\pagebreak


**Table S4** Raw data for figure four showing the Shannon diversity per admin1 region over time



| Week       |   England |    Wales |   Scotland |   Northern Ireland |
|:-----------|----------:|---------:|-----------:|-------------------:|
| 2020-01-26 |   0       | -0       |   0        |            0       |
| 2020-02-02 |   1.66746 |  0       |   0        |            0       |
| 2020-02-09 |   2.07944 |  0       |   0        |            0       |
| 2020-02-16 |   1.94591 |  0       |   0        |            0       |
| 2020-02-23 |   3.50848 | -0       |  -0        |            0       |
| 2020-03-01 |   5.01408 |  1.60944 |   2.88924  |            0       |
| 2020-03-08 |   5.94062 |  1.90029 |   4.15437  |            2.36938 |
| 2020-03-15 |   5.98205 |  2.13478 |   4.26153  |            2.28424 |
| 2020-03-22 |   6.35058 |  3.32168 |   4.4781   |            3.56169 |
| 2020-03-29 |   6.40142 |  4.89376 |   4.41593  |            2.68199 |
| 2020-04-05 |   6.17167 |  4.81595 |   4.1716   |            2.75624 |
| 2020-04-12 |   5.74843 |  4.33732 |   3.93543  |            1.70581 |
| 2020-04-19 |   5.00521 |  3.99639 |   3.93917  |            1.99019 |
| 2020-04-26 |   5.04672 |  3.78135 |   3.91741  |            0       |
| 2020-05-03 |   4.51001 |  3.39064 |   3.3851   |            0       |
| 2020-05-10 |   4.01401 |  3.15007 |   3.13504  |            0       |
| 2020-05-17 |   3.38638 |  1.09861 |   2.94776  |            0       |
| 2020-05-24 |   2.78028 |  0       |   0.950271 |            0       |
| 2020-05-31 |   1.53965 |  0       |   0        |            0       |

\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-01-27 |                            1 |                                0 |       1 |
| 2020-02-03 |                            2 |                                1 |       3 |
| 2020-02-05 |                            1 |                                0 |       1 |
| 2020-02-08 |                            2 |                                0 |       2 |
| 2020-02-09 |                            1 |                                1 |       2 |
| 2020-02-13 |                            1 |                                1 |       2 |
| 2020-02-14 |                            0 |                                1 |       1 |
| 2020-02-15 |                            0 |                                2 |       2 |
| 2020-02-16 |                            2 |                                1 |       3 |
| 2020-02-18 |                            1 |                                0 |       1 |
| 2020-02-19 |                            1 |                                0 |       1 |
| 2020-02-20 |                            1 |                                0 |       1 |
| 2020-02-23 |                            1 |                                1 |       2 |
| 2020-02-24 |                            2 |                                1 |       3 |
| 2020-02-25 |                            3 |                                4 |       7 |
| 2020-02-26 |                            4 |                                2 |       6 |
| 2020-02-27 |                            7 |                                2 |       9 |
| 2020-02-28 |                            5 |                                6 |      11 |
| 2020-02-29 |                            9 |                                1 |      10 |
| 2020-03-01 |                           14 |                               11 |      25 |
| 2020-03-02 |                           36 |                               10 |      46 |
| 2020-03-03 |                           31 |                               14 |      45 |
| 2020-03-04 |                           35 |                               17 |      52 |
| 2020-03-05 |                           38 |                               12 |      50 |
| 2020-03-06 |                           34 |                               23 |      57 |
| 2020-03-07 |                           22 |                                6 |      28 |
| 2020-03-08 |                           24 |                               12 |      36 |
| 2020-03-09 |                           37 |                               17 |      54 |
| 2020-03-10 |                           43 |                               28 |      71 |
| 2020-03-11 |                           74 |                               36 |     110 |
| 2020-03-12 |                          104 |                               41 |     145 |
| 2020-03-13 |                           45 |                               31 |      76 |
| 2020-03-14 |                           41 |                               25 |      66 |
| 2020-03-15 |                           29 |                               18 |      47 |
| 2020-03-16 |                           32 |                               19 |      51 |
| 2020-03-17 |                           46 |                               33 |      79 |
| 2020-03-18 |                           70 |                               50 |     120 |
| 2020-03-19 |                           61 |                               32 |      93 |
| 2020-03-20 |                           73 |                               44 |     117 |
| 2020-03-21 |                           79 |                               38 |     117 |
| 2020-03-22 |                           77 |                               28 |     105 |
| 2020-03-23 |                          133 |                               52 |     185 |
| 2020-03-24 |                          140 |                               34 |     174 |
| 2020-03-25 |                          134 |                               40 |     174 |
| 2020-03-26 |                          115 |                               51 |     166 |
| 2020-03-27 |                          122 |                               48 |     170 |
| 2020-03-28 |                          114 |                               39 |     153 |
| 2020-03-29 |                          112 |                               44 |     156 |
| 2020-03-30 |                          175 |                               60 |     235 |
| 2020-03-31 |                          163 |                               62 |     225 |
| 2020-04-01 |                          165 |                               39 |     204 |
| 2020-04-02 |                          150 |                               46 |     196 |
| 2020-04-03 |                          146 |                               38 |     184 |
| 2020-04-04 |                          134 |                               39 |     173 |
| 2020-04-05 |                          121 |                               24 |     145 |
| 2020-04-06 |                          169 |                               28 |     197 |
| 2020-04-07 |                          152 |                               27 |     179 |
| 2020-04-08 |                           98 |                               29 |     127 |
| 2020-04-09 |                           75 |                               14 |      89 |
| 2020-04-10 |                           97 |                               12 |     109 |
| 2020-04-11 |                           64 |                               15 |      79 |
| 2020-04-12 |                           62 |                               11 |      73 |
| 2020-04-13 |                           57 |                               13 |      70 |
| 2020-04-14 |                           70 |                               18 |      88 |
| 2020-04-15 |                           68 |                               17 |      85 |
| 2020-04-16 |                           58 |                               14 |      72 |
| 2020-04-17 |                           55 |                               10 |      65 |
| 2020-04-18 |                           26 |                                7 |      33 |
| 2020-04-19 |                           32 |                                5 |      37 |
| 2020-04-20 |                           36 |                                8 |      44 |
| 2020-04-21 |                           34 |                                1 |      35 |
| 2020-04-22 |                           15 |                                9 |      24 |
| 2020-04-23 |                           16 |                                3 |      19 |
| 2020-04-24 |                           21 |                                5 |      26 |
| 2020-04-25 |                           11 |                                3 |      14 |
| 2020-04-26 |                           12 |                                2 |      14 |
| 2020-04-27 |                           19 |                                6 |      25 |
| 2020-04-28 |                           15 |                                2 |      17 |
| 2020-04-29 |                           21 |                                5 |      26 |
| 2020-04-30 |                           17 |                                4 |      21 |
| 2020-05-01 |                           30 |                                7 |      37 |
| 2020-05-02 |                            9 |                                2 |      11 |
| 2020-05-03 |                            7 |                                2 |       9 |
| 2020-05-04 |                           17 |                                2 |      19 |
| 2020-05-05 |                           11 |                                1 |      12 |
| 2020-05-06 |                           11 |                                1 |      12 |
| 2020-05-07 |                            5 |                                2 |       7 |
| 2020-05-08 |                            7 |                                0 |       7 |
| 2020-05-09 |                            2 |                                1 |       3 |
| 2020-05-10 |                            6 |                                1 |       7 |
| 2020-05-11 |                            8 |                                2 |      10 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-13 |                            1 |                                2 |       3 |
| 2020-05-14 |                            3 |                                2 |       5 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            5 |                                0 |       5 |
| 2020-05-18 |                            3 |                                0 |       3 |
| 2020-05-19 |                            2 |                                0 |       2 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-05-21 |                            3 |                                0 |       3 |
| 2020-05-22 |                            1 |                                0 |       1 |
| 2020-05-23 |                            2 |                                0 |       2 |
| 2020-05-24 |                            1 |                                0 |       1 |

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
| 2020-03-19 |       142 |         28 |      30 |                  3 |
| 2020-03-20 |       194 |         32 |      12 |                  6 |
| 2020-03-21 |       203 |         35 |       0 |                 13 |
| 2020-03-22 |       193 |         32 |       0 |                  8 |
| 2020-03-23 |       332 |         84 |       1 |                 29 |
| 2020-03-24 |       285 |         87 |      22 |                 23 |
| 2020-03-25 |       276 |         71 |      94 |                 16 |
| 2020-03-26 |       299 |         91 |      18 |                 27 |
| 2020-03-27 |       292 |         87 |      29 |                  7 |
| 2020-03-28 |       299 |         38 |      17 |                 12 |
| 2020-03-29 |       339 |         46 |      22 |                 10 |
| 2020-03-30 |       482 |         59 |      75 |                  6 |
| 2020-03-31 |       441 |         74 |     143 |                  8 |
| 2020-04-01 |       401 |         71 |     134 |                  0 |
| 2020-04-02 |       414 |         48 |      99 |                  1 |
| 2020-04-03 |       416 |         55 |     112 |                  0 |
| 2020-04-04 |       336 |         45 |     137 |                  1 |
| 2020-04-05 |       346 |         50 |      65 |                  0 |
| 2020-04-06 |       428 |         70 |     167 |                 13 |
| 2020-04-07 |       396 |         70 |     184 |                  0 |
| 2020-04-08 |       344 |         41 |     122 |                  0 |
| 2020-04-09 |       293 |         20 |      79 |                  0 |
| 2020-04-10 |       303 |         18 |     119 |                 11 |
| 2020-04-11 |       256 |         38 |      69 |                  8 |
| 2020-04-12 |       206 |         48 |      86 |                  7 |
| 2020-04-13 |       239 |         53 |      76 |                  5 |
| 2020-04-14 |       309 |         50 |     120 |                  0 |
| 2020-04-15 |       302 |         44 |      79 |                  8 |
| 2020-04-16 |       286 |         48 |      71 |                  0 |
| 2020-04-17 |       219 |         19 |      46 |                  0 |
| 2020-04-18 |       137 |         37 |      38 |                  0 |
| 2020-04-19 |       155 |         30 |      26 |                  1 |
| 2020-04-20 |       153 |         45 |      64 |                  2 |
| 2020-04-21 |       113 |         62 |      27 |                 12 |
| 2020-04-22 |       122 |         78 |       9 |                 14 |
| 2020-04-23 |        86 |         68 |      17 |                  0 |
| 2020-04-24 |        49 |         89 |      53 |                  0 |
| 2020-04-25 |        50 |         66 |      26 |                  0 |
| 2020-04-26 |        80 |         49 |      13 |                  0 |
| 2020-04-27 |       125 |         53 |      63 |                  0 |
| 2020-04-28 |       102 |         31 |      46 |                  0 |
| 2020-04-29 |       190 |         17 |      28 |                  0 |
| 2020-04-30 |       170 |         23 |      35 |                  0 |
| 2020-05-01 |       205 |         23 |      35 |                  0 |
| 2020-05-02 |       106 |         13 |      31 |                  0 |
| 2020-05-03 |        68 |         16 |      18 |                  0 |
| 2020-05-04 |       115 |          8 |      40 |                  0 |
| 2020-05-05 |        75 |         16 |      25 |                  0 |
| 2020-05-06 |        86 |         30 |      17 |                  0 |
| 2020-05-07 |        87 |         31 |      30 |                  0 |
| 2020-05-08 |        44 |         22 |       9 |                  0 |
| 2020-05-09 |        43 |         13 |       9 |                  0 |
| 2020-05-10 |        41 |         17 |      15 |                  0 |
| 2020-05-11 |        82 |         13 |      41 |                  0 |
| 2020-05-12 |        56 |         14 |      34 |                  0 |
| 2020-05-13 |        49 |         10 |      40 |                  0 |
| 2020-05-14 |        31 |          1 |      21 |                  0 |
| 2020-05-15 |        22 |          7 |      20 |                  0 |
| 2020-05-16 |        15 |          1 |       4 |                  0 |
| 2020-05-17 |        14 |          7 |       3 |                  0 |
| 2020-05-18 |        44 |          3 |       0 |                  0 |
| 2020-05-19 |        42 |          8 |       0 |                  0 |
| 2020-05-20 |        28 |          8 |       0 |                  0 |
| 2020-05-21 |        32 |          4 |       0 |                  0 |
| 2020-05-22 |        26 |          2 |       0 |                  0 |
| 2020-05-23 |        11 |          4 |       0 |                  0 |
| 2020-05-24 |         9 |          2 |       0 |                  0 |
| 2020-05-25 |        13 |          2 |       0 |                  0 |
| 2020-05-26 |        11 |          1 |       0 |                  0 |
| 2020-05-27 |         9 |          0 |       0 |                  0 |
| 2020-05-28 |        11 |          0 |       0 |                  0 |
| 2020-05-29 |         4 |          0 |       0 |                  0 |
| 2020-05-30 |         5 |          0 |       0 |                  0 |
| 2020-05-31 |         4 |          0 |       0 |                  0 |
| 2020-06-01 |         3 |          0 |       0 |                  0 |
| 2020-06-02 |         5 |          0 |       0 |                  0 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                       | Country          |   Number of sequences | Sequence group   |
|:-----------------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN                     | Scotland         |                    22 | 10-50            |
| ABERDEENSHIRE                | Scotland         |                     5 | 1-10             |
| ANGLESEY                     | Wales            |                    36 | 10-50            |
| ANGUS                        | Scotland         |                    13 | 10-50            |
| ANTRIM                       | Northern Ireland |                   142 | 100-150          |
| ARGYLL AND BUTE              | Scotland         |                     2 | 1-10             |
| ARMAGH                       | Northern Ireland |                    12 | 10-50            |
| BATH AND NORTH EAST SOMERSET | England          |                     0 | 0                |
| BEDFORDSHIRE                 | England          |                   418 | 400-500          |
| BERKSHIRE                    | England          |                     8 | 1-10             |
| BLACKBURN WITH DARWEN        | England          |                     0 | 0                |
| BLACKPOOL                    | England          |                     0 | 0                |
| BLAENAU GWENT                | Wales            |                    52 | 50-100           |
| BOLTON                       | England          |                     0 | 0                |
| BOURNEMOUTH                  | England          |                     0 | 0                |
| BRIDGEND                     | Wales            |                   104 | 100-150          |
| BRIGHTON AND HOVE            | England          |                     0 | 0                |
| BRISTOL                      | England          |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England          |                   349 | 300-400          |
| BURY                         | England          |                     0 | 0                |
| CAERPHILLY                   | Wales            |                   121 | 100-150          |
| CAMBRIDGESHIRE               | England          |                   668 | >500             |
| CARDIFF                      | Wales            |                   430 | 400-500          |
| CARMARTHENSHIRE              | Wales            |                   114 | 100-150          |
| CENTRAL BEDFORDSHIRE         | England          |                     0 | 0                |
| CEREDIGION                   | Wales            |                    16 | 10-50            |
| CHESHIRE                     | England          |                    12 | 10-50            |
| CLACKMANNANSHIRE             | Scotland         |                     2 | 1-10             |
| CONWY                        | Wales            |                    88 | 50-100           |
| CORNWALL                     | England          |                    20 | 10-50            |
| CUMBRIA                      | England          |                    32 | 10-50            |
| DARLINGTON                   | England          |                     0 | 0                |
| DENBIGHSHIRE                 | Wales            |                   115 | 100-150          |
| DERBY                        | England          |                     0 | 0                |
| DERBYSHIRE                   | England          |                    25 | 10-50            |
| DEVON                        | England          |                   283 | 250-300          |
| DORSET                       | England          |                   159 | 150-200          |
| DOWN                         | Northern Ireland |                    94 | 50-100           |
| DUMFRIES AND GALLOWAY        | Scotland         |                    54 | 50-100           |
| DUNDEE                       | Scotland         |                    93 | 50-100           |
| DURHAM                       | England          |                     6 | 1-10             |
| EAST AYRSHIRE                | Scotland         |                    75 | 50-100           |
| EAST DUNBARTONSHIRE          | Scotland         |                     6 | 1-10             |
| EAST LOTHIAN                 | Scotland         |                    54 | 50-100           |
| EAST RENFREWSHIRE            | Scotland         |                     5 | 1-10             |
| EAST RIDING OF YORKSHIRE     | England          |                    33 | 10-50            |
| EDINBURGH                    | Scotland         |                   426 | 400-500          |
| EILEAN SIAR                  | Scotland         |                     2 | 1-10             |
| ESSEX                        | England          |                  1209 | >500             |
| FALKIRK                      | Scotland         |                    92 | 50-100           |
| FERMANAGH                    | Northern Ireland |                     3 | 1-10             |
| FIFE                         | Scotland         |                    43 | 10-50            |
| FLINTSHIRE                   | Wales            |                    79 | 50-100           |
| GATESHEAD                    | England          |                     0 | 0                |
| GLASGOW                      | Scotland         |                   791 | >500             |
| GLOUCESTERSHIRE              | England          |                   456 | 400-500          |
| GREATER LONDON               | England          |                  2312 | >500             |
| GUERNSEY                     | Channel_islands  |                    41 | 10-50            |
| GWYNEDD                      | Wales            |                    69 | 50-100           |
| HALTON                       | England          |                     0 | 0                |
| HAMPSHIRE                    | England          |                   122 | 100-150          |
| HARTLEPOOL                   | England          |                     0 | 0                |
| HEREFORDSHIRE                | England          |                     4 | 1-10             |
| HERTFORDSHIRE                | England          |                   933 | >500             |
| HIGHLAND                     | Scotland         |                     9 | 1-10             |
| INVERCLYDE                   | Scotland         |                     3 | 1-10             |
| ISLE OF WIGHT                | England          |                     0 | 0                |
| ISLES OF SCILLY              | England          |                     0 | 0                |
| JERSEY                       | Channel_islands  |                    77 | 50-100           |
| KENT                         | England          |                    29 | 10-50            |
| KINGSTON UPON HULL           | England          |                     0 | 0                |
| LANCASHIRE                   | England          |                     8 | 1-10             |
| LEICESTER                    | England          |                     0 | 0                |
| LEICESTERSHIRE               | England          |                     5 | 1-10             |
| LINCOLNSHIRE                 | England          |                    16 | 10-50            |
| LONDONDERRY                  | Northern Ireland |                    16 | 10-50            |
| LUTON                        | England          |                     0 | 0                |
| MANCHESTER                   | England          |                    30 | 10-50            |
| MEDWAY                       | England          |                     0 | 0                |
| MERSEYSIDE                   | England          |                    59 | 50-100           |
| MERTHYR TYDFIL               | Wales            |                    67 | 50-100           |
| MIDDLESBROUGH                | England          |                     0 | 0                |
| MIDLOTHIAN                   | Scotland         |                   131 | 100-150          |
| MILTON KEYNES                | England          |                     0 | 0                |
| MONMOUTHSHIRE                | Wales            |                    63 | 50-100           |
| MORAY                        | Scotland         |                     0 | 0                |
| NEATH PORT TALBOT            | Wales            |                   107 | 100-150          |
| NEWPORT                      | Wales            |                   144 | 100-150          |
| NORFOLK                      | England          |                   559 | >500             |
| NORTH AYRSHIRE               | Scotland         |                     2 | 1-10             |
| NORTH LANARKSHIRE            | Scotland         |                   163 | 150-200          |
| NORTH LINCOLNSHIRE           | England          |                     0 | 0                |
| NORTH SOMERSET               | England          |                     0 | 0                |
| NORTH YORKSHIRE              | England          |                    63 | 50-100           |
| NORTHAMPTONSHIRE             | England          |                    22 | 10-50            |
| NORTHUMBERLAND               | England          |                     4 | 1-10             |
| NOTTINGHAM                   | England          |                   634 | >500             |
| NOTTINGHAMSHIRE              | England          |                    58 | 50-100           |
| OLDHAM                       | England          |                     0 | 0                |
| ORKNEY ISLANDS               | Scotland         |                     1 | 1-10             |
| OXFORDSHIRE                  | England          |                    97 | 50-100           |
| PEMBROKESHIRE                | Wales            |                    67 | 50-100           |
| PERTHSHIRE AND KINROSS       | Scotland         |                    48 | 10-50            |
| PETERBOROUGH                 | England          |                     0 | 0                |
| PLYMOUTH                     | England          |                     1 | 1-10             |
| POOLE                        | England          |                     0 | 0                |
| PORTSMOUTH                   | England          |                     0 | 0                |
| POWYS                        | Wales            |                    60 | 50-100           |
| REDCAR AND CLEVELAND         | England          |                     0 | 0                |
| RENFREWSHIRE                 | Scotland         |                   227 | 200-250          |
| RHONDDA, CYNON, TAFF         | Wales            |                     0 | 0                |
| ROCHDALE                     | England          |                     0 | 0                |
| RUTLAND                      | England          |                     0 | 0                |
| SALFORD                      | England          |                     0 | 0                |
| SCOTTISH BORDERS             | Scotland         |                   132 | 100-150          |
| SHETLAND ISLANDS             | Scotland         |                    14 | 10-50            |
| SHROPSHIRE                   | England          |                     1 | 1-10             |
| SOMERSET                     | England          |                   356 | 300-400          |
| SOUTH AYRSHIRE               | Scotland         |                     0 | 0                |
| SOUTH GLOUCESTERSHIRE        | England          |                     0 | 0                |
| SOUTH LANARKSHIRE            | Scotland         |                     9 | 1-10             |
| SOUTH YORKSHIRE              | England          |                  1250 | >500             |
| SOUTHAMPTON                  | England          |                     0 | 0                |
| SOUTHEND-ON-SEA              | England          |                     0 | 0                |
| STAFFORDSHIRE                | England          |                    49 | 10-50            |
| STIRLING                     | Scotland         |                     0 | 0                |
| STOCKPORT                    | England          |                     0 | 0                |
| STOCKTON-ON-TEES             | England          |                     0 | 0                |
| STOKE-ON-TRENT               | England          |                     0 | 0                |
| SUFFOLK                      | England          |                   503 | >500             |
| SURREY                       | England          |                    64 | 50-100           |
| SUSSEX                       | England          |                     1 | 1-10             |
| SWANSEA                      | Wales            |                   252 | 250-300          |
| SWINDON                      | England          |                     0 | 0                |
| TAMESIDE                     | England          |                     0 | 0                |
| TELFORD AND WREKIN           | England          |                     0 | 0                |
| THURROCK                     | England          |                     0 | 0                |
| TORBAY                       | England          |                     0 | 0                |
| TORFAEN                      | Wales            |                    85 | 50-100           |
| TRAFFORD                     | England          |                     0 | 0                |
| TYNE AND WEAR                | England          |                    38 | 10-50            |
| TYRONE                       | Northern Ireland |                    15 | 10-50            |
| VALE OF GLAMORGAN            | Wales            |                   159 | 150-200          |
| WARRINGTON                   | England          |                     0 | 0                |
| WARWICKSHIRE                 | England          |                    10 | 10-50            |
| WEST DUNBARTONSHIRE          | Scotland         |                    10 | 10-50            |
| WEST LOTHIAN                 | Scotland         |                    95 | 50-100           |
| WEST MIDLANDS                | England          |                    95 | 50-100           |
| WEST YORKSHIRE               | England          |                    20 | 10-50            |
| WIGAN                        | England          |                     0 | 0                |
| WILTSHIRE                    | England          |                   245 | 200-250          |
| WORCESTERSHIRE               | England          |                    12 | 10-50            |
| WREXHAM                      | Wales            |                   102 | 100-150          |
| YORK                         | England          |                     0 | 0                |

\pagebreak






