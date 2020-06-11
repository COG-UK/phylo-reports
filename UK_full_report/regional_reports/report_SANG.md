







# Lineages report for SANG




This report gives summaries of UK specific lineages sequenced by SANG for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-25. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
4816 sequences in the UK from the sequencing centre SANG have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 1871 and the maximum is 2625


Sequences which were replicates or too error-prone were removed from this analysis.



1711 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 55 that remain:
53 are pending extinction, ie last seen three weeks ago.
2 lineages have reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England     | Scotland    | Northern Ireland   | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:------------|:-------------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 313 (96.9%) | 9 (2.79%)   | 1 (0.31%)          | Mar-07, May-25 |               323 | B.1.1.1          |                               0 | active today     |
| UK2464         | 97 (84.35%) | 18 (15.65%) | 0 (0%)             | Mar-12, May-01 |               115 | B.1.p11          |                              24 | 0.0183           |
| UK9            | 93 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-19, May-03 |                93 | B.1.13           |                              22 | 0.0222           |
| UK494          | 68 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-21, May-01 |                68 | B.1.p11          |                              24 | 0.0255           |
| UK177          | 56 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-27, May-01 |                56 | B.1.1            |                              24 | 0.0265           |
| UK115          | 53 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-17, Apr-20 |                53 | B.2.1            |                              35 | 0.0187           |
| UK66           | 52 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, May-01 |                52 | B.1.1.8          |                              24 | 0.0359           |
| UK2916         | 47 (97.92%) | 0 (0%)      | 1 (2.08%)          | Feb-27, May-10 |                48 | B.1              |                              15 | 0.1035           |
| UK2913         | 46 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-16, Apr-30 |                46 | B.1.p11          |                              25 | 0.04             |
| UK26           | 37 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, May-06 |                37 | B.1.1.3          |                              19 | 0.0716           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/SANG/figures/report_SANG_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
The lag for this sequencing centre is 11 days
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/SANG/figures/report_SANG_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/SANG/figures/report_SANG_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/SANG/figures/report_SANG_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/SANG/figures/report_SANG_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 415 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-05/analysis/7/regional_reports/SANG/figures/report_SANG_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England     | Scotland    | Northern Ireland   | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) | Activity score   |
|:---------------|:------------|:------------|:-------------------|:---------------|------------------:|:-----------------|--------------------------------:|:-----------------|
| UK5            | 313 (96.9%) | 9 (2.79%)   | 1 (0.31%)          | Mar-07, May-25 |               323 | B.1.1.1          |                               0 | active today     |
| UK2464         | 97 (84.35%) | 18 (15.65%) | 0 (0%)             | Mar-12, May-01 |               115 | B.1.p11          |                              24 | 0.0183           |
| UK9            | 93 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-19, May-03 |                93 | B.1.13           |                              22 | 0.0222           |
| UK494          | 68 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-21, May-01 |                68 | B.1.p11          |                              24 | 0.0255           |
| UK177          | 56 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-27, May-01 |                56 | B.1.1            |                              24 | 0.0265           |
| UK115          | 53 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-17, Apr-20 |                53 | B.2.1            |                              35 | 0.0187           |
| UK66           | 52 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, May-01 |                52 | B.1.1.8          |                              24 | 0.0359           |
| UK2916         | 47 (97.92%) | 0 (0%)      | 1 (2.08%)          | Feb-27, May-10 |                48 | B.1              |                              15 | 0.1035           |
| UK2913         | 46 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-16, Apr-30 |                46 | B.1.p11          |                              25 | 0.04             |
| UK26           | 37 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, May-06 |                37 | B.1.1.3          |                              19 | 0.0716           |
| UK346          | 34 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-16, Apr-19 |                34 | B.1.72, B.1      |                              36 | 0.0286           |
| UK4            | 32 (96.97%) | 0 (0%)      | 1 (3.03%)          | Mar-11, Apr-14 |                33 | B                |                              41 | 0.0259           |
| UK19           | 33 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-14, May-10 |                33 | B.1              |                              15 | 0.1188           |
| UK63           | 33 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-28, Apr-30 |                33 | B.1.1            |                              25 | 0.0412           |
| UK760          | 0 (0%)      | 0 (0%)      | 32 (100.0%)        | Mar-27, Apr-22 |                32 | B.1.1            |                              33 | 0.0254           |
| UK28           | 31 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-26, May-01 |                31 | B.1.1.10         |                              24 | 0.05             |
| UK40           | 0 (0%)      | 31 (100.0%) | 0 (0%)             | Mar-21, Apr-07 |                31 | B.16             |                              48 | 0.0118           |
| UK112          | 30 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-21, May-04 |                30 | B.1.1            |                              21 | 0.0722           |
| UK13           | 30 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-13, May-09 |                30 | B.1.1            |                              16 | 0.1228           |
| UK371          | 30 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-29, May-09 |                30 | B.1.1            |                              16 | 0.0884           |
| UK31           | 28 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-21, May-06 |                28 | B.1              |                              19 | 0.0897           |
| UK37           | 28 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-17, May-04 |                28 | B.1.30           |                              21 | 0.0847           |
| UK138          | 27 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-23, Apr-17 |                27 | B.2.1            |                              38 | 0.0253           |
| UK79           | 25 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-24, May-04 |                25 | B.1              |                              21 | 0.0813           |
| UK8            | 24 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-10, Apr-08 |                24 | B                |                              47 | 0.0268           |
| UK36           | 10 (41.67%) | 13 (54.17%) | 1 (4.17%)          | Mar-19, Apr-14 |                24 | B.1              |                              41 | 0.0276           |
| UK3035         | 23 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-24, May-08 |                23 | B.1              |                              17 | 0.1203           |
| UK81           | 22 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-19, Apr-27 |                22 | B.1.1            |                              28 | 0.0663           |
| UK5098         | 0 (0%)      | 21 (100.0%) | 0 (0%)             | Mar-23, Apr-07 |                21 | B.1.p73          |                              48 | 0.0156           |
| UK114          | 20 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-16, Apr-13 |                20 | B.1.1            |                              42 | 0.0351           |
| UK109          | 20 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-21, May-01 |                20 | B.1.5            |                              24 | 0.0899           |
| UK61           | 20 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-12, Apr-18 |                20 | B.3              |                              37 | 0.0526           |
| UK158          | 19 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-23, Apr-19 |                19 | B.1.1            |                              36 | 0.0417           |
| UK339          | 17 (89.47%) | 2 (10.53%)  | 0 (0%)             | Mar-14, Apr-16 |                19 | B.3              |                              39 | 0.047            |
| UK51           | 18 (94.74%) | 1 (5.26%)   | 0 (0%)             | Mar-26, May-08 |                19 | B.1.36           |                              17 | 0.1405           |
| UK3            | 18 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, May-05 |                18 | B.1              |                              20 | 0.1412           |
| UK39           | 0 (0%)      | 18 (100.0%) | 0 (0%)             | Mar-24, Apr-07 |                18 | A.2              |                              48 | 0.0172           |
| UK5675         | 18 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-22, Apr-01 |                18 | B.2              |                              54 | 0.0109           |
| UK77           | 18 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-23, Apr-26 |                18 | B.2              |                              29 | 0.069            |
| UK276          | 17 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, Apr-16 |                17 | B.1.1            |                              39 | 0.0465           |
| UK2735         | 13 (76.47%) | 1 (5.88%)   | 3 (17.65%)         | Mar-24, May-07 |                17 | B.1.1            |                              18 | 0.1528           |
| UK225          | 0 (0%)      | 17 (100.0%) | 0 (0%)             | Mar-21, Apr-07 |                17 | B.2              |                              48 | 0.0221           |
| UK5741         | 16 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-30, Apr-19 |                16 | B.1              |                              36 | 0.037            |
| UK274          | 16 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-15, Apr-08 |                16 | B.3              |                              47 | 0.034            |
| UK101          | 16 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-21, Apr-26 |                16 | B.1.5            |                              29 | 0.0828           |
| UK33           | 15 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-30, May-08 |                15 | B.1.1            |                              17 | 0.1639           |
| UK5309         | 15 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-25, Apr-29 |                15 | B.1.1.10, B.1.1  |                              26 | 0.0962           |
| UK183          | 15 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-29, Apr-15 |                15 | B.1.1            |                              40 | 0.0304           |
| UK179          | 14 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-26, Apr-18 |                14 | B.1.1.p11        |                              37 | 0.0478           |
| UK254          | 14 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-20, Apr-14 |                14 | B.1.1            |                              41 | 0.0469           |
| UK126          | 14 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-29, May-01 |                14 | B.1.1            |                              24 | 0.1058           |
| UK632          | 14 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-25, Apr-18 |                14 | B.1.1            |                              37 | 0.0499           |
| UK128          | 13 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-03, May-07 |                13 | B.1.1            |                              18 | 0.1574           |
| UK397          | 13 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-28, Apr-14 |                13 | B.1.1.13         |                              41 | 0.0346           |
| UK72           | 3 (23.08%)  | 0 (0%)      | 10 (76.92%)        | Mar-13, Apr-21 |                13 | B.10             |                              34 | 0.0956           |
| UK173          | 13 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-16, Apr-11 |                13 | B                |                              44 | 0.0492           |
| UK5498         | 13 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-01, Apr-20 |                13 | B.2              |                              35 | 0.0452           |
| UK23           | 12 (92.31%) | 1 (7.69%)   | 0 (0%)             | Mar-18, Apr-03 |                13 | B.9, B           |                              52 | 0.0256           |
| UK3021         | 12 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-16, Apr-16 |                12 | B.1              |                              39 | 0.0723           |
| UK146          | 12 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-01, May-07 |                12 | B.1.1            |                              18 | 0.1818           |
| UK214          | 12 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-14, May-01 |                12 | B.1.1            |                              24 | 0.1818           |
| UK569          | 12 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-23, Apr-14 |                12 | B.1.1            |                              41 | 0.0488           |
| UK637          | 12 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-28, May-01 |                12 | B.1.1            |                              24 | 0.1288           |
| UK368          | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-18, May-01 |                11 | B.1              |                              24 | 0.1833           |
| UK5260         | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-05, May-02 |                11 | B.1.1            |                              23 | 0.1174           |
| UK103          | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-30, May-04 |                11 | B.1.1            |                              21 | 0.1667           |
| UK5339         | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-15, Apr-29 |                11 | B.1.1            |                              26 | 0.0538           |
| UK18           | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-12, May-03 |                11 | B.1.1.7          |                              22 | 0.2364           |
| UK726          | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-04, May-01 |                11 | B.1              |                              24 | 0.1125           |
| UK174          | 11 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-19, May-02 |                11 | B.1.5            |                              23 | 0.1913           |
| UK354          | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-28, Apr-07 |                10 | B.1.1            |                              48 | 0.0231           |
| UK513          | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Apr-03, Apr-11 |                10 | B.1.p11          |                              44 | 0.0202           |
| UK134          | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-09, Apr-07 |                10 | B.1              |                              48 | 0.0671           |
| UK88           | 0 (0%)      | 10 (100.0%) | 0 (0%)             | Mar-23, Apr-07 |                10 | B.1              |                              48 | 0.0347           |
| UK5713         | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-26, Apr-14 |                10 | B.1.1, B.2       |                              41 | 0.0515           |
| UK2045         | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-17, Apr-29 |                10 | B, B.1           |                              26 | 0.1838           |
| UK241          | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-22, Apr-16 |                10 | B.1.5.3          |                              39 | 0.0712           |
| UK6            | 10 (100.0%) | 0 (0%)      | 0 (0%)             | Mar-17, Apr-14 |                10 | B.1              |                              41 | 0.0759           |
| UK132          | 8 (88.89%)  | 1 (11.11%)  | 0 (0%)             | Mar-27, Apr-29 |                 9 | B.1              |                              26 | 0.1587           |
| UK12           | 8 (88.89%)  | 0 (0%)      | 1 (11.11%)         | Mar-22, Apr-13 |                 9 | B.1.p11          |                              42 | 0.0655           |
| UK5649         | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-04, Apr-19 |                 9 | B.2.6            |                              36 | 0.0521           |
| UK5338         | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-29, May-02 |                 9 | B.1.1            |                              23 | 0.0163           |
| UK123          | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-23, May-01 |                 9 | B.1              |                              24 | 0.2031           |
| UK2013         | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-29, Apr-26 |                 9 | B.1              |                              29 | 0.1207           |
| UK95           | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-17, Apr-05 |                 9 | B.2.1            |                              50 | 0.0475           |
| UK58           | 6 (66.67%)  | 3 (33.33%)  | 0 (0%)             | Mar-17, Apr-09 |                 9 | B.1              |                              46 | 0.0625           |
| UK5409         | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-27, Apr-19 |                 9 | B.1.1            |                              36 | 0.0799           |
| UK2200         | 3 (33.33%)  | 6 (66.67%)  | 0 (0%)             | Mar-20, Apr-07 |                 9 | B.1.5.6, B.1.5   |                              48 | 0.0469           |
| UK5707         | 7 (77.78%)  | 0 (0%)      | 2 (22.22%)         | Mar-18, Apr-15 |                 9 | B.1.1, B.2       |                              40 | 0.0875           |
| UK5672         | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-19, Apr-04 |                 9 | B.2              |                              51 | 0.0392           |
| UK441          | 9 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-04, May-01 |                 9 | B.1.1            |                              24 | 0.1406           |
| UK318          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-20, Apr-10 |                 8 | B                |                              45 | 0.0667           |
| UK62           | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-24, Apr-09 |                 8 | B.3              |                              46 | 0.0497           |
| UK645          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-29, Apr-08 |                 8 | B.2.1            |                              47 | 0.0304           |
| UK291          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-13, Apr-05 |                 8 | B.2.1            |                              50 | 0.0657           |
| UK163          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-27, Apr-07 |                 8 | B.1.1            |                              48 | 0.0327           |
| UK86           | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-23, Mar-30 |                 8 | B.1              |                              56 | 0.0179           |
| UK53           | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-02, Apr-16 |                 8 | B.1.1.4          |                              39 | 0.0513           |
| UK341          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-23, Apr-12 |                 8 | B.1              |                              43 | 0.0664           |
| UK45           | 7 (87.5%)   | 1 (12.5%)   | 0 (0%)             | Mar-26, Apr-15 |                 8 | B.1.1            |                              40 | 0.0714           |
| UK251          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-26, May-02 |                 8 | B.1.1            |                              23 | 0.2298           |
| UK2904         | 0 (0%)      | 0 (0%)      | 8 (100.0%)         | Apr-06, Apr-22 |                 8 | B.1.p11          |                              33 | 0.0693           |
| UK64           | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-01, Apr-15 |                 8 | B.1              |                              40 | 0.05             |
| UK42           | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-28, Apr-28 |                 8 | B.1, B.1.35      |                              27 | 0.164            |
| UK759          | 8 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-28, Apr-04 |                 8 | B.1.1            |                              51 | 0.0196           |
| UK30           | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-23, May-02 |                 7 | B.1.1            |                              23 | 0.2899           |
| UK67           | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-26, May-04 |                 7 | B.1.1            |                              21 | 0.0635           |
| UK195          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-31, May-03 |                 7 | B.1.1            |                              22 | 0.25             |
| UK913          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-03, Apr-29 |                 7 | B.1              |                              26 | 0.1667           |
| UK119          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-23, Apr-07 |                 7 | B.2.5            |                              48 | 0.0521           |
| UK1006         | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-04, Apr-29 |                 7 | B.1.1            |                              26 | 0.1603           |
| UK511          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-05, Apr-29 |                 7 | B.1.1            |                              26 | 0.1538           |
| UK253          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-10, May-03 |                 7 | B.1.1            |                              22 | 0.1742           |
| UK564          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-03, May-02 |                 7 | B.1.1            |                              23 | 0.2101           |
| UK5523         | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | May-01, May-23 |                 7 | B.1              |                               2 | 1.8333           |
| UK5174         | 6 (85.71%)  | 0 (0%)      | 1 (14.29%)         | Mar-26, Apr-07 |                 7 | B.1.1.7          |                              48 | 0.0417           |
| UK190          | 7 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-18, Apr-06 |                 7 | B.1              |                              49 | 0.0646           |
| UK659          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-21, Mar-30 |                 6 | B                |                              56 | 0.0321           |
| UK70           | 5 (83.33%)  | 0 (0%)      | 1 (16.67%)         | Mar-28, Apr-16 |                 6 | B.2              |                              39 | 0.0974           |
| UK46           | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-14, Apr-16 |                 6 | B.2.1            |                              39 | 0.1692           |
| UK92           | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-31, Apr-16 |                 6 | B.1.1            |                              39 | 0.0821           |
| UK444          | 3 (50.0%)   | 0 (0%)      | 3 (50.0%)          | Mar-31, Apr-21 |                 6 | B.1.1            |                              34 | 0.1235           |
| UK552          | 2 (33.33%)  | 4 (66.67%)  | 0 (0%)             | Mar-23, Mar-29 |                 6 | A.1              |                              57 | 0.0211           |
| UK510          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-02, Apr-16 |                 6 | B.1.1            |                              39 | 0.0718           |
| UK517          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-29, Apr-12 |                 6 | B.1.1            |                              43 | 0.0651           |
| UK44           | 0 (0%)      | 6 (100.0%)  | 0 (0%)             | Mar-23, Mar-26 |                 6 | B                |                              60 | 0.01             |
| UK512          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-30, Apr-13 |                 6 | B.1.1            |                              42 | 0.0667           |
| UK541          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-01, Apr-12 |                 6 | B.1.1            |                              43 | 0.0512           |
| UK329          | 5 (83.33%)  | 1 (16.67%)  | 0 (0%)             | Mar-24, May-07 |                 6 | B.1.1            |                              18 | 0.4889           |
| UK237          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-31, May-07 |                 6 | B.1.1            |                              18 | 0.4111           |
| UK746          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-31, Apr-14 |                 6 | B.1.5            |                              41 | 0.0683           |
| UK5084         | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-31, Apr-15 |                 6 | B.1              |                              40 | 0.075            |
| UK255          | 5 (83.33%)  | 1 (16.67%)  | 0 (0%)             | Apr-03, Apr-16 |                 6 | B.1.1            |                              39 | 0.0667           |
| UK566          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Apr-03, Apr-15 |                 6 | B.1.1.10         |                              40 | 0.06             |
| UK330          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-23, Apr-13 |                 6 | B.1.1            |                              42 | 0.1              |
| UK634          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-30, Apr-18 |                 6 | B.1.1            |                              37 | 0.1027           |
| UK287          | 6 (100.0%)  | 0 (0%)      | 0 (0%)             | Mar-31, Apr-06 |                 6 | B.1              |                              49 | 0.0245           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | SANG     |            11 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2464 |   UK9 |   UK494 |   UK177 |   UK66 |   UK2916 |   UK2913 |   UK26 |   UK63 |
|:------------------|------:|---------:|------:|--------:|--------:|-------:|---------:|---------:|-------:|-------:|
| 2020-02-23        |     0 |        0 |     0 |       0 |       0 |      0 |        2 |        0 |      0 |      0 |
| 2020-03-01        |     1 |        0 |     0 |       0 |       0 |      0 |        3 |        0 |      0 |      0 |
| 2020-03-08        |     6 |        1 |     0 |       0 |       0 |      0 |        3 |        0 |      0 |      0 |
| 2020-03-15        |     6 |        4 |     2 |       1 |       0 |      2 |        5 |        1 |      1 |      0 |
| 2020-03-22        |    13 |       11 |     3 |       3 |       1 |      2 |        4 |        6 |      0 |      1 |
| 2020-03-29        |    16 |        9 |    10 |       7 |       3 |      5 |        5 |        7 |      1 |      7 |
| 2020-04-05        |    13 |       10 |     7 |       4 |       6 |      5 |        5 |        4 |      1 |      5 |
| 2020-04-12        |    12 |        6 |     6 |       3 |       4 |      3 |        1 |        3 |      2 |      2 |
| 2020-04-19        |     4 |        0 |     0 |       1 |       0 |      2 |        0 |        0 |      0 |      0 |
| 2020-04-26        |    11 |        3 |     1 |       2 |       3 |      2 |        1 |        2 |      3 |      2 |
| 2020-05-03        |     6 |        0 |     1 |       0 |       0 |      0 |        1 |        0 |      1 |      0 |
| 2020-05-10        |     0 |        0 |     0 |       0 |       0 |      0 |        1 |        0 |      0 |      0 |
| 2020-05-17        |     3 |        0 |     0 |       0 |       0 |      0 |        0 |        0 |      0 |      0 |
| 2020-05-24        |     1 |        0 |     0 |       0 |       0 |      0 |        0 |        0 |      0 |      0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-02-27 |                            0 |                                1 |       1 |
| 2020-02-28 |                            1 |                                0 |       1 |
| 2020-03-01 |                            1 |                                0 |       1 |
| 2020-03-02 |                            3 |                                0 |       3 |
| 2020-03-03 |                            4 |                                1 |       5 |
| 2020-03-04 |                            2 |                                3 |       5 |
| 2020-03-05 |                            1 |                                0 |       1 |
| 2020-03-06 |                            2 |                                0 |       2 |
| 2020-03-07 |                            0 |                                2 |       2 |
| 2020-03-08 |                            2 |                                1 |       3 |
| 2020-03-09 |                            7 |                                2 |       9 |
| 2020-03-10 |                            8 |                                3 |      11 |
| 2020-03-11 |                           10 |                                4 |      14 |
| 2020-03-12 |                           12 |                                6 |      18 |
| 2020-03-13 |                           14 |                                6 |      20 |
| 2020-03-14 |                           11 |                                8 |      19 |
| 2020-03-15 |                            5 |                                4 |       9 |
| 2020-03-16 |                           11 |                               10 |      21 |
| 2020-03-17 |                            8 |                               12 |      20 |
| 2020-03-18 |                           14 |                               14 |      28 |
| 2020-03-19 |                           17 |                               13 |      30 |
| 2020-03-20 |                           29 |                               10 |      39 |
| 2020-03-21 |                           46 |                               15 |      61 |
| 2020-03-22 |                           38 |                                9 |      47 |
| 2020-03-23 |                           53 |                               29 |      82 |
| 2020-03-24 |                           37 |                                9 |      46 |
| 2020-03-25 |                           30 |                               11 |      41 |
| 2020-03-26 |                           39 |                               25 |      64 |
| 2020-03-27 |                           31 |                               11 |      42 |
| 2020-03-28 |                           42 |                               20 |      62 |
| 2020-03-29 |                           60 |                               23 |      83 |
| 2020-03-30 |                           75 |                               24 |      99 |
| 2020-03-31 |                           54 |                               25 |      79 |
| 2020-04-01 |                           74 |                               17 |      91 |
| 2020-04-02 |                           78 |                               18 |      96 |
| 2020-04-03 |                           70 |                               18 |      88 |
| 2020-04-04 |                           47 |                               12 |      59 |
| 2020-04-05 |                           68 |                               13 |      81 |
| 2020-04-06 |                           94 |                                8 |     102 |
| 2020-04-07 |                           38 |                                8 |      46 |
| 2020-04-08 |                           33 |                                3 |      36 |
| 2020-04-09 |                           16 |                                5 |      21 |
| 2020-04-10 |                           35 |                                5 |      40 |
| 2020-04-11 |                           20 |                                3 |      23 |
| 2020-04-12 |                           16 |                                2 |      18 |
| 2020-04-13 |                           18 |                                4 |      22 |
| 2020-04-14 |                           17 |                                2 |      19 |
| 2020-04-15 |                           23 |                                4 |      27 |
| 2020-04-16 |                           21 |                                5 |      26 |
| 2020-04-17 |                            7 |                                0 |       7 |
| 2020-04-18 |                            1 |                                1 |       2 |
| 2020-04-19 |                            6 |                                0 |       6 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-21 |                            2 |                                0 |       2 |
| 2020-04-22 |                            2 |                                0 |       2 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-04-26 |                            1 |                                3 |       4 |
| 2020-04-27 |                            3 |                                0 |       3 |
| 2020-04-28 |                            6 |                                0 |       6 |
| 2020-04-29 |                            6 |                                3 |       9 |
| 2020-04-30 |                            4 |                                2 |       6 |
| 2020-05-01 |                           12 |                                4 |      16 |
| 2020-05-02 |                            3 |                                0 |       3 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-04 |                            3 |                                0 |       3 |
| 2020-05-06 |                            5 |                                0 |       5 |
| 2020-05-07 |                            3 |                                2 |       5 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-10 |                            1 |                                0 |       1 |

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
| 2020-03-19 |        43 |          0 |                  0 |
| 2020-03-20 |        54 |          0 |                  0 |
| 2020-03-21 |        79 |          3 |                  0 |
| 2020-03-22 |        84 |          3 |                  0 |
| 2020-03-23 |       102 |         38 |                  0 |
| 2020-03-24 |        37 |         59 |                  0 |
| 2020-03-25 |        49 |         41 |                  0 |
| 2020-03-26 |       102 |         38 |                  8 |
| 2020-03-27 |        70 |         26 |                  7 |
| 2020-03-28 |       122 |          0 |                  0 |
| 2020-03-29 |       169 |          0 |                  0 |
| 2020-03-30 |       216 |          0 |                  6 |
| 2020-03-31 |       186 |          0 |                  7 |
| 2020-04-01 |       205 |          0 |                  0 |
| 2020-04-02 |       203 |          0 |                  1 |
| 2020-04-03 |       230 |          1 |                  0 |
| 2020-04-04 |       163 |          0 |                  1 |
| 2020-04-05 |       203 |          3 |                  0 |
| 2020-04-06 |       257 |         29 |                 13 |
| 2020-04-07 |       175 |         33 |                  0 |
| 2020-04-08 |       106 |          0 |                  0 |
| 2020-04-09 |        87 |          0 |                  0 |
| 2020-04-10 |       141 |          0 |                 11 |
| 2020-04-11 |        82 |          0 |                  8 |
| 2020-04-12 |        68 |          0 |                  7 |
| 2020-04-13 |        65 |          0 |                  5 |
| 2020-04-14 |       137 |          0 |                  0 |
| 2020-04-15 |       105 |          0 |                  8 |
| 2020-04-16 |       112 |          0 |                  0 |
| 2020-04-17 |        25 |          0 |                  0 |
| 2020-04-18 |        24 |          0 |                  0 |
| 2020-04-19 |        42 |          0 |                  1 |
| 2020-04-20 |        20 |          0 |                  2 |
| 2020-04-21 |         0 |          0 |                 12 |
| 2020-04-22 |         1 |          0 |                 14 |
| 2020-04-25 |         5 |          0 |                  0 |
| 2020-04-26 |        23 |          0 |                  0 |
| 2020-04-27 |        28 |          0 |                  0 |
| 2020-04-28 |        20 |          0 |                  0 |
| 2020-04-29 |        49 |          0 |                  0 |
| 2020-04-30 |        52 |          0 |                  0 |
| 2020-05-01 |        69 |          0 |                  0 |
| 2020-05-02 |        25 |          0 |                  0 |
| 2020-05-03 |        10 |          0 |                  0 |
| 2020-05-04 |        25 |          0 |                  0 |
| 2020-05-05 |        10 |          0 |                  0 |
| 2020-05-06 |        17 |          0 |                  0 |
| 2020-05-07 |        26 |          0 |                  0 |
| 2020-05-08 |        11 |          0 |                  0 |
| 2020-05-09 |         9 |          0 |                  0 |
| 2020-05-10 |         5 |          0 |                  0 |
| 2020-05-18 |         1 |          0 |                  0 |
| 2020-05-20 |         7 |          0 |                  0 |
| 2020-05-21 |         5 |          0 |                  0 |
| 2020-05-22 |         4 |          0 |                  0 |
| 2020-05-23 |         5 |          0 |                  0 |
| 2020-05-24 |         1 |          0 |                  0 |
| 2020-05-25 |         1 |          0 |                  0 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country          |   Number of sequences | Sequence group   |
|:-----------------------|:-----------------|----------------------:|:-----------------|
| ABERDEEN               | Scotland         |                     1 | 1-10             |
| ANTRIM                 | Northern Ireland |                    56 | 50-100           |
| BEDFORDSHIRE           | England          |                   372 | 300-400          |
| BERKSHIRE              | England          |                     1 | 1-10             |
| BRISTOL                | England          |                     2 | 1-10             |
| BUCKINGHAMSHIRE        | England          |                   261 | 250-300          |
| CAMBRIDGESHIRE         | England          |                   181 | 150-200          |
| CARMARTHENSHIRE        | Wales            |                     1 | 1-10             |
| CORNWALL               | England          |                    16 | 10-50            |
| DEVON                  | England          |                    33 | 10-50            |
| DORSET                 | England          |                   142 | 100-150          |
| DOWN                   | Northern Ireland |                    44 | 10-50            |
| DUMFRIES AND GALLOWAY  | Scotland         |                    15 | 10-50            |
| EAST AYRSHIRE          | Scotland         |                    31 | 10-50            |
| EDINBURGH              | Scotland         |                     1 | 1-10             |
| ESSEX                  | England          |                   865 | >500             |
| FALKIRK                | Scotland         |                    22 | 10-50            |
| GLASGOW                | Scotland         |                   121 | 100-150          |
| GLOUCESTERSHIRE        | England          |                   447 | 400-500          |
| GREATER LONDON         | England          |                   386 | 300-400          |
| HAMPSHIRE              | England          |                    22 | 10-50            |
| HERTFORDSHIRE          | England          |                   475 | 400-500          |
| LONDONDERRY            | Northern Ireland |                     7 | 1-10             |
| MONMOUTHSHIRE          | Wales            |                     1 | 1-10             |
| NORFOLK                | England          |                    11 | 10-50            |
| NORTH LANARKSHIRE      | Scotland         |                    32 | 10-50            |
| NORTHAMPTONSHIRE       | England          |                     6 | 1-10             |
| NOTTINGHAMSHIRE        | England          |                     3 | 1-10             |
| OXFORDSHIRE            | England          |                     5 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland         |                    28 | 10-50            |
| RENFREWSHIRE           | Scotland         |                    22 | 10-50            |
| SOMERSET               | England          |                   283 | 250-300          |
| SUFFOLK                | England          |                   248 | 200-250          |
| SURREY                 | England          |                    21 | 10-50            |
| SUSSEX                 | England          |                     1 | 1-10             |
| TYRONE                 | Northern Ireland |                     4 | 1-10             |
| WARWICKSHIRE           | England          |                     1 | 1-10             |
| WILTSHIRE              | England          |                   231 | 200-250          |

\pagebreak






