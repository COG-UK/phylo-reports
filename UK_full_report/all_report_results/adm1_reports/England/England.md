







# Lineages report for England




This report gives summaries of lineages sampled in England for week 2020-07-03. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-27. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
18644 sequences from England have been included in this analysis.
950 lineages have been recorded, 463 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 751 and the maximum is 8279


Sequences which were replicates or too error-prone were removed from this analysis.



891 are lineages which were sampled less than five times in England, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 59 that remain:
37 are pending extinction, ie last seen three weeks ago.
15 lineages have gone quiet, ie haven't been seen this week.
3 lineages have reactivated.
4 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Date range     |   Number of sequences | Global lineage                                                                               |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:---------------------------------------------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | Feb-16, Jun-27 |                  6696 | B.1.1.1, B.1.1.4, B.1.1.13, B.1.1.5, B.1.1, B.1.1.3, B.1.1.10, B.1.1.p11, B.1.1.p15, B.1.1.2 |                               0 | active today     |
| UK107          | Feb-09, Jun-02 |                  1293 | B.2.5, B.2, B.2.1, B                                                                         |                              25 | 0.0032           |
| UK42           | Feb-24, Jun-21 |                   794 | B.1.72, B.1.5, B.1.35, B.1                                                                   |                               6 | 0.0144           |
| UK2913         | Mar-07, Jun-16 |                   387 | B.1.p11, B.1                                                                                 |                              11 | 0.0173           |
| UK5676         | Feb-26, May-27 |                   362 | B.2                                                                                          |                              31 | 0.0051           |
| UK2916         | Feb-03, Jun-10 |                   301 | B.1                                                                                          |                              17 | 0.02             |
| UK2464         | Mar-09, Jun-18 |                   298 | B.1.p11, B.1                                                                                 |                               9 | 0.0202           |
| UK72           | Feb-05, Jun-02 |                   265 | B.2.2, B                                                                                     |                              25 | 0.0139           |
| UK199          | Feb-26, Jun-22 |                   260 | B.1.5, B.1.5.5, B.1                                                                          |                               5 | 0.0429           |
| UK167          | Mar-06, Jun-07 |                   240 | B.1.66, B.1                                                                                  |                              20 | 0.0146           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 



NB the lineage may have started anywhere in the UK, but has been recorded at least once in England



![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-07-03/analysis/7/adm1_reports/England/figures/England_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Date range     |   Number of sequences | Global lineage                                                                               |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:---------------------------------------------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | Feb-16, Jun-27 |                  6696 | B.1.1.1, B.1.1.4, B.1.1.13, B.1.1.5, B.1.1, B.1.1.3, B.1.1.10, B.1.1.p11, B.1.1.p15, B.1.1.2 |                               0 | active today     |
| UK107          | Feb-09, Jun-02 |                  1293 | B.2.5, B.2, B.2.1, B                                                                         |                              25 | 0.0032           |
| UK42           | Feb-24, Jun-21 |                   794 | B.1.72, B.1.5, B.1.35, B.1                                                                   |                               6 | 0.0144           |
| UK2913         | Mar-07, Jun-16 |                   387 | B.1.p11, B.1                                                                                 |                              11 | 0.0173           |
| UK5676         | Feb-26, May-27 |                   362 | B.2                                                                                          |                              31 | 0.0051           |
| UK2916         | Feb-03, Jun-10 |                   301 | B.1                                                                                          |                              17 | 0.02             |
| UK2464         | Mar-09, Jun-18 |                   298 | B.1.p11, B.1                                                                                 |                               9 | 0.0202           |
| UK72           | Feb-05, Jun-02 |                   265 | B.2.2, B                                                                                     |                              25 | 0.0139           |
| UK199          | Feb-26, Jun-22 |                   260 | B.1.5, B.1.5.5, B.1                                                                          |                               5 | 0.0429           |
| UK167          | Mar-06, Jun-07 |                   240 | B.1.66, B.1                                                                                  |                              20 | 0.0146           |
| UK9            | Mar-09, May-15 |                   226 | B.1.13                                                                                       |                              43 | 0.0069           |
| UK5741         | Mar-09, Jun-12 |                   191 | B.1                                                                                          |                              15 | 0.0215           |
| UK240          | Feb-25, May-27 |                   169 | B, B.2, B.2.1, B.2.5                                                                         |                              31 | 0.0162           |
| UK5561         | Feb-25, May-24 |                   169 | B.2, B.2.2                                                                                   |                              34 | 0.0132           |
| UK2735         | Mar-18, Jun-10 |                   150 | B.1.1                                                                                        |                              17 | 0.0182           |
| UK15           | Feb-27, May-06 |                   141 | B.1.1                                                                                        |                              52 | 0.007            |
| UK6            | Mar-06, Jun-16 |                   135 | B.1                                                                                          |                              11 | 0.0667           |
| UK63           | Mar-18, May-10 |                   128 | B.1.1                                                                                        |                              48 | 0.0083           |
| UK494          | Mar-19, May-05 |                   125 | B.1.p11, B.1                                                                                 |                              53 | 0.007            |
| UK4            | Feb-28, Apr-29 |                   124 | B                                                                                            |                              59 | 0.008            |
| UK109          | Mar-12, Jun-12 |                   111 | B.1.5                                                                                        |                              15 | 0.0154           |
| UK61           | Feb-23, May-27 |                   107 | B.3                                                                                          |                              31 | 0.0057           |
| UK66           | Mar-18, May-20 |                   105 | B.1.1.8                                                                                      |                              38 | 0.0136           |
| UK28           | Mar-13, May-08 |                    99 | B.1.1.10                                                                                     |                              50 | 0.0114           |
| UK5180         | Mar-07, May-09 |                    93 | B.1.1.7                                                                                      |                              49 | 0.0129           |
| UK370          | Mar-06, Jun-16 |                    93 | B.1.1.10                                                                                     |                              11 | 0.0488           |
| UK51           | Mar-25, Jun-20 |                    88 | B.1.36                                                                                       |                               7 | 0.1368           |
| UK77           | Mar-11, May-20 |                    88 | B.2                                                                                          |                              38 | 0.0202           |
| UK829          | Mar-03, Apr-29 |                    84 | B.2.5                                                                                        |                              59 | 0.0115           |
| UK31           | Mar-12, Jun-27 |                    78 | B.3                                                                                          |                               0 | active today     |
| UK319          | Mar-28, Jun-03 |                    77 | B.1                                                                                          |                              24 | 0.0367           |
| UK5498         | Mar-06, May-28 |                    72 | B.2, B                                                                                       |                              30 | 0.0307           |
| UK2906         | Mar-03, Jun-02 |                    72 | B.1                                                                                          |                              25 | 0.0473           |
| UK384          | Feb-28, Apr-23 |                    70 | B.2, B.2.1                                                                                   |                              65 | 0.0118           |
| UK339          | Mar-09, Jun-18 |                    70 | B.3                                                                                          |                               9 | 0.1496           |
| UK36           | Mar-19, Jun-06 |                    68 | B.1                                                                                          |                              21 | 0.0063           |
| UK37           | Mar-17, May-04 |                    67 | B.1.30, B.1                                                                                  |                              54 | 0.0131           |
| UK501          | Mar-11, Jun-18 |                    66 | B.1                                                                                          |                               9 | 0.1279           |
| UK13           | Mar-13, May-21 |                    64 | B.1.1                                                                                        |                              37 | 0.0296           |
| UK274          | Mar-06, May-19 |                    63 | B, B.3                                                                                       |                              39 | 0.0292           |
| UK509          | Apr-07, May-29 |                    63 | B.1.1                                                                                        |                              29 | 0.0289           |
| UK607          | Mar-02, May-18 |                    58 | B                                                                                            |                              40 | 0.0279           |
| UK120          | Feb-27, Jun-07 |                    58 | B.14, B                                                                                      |                              20 | 0.0701           |
| UK89           | Mar-21, Jun-22 |                    58 | B.1.1.9, B.1.1                                                                               |                               5 | 0.2696           |
| UK335          | Mar-07, Jun-22 |                    58 | B.1.1                                                                                        |                               5 | 0.3057           |
| UK476          | Mar-14, May-06 |                    56 | B.1.1                                                                                        |                              52 | 0.0185           |
| UK376          | Mar-11, May-03 |                    55 | B.1.1.9                                                                                      |                              55 | 0.0178           |
| UK371          | Mar-12, May-06 |                    54 | B.1.1                                                                                        |                              52 | 0.0196           |
| UK5523         | Apr-16, Jun-01 |                    51 | B.1                                                                                          |                              26 | 0.0354           |
| UK448          | Apr-04, May-26 |                    50 | B.1.1                                                                                        |                              32 | 0.0325           |
| UK641          | Mar-25, Jun-17 |                    47 | B.1.1                                                                                        |                              10 | 0.1826           |
| UK517          | Mar-02, Apr-30 |                    47 | B.1.1                                                                                        |                              58 | 0.0208           |
| UK276          | Mar-15, May-13 |                    46 | B.1.1                                                                                        |                              45 | 0.0285           |
| UK478          | Mar-20, May-19 |                    46 | B.1.1                                                                                        |                              39 | 0.0342           |
| UK275          | Mar-09, Apr-27 |                    44 | B.1.13                                                                                       |                              61 | 0.0154           |
| UK632          | Mar-23, Jun-10 |                    42 | B.1.1                                                                                        |                              17 | 0.017            |
| UK3126         | Apr-06, May-19 |                    41 | B.1.1                                                                                        |                              39 | 0.0276           |
| UK623          | May-10, Jun-11 |                    40 | B.1.1                                                                                        |                              16 | 0.0513           |
| UK497          | Mar-13, Jun-03 |                    39 | A.2                                                                                          |                              24 | 0.0795           |
| UK12           | Mar-12, May-07 |                    39 | B.1.p11, B.1                                                                                 |                              51 | 0.0282           |
| UK5309         | Mar-20, Jun-18 |                    38 | B.1.1.10, B.1.1                                                                              |                               9 | 0.25             |
| UK1207         | Mar-23, Jun-01 |                    37 | B.1.1                                                                                        |                              26 | 0.0748           |
| UK2200         | Feb-28, Jun-06 |                    37 | B.1.5, B.1.5.6                                                                               |                              21 | 0.0441           |
| UK79           | Mar-24, May-05 |                    35 | B.1                                                                                          |                              53 | 0.0233           |
| UK636          | Mar-16, May-25 |                    34 | B.1.1                                                                                        |                              33 | 0.0643           |
| UK131          | Mar-11, Apr-14 |                    34 | B.15                                                                                         |                              74 | 0.0124           |
| UK404          | Mar-01, Apr-19 |                    32 | B.1                                                                                          |                              69 | 0.0229           |
| UK5549         | Mar-04, May-18 |                    31 | B.2.2                                                                                        |                              40 | 0.0536           |
| UK27           | Mar-05, May-21 |                    31 | B.1.1                                                                                        |                              37 | 0.0595           |
| UK18           | Mar-11, Apr-14 |                    31 | B.1.1.7                                                                                      |                              74 | 0.0153           |
| UK64           | Mar-12, May-05 |                    31 | B.1                                                                                          |                              53 | 0.0243           |
| UK241          | Mar-22, Apr-16 |                    31 | B.1.5.3                                                                                      |                              72 | 0.0116           |
| UK23           | Mar-18, May-09 |                    30 | B.9                                                                                          |                              49 | 0.0366           |
| UK119          | Mar-11, Apr-24 |                    29 | B.2.5                                                                                        |                              64 | 0.0191           |
| UK158          | Mar-23, Apr-24 |                    29 | B.1.1                                                                                        |                              64 | 0.0179           |
| UK5649         | Mar-15, May-04 |                    29 | B.2.6                                                                                        |                              54 | 0.0299           |
| UK668          | Mar-21, Jun-10 |                    28 | B.1                                                                                          |                              17 | 0.0419           |
| UK1721         | Mar-19, May-08 |                    27 | B.1                                                                                          |                              50 | 0.037            |
| UK101          | Mar-21, Apr-25 |                    26 | B.1.5                                                                                        |                              63 | 0.0214           |
| UK94           | Mar-12, Apr-19 |                    26 | B.2, B.2.1                                                                                   |                              69 | 0.022            |
| UK173          | Mar-14, Apr-20 |                    26 | B                                                                                            |                              68 | 0.0218           |
| UK615          | Mar-15, May-15 |                    26 | B.1.1                                                                                        |                              43 | 0.0567           |
| UK462          | May-01, Jun-09 |                    25 | B.1                                                                                          |                              18 | 0.1237           |
| UK46           | Mar-02, May-08 |                    25 | B.2.1                                                                                        |                              50 | 0.0515           |
| UK1177         | Apr-22, Jun-09 |                    25 | B.1.1                                                                                        |                              18 | 0.1111           |
| UK617          | Mar-29, Apr-28 |                    25 | B.1.1                                                                                        |                              60 | 0.0208           |
| UK326          | Mar-22, May-22 |                    24 | B.1.1.10                                                                                     |                              36 | 0.0706           |
| UK712          | Apr-08, Jun-18 |                    24 | B.1.5, B.1                                                                                   |                               9 | 0.343            |
| UK684          | Apr-11, May-21 |                    24 | B.1                                                                                          |                              37 | 0.0484           |
| UK605          | Mar-20, May-24 |                    24 | B.1.1                                                                                        |                              34 | 0.0187           |
| UK2045         | Mar-17, May-09 |                    23 | B.1                                                                                          |                              49 | 0.0492           |
| UK3021         | Mar-12, Jun-09 |                    23 | B.1                                                                                          |                              18 | 0.02             |
| UK601          | Mar-13, May-11 |                    23 | B.10                                                                                         |                              47 | 0.0134           |
| UK2787         | Apr-07, Jun-26 |                    23 | B.1.1                                                                                        |                               1 | 3.6364           |
| UK4237         | Mar-28, Jun-10 |                    22 | B.1.1                                                                                        |                              17 | 0.2073           |
| UK5300         | Apr-17, Jun-16 |                    22 | B.1.1                                                                                        |                              11 | 0.2479           |
| UK5503         | Mar-20, Jun-12 |                    21 | B.1                                                                                          |                              15 | 0.28             |
| UK24           | Mar-14, Apr-10 |                    21 | B.2.1                                                                                        |                              78 | 0.0173           |
| UK329          | Mar-17, Apr-26 |                    21 | B.1.34, B.1                                                                                  |                              62 | 0.0323           |
| UK174          | Mar-19, May-22 |                    21 | B.1.5                                                                                        |                              36 | 0.0889           |
| UK161          | Mar-10, May-25 |                    21 | B.1.1                                                                                        |                              33 | 0.096            |
| UK233          | May-25, Jun-15 |                    21 | B.1                                                                                          |                              12 | 0.0875           |
| UK47           | Mar-17, May-18 |                    20 | B.1.1                                                                                        |                              40 | 0.0646           |
| UK203          | Mar-22, Jun-03 |                    20 | B.1.1                                                                                        |                              24 | 0.1521           |
| UK1703         | Mar-16, May-01 |                    20 | B.1                                                                                          |                              57 | 0.0425           |
| UK125          | Apr-03, May-29 |                    19 | B.1.1                                                                                        |                              29 | 0.1089           |
| UK146          | Mar-24, May-07 |                    18 | B.1.1                                                                                        |                              51 | 0.0479           |
| UK179          | Mar-26, May-07 |                    17 | B.1.1, B.1.1.p11                                                                             |                              51 | 0.0278           |
| UK71           | Mar-08, May-06 |                    16 | B                                                                                            |                              52 | 0.0709           |
| UK5660         | Apr-25, May-08 |                    16 | B.1.1                                                                                        |                              50 | 0.0173           |
| UK70           | Mar-06, Apr-22 |                    16 | B.2                                                                                          |                              66 | 0.0396           |
| UK134          | Mar-04, Apr-07 |                    16 | B.1                                                                                          |                              81 | 0.0221           |
| UK569          | Mar-23, Jun-16 |                    16 | B.1.1                                                                                        |                              11 | 0.5152           |
| UK186          | Apr-08, Jun-09 |                    15 | B                                                                                            |                              18 | 0.2741           |
| UK153          | Mar-13, Apr-14 |                    15 | B.2, B.3                                                                                     |                              74 | 0.0309           |
| UK3692         | Mar-27, May-19 |                    15 | B.1.1                                                                                        |                              39 | 0.0969           |
| UK604          | Mar-09, Mar-17 |                    15 | B.1.1                                                                                        |                             102 | 0.0057           |
| UK38           | Mar-04, Apr-20 |                    14 | B.2.1                                                                                        |                              68 | 0.0494           |
| UK565          | Apr-14, May-14 |                    14 | B.1.1                                                                                        |                              44 | 0.0524           |
| UK32           | Mar-29, May-03 |                    14 | B.1.1                                                                                        |                              55 | 0.049            |
| UK832          | Mar-09, May-10 |                    14 | A.5                                                                                          |                              48 | 0.0923           |
| UK328          | Apr-13, Apr-23 |                    13 | B.1                                                                                          |                              65 | 0.0128           |
| UK268          | Mar-23, Jun-03 |                    13 | B.1.1                                                                                        |                              24 | 0.1875           |
| UK5663         | Mar-23, May-02 |                    13 | B.2                                                                                          |                              56 | 0.0595           |
| UK141          | Mar-22, Apr-24 |                    13 | B.1.1                                                                                        |                              64 | 0.043            |
| UK83           | Feb-29, Apr-13 |                    13 | B.1.1                                                                                        |                              75 | 0.0391           |
| UK5715         | Feb-29, Apr-22 |                    13 | B.2                                                                                          |                              66 | 0.0618           |
| UK602          | Mar-20, Apr-02 |                    13 | B.1.1                                                                                        |                              86 | 0.0126           |
| UK34           | Feb-27, Apr-02 |                    13 | B.4                                                                                          |                              86 | 0.0339           |
| UK165          | Apr-13, May-19 |                    13 | B                                                                                            |                              39 | 0.0769           |
| UK49           | Mar-12, May-01 |                    12 | B.9                                                                                          |                              57 | 0.0675           |
| UK132          | Mar-27, Apr-30 |                    12 | B.1                                                                                          |                              58 | 0.0489           |
| UK291          | Mar-29, May-14 |                    12 | B.1.5                                                                                        |                              44 | 0.095            |
| UK507          | Mar-18, Apr-30 |                    12 | B.1.1.10                                                                                     |                              58 | 0.0674           |
| UK22           | Mar-02, Apr-21 |                    11 | B                                                                                            |                              67 | 0.0746           |
| UK566          | Apr-02, Apr-21 |                    11 | B.1.1.10, B.1.1                                                                              |                              67 | 0.0258           |
| UK2888         | Apr-09, May-14 |                    11 | B.1.1                                                                                        |                              44 | 0.0795           |
| UK653          | Apr-07, May-19 |                    11 | B.1.1                                                                                        |                              39 | 0.1077           |
| UK193          | Mar-30, May-01 |                    11 | B.1.1                                                                                        |                              57 | 0.051            |
| UK287          | Mar-28, Apr-24 |                    11 | B.1                                                                                          |                              64 | 0.0384           |
| UK266          | Apr-06, Apr-30 |                    11 | B.1                                                                                          |                              58 | 0.0414           |
| UK215          | Mar-16, Apr-11 |                    11 | B.2                                                                                          |                              77 | 0.0338           |
| UK467          | Mar-23, Jun-05 |                    11 | B.1.1                                                                                        |                              22 | 0.3364           |
| UK759          | Mar-28, Apr-04 |                    11 | B.1.1                                                                                        |                              84 | 0.0083           |
| UK178          | Mar-14, Apr-13 |                    11 | B.1.1                                                                                        |                              75 | 0.04             |
| UK317          | Mar-13, Apr-20 |                    11 | B.3                                                                                          |                              68 | 0.0224           |
| UK415          | Apr-19, May-06 |                    11 | B.1                                                                                          |                              52 | 0.0327           |
| UK527          | Mar-22, Apr-18 |                    10 | B.1                                                                                          |                              70 | 0.0297           |
| UK5307         | Mar-10, May-12 |                    10 | B.1.1                                                                                        |                              46 | 0.1178           |
| UK5525         | Mar-31, Apr-29 |                    10 | B.1                                                                                          |                              59 | 0.0546           |
| UK340          | Mar-17, May-17 |                    10 | B.1.1                                                                                        |                              41 | 0.1488           |
| UK202          | Mar-10, Jun-04 |                    10 | B.1.1                                                                                        |                              23 | 0.1558           |
| UK5084         | Mar-28, Apr-16 |                    10 | B.1                                                                                          |                              72 | 0.024            |
| UK788          | Feb-28, Mar-05 |                    10 | B.4                                                                                          |                             114 | 0.0058           |
| UK819          | Apr-01, May-15 |                     9 | B.1                                                                                          |                              43 | 0.1279           |
| UK575          | Mar-14, Apr-16 |                     9 | B.2.1                                                                                        |                              72 | 0.0573           |
| UK284          | Apr-02, Apr-25 |                     9 | B.1.1                                                                                        |                              63 | 0.0456           |
| UK454          | Mar-22, Apr-29 |                     9 | B.1.1                                                                                        |                              59 | 0.0805           |
| UK491          | Mar-03, Apr-03 |                     9 | B.2, B                                                                                       |                              85 | 0.0456           |
| UK86           | Mar-05, May-30 |                     9 | B.1                                                                                          |                              28 | 0.0439           |
| UK5501         | Apr-16, Jun-01 |                     9 | B.1.12                                                                                       |                              26 | 0.2212           |
| UK756          | Feb-27, Mar-05 |                     9 | B.1.1                                                                                        |                             114 | 0.0077           |
| UK563          | Mar-11, May-01 |                     9 | B.1.1                                                                                        |                              57 | 0.1118           |
| UK5653         | Mar-10, Apr-01 |                     9 | B.2.6                                                                                        |                              87 | 0.0281           |
| UK263          | Mar-20, Apr-13 |                     9 | B.1.p11                                                                                      |                              75 | 0.04             |
| UK116          | Mar-24, Jun-02 |                     9 | B.1                                                                                          |                              25 | 0.1167           |
| UK113          | Mar-22, Jun-02 |                     9 | B.1.1                                                                                        |                              25 | 0.36             |
| UK629          | Mar-23, May-05 |                     9 | B.1                                                                                          |                              53 | 0.1014           |
| UK584          | Mar-21, Apr-02 |                     9 | B.2, B.2.1                                                                                   |                              86 | 0.0207           |
| UK3509         | Mar-23, Apr-21 |                     9 | B.1.1.10                                                                                     |                              67 | 0.0333           |
| UK121          | Apr-21, May-27 |                     9 | B.1.1.7                                                                                      |                              31 | 0.1452           |
| UK1810         | Mar-21, Apr-20 |                     8 | B.1.5, B.1                                                                                   |                              68 | 0.0551           |
| UK5308         | Apr-29, May-01 |                     8 | B.1.1                                                                                        |                              57 | 0.005            |
| UK698          | Mar-23, Apr-12 |                     8 | B.1                                                                                          |                              76 | 0.0329           |
| UK739          | Mar-01, Mar-08 |                     8 | B.4                                                                                          |                             111 | 0.009            |
| UK342          | Apr-02, Apr-22 |                     8 | B.1.1                                                                                        |                              66 | 0.0433           |
| UK65           | Mar-07, Apr-21 |                     8 | B.1.1                                                                                        |                              67 | 0.084            |
| UK4658         | Mar-13, Apr-10 |                     8 | B.2.1                                                                                        |                              78 | 0.0513           |
| UK570          | Mar-24, Apr-29 |                     8 | B.1.1                                                                                        |                              59 | 0.0872           |
| UK91           | Mar-01, Apr-01 |                     8 | B.1                                                                                          |                              87 | 0.0445           |
| UK244          | Mar-10, Apr-06 |                     8 | B.1.1                                                                                        |                              82 | 0.0412           |
| UK755          | Mar-06, May-21 |                     8 | B.1.1                                                                                        |                              37 | 0.2934           |
| UK767          | Apr-05, Apr-19 |                     7 | B.1                                                                                          |                              69 | 0.0338           |
| UK490          | Apr-03, May-02 |                     7 | B.1.1                                                                                        |                              56 | 0.0863           |
| UK195          | May-19, Jun-15 |                     7 | B.1                                                                                          |                              12 | 0.3214           |
| UK390          | Mar-27, May-01 |                     7 | B.1.5                                                                                        |                              57 | 0.1023           |
| UK799          | Mar-01, Mar-07 |                     7 | B.1                                                                                          |                             112 | 0.0089           |
| UK232          | Mar-04, Mar-30 |                     7 | B.1.1                                                                                        |                              89 | 0.0487           |
| UK54           | Mar-11, Apr-02 |                     7 | B.2.4                                                                                        |                              86 | 0.0426           |
| UK520          | Mar-14, Apr-08 |                     7 | B.2.1                                                                                        |                              80 | 0.0521           |
| UK269          | Mar-25, Jun-02 |                     7 | B.1.1                                                                                        |                              25 | 0.46             |
| UK1003         | Apr-02, Apr-22 |                     7 | B.1.1                                                                                        |                              66 | 0.0505           |
| UK728          | Mar-19, Apr-01 |                     7 | B.2, B.2.1                                                                                   |                              87 | 0.0249           |
| UK369          | Mar-22, Apr-11 |                     7 | B.1.1                                                                                        |                              77 | 0.0371           |
| UK98           | Mar-24, Jun-08 |                     7 | B.6                                                                                          |                              19 | 0.6667           |
| UK598          | Mar-22, Apr-14 |                     7 | B.1.1                                                                                        |                              74 | 0.0444           |
| UK60           | Mar-21, Mar-30 |                     6 | B                                                                                            |                              89 | 0.0202           |
| UK55           | Mar-13, May-06 |                     6 | B.1.1                                                                                        |                              52 | 0.1154           |
| UK654          | Feb-27, Mar-08 |                     6 | B.2.5                                                                                        |                             111 | 0.018            |
| UK293          | Mar-13, Apr-16 |                     6 | B.3                                                                                          |                              72 | 0.0944           |
| UK40           | Mar-31, Jun-08 |                     6 | B.16                                                                                         |                              19 | 0.0206           |
| UK75           | Mar-28, Apr-12 |                     6 | B                                                                                            |                              76 | 0.0329           |
| UK403          | Mar-23, Apr-14 |                     6 | B.1.1                                                                                        |                              74 | 0.0595           |
| UK270          | Mar-04, Apr-03 |                     6 | B                                                                                            |                              85 | 0.0588           |
| UK456          | Apr-03, Apr-23 |                     6 | B.1.1                                                                                        |                              65 | 0.0615           |
| UK479          | Apr-05, Jun-12 |                     6 | B.1.1                                                                                        |                              15 | 0.1374           |
| UK5098         | Mar-16, Jun-05 |                     6 | B.1.p73, B.1.8, B.1                                                                          |                              22 | 0.0099           |
| UK5648         | Mar-08, Apr-02 |                     6 | B.2                                                                                          |                              86 | 0.0581           |
| UK777          | Apr-01, Apr-14 |                     6 | B.1                                                                                          |                              74 | 0.0351           |
| UK521          | Mar-31, May-01 |                     6 | B.1.1                                                                                        |                              57 | 0.1088           |
| UK1867         | Mar-18, Apr-30 |                     6 | B.1.1                                                                                        |                              58 | 0.1483           |
| UK957          | Mar-24, May-26 |                     6 | B.1.1                                                                                        |                              32 | 0.3281           |
| UK320          | Apr-11, Jun-02 |                     6 | B.1                                                                                          |                              25 | 0.24             |
| UK196          | Mar-15, Mar-31 |                     6 | B.2.1                                                                                        |                              88 | 0.0364           |
| UK58           | Mar-13, Apr-24 |                     6 | B.1                                                                                          |                              64 | 0.0305           |
| UK743          | Feb-24, Jun-14 |                     6 | B.1.5.1                                                                                      |                              13 | 1.7077           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NOTT     |             6 |
|  1 | BIRM     |             8 |
|  2 | SHEF     |             9 |
|  3 | CAMB     |            10 |
|  4 | NORW     |            15 |
|  5 | PHEC     |            16 |
|  6 | LIVE     |            17 |
|  7 | SANG     |            24 |
|  8 | PORT     |            24 |
|  9 | EXET     |            30 |
| 10 | NORT     |            33 |
| 11 | OXON     |            45 |
| 12 | LOND     |            50 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK107 |   UK42 |   UK2913 |   UK2916 |   UK2464 |   UK72 |   UK199 |   UK167 |   UK5741 |
|:------------------|------:|--------:|-------:|---------:|---------:|---------:|-------:|--------:|--------:|---------:|
| 2020-02-02        |     0 |       0 |      0 |        0 |        1 |        0 |      1 |       0 |       0 |        0 |
| 2020-02-09        |     0 |       1 |      0 |        0 |        0 |        0 |      0 |       0 |       0 |        0 |
| 2020-02-16        |     1 |       0 |      0 |        0 |        0 |        0 |      0 |       0 |       0 |        0 |
| 2020-02-23        |     1 |       5 |      4 |        0 |       10 |        0 |      2 |       1 |       0 |        0 |
| 2020-03-01        |     9 |       6 |     14 |        1 |       14 |        0 |      8 |       1 |       1 |        0 |
| 2020-03-08        |    22 |      17 |     11 |        4 |        8 |        4 |     12 |       3 |       6 |        2 |
| 2020-03-15        |    25 |      22 |     16 |        6 |        9 |        7 |     17 |       7 |       4 |        4 |
| 2020-03-22        |    33 |      25 |     21 |       16 |        9 |       13 |     18 |      14 |      11 |        7 |
| 2020-03-29        |    36 |      27 |     24 |       19 |       14 |       17 |     17 |      18 |      12 |       12 |
| 2020-04-05        |    36 |      21 |     23 |       17 |       11 |       13 |     13 |      17 |      14 |       11 |
| 2020-04-12        |    39 |      19 |     17 |       13 |        9 |       13 |      4 |      11 |      14 |        7 |
| 2020-04-19        |    50 |      15 |     18 |       10 |       10 |       11 |      9 |      10 |      11 |       12 |
| 2020-04-26        |    47 |      10 |     14 |        7 |        6 |        8 |      2 |      10 |       5 |        6 |
| 2020-05-03        |    49 |       4 |     12 |        2 |        3 |        4 |      3 |       6 |       6 |        4 |
| 2020-05-10        |    44 |       1 |      5 |        3 |        2 |        3 |      1 |       5 |       5 |        2 |
| 2020-05-17        |    35 |       1 |      2 |        2 |        0 |        2 |      0 |       2 |       6 |        0 |
| 2020-05-24        |    24 |       0 |      2 |        3 |        0 |        1 |      3 |       3 |       2 |        0 |
| 2020-05-31        |    26 |       1 |      5 |        4 |        2 |        2 |      1 |       1 |       3 |        0 |
| 2020-06-07        |    21 |       0 |      0 |        0 |        1 |        1 |      0 |       1 |       1 |        1 |
| 2020-06-14        |    10 |       0 |      0 |        1 |        0 |        2 |      0 |       0 |       0 |        0 |
| 2020-06-21        |     5 |       0 |      1 |        0 |        0 |        0 |      0 |       0 |       0 |        0 |

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
| 2020-03-06 |                            4 |                                8 |      12 |
| 2020-03-07 |                            4 |                                6 |      10 |
| 2020-03-08 |                            1 |                                4 |       5 |
| 2020-03-09 |                            4 |                               12 |      16 |
| 2020-03-10 |                            5 |                                8 |      13 |
| 2020-03-11 |                            7 |                               14 |      21 |
| 2020-03-12 |                            5 |                               23 |      28 |
| 2020-03-13 |                            8 |                               11 |      19 |
| 2020-03-14 |                            3 |                                8 |      11 |
| 2020-03-15 |                            6 |                                5 |      11 |
| 2020-03-16 |                            2 |                                5 |       7 |
| 2020-03-17 |                            4 |                               15 |      19 |
| 2020-03-18 |                            8 |                               18 |      26 |
| 2020-03-19 |                            6 |                               10 |      16 |
| 2020-03-20 |                            6 |                               20 |      26 |
| 2020-03-21 |                            7 |                               11 |      18 |
| 2020-03-22 |                            9 |                               17 |      26 |
| 2020-03-23 |                            8 |                               23 |      31 |
| 2020-03-24 |                            9 |                               18 |      27 |
| 2020-03-25 |                           12 |                               15 |      27 |
| 2020-03-26 |                            7 |                               17 |      24 |
| 2020-03-27 |                            9 |                               11 |      20 |
| 2020-03-28 |                           10 |                               15 |      25 |
| 2020-03-29 |                           15 |                                9 |      24 |
| 2020-03-30 |                           14 |                               18 |      32 |
| 2020-03-31 |                           22 |                               19 |      41 |
| 2020-04-01 |                           12 |                                9 |      21 |
| 2020-04-02 |                            8 |                               15 |      23 |
| 2020-04-03 |                           14 |                                9 |      23 |
| 2020-04-04 |                            8 |                                4 |      12 |
| 2020-04-05 |                           12 |                                8 |      20 |
| 2020-04-06 |                            6 |                               12 |      18 |
| 2020-04-07 |                            6 |                               10 |      16 |
| 2020-04-08 |                            9 |                                6 |      15 |
| 2020-04-09 |                            7 |                                2 |       9 |
| 2020-04-10 |                            8 |                                3 |      11 |
| 2020-04-11 |                            8 |                                3 |      11 |
| 2020-04-12 |                            4 |                                2 |       6 |
| 2020-04-13 |                           10 |                                5 |      15 |
| 2020-04-14 |                            7 |                                4 |      11 |
| 2020-04-15 |                            1 |                                4 |       5 |
| 2020-04-16 |                           13 |                                4 |      17 |
| 2020-04-17 |                            5 |                                3 |       8 |
| 2020-04-18 |                            7 |                                3 |      10 |
| 2020-04-19 |                            4 |                                2 |       6 |
| 2020-04-20 |                            4 |                                2 |       6 |
| 2020-04-21 |                           10 |                                2 |      12 |
| 2020-04-22 |                            3 |                                2 |       5 |
| 2020-04-23 |                            1 |                                4 |       5 |
| 2020-04-24 |                            3 |                                2 |       5 |
| 2020-04-25 |                            1 |                                2 |       3 |
| 2020-04-26 |                            2 |                                0 |       2 |
| 2020-04-27 |                            2 |                                2 |       4 |
| 2020-04-28 |                            6 |                                3 |       9 |
| 2020-04-29 |                            3 |                                1 |       4 |
| 2020-04-30 |                            3 |                                0 |       3 |
| 2020-05-01 |                            2 |                                1 |       3 |
| 2020-05-03 |                            3 |                                0 |       3 |
| 2020-05-04 |                            4 |                                2 |       6 |
| 2020-05-05 |                            1 |                                0 |       1 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-07 |                            0 |                                2 |       2 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-10 |                            0 |                                1 |       1 |
| 2020-05-11 |                            2 |                                0 |       2 |
| 2020-05-12 |                            2 |                                0 |       2 |
| 2020-05-14 |                            2 |                                1 |       3 |
| 2020-05-17 |                            2 |                                0 |       2 |
| 2020-05-19 |                            0 |                                1 |       1 |
| 2020-05-20 |                            0 |                                1 |       1 |
| 2020-05-22 |                            1 |                                0 |       1 |
| 2020-05-25 |                            0 |                                1 |       1 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-06-03 |                            1 |                                0 |       1 |
| 2020-06-04 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-06 |                            0 |                                1 |       1 |
| 2020-06-08 |                            1 |                                0 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-02-03 |         1 |
| 2020-02-05 |         1 |
| 2020-02-08 |         2 |
| 2020-02-09 |         1 |
| 2020-02-13 |         1 |
| 2020-02-16 |         1 |
| 2020-02-23 |         2 |
| 2020-02-24 |         5 |
| 2020-02-25 |         7 |
| 2020-02-26 |         6 |
| 2020-02-27 |        19 |
| 2020-02-28 |        24 |
| 2020-02-29 |        23 |
| 2020-03-01 |        51 |
| 2020-03-02 |        76 |
| 2020-03-03 |        97 |
| 2020-03-04 |       107 |
| 2020-03-05 |        85 |
| 2020-03-06 |        81 |
| 2020-03-07 |        46 |
| 2020-03-08 |        53 |
| 2020-03-09 |        75 |
| 2020-03-10 |        98 |
| 2020-03-11 |       151 |
| 2020-03-12 |       193 |
| 2020-03-13 |       113 |
| 2020-03-14 |        95 |
| 2020-03-15 |        86 |
| 2020-03-16 |        95 |
| 2020-03-17 |       136 |
| 2020-03-18 |       209 |
| 2020-03-19 |       172 |
| 2020-03-20 |       225 |
| 2020-03-21 |       232 |
| 2020-03-22 |       213 |
| 2020-03-23 |       385 |
| 2020-03-24 |       347 |
| 2020-03-25 |       341 |
| 2020-03-26 |       367 |
| 2020-03-27 |       356 |
| 2020-03-28 |       372 |
| 2020-03-29 |       407 |
| 2020-03-30 |       573 |
| 2020-03-31 |       562 |
| 2020-04-01 |       467 |
| 2020-04-02 |       461 |
| 2020-04-03 |       507 |
| 2020-04-04 |       382 |
| 2020-04-05 |       374 |
| 2020-04-06 |       447 |
| 2020-04-07 |       407 |
| 2020-04-08 |       397 |
| 2020-04-09 |       372 |
| 2020-04-10 |       350 |
| 2020-04-11 |       277 |
| 2020-04-12 |       233 |
| 2020-04-13 |       296 |
| 2020-04-14 |       335 |
| 2020-04-15 |       336 |
| 2020-04-16 |       376 |
| 2020-04-17 |       349 |
| 2020-04-18 |       262 |
| 2020-04-19 |       236 |
| 2020-04-20 |       318 |
| 2020-04-21 |       272 |
| 2020-04-22 |       284 |
| 2020-04-23 |       268 |
| 2020-04-24 |       175 |
| 2020-04-25 |       120 |
| 2020-04-26 |       119 |
| 2020-04-27 |       193 |
| 2020-04-28 |       169 |
| 2020-04-29 |       240 |
| 2020-04-30 |       202 |
| 2020-05-01 |       229 |
| 2020-05-02 |       123 |
| 2020-05-03 |       104 |
| 2020-05-04 |       194 |
| 2020-05-05 |       133 |
| 2020-05-06 |       158 |
| 2020-05-07 |       143 |
| 2020-05-08 |        90 |
| 2020-05-09 |        66 |
| 2020-05-10 |        92 |
| 2020-05-11 |       132 |
| 2020-05-12 |        92 |
| 2020-05-13 |        87 |
| 2020-05-14 |        61 |
| 2020-05-15 |        70 |
| 2020-05-16 |        49 |
| 2020-05-17 |        34 |
| 2020-05-18 |        76 |
| 2020-05-19 |        64 |
| 2020-05-20 |        36 |
| 2020-05-21 |        47 |
| 2020-05-22 |        40 |
| 2020-05-23 |        21 |
| 2020-05-24 |        21 |
| 2020-05-25 |        42 |
| 2020-05-26 |        46 |
| 2020-05-27 |        34 |
| 2020-05-28 |        35 |
| 2020-05-29 |        21 |
| 2020-05-30 |        29 |
| 2020-05-31 |        39 |
| 2020-06-01 |        49 |
| 2020-06-02 |        51 |
| 2020-06-03 |        49 |
| 2020-06-04 |        41 |
| 2020-06-05 |        30 |
| 2020-06-06 |        21 |
| 2020-06-07 |        26 |
| 2020-06-08 |        32 |
| 2020-06-09 |        31 |
| 2020-06-10 |        29 |
| 2020-06-11 |        19 |
| 2020-06-12 |        16 |
| 2020-06-13 |        12 |
| 2020-06-14 |        11 |
| 2020-06-15 |        21 |
| 2020-06-16 |        18 |
| 2020-06-17 |        14 |
| 2020-06-18 |        26 |
| 2020-06-19 |         7 |
| 2020-06-20 |         4 |
| 2020-06-21 |         3 |
| 2020-06-22 |         2 |
| 2020-06-23 |         4 |
| 2020-06-24 |         1 |
| 2020-06-25 |         1 |
| 2020-06-26 |         1 |
| 2020-06-27 |         1 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                       | Country   |   Number of sequences | Sequence group   |
|:-----------------------------|:----------|----------------------:|:-----------------|
| BATH AND NORTH EAST SOMERSET | England   |                     0 | 0                |
| BEDFORDSHIRE                 | England   |                   452 | 400-500          |
| BERKSHIRE                    | England   |                    21 | 10-50            |
| BLACKBURN WITH DARWEN        | England   |                     0 | 0                |
| BLACKPOOL                    | England   |                     0 | 0                |
| BOLTON                       | England   |                     0 | 0                |
| BOURNEMOUTH                  | England   |                     0 | 0                |
| BRIGHTON AND HOVE            | England   |                     0 | 0                |
| BRISTOL                      | England   |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England   |                   413 | 400-500          |
| BURY                         | England   |                     0 | 0                |
| CAMBRIDGESHIRE               | England   |                   727 | >500             |
| CENTRAL BEDFORDSHIRE         | England   |                     0 | 0                |
| CHESHIRE                     | England   |                    44 | 10-50            |
| CORNWALL                     | England   |                    27 | 10-50            |
| CUMBRIA                      | England   |                    78 | 50-100           |
| DARLINGTON                   | England   |                     0 | 0                |
| DERBY                        | England   |                     0 | 0                |
| DERBYSHIRE                   | England   |                    30 | 10-50            |
| DEVON                        | England   |                   421 | 400-500          |
| DORSET                       | England   |                   192 | 150-200          |
| DURHAM                       | England   |                   161 | 150-200          |
| EAST RIDING OF YORKSHIRE     | England   |                    35 | 10-50            |
| ESSEX                        | England   |                  1432 | >500             |
| GATESHEAD                    | England   |                     0 | 0                |
| GLOUCESTERSHIRE              | England   |                   708 | >500             |
| GREATER LONDON               | England   |                  2654 | >500             |
| HALTON                       | England   |                     0 | 0                |
| HAMPSHIRE                    | England   |                   347 | 300-400          |
| HARTLEPOOL                   | England   |                     0 | 0                |
| HEREFORDSHIRE                | England   |                    59 | 50-100           |
| HERTFORDSHIRE                | England   |                  1031 | >500             |
| ISLE OF WIGHT                | England   |                     1 | 1-10             |
| ISLES OF SCILLY              | England   |                     0 | 0                |
| KENT                         | England   |                    38 | 10-50            |
| KINGSTON UPON HULL           | England   |                     0 | 0                |
| LANCASHIRE                   | England   |                    53 | 50-100           |
| LEICESTER                    | England   |                     0 | 0                |
| LEICESTERSHIRE               | England   |                   109 | 100-150          |
| LINCOLNSHIRE                 | England   |                    73 | 50-100           |
| LUTON                        | England   |                     0 | 0                |
| MANCHESTER                   | England   |                    30 | 10-50            |
| MEDWAY                       | England   |                     0 | 0                |
| MERSEYSIDE                   | England   |                   549 | >500             |
| MIDDLESBROUGH                | England   |                     0 | 0                |
| MILTON KEYNES                | England   |                     0 | 0                |
| NORFOLK                      | England   |                   626 | >500             |
| NORTH LINCOLNSHIRE           | England   |                     0 | 0                |
| NORTH SOMERSET               | England   |                     0 | 0                |
| NORTH YORKSHIRE              | England   |                   123 | 100-150          |
| NORTHAMPTONSHIRE             | England   |                    28 | 10-50            |
| NORTHUMBERLAND               | England   |                   172 | 150-200          |
| NOTTINGHAM                   | England   |                   685 | >500             |
| NOTTINGHAMSHIRE              | England   |                    59 | 50-100           |
| OLDHAM                       | England   |                     0 | 0                |
| OXFORDSHIRE                  | England   |                    98 | 50-100           |
| PETERBOROUGH                 | England   |                     0 | 0                |
| PLYMOUTH                     | England   |                     1 | 1-10             |
| POOLE                        | England   |                     0 | 0                |
| PORTSMOUTH                   | England   |                     0 | 0                |
| REDCAR AND CLEVELAND         | England   |                     0 | 0                |
| ROCHDALE                     | England   |                     0 | 0                |
| RUTLAND                      | England   |                     0 | 0                |
| SALFORD                      | England   |                     0 | 0                |
| SHROPSHIRE                   | England   |                     6 | 1-10             |
| SOMERSET                     | England   |                   652 | >500             |
| SOUTH GLOUCESTERSHIRE        | England   |                     0 | 0                |
| SOUTH YORKSHIRE              | England   |                  1594 | >500             |
| SOUTHAMPTON                  | England   |                     0 | 0                |
| SOUTHEND-ON-SEA              | England   |                     0 | 0                |
| STAFFORDSHIRE                | England   |                    62 | 50-100           |
| STOCKPORT                    | England   |                     0 | 0                |
| STOCKTON-ON-TEES             | England   |                     0 | 0                |
| STOKE-ON-TRENT               | England   |                     0 | 0                |
| SUFFOLK                      | England   |                   596 | >500             |
| SURREY                       | England   |                    73 | 50-100           |
| SUSSEX                       | England   |                     1 | 1-10             |
| SWINDON                      | England   |                     0 | 0                |
| TAMESIDE                     | England   |                     0 | 0                |
| TELFORD AND WREKIN           | England   |                     0 | 0                |
| THURROCK                     | England   |                     0 | 0                |
| TORBAY                       | England   |                     0 | 0                |
| TRAFFORD                     | England   |                     0 | 0                |
| TYNE AND WEAR                | England   |                   496 | 400-500          |
| WARRINGTON                   | England   |                     0 | 0                |
| WARWICKSHIRE                 | England   |                    11 | 10-50            |
| WEST MIDLANDS                | England   |                   167 | 150-200          |
| WEST YORKSHIRE               | England   |                    22 | 10-50            |
| WIGAN                        | England   |                     0 | 0                |
| WILTSHIRE                    | England   |                   386 | 300-400          |
| WORCESTERSHIRE               | England   |                    13 | 10-50            |
| YORK                         | England   |                     0 | 0                |

\pagebreak






