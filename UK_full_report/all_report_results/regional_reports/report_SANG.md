







# Lineages report for SANG




This report gives summaries of UK specific lineages sequenced by SANG for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-05. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
6352 sequences in the UK from the sequencing centre SANG have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 208 and the maximum is 3097


Sequences which were replicates or too error-prone were removed from this analysis.



331 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 24 that remain:
19 are pending extinction, ie last seen three weeks ago.
3 lineages have reactivated.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England       | Northern Ireland   | Scotland    | Date range     |   Total sequences | Global lineage                        |   Time since last sample (days) |   Activity score |
|:---------------|:--------------|:-------------------|:------------|:---------------|------------------:|:--------------------------------------|--------------------------------:|-----------------:|
| UK5            | 1991 (90.34%) | 170 (7.71%)        | 43 (1.95%)  | Mar-07, Jun-04 |              2204 | B.1.1, B.1.1.1, B.1.1.13, B.1.1.10    |                               1 |           0.0404 |
| UK107          | 385 (97.22%)  | 7 (1.77%)          | 4 (1.01%)   | Mar-08, May-01 |               396 | B.2.1                                 |                              35 |           0.0039 |
| UK42           | 302 (93.79%)  | 1 (0.31%)          | 19 (5.9%)   | Mar-03, May-17 |               322 | B.1.p11, B.1.35, B.1.72, B.1.p73, B.1 |                              19 |           0.0123 |
| UK5676         | 119 (79.87%)  | 0 (0%)             | 30 (20.13%) | Mar-09, Apr-20 |               149 | B.2                                   |                              46 |           0.0062 |
| UK167          | 123 (89.13%)  | 12 (8.7%)          | 3 (2.17%)   | Mar-11, Jun-04 |               138 | B.1                                   |                               1 |           0.6204 |
| UK2464         | 110 (83.97%)  | 0 (0%)             | 21 (16.03%) | Mar-12, May-01 |               131 | B.1.p11, B.1                          |                              35 |           0.011  |
| UK2913         | 93 (85.32%)   | 11 (10.09%)        | 5 (4.59%)   | Mar-11, Jun-01 |               109 | B.1.p11, B.1                          |                               4 |           0.1898 |
| UK9            | 105 (100.0%)  | 0 (0%)             | 0 (0%)      | Mar-19, May-04 |               105 | B.1.13                                |                              32 |           0.0138 |
| UK72           | 98 (97.03%)   | 2 (1.98%)          | 1 (0.99%)   | Mar-10, Apr-26 |               101 | B                                     |                              40 |           0.0118 |
| UK199          | 76 (87.36%)   | 0 (0%)             | 11 (12.64%) | Mar-19, May-11 |                87 | B.1, B.1.5, B.1.5.5                   |                              25 |           0.0247 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SANG/figures/report_SANG_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 14 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SANG/figures/report_SANG_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SANG/figures/report_SANG_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SANG/figures/report_SANG_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SANG/figures/report_SANG_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 536 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/regional_reports/SANG/figures/report_SANG_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England       | Northern Ireland   | Scotland    | Date range     |   Total sequences | Global lineage                        |   Time since last sample (days) |   Activity score |
|:---------------|:--------------|:-------------------|:------------|:---------------|------------------:|:--------------------------------------|--------------------------------:|-----------------:|
| UK5            | 1991 (90.34%) | 170 (7.71%)        | 43 (1.95%)  | Mar-07, Jun-04 |              2204 | B.1.1, B.1.1.1, B.1.1.13, B.1.1.10    |                               1 |           0.0404 |
| UK107          | 385 (97.22%)  | 7 (1.77%)          | 4 (1.01%)   | Mar-08, May-01 |               396 | B.2.1                                 |                              35 |           0.0039 |
| UK42           | 302 (93.79%)  | 1 (0.31%)          | 19 (5.9%)   | Mar-03, May-17 |               322 | B.1.p11, B.1.35, B.1.72, B.1.p73, B.1 |                              19 |           0.0123 |
| UK5676         | 119 (79.87%)  | 0 (0%)             | 30 (20.13%) | Mar-09, Apr-20 |               149 | B.2                                   |                              46 |           0.0062 |
| UK167          | 123 (89.13%)  | 12 (8.7%)          | 3 (2.17%)   | Mar-11, Jun-04 |               138 | B.1                                   |                               1 |           0.6204 |
| UK2464         | 110 (83.97%)  | 0 (0%)             | 21 (16.03%) | Mar-12, May-01 |               131 | B.1.p11, B.1                          |                              35 |           0.011  |
| UK2913         | 93 (85.32%)   | 11 (10.09%)        | 5 (4.59%)   | Mar-11, Jun-01 |               109 | B.1.p11, B.1                          |                               4 |           0.1898 |
| UK9            | 105 (100.0%)  | 0 (0%)             | 0 (0%)      | Mar-19, May-04 |               105 | B.1.13                                |                              32 |           0.0138 |
| UK72           | 98 (97.03%)   | 2 (1.98%)          | 1 (0.99%)   | Mar-10, Apr-26 |               101 | B                                     |                              40 |           0.0118 |
| UK199          | 76 (87.36%)   | 0 (0%)             | 11 (12.64%) | Mar-19, May-11 |                87 | B.1, B.1.5, B.1.5.5                   |                              25 |           0.0247 |
| UK3929         | 86 (98.85%)   | 1 (1.15%)          | 0 (0%)      | Mar-18, May-06 |                87 | B.1.1, B.1.1.3, B.1.1.4               |                              30 |           0.019  |
| UK494          | 80 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, May-01 |                80 | B.1.p11                               |                              35 |           0.0148 |
| UK5741         | 77 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-11, May-10 |                77 | B.1                                   |                              26 |           0.0304 |
| UK66           | 76 (98.7%)    | 0 (0%)             | 1 (1.3%)    | Mar-18, May-16 |                77 | B.1.1.8                               |                              20 |           0.0388 |
| UK28           | 72 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-26, May-08 |                72 | B.1.1.10                              |                              28 |           0.0216 |
| UK2735         | 50 (81.97%)   | 10 (16.39%)        | 1 (1.64%)   | Mar-24, May-07 |                61 | B.1.1                                 |                              29 |           0.0253 |
| UK2916         | 51 (96.23%)   | 1 (1.89%)          | 1 (1.89%)   | Feb-27, May-10 |                53 | B.1                                   |                              26 |           0.054  |
| UK5523         | 46 (100.0%)   | 0 (0%)             | 0 (0%)      | May-01, Jun-01 |                46 | B.1                                   |                               4 |           0.1722 |
| UK370          | 34 (75.56%)   | 6 (13.33%)         | 5 (11.11%)  | Mar-13, May-12 |                45 | B.1.1.10                              |                              24 |           0.0568 |
| UK40           | 0 (0%)        | 0 (0%)             | 43 (100.0%) | Mar-21, Apr-07 |                43 | B.16                                  |                              59 |           0.0069 |
| UK5498         | 40 (97.56%)   | 0 (0%)             | 1 (2.44%)   | Mar-14, May-15 |                41 | B.2                                   |                              21 |           0.0738 |
| UK61           | 39 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-12, May-18 |                39 | B.3                                   |                              18 |           0.098  |
| UK63           | 39 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-28, Apr-30 |                39 | B.1.1                                 |                              36 |           0.0241 |
| UK565          | 39 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-22, May-14 |                39 | B.1.1                                 |                              22 |           0.0634 |
| UK13           | 38 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, May-12 |                38 | B.1.1                                 |                              24 |           0.0676 |
| UK4            | 36 (97.3%)    | 1 (2.7%)           | 0 (0%)      | Mar-10, Apr-25 |                37 | B                                     |                              41 |           0.0312 |
| UK5180         | 34 (91.89%)   | 3 (8.11%)          | 0 (0%)      | Mar-13, Apr-22 |                37 | B.1.1.7                               |                              44 |           0.0253 |
| UK5098         | 2 (5.71%)     | 0 (0%)             | 33 (94.29%) | Mar-23, Apr-16 |                35 | B.1, B.1.p73                          |                              50 |           0.0141 |
| UK37           | 31 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-17, May-04 |                31 | B.1.30                                |                              32 |           0.05   |
| UK5561         | 29 (93.55%)   | 0 (0%)             | 2 (6.45%)   | Mar-18, May-07 |                31 | B.2, B.2.2                            |                              29 |           0.0575 |
| UK79           | 30 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-24, May-04 |                30 | B.1                                   |                              32 |           0.0442 |
| UK36           | 11 (36.67%)   | 1 (3.33%)          | 18 (60.0%)  | Mar-19, Apr-18 |                30 | B.1                                   |                              48 |           0.0216 |
| UK15           | 25 (89.29%)   | 0 (0%)             | 3 (10.71%)  | Mar-01, Apr-16 |                28 | B.1.1                                 |                              50 |           0.0341 |
| UK51           | 26 (96.3%)    | 0 (0%)             | 1 (3.7%)    | Mar-26, May-08 |                27 | B.1.36                                |                              28 |           0.0591 |
| UK158          | 26 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, May-31 |                26 | B.1.1, B.1.1.2                        |                               5 |           0.552  |
| UK39           | 0 (0%)        | 0 (0%)             | 24 (100.0%) | Mar-24, Apr-07 |                24 | A.2                                   |                              59 |           0.0103 |
| UK601          | 3 (13.64%)    | 19 (86.36%)        | 0 (0%)      | Mar-13, Apr-27 |                22 | B.10                                  |                              39 |           0.0549 |
| UK501          | 19 (95.0%)    | 0 (0%)             | 1 (5.0%)    | Mar-25, Apr-19 |                20 | B.1                                   |                              47 |           0.028  |
| UK5309         | 20 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-25, May-02 |                20 | B.1.1, B.1.1.10                       |                              34 |           0.0588 |
| UK497          | 20 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, Apr-27 |                20 | A.2                                   |                              39 |           0.0607 |
| UK829          | 20 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, Apr-17 |                20 | B.2.5                                 |                              49 |           0.0376 |
| UK101          | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, Apr-21 |                19 | B.1.5                                 |                              45 |           0.0383 |
| UK276          | 18 (94.74%)   | 0 (0%)             | 1 (5.26%)   | Mar-18, Apr-09 |                19 | B.1.1                                 |                              57 |           0.0214 |
| UK339          | 17 (89.47%)   | 0 (0%)             | 2 (10.53%)  | Mar-14, Apr-16 |                19 | B.3                                   |                              50 |           0.0367 |
| UK77           | 18 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-26 |                18 | B.2                                   |                              40 |           0.05   |
| UK1721         | 18 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, May-08 |                18 | B.1                                   |                              28 |           0.0966 |
| UK109          | 14 (77.78%)   | 4 (22.22%)         | 0 (0%)      | Mar-14, May-01 |                18 | B.1.5                                 |                              35 |           0.0807 |
| UK517          | 18 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-02, Apr-18 |                18 | B.1.1                                 |                              48 |           0.0576 |
| UK85           | 17 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-11 |                17 | B.3                                   |                              55 |           0.0295 |
| UK3126         | 17 (100.0%)   | 0 (0%)             | 0 (0%)      | May-04, May-09 |                17 | B.1.1                                 |                              27 |           0.0116 |
| UK513          | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-03, Apr-27 |                16 | B.1.p11                               |                              39 |           0.041  |
| UK31           | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, Apr-20 |                16 | B.3                                   |                              46 |           0.0435 |
| UK6            | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-12, Apr-14 |                16 | B.1                                   |                              52 |           0.0423 |
| UK179          | 15 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-26, Apr-18 |                15 | B.1.1, B.1.1.p11                      |                              48 |           0.0342 |
| UK462          | 15 (100.0%)   | 0 (0%)             | 0 (0%)      | May-02, May-18 |                15 | B.1                                   |                              18 |           0.0635 |
| UK371          | 15 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-29, May-09 |                15 | B.1.1                                 |                              27 |           0.1085 |
| UK274          | 15 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, Apr-08 |                15 | B.3                                   |                              58 |           0.0222 |
| UK240          | 12 (80.0%)    | 0 (0%)             | 3 (20.0%)   | Mar-14, May-01 |                15 | B.3, B.2, B                           |                              35 |           0.098  |
| UK173          | 14 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-13 |                14 | B                                     |                              53 |           0.0406 |
| UK146          | 14 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-01, May-07 |                14 | B.1.1                                 |                              29 |           0.0955 |
| UK275          | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, Apr-17 |                13 | B.1.13                                |                              49 |           0.0595 |
| UK5649         | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-05, May-04 |                13 | B.2.6                                 |                              32 |           0.0755 |
| UK569          | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-18 |                13 | B.1.1                                 |                              48 |           0.0451 |
| UK1207         | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-29, May-12 |                13 | B.1.1                                 |                              24 |           0.1528 |
| UK706          | 1 (7.69%)     | 12 (92.31%)        | 0 (0%)      | Apr-01, Apr-29 |                13 | B.1.1                                 |                              37 |           0.0631 |
| UK1703         | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-09, May-01 |                12 | B.1                                   |                              35 |           0.0571 |
| UK3021         | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-16 |                12 | B.1                                   |                              50 |           0.0564 |
| UK1006         | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-04, Apr-29 |                12 | B.1.1                                 |                              37 |           0.0614 |
| UK241          | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-22, Apr-16 |                12 | B.1.5.3                               |                              50 |           0.0455 |
| UK566          | 11 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-02, Apr-21 |                11 | B.1.1, B.1.1.10                       |                              45 |           0.0422 |
| UK174          | 11 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-19, May-02 |                11 | B.1.5                                 |                              34 |           0.1294 |
| UK2200         | 3 (27.27%)    | 2 (18.18%)         | 6 (54.55%)  | Mar-20, Apr-29 |                11 | B.1.5, B.1.5.6                        |                              37 |           0.1081 |
| UK198          | 2 (20.0%)     | 2 (20.0%)          | 6 (60.0%)   | Mar-23, Apr-12 |                10 | B.1.5                                 |                              54 |           0.0412 |
| UK18           | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-12, Apr-14 |                10 | B.1.1.7                               |                              52 |           0.0705 |
| UK2045         | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-17, Apr-29 |                10 | B.1                                   |                              37 |           0.1291 |
| UK394          | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-20, May-18 |                10 | B.1.1                                 |                              18 |           0.3642 |
| UK134          | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-09, Apr-07 |                10 | B.1                                   |                              59 |           0.0546 |
| UK132          | 9 (90.0%)     | 0 (0%)             | 1 (10.0%)   | Mar-27, Apr-28 |                10 | B.1                                   |                              38 |           0.0936 |
| UK119          | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-24 |                10 | B.2.5                                 |                              42 |           0.0847 |
| UK58           | 6 (66.67%)    | 0 (0%)             | 3 (33.33%)  | Mar-17, Apr-09 |                 9 | B.1                                   |                              57 |           0.0504 |
| UK632          | 8 (88.89%)    | 0 (0%)             | 1 (11.11%)  | Mar-25, Apr-13 |                 9 | B.1.1                                 |                              53 |           0.0448 |
| UK448          | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-04, May-02 |                 9 | B.1.1                                 |                              34 |           0.1029 |
| UK71           | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-26, May-06 |                 9 | B                                     |                              30 |           0.1708 |
| UK12           | 8 (88.89%)    | 1 (11.11%)         | 0 (0%)      | Mar-22, Apr-13 |                 9 | B.1.p11                               |                              53 |           0.0519 |
| UK64           | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-01, Apr-15 |                 8 | B.1                                   |                              51 |           0.0392 |
| UK335          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-27, Apr-07 |                 8 | B.1.1                                 |                              59 |           0.0266 |
| UK46           | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-14, Apr-15 |                 8 | B.2.1                                 |                              51 |           0.0896 |
| UK86           | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-23, Mar-30 |                 8 | B.1                                   |                              67 |           0.0149 |
| UK287          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-31, Apr-18 |                 8 | B.1                                   |                              48 |           0.0536 |
| UK27           | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-12, Apr-19 |                 8 | B.1.1                                 |                              47 |           0.1155 |
| UK23           | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-21, May-09 |                 8 | B.9                                   |                              27 |           0.2593 |
| UK384          | 7 (87.5%)     | 0 (0%)             | 1 (12.5%)   | Feb-28, Mar-30 |                 8 | B.2.1                                 |                              67 |           0.0661 |
| UK759          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-28, Apr-04 |                 8 | B.1.1                                 |                              62 |           0.0161 |
| UK5503         | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-02, May-13 |                 7 | B.1                                   |                              23 |           0.2971 |
| UK203          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-28, Apr-17 |                 7 | B.1.1                                 |                              49 |           0.068  |
| UK404          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-18, Apr-06 |                 7 | B.1                                   |                              60 |           0.0528 |
| UK5348         | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-14, Apr-24 |                 7 | B.1.1                                 |                              42 |           0.1627 |
| UK523          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-25, May-14 |                 7 | B.1.1                                 |                              22 |           0.1439 |
| UK38           | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-04, Apr-08 |                 7 | B.2.1                                 |                              58 |           0.1006 |
| UK70           | 6 (85.71%)    | 1 (14.29%)         | 0 (0%)      | Mar-28, Apr-18 |                 7 | B.2                                   |                              48 |           0.0729 |
| UK2906         | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-12, Apr-20 |                 7 | B.1                                   |                              46 |           0.1413 |
| UK3692         | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-23, Apr-29 |                 7 | B.1.1                                 |                              37 |           0.1667 |
| UK284          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-02, Apr-20 |                 6 | B.1.1                                 |                              46 |           0.0783 |
| UK47           | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-22, Apr-20 |                 6 | B.1.1                                 |                              46 |           0.1261 |
| UK49           | 4 (66.67%)    | 1 (16.67%)         | 1 (16.67%)  | Mar-18, Apr-12 |                 6 | B.9                                   |                              54 |           0.0926 |
| UK32           | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-10, May-01 |                 6 | B.1.1                                 |                              35 |           0.12   |
| UK4237         | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-02, Apr-16 |                 6 | B.1.1                                 |                              50 |           0.056  |
| UK581          | 0 (0%)        | 6 (100.0%)         | 0 (0%)      | Apr-06, May-01 |                 6 | B.1.1                                 |                              35 |           0.1429 |
| UK5549         | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-12, Apr-06 |                 6 | B.2.2                                 |                              60 |           0.0833 |
| UK340          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-09, May-17 |                 6 | B.1.1                                 |                              19 |           0.4    |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | SANG     |            14 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK42 |   UK167 |   UK2913 |   UK199 |   UK5741 |   UK66 |   UK2916 |   UK5523 |   UK370 |
|:------------------|------:|-------:|--------:|---------:|--------:|---------:|-------:|---------:|---------:|--------:|
| 2020-02-23        |     0 |      0 |       0 |        0 |       0 |        0 |      0 |        2 |        0 |       0 |
| 2020-03-01        |     1 |      1 |       0 |        0 |       0 |        0 |      0 |        3 |        0 |       0 |
| 2020-03-08        |     8 |      1 |       3 |        1 |       0 |        2 |      0 |        3 |        0 |       1 |
| 2020-03-15        |    14 |      8 |       3 |        2 |       2 |        0 |      2 |        5 |        0 |       0 |
| 2020-03-22        |    23 |     13 |       8 |        8 |       7 |        3 |      2 |        4 |        0 |       2 |
| 2020-03-29        |    21 |     13 |       8 |       10 |      10 |        7 |      7 |        6 |        0 |       8 |
| 2020-04-05        |    26 |     14 |      10 |       10 |       9 |        7 |      7 |        4 |        0 |       9 |
| 2020-04-12        |    24 |     11 |       8 |        6 |       7 |        4 |      6 |        1 |        0 |       1 |
| 2020-04-19        |    22 |     11 |       7 |        5 |       1 |        6 |      2 |        4 |        0 |       1 |
| 2020-04-26        |    20 |      6 |       2 |        4 |       2 |        2 |      2 |        1 |        1 |       1 |
| 2020-05-03        |    15 |      6 |       5 |        0 |       1 |        2 |      2 |        1 |        1 |       5 |
| 2020-05-10        |    12 |      0 |       4 |        1 |       2 |        1 |      2 |        1 |        3 |       1 |
| 2020-05-17        |     9 |      1 |       0 |        0 |       0 |        0 |      0 |        0 |        1 |       0 |
| 2020-05-24        |     2 |      0 |       0 |        0 |       0 |        0 |      0 |        0 |        0 |       0 |
| 2020-05-31        |     1 |      0 |       1 |        1 |       0 |        0 |      0 |        0 |        3 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-02-27 |                            0 |                                1 |       1 |
| 2020-02-28 |                            0 |                                1 |       1 |
| 2020-03-01 |                            0 |                                1 |       1 |
| 2020-03-02 |                            1 |                                1 |       2 |
| 2020-03-03 |                            1 |                                2 |       3 |
| 2020-03-04 |                            0 |                                4 |       4 |
| 2020-03-07 |                            0 |                                2 |       2 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-09 |                            3 |                                2 |       5 |
| 2020-03-10 |                            2 |                                4 |       6 |
| 2020-03-11 |                            2 |                                5 |       7 |
| 2020-03-12 |                            3 |                                9 |      12 |
| 2020-03-13 |                            3 |                                8 |      11 |
| 2020-03-14 |                            0 |                                7 |       7 |
| 2020-03-15 |                            1 |                                0 |       1 |
| 2020-03-16 |                            1 |                                6 |       7 |
| 2020-03-17 |                            1 |                                4 |       5 |
| 2020-03-18 |                            2 |                               10 |      12 |
| 2020-03-19 |                            2 |                                4 |       6 |
| 2020-03-20 |                            4 |                                6 |      10 |
| 2020-03-21 |                            3 |                               10 |      13 |
| 2020-03-22 |                            5 |                                8 |      13 |
| 2020-03-23 |                            3 |                               22 |      25 |
| 2020-03-24 |                            6 |                                4 |      10 |
| 2020-03-25 |                            2 |                                7 |       9 |
| 2020-03-26 |                            6 |                                9 |      15 |
| 2020-03-27 |                            6 |                                4 |      10 |
| 2020-03-28 |                            5 |                                5 |      10 |
| 2020-03-29 |                            7 |                                6 |      13 |
| 2020-03-30 |                           13 |                                5 |      18 |
| 2020-03-31 |                           15 |                                7 |      22 |
| 2020-04-01 |                           10 |                                6 |      16 |
| 2020-04-02 |                           12 |                                5 |      17 |
| 2020-04-03 |                            4 |                                6 |      10 |
| 2020-04-04 |                            8 |                                6 |      14 |
| 2020-04-05 |                           11 |                                6 |      17 |
| 2020-04-06 |                           11 |                                6 |      17 |
| 2020-04-07 |                            7 |                                2 |       9 |
| 2020-04-08 |                            2 |                                2 |       4 |
| 2020-04-09 |                            3 |                                2 |       5 |
| 2020-04-10 |                            3 |                                4 |       7 |
| 2020-04-11 |                            0 |                                2 |       2 |
| 2020-04-12 |                            2 |                                1 |       3 |
| 2020-04-13 |                            5 |                                0 |       5 |
| 2020-04-14 |                            3 |                                1 |       4 |
| 2020-04-15 |                            1 |                                0 |       1 |
| 2020-04-16 |                            3 |                                1 |       4 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            2 |                                1 |       3 |
| 2020-04-19 |                            3 |                                0 |       3 |
| 2020-04-20 |                            1 |                                1 |       2 |
| 2020-04-21 |                            2 |                                2 |       4 |
| 2020-04-23 |                            1 |                                2 |       3 |
| 2020-04-24 |                            2 |                                0 |       2 |
| 2020-04-25 |                            1 |                                2 |       3 |
| 2020-04-26 |                            1 |                                2 |       3 |
| 2020-04-28 |                            1 |                                0 |       1 |
| 2020-04-29 |                            1 |                                1 |       2 |
| 2020-05-01 |                            1 |                                1 |       2 |
| 2020-05-02 |                            0 |                                1 |       1 |
| 2020-05-03 |                            3 |                                0 |       3 |
| 2020-05-04 |                            2 |                                1 |       3 |
| 2020-05-05 |                            1 |                                0 |       1 |
| 2020-05-07 |                            2 |                                1 |       3 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Scotland |   Northern Ireland |
|:-----------|----------:|-----------:|-------------------:|
| 2020-02-27 |         1 |          0 |                  0 |
| 2020-02-28 |         2 |          0 |                  0 |
| 2020-03-01 |         1 |          0 |                  0 |
| 2020-03-02 |         6 |          0 |                  0 |
| 2020-03-03 |         7 |          0 |                  0 |
| 2020-03-04 |         8 |          0 |                  0 |
| 2020-03-05 |         1 |          0 |                  0 |
| 2020-03-06 |         2 |          0 |                  0 |
| 2020-03-07 |         3 |          0 |                  0 |
| 2020-03-08 |         5 |          0 |                  0 |
| 2020-03-09 |        10 |          0 |                  0 |
| 2020-03-10 |        19 |          0 |                  0 |
| 2020-03-11 |        15 |          0 |                  0 |
| 2020-03-12 |        24 |          0 |                  0 |
| 2020-03-13 |        29 |          0 |                  0 |
| 2020-03-14 |        21 |          0 |                  0 |
| 2020-03-15 |        13 |          0 |                  0 |
| 2020-03-16 |        25 |          0 |                  0 |
| 2020-03-17 |        27 |          0 |                  0 |
| 2020-03-18 |        40 |          0 |                  0 |
| 2020-03-19 |        42 |          0 |                  0 |
| 2020-03-20 |        54 |          0 |                  0 |
| 2020-03-21 |        79 |          3 |                  0 |
| 2020-03-22 |        84 |          3 |                  0 |
| 2020-03-23 |       102 |         38 |                  0 |
| 2020-03-24 |        38 |         59 |                  0 |
| 2020-03-25 |        49 |         41 |                  0 |
| 2020-03-26 |       103 |         38 |                  8 |
| 2020-03-27 |        70 |         26 |                  7 |
| 2020-03-28 |       122 |          1 |                  0 |
| 2020-03-29 |       169 |          7 |                  0 |
| 2020-03-30 |       217 |         61 |                  6 |
| 2020-03-31 |       189 |         12 |                  7 |
| 2020-04-01 |       230 |          0 |                  0 |
| 2020-04-02 |       214 |          0 |                  1 |
| 2020-04-03 |       232 |          1 |                  0 |
| 2020-04-04 |       168 |          0 |                  1 |
| 2020-04-05 |       211 |          3 |                  0 |
| 2020-04-06 |       267 |         29 |                 18 |
| 2020-04-07 |       185 |         33 |                  5 |
| 2020-04-08 |       141 |          0 |                 14 |
| 2020-04-09 |       153 |          0 |                  1 |
| 2020-04-10 |       167 |          0 |                 19 |
| 2020-04-11 |        85 |          0 |                 14 |
| 2020-04-12 |        73 |          0 |                 23 |
| 2020-04-13 |        69 |          0 |                 22 |
| 2020-04-14 |       138 |          0 |                 11 |
| 2020-04-15 |       112 |          0 |                 13 |
| 2020-04-16 |       179 |          0 |                  0 |
| 2020-04-17 |       119 |          0 |                  6 |
| 2020-04-18 |       118 |          0 |                  7 |
| 2020-04-19 |        89 |          0 |                  2 |
| 2020-04-20 |       116 |          0 |                  2 |
| 2020-04-21 |        86 |          0 |                 17 |
| 2020-04-22 |        36 |          0 |                 23 |
| 2020-04-23 |        49 |          0 |                 11 |
| 2020-04-24 |        47 |          0 |                  2 |
| 2020-04-25 |        28 |          0 |                  5 |
| 2020-04-26 |        32 |          0 |                  2 |
| 2020-04-27 |        33 |          0 |                  2 |
| 2020-04-28 |        22 |          0 |                  9 |
| 2020-04-29 |        49 |          0 |                 11 |
| 2020-04-30 |        54 |          0 |                 15 |
| 2020-05-01 |        72 |          0 |                  7 |
| 2020-05-02 |        29 |          0 |                  2 |
| 2020-05-03 |        20 |          0 |                  0 |
| 2020-05-04 |        66 |          0 |                  0 |
| 2020-05-05 |        30 |          0 |                  0 |
| 2020-05-06 |        57 |          0 |                  0 |
| 2020-05-07 |        54 |          0 |                  0 |
| 2020-05-08 |        35 |          0 |                  0 |
| 2020-05-09 |        25 |          0 |                  0 |
| 2020-05-10 |        22 |          0 |                  0 |
| 2020-05-11 |        23 |          0 |                  0 |
| 2020-05-12 |        13 |          0 |                  0 |
| 2020-05-13 |        20 |          0 |                  0 |
| 2020-05-14 |        18 |          0 |                  0 |
| 2020-05-15 |        27 |          0 |                  0 |
| 2020-05-16 |        21 |          0 |                  0 |
| 2020-05-17 |        10 |          0 |                  0 |
| 2020-05-18 |        26 |          0 |                  0 |
| 2020-05-19 |         6 |          0 |                  0 |
| 2020-05-20 |         7 |          0 |                  0 |
| 2020-05-21 |         5 |          0 |                  0 |
| 2020-05-22 |         4 |          0 |                  0 |
| 2020-05-23 |         6 |          0 |                  0 |
| 2020-05-24 |         1 |          0 |                  0 |
| 2020-05-25 |         1 |          0 |                  0 |
| 2020-05-26 |         1 |          0 |                  0 |
| 2020-05-27 |         1 |          0 |                  0 |
| 2020-05-28 |         1 |          0 |                  0 |
| 2020-05-29 |         1 |          0 |                  0 |
| 2020-05-30 |         3 |          0 |                  0 |
| 2020-05-31 |         8 |          0 |                  0 |
| 2020-06-01 |         9 |          0 |                  0 |
| 2020-06-04 |         2 |          0 |                  0 |
| 2020-06-05 |         1 |          0 |                  0 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country          |   Number of sequences | Sequence group   |
|:-----------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN               | Scotland         |                     1 | 1-10             |
| ANTRIM                 | Northern Ireland |                   156 | 150-200          |
| ARMAGH                 | Northern Ireland |                     3 | 1-10             |
| BEDFORDSHIRE           | England          |                   403 | 400-500          |
| BERKSHIRE              | England          |                     3 | 1-10             |
| BRISTOL                | England          |                     2 | 1-10             |
| BUCKINGHAMSHIRE        | England          |                   312 | 300-400          |
| CAMBRIDGESHIRE         | England          |                   192 | 150-200          |
| CARMARTHENSHIRE        | Wales            |                     1 | 1-10             |
| CORNWALL               | England          |                    19 | 10-50            |
| DERBYSHIRE             | England          |                     1 | 1-10             |
| DEVON                  | England          |                    72 | 50-100           |
| DORSET                 | England          |                   166 | 150-200          |
| DOWN                   | Northern Ireland |                   111 | 100-150          |
| DUMFRIES AND GALLOWAY  | Scotland         |                    25 | 10-50            |
| DURHAM                 | England          |                     7 | 1-10             |
| EAST AYRSHIRE          | Scotland         |                    31 | 10-50            |
| EDINBURGH              | Scotland         |                     1 | 1-10             |
| ESSEX                  | England          |                  1021 | >500             |
| FALKIRK                | Scotland         |                    22 | 10-50            |
| FERMANAGH              | Northern Ireland |                     1 | 1-10             |
| GLASGOW                | Scotland         |                   159 | 150-200          |
| GLOUCESTERSHIRE        | England          |                   617 | >500             |
| GREATER LONDON         | England          |                   439 | 400-500          |
| HAMPSHIRE              | England          |                    34 | 10-50            |
| HEREFORDSHIRE          | England          |                    33 | 10-50            |
| HERTFORDSHIRE          | England          |                   545 | >500             |
| LINCOLNSHIRE           | England          |                     1 | 1-10             |
| LONDONDERRY            | Northern Ireland |                    13 | 10-50            |
| MERSEYSIDE             | England          |                     1 | 1-10             |
| MONMOUTHSHIRE          | Wales            |                     3 | 1-10             |
| NORFOLK                | England          |                    16 | 10-50            |
| NORTH LANARKSHIRE      | Scotland         |                    55 | 50-100           |
| NORTH YORKSHIRE        | England          |                    28 | 10-50            |
| NORTHAMPTONSHIRE       | England          |                     8 | 1-10             |
| NOTTINGHAMSHIRE        | England          |                     3 | 1-10             |
| OXFORDSHIRE            | England          |                     6 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland         |                    28 | 10-50            |
| RENFREWSHIRE           | Scotland         |                    31 | 10-50            |
| SHROPSHIRE             | England          |                     3 | 1-10             |
| SOMERSET               | England          |                   529 | >500             |
| SOUTH YORKSHIRE        | England          |                    10 | 10-50            |
| SUFFOLK                | England          |                   291 | 250-300          |
| SURREY                 | England          |                    22 | 10-50            |
| SUSSEX                 | England          |                     1 | 1-10             |
| TYRONE                 | Northern Ireland |                     8 | 1-10             |
| WARWICKSHIRE           | England          |                     1 | 1-10             |
| WILTSHIRE              | England          |                   334 | 300-400          |

\pagebreak






