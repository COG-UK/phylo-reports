







# Lineages report for SANG




This report gives summaries of UK specific lineages sequenced by SANG for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-09. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
7881 sequences in the UK from the sequencing centre SANG have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 439 and the maximum is 3652


Sequences which were replicates or too error-prone were removed from this analysis.



409 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 21 that remain:
13 are pending extinction, ie last seen three weeks ago.
2 lineages have gone quiet, ie haven't been seen this week.
4 lineages have reactivated.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England       | Northern Ireland   | Scotland    | Date range     |   Total sequences | Global lineage                                                         |   Time since last sample (days) |   Activity score |
|:---------------|:--------------|:-------------------|:------------|:---------------|------------------:|:-----------------------------------------------------------------------|--------------------------------:|-----------------:|
| UK5            | 2395 (86.15%) | 312 (11.22%)       | 73 (2.63%)  | Mar-03, Jun-07 |              2780 | B.1.1.4, B.1.1.13, B.1.1.1, B.1.1.5, B.1.1.10, B.1.1, B.1.1.3, B.1.1.2 |                               2 |           0.0173 |
| UK107          | 412 (96.26%)  | 10 (2.34%)         | 6 (1.4%)    | Mar-08, May-01 |               428 | B.2.1, B                                                               |                              39 |           0.0032 |
| UK42           | 343 (89.79%)  | 1 (0.26%)          | 38 (9.95%)  | Mar-03, May-17 |               382 | B.1.5, B.1.35, B.1.p73, B.1.p11, B.1, B.1.72                           |                              23 |           0.0086 |
| UK5676         | 131 (76.16%)  | 0 (0%)             | 41 (23.84%) | Mar-09, Apr-20 |               172 | B.2                                                                    |                              50 |           0.0049 |
| UK2464         | 108 (65.45%)  | 0 (0%)             | 57 (34.55%) | Mar-12, Apr-27 |               165 | B.1.p11, B.1                                                           |                              43 |           0.0065 |
| UK167          | 120 (76.43%)  | 23 (14.65%)        | 14 (8.92%)  | Mar-11, Jun-04 |               157 | B.1                                                                    |                               5 |           0.109  |
| UK2913         | 117 (80.69%)  | 17 (11.72%)        | 11 (7.59%)  | Mar-11, Jun-01 |               145 | B.1.p11, B.1                                                           |                               8 |           0.0712 |
| UK199          | 80 (71.43%)   | 2 (1.79%)          | 30 (26.79%) | Mar-14, May-13 |               112 | B.1.5.5, B.1, B.1.5                                                    |                              27 |           0.02   |
| UK9            | 111 (100.0%)  | 0 (0%)             | 0 (0%)      | Mar-19, May-04 |               111 | B.1.13                                                                 |                              36 |           0.0116 |
| UK72           | 106 (95.5%)   | 2 (1.8%)           | 3 (2.7%)    | Mar-10, Apr-26 |               111 | B                                                                      |                              44 |           0.0097 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/SANG/figures/report_SANG_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 24 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/SANG/figures/report_SANG_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/SANG/figures/report_SANG_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/SANG/figures/report_SANG_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/SANG/figures/report_SANG_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 587 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/regional_reports/SANG/figures/report_SANG_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England       | Northern Ireland   | Scotland    | Date range     |   Total sequences | Global lineage                                                         |   Time since last sample (days) | Activity score   |
|:---------------|:--------------|:-------------------|:------------|:---------------|------------------:|:-----------------------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | 2395 (86.15%) | 312 (11.22%)       | 73 (2.63%)  | Mar-03, Jun-07 |              2780 | B.1.1.4, B.1.1.13, B.1.1.1, B.1.1.5, B.1.1.10, B.1.1, B.1.1.3, B.1.1.2 |                               2 | 0.0173           |
| UK107          | 412 (96.26%)  | 10 (2.34%)         | 6 (1.4%)    | Mar-08, May-01 |               428 | B.2.1, B                                                               |                              39 | 0.0032           |
| UK42           | 343 (89.79%)  | 1 (0.26%)          | 38 (9.95%)  | Mar-03, May-17 |               382 | B.1.5, B.1.35, B.1.p73, B.1.p11, B.1, B.1.72                           |                              23 | 0.0086           |
| UK5676         | 131 (76.16%)  | 0 (0%)             | 41 (23.84%) | Mar-09, Apr-20 |               172 | B.2                                                                    |                              50 | 0.0049           |
| UK2464         | 108 (65.45%)  | 0 (0%)             | 57 (34.55%) | Mar-12, Apr-27 |               165 | B.1.p11, B.1                                                           |                              43 | 0.0065           |
| UK167          | 120 (76.43%)  | 23 (14.65%)        | 14 (8.92%)  | Mar-11, Jun-04 |               157 | B.1                                                                    |                               5 | 0.109            |
| UK2913         | 117 (80.69%)  | 17 (11.72%)        | 11 (7.59%)  | Mar-11, Jun-01 |               145 | B.1.p11, B.1                                                           |                               8 | 0.0712           |
| UK199          | 80 (71.43%)   | 2 (1.79%)          | 30 (26.79%) | Mar-14, May-13 |               112 | B.1.5.5, B.1, B.1.5                                                    |                              27 | 0.02             |
| UK9            | 111 (100.0%)  | 0 (0%)             | 0 (0%)      | Mar-19, May-04 |               111 | B.1.13                                                                 |                              36 | 0.0116           |
| UK72           | 106 (95.5%)   | 2 (1.8%)           | 3 (2.7%)    | Mar-10, Apr-26 |               111 | B                                                                      |                              44 | 0.0097           |
| UK36           | 18 (16.82%)   | 1 (0.93%)          | 88 (82.24%) | Mar-19, May-15 |               107 | B.1                                                                    |                              25 | 0.0215           |
| UK66           | 86 (98.85%)   | 0 (0%)             | 1 (1.15%)   | Mar-18, May-16 |                87 | B.1.1.8                                                                |                              24 | 0.0286           |
| UK5741         | 82 (98.8%)    | 0 (0%)             | 1 (1.2%)    | Mar-11, May-10 |                83 | B.1                                                                    |                              30 | 0.0244           |
| UK494          | 83 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, May-01 |                83 | B.1.p11, B.1                                                           |                              39 | 0.0128           |
| UK240          | 70 (88.61%)   | 0 (0%)             | 9 (11.39%)  | Mar-12, May-01 |                79 | B.2.5, B.2                                                             |                              39 | 0.0164           |
| UK28           | 79 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-22, May-08 |                79 | B.1.1.10                                                               |                              32 | 0.0188           |
| UK2735         | 56 (73.68%)   | 13 (17.11%)        | 7 (9.21%)   | Mar-24, May-07 |                76 | B.1.1                                                                  |                              33 | 0.0178           |
| UK2916         | 71 (95.95%)   | 1 (1.35%)          | 2 (2.7%)    | Feb-27, May-11 |                74 | B.1                                                                    |                              29 | 0.035            |
| UK5561         | 63 (94.03%)   | 0 (0%)             | 4 (5.97%)   | Mar-05, May-07 |                67 | B.2.2, B.2                                                             |                              33 | 0.0289           |
| UK61           | 60 (96.77%)   | 0 (0%)             | 2 (3.23%)   | Mar-12, May-18 |                62 | B.3                                                                    |                              22 | 0.0499           |
| UK109          | 53 (86.89%)   | 8 (13.11%)         | 0 (0%)      | Mar-14, May-11 |                61 | B.1.5                                                                  |                              29 | 0.0333           |
| UK40           | 0 (0%)        | 0 (0%)             | 61 (100.0%) | Mar-19, Apr-07 |                61 | B.16                                                                   |                              63 | 0.005            |
| UK5523         | 51 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-16, Jun-01 |                51 | B.1                                                                    |                               8 | 0.115            |
| UK13           | 46 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, May-12 |                46 | B.1.1                                                                  |                              28 | 0.0476           |
| UK5498         | 44 (97.78%)   | 0 (0%)             | 1 (2.22%)   | Mar-14, May-15 |                45 | B.2                                                                    |                              25 | 0.0564           |
| UK370          | 33 (75.0%)    | 6 (13.64%)         | 5 (11.36%)  | Mar-12, May-12 |                44 | B.1.1.10                                                               |                              28 | 0.0507           |
| UK63           | 42 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-26, Apr-30 |                42 | B.1.1                                                                  |                              40 | 0.0213           |
| UK5180         | 38 (92.68%)   | 3 (7.32%)          | 0 (0%)      | Mar-13, Apr-25 |                41 | B.1.1.7                                                                |                              45 | 0.0239           |
| UK668          | 21 (52.5%)    | 0 (0%)             | 19 (47.5%)  | Mar-21, May-07 |                40 | B.1                                                                    |                              33 | 0.0365           |
| UK4            | 37 (94.87%)   | 1 (2.56%)          | 1 (2.56%)   | Mar-11, Apr-25 |                39 | B                                                                      |                              45 | 0.0263           |
| UK5098         | 1 (2.56%)     | 0 (0%)             | 38 (97.44%) | Mar-19, Apr-16 |                39 | B.1.p73, B.1                                                           |                              54 | 0.0136           |
| UK15           | 34 (87.18%)   | 1 (2.56%)          | 4 (10.26%)  | Mar-01, Apr-21 |                39 | B.1.1                                                                  |                              49 | 0.0274           |
| UK39           | 0 (0%)        | 0 (0%)             | 36 (100.0%) | Mar-20, Apr-07 |                36 | A.2                                                                    |                              63 | 0.0082           |
| UK335          | 33 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-17, May-12 |                33 | B.1.1                                                                  |                              28 | 0.0625           |
| UK37           | 33 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-17, May-04 |                33 | B.1.30                                                                 |                              36 | 0.0417           |
| UK51           | 31 (96.88%)   | 0 (0%)             | 1 (3.12%)   | Mar-26, May-08 |                32 | B.1.36                                                                 |                              32 | 0.0433           |
| UK5309         | 30 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-25, May-16 |                30 | B.1.1, B.1.1.10                                                        |                              24 | 0.0747           |
| UK79           | 30 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-24, May-04 |                30 | B.1                                                                    |                              36 | 0.0393           |
| UK636          | 29 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-13 |                29 | B.1.1                                                                  |                              57 | 0.0175           |
| UK31           | 29 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-15, May-17 |                29 | B.3                                                                    |                              23 | 0.0978           |
| UK482          | 1 (3.57%)     | 27 (96.43%)        | 0 (0%)      | Apr-04, May-05 |                28 | B.1.1                                                                  |                              35 | 0.0328           |
| UK601          | 5 (18.52%)    | 21 (77.78%)        | 1 (3.7%)    | Mar-13, May-11 |                27 | B.10                                                                   |                              29 | 0.0782           |
| UK158          | 26 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-24 |                26 | B.1.1                                                                  |                              46 | 0.0278           |
| UK462          | 23 (100.0%)   | 0 (0%)             | 0 (0%)      | May-02, Jun-09 |                23 | B.1                                                                    |                               0 | active today     |
| UK501          | 20 (95.24%)   | 0 (0%)             | 1 (4.76%)   | Mar-25, Apr-19 |                21 | B.1                                                                    |                              51 | 0.0245           |
| UK829          | 21 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, Apr-23 |                21 | B.2.5                                                                  |                              47 | 0.0436           |
| UK497          | 20 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, Apr-27 |                20 | A.2                                                                    |                              43 | 0.0551           |
| UK1207         | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-24, May-12 |                19 | B.1.1                                                                  |                              28 | 0.0972           |
| UK101          | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, Apr-21 |                19 | B.1.5                                                                  |                              49 | 0.0351           |
| UK371          | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, May-06 |                19 | B.1.1                                                                  |                              34 | 0.0752           |
| UK517          | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-02, Apr-23 |                19 | B.1.1                                                                  |                              47 | 0.0615           |
| UK77           | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-26 |                19 | B.2                                                                    |                              44 | 0.0429           |
| UK27           | 19 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-12, May-11 |                19 | B.1.1                                                                  |                              29 | 0.1149           |
| UK1721         | 18 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, May-08 |                18 | B.1                                                                    |                              32 | 0.0846           |
| UK3126         | 17 (100.0%)   | 0 (0%)             | 0 (0%)      | May-04, May-09 |                17 | B.1.1                                                                  |                              31 | 0.0101           |
| UK617          | 17 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-29, Apr-20 |                17 | B.1.1                                                                  |                              50 | 0.0275           |
| UK339          | 17 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-11 |                17 | B.3                                                                    |                              59 | 0.0275           |
| UK276          | 16 (94.12%)   | 0 (0%)             | 1 (5.88%)   | Mar-18, Apr-13 |                17 | B.1.1                                                                  |                              57 | 0.0285           |
| UK274          | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, Apr-22 |                16 | B.3                                                                    |                              48 | 0.0444           |
| UK6            | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-12, Apr-14 |                16 | B.1                                                                    |                              56 | 0.0393           |
| UK275          | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-13, Apr-24 |                16 | B.1.13                                                                 |                              46 | 0.0609           |
| UK2200         | 8 (50.0%)     | 3 (18.75%)         | 5 (31.25%)  | Mar-17, Apr-29 |                16 | B.1.5.6, B.1.5                                                         |                              41 | 0.0699           |
| UK179          | 16 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-26, Apr-23 |                16 | B.1.1.p11                                                              |                              47 | 0.0397           |
| UK5649         | 15 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-04, May-04 |                15 | B.2.6                                                                  |                              36 | 0.0595           |
| UK706          | 1 (7.14%)     | 13 (92.86%)        | 0 (0%)      | Apr-01, Apr-29 |                14 | B.1.1                                                                  |                              41 | 0.0525           |
| UK5549         | 12 (85.71%)   | 0 (0%)             | 2 (14.29%)  | Mar-12, Apr-06 |                14 | B.2.2                                                                  |                              64 | 0.03             |
| UK605          | 13 (92.86%)   | 0 (0%)             | 1 (7.14%)   | Mar-20, May-18 |                14 | B.1.1                                                                  |                              22 | 0.2063           |
| UK1703         | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, May-01 |                13 | B.1                                                                    |                              39 | 0.0983           |
| UK146          | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-01, May-07 |                13 | B.1.1                                                                  |                              33 | 0.0909           |
| UK173          | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-13 |                13 | B                                                                      |                              57 | 0.0409           |
| UK569          | 13 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-18 |                13 | B.1.1                                                                  |                              52 | 0.0417           |
| UK44           | 3 (25.0%)     | 1 (8.33%)          | 8 (66.67%)  | Mar-23, Apr-16 |                12 | B                                                                      |                              54 | 0.0404           |
| UK3021         | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-16, Apr-16 |                12 | B.1                                                                    |                              54 | 0.0522           |
| UK241          | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-22, Apr-16 |                12 | B.1.5.3                                                                |                              54 | 0.0421           |
| UK448          | 12 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-04, May-02 |                12 | B.1.1                                                                  |                              38 | 0.067            |
| UK70           | 10 (90.91%)   | 1 (9.09%)          | 0 (0%)      | Mar-12, Apr-22 |                11 | B.2                                                                    |                              48 | 0.0854           |
| UK134          | 11 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-09, Apr-07 |                11 | B.1                                                                    |                              63 | 0.046            |
| UK23           | 11 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-18, May-09 |                11 | B.9                                                                    |                              31 | 0.1677           |
| UK132          | 10 (90.91%)   | 0 (0%)             | 1 (9.09%)   | Mar-27, Apr-28 |                11 | B.1                                                                    |                              42 | 0.0762           |
| UK566          | 11 (100.0%)   | 0 (0%)             | 0 (0%)      | Apr-02, Apr-21 |                11 | B.1.1, B.1.1.10                                                        |                              49 | 0.0388           |
| UK174          | 11 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-19, May-02 |                11 | B.1.5                                                                  |                              38 | 0.1158           |
| UK32           | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-29, Apr-14 |                10 | B.1.1                                                                  |                              56 | 0.0317           |
| UK384          | 9 (90.0%)     | 0 (0%)             | 1 (10.0%)   | Feb-28, Apr-03 |                10 | B.2.1                                                                  |                              67 | 0.058            |
| UK18           | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-12, Apr-14 |                10 | B.1.1.7                                                                |                              56 | 0.0655           |
| UK12           | 9 (90.0%)     | 1 (10.0%)          | 0 (0%)      | Mar-22, Apr-23 |                10 | B.1.p11                                                                |                              47 | 0.0757           |
| UK615          | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-28, Apr-18 |                10 | B.1.1                                                                  |                              52 | 0.0449           |
| UK47           | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-21, Apr-20 |                10 | B.1.1                                                                  |                              50 | 0.0667           |
| UK2045         | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-17, Apr-29 |                10 | B.1                                                                    |                              41 | 0.1165           |
| UK58           | 6 (60.0%)     | 0 (0%)             | 4 (40.0%)   | Mar-13, Apr-09 |                10 | B.1                                                                    |                              61 | 0.0492           |
| UK119          | 10 (100.0%)   | 0 (0%)             | 0 (0%)      | Mar-23, Apr-24 |                10 | B.2.5                                                                  |                              46 | 0.0773           |
| UK565          | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-23, May-14 |                 9 | B.1.1                                                                  |                              26 | 0.101            |
| UK3692         | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-02, Apr-29 |                 9 | B.1.1                                                                  |                              41 | 0.0823           |
| UK581          | 0 (0%)        | 9 (100.0%)         | 0 (0%)      | Apr-06, May-01 |                 9 | B.1.1                                                                  |                              39 | 0.0801           |
| UK203          | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-28, Jun-03 |                 9 | B.1.1                                                                  |                               6 | 1.3958           |
| UK71           | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-26, May-06 |                 9 | B                                                                      |                              34 | 0.1507           |
| UK120          | 6 (66.67%)    | 0 (0%)             | 3 (33.33%)  | Mar-04, Jun-07 |                 9 | B                                                                      |                               2 | 5.9375           |
| UK478          | 9 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-30, May-19 |                 9 | B.1.1                                                                  |                              21 | 0.2976           |
| UK287          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-31, Apr-18 |                 8 | B.1                                                                    |                              52 | 0.0495           |
| UK46           | 7 (87.5%)     | 0 (0%)             | 1 (12.5%)   | Mar-14, Apr-15 |                 8 | B.2.1                                                                  |                              55 | 0.0831           |
| UK698          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-23, Mar-30 |                 8 | B.1                                                                    |                              71 | 0.0141           |
| UK5503         | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-31, May-13 |                 8 | B.1                                                                    |                              27 | 0.2275           |
| UK632          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-25, Apr-08 |                 8 | B.1.1                                                                  |                              62 | 0.0323           |
| UK759          | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-28, Apr-04 |                 8 | B.1.1                                                                  |                              66 | 0.0152           |
| UK14           | 2 (25.0%)     | 0 (0%)             | 6 (75.0%)   | Mar-12, Mar-30 |                 8 | B                                                                      |                              71 | 0.0362           |
| UK64           | 8 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-01, Apr-15 |                 8 | B.1                                                                    |                              55 | 0.0364           |
| UK187          | 0 (0%)        | 6 (75.0%)          | 2 (25.0%)   | Mar-21, Apr-24 |                 8 | B.1                                                                    |                              46 | 0.1056           |
| UK598          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-22, Apr-09 |                 7 | B.1.1                                                                  |                              61 | 0.0492           |
| UK5322         | 1 (14.29%)    | 0 (0%)             | 6 (85.71%)  | Mar-22, Mar-29 |                 7 | B.1.1                                                                  |                              72 | 0.0162           |
| UK3509         | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-30, Apr-11 |                 7 | B.1.1.10                                                               |                              59 | 0.0339           |
| UK284          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-02, Apr-22 |                 7 | B.1.1                                                                  |                              48 | 0.0694           |
| UK563          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-10, May-01 |                 7 | B.1.1                                                                  |                              39 | 0.0897           |
| UK291          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-29, May-02 |                 7 | B.1.5                                                                  |                              38 | 0.1491           |
| UK404          | 7 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-18, Apr-06 |                 7 | B.1                                                                    |                              64 | 0.0495           |
| UK433          | 4 (57.14%)    | 0 (0%)             | 3 (42.86%)  | Mar-22, Apr-07 |                 7 | B                                                                      |                              63 | 0.0423           |
| UK100          | 0 (0%)        | 0 (0%)             | 6 (100.0%)  | Mar-22, Apr-07 |                 6 | B.1, B.1.5                                                             |                              63 | 0.0508           |
| UK38           | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-04, Apr-08 |                 6 | B.2.1                                                                  |                              62 | 0.1129           |
| UK2906         | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-28, Apr-20 |                 6 | B.1                                                                    |                              50 | 0.092            |
| UK4658         | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-13, Apr-10 |                 6 | B.2.1                                                                  |                              60 | 0.0933           |
| UK153          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-20, Apr-03 |                 6 | B.2, B.3                                                               |                              67 | 0.0418           |
| UK60           | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-21, Mar-30 |                 6 | B                                                                      |                              71 | 0.0254           |
| UK195          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | May-19, Jun-04 |                 6 | B.1                                                                    |                               5 | 0.64             |
| UK340          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-22, May-17 |                 6 | B.1.1                                                                  |                              23 | 0.2174           |
| UK456          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-03, Apr-23 |                 6 | B.1.1                                                                  |                              47 | 0.0851           |
| UK767          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-05, Apr-19 |                 6 | B.1                                                                    |                              51 | 0.0549           |
| UK4237         | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-02, Apr-16 |                 6 | B.1.1                                                                  |                              54 | 0.0519           |
| UK317          | 4 (66.67%)    | 0 (0%)             | 2 (33.33%)  | Mar-21, Apr-02 |                 6 | B.3                                                                    |                              68 | 0.0353           |
| UK1810         | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-27, Apr-02 |                 6 | B.1, B.1.5                                                             |                              68 | 0.0176           |
| UK121          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Apr-23, May-03 |                 6 | B.1.1.7                                                                |                              37 | 0.0541           |
| UK521          | 6 (100.0%)    | 0 (0%)             | 0 (0%)      | Mar-31, May-01 |                 6 | B.1.1                                                                  |                              39 | 0.159            |
| UK49           | 4 (66.67%)    | 1 (16.67%)         | 1 (16.67%)  | Mar-18, Apr-12 |                 6 | B.9                                                                    |                              58 | 0.0862           |
| UK43           | 0 (0%)        | 0 (0%)             | 6 (100.0%)  | Mar-18, Mar-31 |                 6 | A.5                                                                    |                              70 | 0.0371           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | SANG     |            24 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK42 |   UK167 |   UK2913 |   UK199 |   UK36 |   UK66 |   UK61 |   UK5523 |   UK5498 |
|:------------------|------:|-------:|--------:|---------:|--------:|-------:|-------:|-------:|---------:|---------:|
| 2020-03-01        |     2 |      3 |       0 |        0 |       0 |      0 |      0 |      0 |        0 |        0 |
| 2020-03-08        |    12 |      2 |       3 |        1 |       1 |      0 |      0 |      2 |        0 |        1 |
| 2020-03-15        |    19 |      8 |       4 |        4 |       4 |      2 |      2 |      3 |        0 |        4 |
| 2020-03-22        |    30 |     16 |       9 |       12 |      12 |      6 |      2 |      8 |        0 |        3 |
| 2020-03-29        |    29 |     20 |      11 |       15 |      15 |     10 |      7 |      6 |        0 |        6 |
| 2020-04-05        |    29 |     16 |      12 |       14 |      12 |      5 |      7 |      6 |        0 |        4 |
| 2020-04-12        |    29 |     12 |       8 |        7 |       5 |      4 |      7 |      6 |        1 |        6 |
| 2020-04-19        |    33 |     13 |       6 |        6 |       5 |      0 |      4 |      5 |        1 |        2 |
| 2020-04-26        |    26 |      8 |       2 |        5 |       1 |      1 |      2 |      0 |        1 |        0 |
| 2020-05-03        |    27 |      9 |       7 |        1 |       1 |      0 |      2 |      1 |        1 |        2 |
| 2020-05-10        |    18 |      0 |       3 |        1 |       2 |      1 |      2 |      0 |        3 |        1 |
| 2020-05-17        |    12 |      1 |       0 |        0 |       0 |      0 |      0 |      1 |        1 |        0 |
| 2020-05-24        |     4 |      0 |       0 |        0 |       0 |      0 |      0 |      0 |        0 |        0 |
| 2020-05-31        |     5 |      0 |       1 |        1 |       0 |      0 |      0 |      0 |        3 |        0 |
| 2020-06-07        |     1 |      0 |       0 |        0 |       0 |      0 |      0 |      0 |        0 |        0 |

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
| 2020-03-03 |                            1 |                                3 |       4 |
| 2020-03-04 |                            0 |                                4 |       4 |
| 2020-03-05 |                            2 |                                1 |       3 |
| 2020-03-06 |                            1 |                                0 |       1 |
| 2020-03-07 |                            0 |                                1 |       1 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-09 |                            2 |                                3 |       5 |
| 2020-03-10 |                            3 |                                4 |       7 |
| 2020-03-11 |                            2 |                                7 |       9 |
| 2020-03-12 |                            3 |                               11 |      14 |
| 2020-03-13 |                            5 |                               10 |      15 |
| 2020-03-14 |                            1 |                                4 |       5 |
| 2020-03-15 |                            2 |                                1 |       3 |
| 2020-03-16 |                            1 |                                7 |       8 |
| 2020-03-17 |                            2 |                                5 |       7 |
| 2020-03-18 |                            3 |                               10 |      13 |
| 2020-03-19 |                            1 |                                6 |       7 |
| 2020-03-20 |                            4 |                                9 |      13 |
| 2020-03-21 |                            3 |                               12 |      15 |
| 2020-03-22 |                            7 |                               11 |      18 |
| 2020-03-23 |                            6 |                               16 |      22 |
| 2020-03-24 |                            8 |                                5 |      13 |
| 2020-03-25 |                            3 |                                7 |      10 |
| 2020-03-26 |                            9 |                                9 |      18 |
| 2020-03-27 |                           10 |                                5 |      15 |
| 2020-03-28 |                            8 |                                6 |      14 |
| 2020-03-29 |                            6 |                                5 |      11 |
| 2020-03-30 |                           12 |                                8 |      20 |
| 2020-03-31 |                           11 |                               14 |      25 |
| 2020-04-01 |                           12 |                                6 |      18 |
| 2020-04-02 |                           14 |                                7 |      21 |
| 2020-04-03 |                           10 |                                6 |      16 |
| 2020-04-04 |                           10 |                                5 |      15 |
| 2020-04-05 |                           11 |                                8 |      19 |
| 2020-04-06 |                            8 |                                8 |      16 |
| 2020-04-07 |                            4 |                                2 |       6 |
| 2020-04-08 |                            4 |                                0 |       4 |
| 2020-04-09 |                            5 |                                0 |       5 |
| 2020-04-10 |                            5 |                                5 |      10 |
| 2020-04-11 |                            3 |                                1 |       4 |
| 2020-04-12 |                            4 |                                2 |       6 |
| 2020-04-13 |                            6 |                                1 |       7 |
| 2020-04-14 |                            3 |                                0 |       3 |
| 2020-04-15 |                            2 |                                1 |       3 |
| 2020-04-16 |                            4 |                                6 |      10 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            3 |                                0 |       3 |
| 2020-04-19 |                            2 |                                1 |       3 |
| 2020-04-20 |                            6 |                                0 |       6 |
| 2020-04-21 |                            5 |                                3 |       8 |
| 2020-04-22 |                            5 |                                2 |       7 |
| 2020-04-23 |                            0 |                                6 |       6 |
| 2020-04-24 |                            5 |                                1 |       6 |
| 2020-04-25 |                            2 |                                0 |       2 |
| 2020-04-26 |                            3 |                                1 |       4 |
| 2020-04-27 |                            1 |                                1 |       2 |
| 2020-04-28 |                            2 |                                1 |       3 |
| 2020-04-29 |                            1 |                                1 |       2 |
| 2020-04-30 |                            1 |                                0 |       1 |
| 2020-05-01 |                            2 |                                0 |       2 |
| 2020-05-02 |                            0 |                                1 |       1 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-04 |                            2 |                                1 |       3 |
| 2020-05-05 |                            1 |                                0 |       1 |
| 2020-05-06 |                            3 |                                0 |       3 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-08 |                            2 |                                0 |       2 |
| 2020-05-17 |                            1 |                                0 |       1 |
| 2020-05-19 |                            0 |                                1 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Scotland |   Northern Ireland |
|:-----------|----------:|-----------:|-------------------:|
| 2020-02-27 |         1 |          0 |                  0 |
| 2020-02-28 |         2 |          0 |                  0 |
| 2020-02-29 |         1 |          0 |                  0 |
| 2020-03-01 |         1 |          0 |                  0 |
| 2020-03-02 |         9 |          0 |                  0 |
| 2020-03-03 |        13 |          0 |                  0 |
| 2020-03-04 |         9 |          0 |                  0 |
| 2020-03-05 |         5 |          0 |                  0 |
| 2020-03-06 |         9 |          0 |                  0 |
| 2020-03-07 |         5 |          0 |                  0 |
| 2020-03-08 |         7 |          0 |                  0 |
| 2020-03-09 |        14 |          0 |                  0 |
| 2020-03-10 |        25 |          0 |                  0 |
| 2020-03-11 |        20 |          0 |                  0 |
| 2020-03-12 |        29 |          0 |                  0 |
| 2020-03-13 |        34 |          0 |                  0 |
| 2020-03-14 |        24 |          0 |                  0 |
| 2020-03-15 |        22 |          0 |                  0 |
| 2020-03-16 |        32 |          0 |                  0 |
| 2020-03-17 |        32 |          2 |                  0 |
| 2020-03-18 |        50 |          3 |                  0 |
| 2020-03-19 |        55 |          3 |                  0 |
| 2020-03-20 |        64 |          8 |                  0 |
| 2020-03-21 |        90 |         12 |                  0 |
| 2020-03-22 |        91 |         21 |                  0 |
| 2020-03-23 |       111 |         50 |                  0 |
| 2020-03-24 |        50 |         59 |                  0 |
| 2020-03-25 |        62 |         48 |                  0 |
| 2020-03-26 |       122 |         58 |                  8 |
| 2020-03-27 |        93 |         69 |                  7 |
| 2020-03-28 |       151 |         43 |                  0 |
| 2020-03-29 |       201 |         17 |                  0 |
| 2020-03-30 |       242 |         75 |                  6 |
| 2020-03-31 |       234 |         24 |                  7 |
| 2020-04-01 |       255 |         13 |                  0 |
| 2020-04-02 |       225 |         13 |                  1 |
| 2020-04-03 |       275 |         25 |                  0 |
| 2020-04-04 |       188 |         13 |                  1 |
| 2020-04-05 |       215 |          8 |                  0 |
| 2020-04-06 |       269 |         61 |                 18 |
| 2020-04-07 |       183 |         56 |                  5 |
| 2020-04-08 |       141 |         13 |                 14 |
| 2020-04-09 |       152 |          0 |                  1 |
| 2020-04-10 |       170 |          0 |                 19 |
| 2020-04-11 |        88 |          0 |                 14 |
| 2020-04-12 |        83 |          0 |                 23 |
| 2020-04-13 |       103 |          0 |                 22 |
| 2020-04-14 |       141 |          0 |                 14 |
| 2020-04-15 |       111 |          0 |                 23 |
| 2020-04-16 |       179 |          0 |                 32 |
| 2020-04-17 |       120 |          0 |                 28 |
| 2020-04-18 |       118 |          0 |                  7 |
| 2020-04-19 |        94 |          0 |                  9 |
| 2020-04-20 |       138 |          0 |                 25 |
| 2020-04-21 |       123 |          0 |                 23 |
| 2020-04-22 |       136 |          0 |                 23 |
| 2020-04-23 |       135 |          0 |                 11 |
| 2020-04-24 |        95 |          0 |                 10 |
| 2020-04-25 |        57 |          0 |                 14 |
| 2020-04-26 |        40 |          0 |                  4 |
| 2020-04-27 |        42 |          0 |                 11 |
| 2020-04-28 |        39 |          0 |                 15 |
| 2020-04-29 |        53 |          0 |                 11 |
| 2020-04-30 |        64 |          0 |                 15 |
| 2020-05-01 |        69 |          0 |                 16 |
| 2020-05-02 |        29 |          0 |                  9 |
| 2020-05-03 |        24 |          0 |                 12 |
| 2020-05-04 |        71 |          0 |                 20 |
| 2020-05-05 |        40 |          0 |                  4 |
| 2020-05-06 |        66 |          0 |                  2 |
| 2020-05-07 |        62 |          0 |                  3 |
| 2020-05-08 |        37 |          0 |                  7 |
| 2020-05-09 |        24 |          0 |                 10 |
| 2020-05-10 |        30 |          0 |                  1 |
| 2020-05-11 |        32 |          0 |                  3 |
| 2020-05-12 |        18 |          0 |                  4 |
| 2020-05-13 |        25 |          0 |                  0 |
| 2020-05-14 |        18 |          0 |                  0 |
| 2020-05-15 |        31 |          0 |                  0 |
| 2020-05-16 |        21 |          0 |                  0 |
| 2020-05-17 |        14 |          0 |                  0 |
| 2020-05-18 |        29 |          0 |                  1 |
| 2020-05-19 |        10 |          0 |                  1 |
| 2020-05-20 |         9 |          0 |                  0 |
| 2020-05-21 |         7 |          0 |                  0 |
| 2020-05-22 |         4 |          0 |                  0 |
| 2020-05-23 |         6 |          0 |                  0 |
| 2020-05-24 |         2 |          0 |                  0 |
| 2020-05-25 |         2 |          0 |                  0 |
| 2020-05-26 |         3 |          0 |                  0 |
| 2020-05-27 |         2 |          0 |                  1 |
| 2020-05-28 |         2 |          0 |                  0 |
| 2020-05-29 |         1 |          0 |                  0 |
| 2020-05-30 |         3 |          0 |                  0 |
| 2020-05-31 |        10 |          0 |                  0 |
| 2020-06-01 |         9 |          0 |                  1 |
| 2020-06-02 |         4 |          0 |                  0 |
| 2020-06-03 |         6 |          0 |                  0 |
| 2020-06-04 |         4 |          0 |                  0 |
| 2020-06-05 |         1 |          0 |                  0 |
| 2020-06-07 |         2 |          0 |                  0 |
| 2020-06-09 |         2 |          0 |                  0 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                   | Country          |   Number of sequences | Sequence group   |
|:-------------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN                 | Scotland         |                     2 | 1-10             |
| ABERDEENSHIRE            | Scotland         |                     6 | 1-10             |
| ANGUS                    | Scotland         |                    23 | 10-50            |
| ANTRIM                   | Northern Ireland |                   237 | 200-250          |
| ARMAGH                   | Northern Ireland |                    17 | 10-50            |
| BEDFORDSHIRE             | England          |                   405 | 400-500          |
| BERKSHIRE                | England          |                     4 | 1-10             |
| BRISTOL                  | England          |                     2 | 1-10             |
| BUCKINGHAMSHIRE          | England          |                   324 | 300-400          |
| CAMBRIDGESHIRE           | England          |                   207 | 200-250          |
| CARMARTHENSHIRE          | Wales            |                     1 | 1-10             |
| CLACKMANNANSHIRE         | Scotland         |                     1 | 1-10             |
| CORNWALL                 | England          |                    23 | 10-50            |
| CUMBRIA                  | England          |                    15 | 10-50            |
| DERBYSHIRE               | England          |                     1 | 1-10             |
| DEVON                    | England          |                    93 | 50-100           |
| DORSET                   | England          |                   175 | 150-200          |
| DOWN                     | Northern Ireland |                   222 | 200-250          |
| DUMFRIES AND GALLOWAY    | Scotland         |                    44 | 10-50            |
| DUNDEE                   | Scotland         |                   113 | 100-150          |
| DURHAM                   | England          |                   122 | 100-150          |
| EAST AYRSHIRE            | Scotland         |                    34 | 10-50            |
| EAST RIDING OF YORKSHIRE | England          |                     2 | 1-10             |
| EDINBURGH                | Scotland         |                     2 | 1-10             |
| ESSEX                    | England          |                  1075 | >500             |
| FALKIRK                  | Scotland         |                    28 | 10-50            |
| FERMANAGH                | Northern Ireland |                     2 | 1-10             |
| FIFE                     | Scotland         |                     3 | 1-10             |
| GLASGOW                  | Scotland         |                   239 | 200-250          |
| GLOUCESTERSHIRE          | England          |                   699 | >500             |
| GREATER LONDON           | England          |                   450 | 400-500          |
| HAMPSHIRE                | England          |                    36 | 10-50            |
| HEREFORDSHIRE            | England          |                    53 | 50-100           |
| HERTFORDSHIRE            | England          |                   573 | >500             |
| HIGHLAND                 | Scotland         |                     1 | 1-10             |
| LINCOLNSHIRE             | England          |                     1 | 1-10             |
| LONDONDERRY              | Northern Ireland |                    23 | 10-50            |
| MERSEYSIDE               | England          |                     1 | 1-10             |
| MONMOUTHSHIRE            | Wales            |                     3 | 1-10             |
| NORFOLK                  | England          |                    16 | 10-50            |
| NORTH LANARKSHIRE        | Scotland         |                    76 | 50-100           |
| NORTH YORKSHIRE          | England          |                    49 | 10-50            |
| NORTHAMPTONSHIRE         | England          |                     8 | 1-10             |
| NORTHUMBERLAND           | England          |                   127 | 100-150          |
| NOTTINGHAMSHIRE          | England          |                     3 | 1-10             |
| OXFORDSHIRE              | England          |                     6 | 1-10             |
| PERTHSHIRE AND KINROSS   | Scotland         |                    87 | 50-100           |
| RENFREWSHIRE             | Scotland         |                    31 | 10-50            |
| SHROPSHIRE               | England          |                     3 | 1-10             |
| SOMERSET                 | England          |                   579 | >500             |
| SOUTH YORKSHIRE          | England          |                    10 | 10-50            |
| STIRLING                 | Scotland         |                     2 | 1-10             |
| SUFFOLK                  | England          |                   311 | 300-400          |
| SURREY                   | England          |                    23 | 10-50            |
| SUSSEX                   | England          |                     1 | 1-10             |
| TYNE AND WEAR            | England          |                   252 | 250-300          |
| TYRONE                   | Northern Ireland |                    14 | 10-50            |
| WARWICKSHIRE             | England          |                     1 | 1-10             |
| WEST YORKSHIRE           | England          |                     1 | 1-10             |
| WILTSHIRE                | England          |                   372 | 300-400          |
| WORCESTERSHIRE           | England          |                     1 | 1-10             |

\pagebreak






