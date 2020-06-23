







# Lineages report for England




This report gives summaries of lineages sampled in England for week 2020-06-19. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-14. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
16137 sequences from England have been included in this analysis.
859 lineages have been recorded, 423 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 386 and the maximum is 7493


Sequences which were replicates or too error-prone were removed from this analysis.



788 are lineages which were sampled less than five times in England, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 71 that remain:
36 are pending extinction, ie last seen three weeks ago.
29 lineages have gone quiet, ie haven't been seen this week.
1 has reactivated.
5 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Date range     |   Number of sequences | Global lineage                                           |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:---------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | Feb-23, Jun-14 |                  5390 | B.1.1, B.1.1.p15, B.1.1.10, B.1.1.p11, B.1.1.13, B.1.1.1 |                               0 | active today     |
| UK107          | Feb-09, Jun-02 |                  1183 | B.2, B.2.1, B.2.5                                        |                              12 | 0.0074           |
| UK42           | Feb-03, Jun-04 |                   699 | B.1.72, B.1, B.1.35, B.1.5                               |                              10 | 0.0093           |
| UK5676         | Feb-14, May-22 |                   328 | B.2                                                      |                              23 | 0.0081           |
| UK2913         | Mar-07, Jun-01 |                   307 | B.1.p11, B.1                                             |                              13 | 0.016            |
| UK2464         | Mar-09, Jun-07 |                   283 | B.1.p11, B.1                                             |                               7 | 0.0264           |
| UK2916         | Feb-03, Jun-01 |                   252 | B.1                                                      |                              13 | 0.0283           |
| UK72           | Feb-05, May-27 |                   251 | B.2, B.2.2, B                                            |                              18 | 0.0193           |
| UK199          | Feb-26, Jun-08 |                   243 | B.1.5.5, B.1.5, B.1                                      |                               6 | 0.0398           |
| UK167          | Mar-06, Jun-07 |                   241 | B.1.66, B.1                                              |                               7 | 0.0482           |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 



NB the lineage may have started anywhere in the UK, but has been recorded at least once in England



![Lineage starts per week, split by singletons and non-singletons](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](/cephfs/covid/bham/raccoon-dog/2020-06-19/analysis/7/adm1_reports/England/figures/England_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Date range     |   Number of sequences | Global lineage                                           |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:---------------------------------------------------------|--------------------------------:|:-----------------|
| UK5            | Feb-23, Jun-14 |                  5390 | B.1.1, B.1.1.p15, B.1.1.10, B.1.1.p11, B.1.1.13, B.1.1.1 |                               0 | active today     |
| UK107          | Feb-09, Jun-02 |                  1183 | B.2, B.2.1, B.2.5                                        |                              12 | 0.0074           |
| UK42           | Feb-03, Jun-04 |                   699 | B.1.72, B.1, B.1.35, B.1.5                               |                              10 | 0.0093           |
| UK5676         | Feb-14, May-22 |                   328 | B.2                                                      |                              23 | 0.0081           |
| UK2913         | Mar-07, Jun-01 |                   307 | B.1.p11, B.1                                             |                              13 | 0.016            |
| UK2464         | Mar-09, Jun-07 |                   283 | B.1.p11, B.1                                             |                               7 | 0.0264           |
| UK2916         | Feb-03, Jun-01 |                   252 | B.1                                                      |                              13 | 0.0283           |
| UK72           | Feb-05, May-27 |                   251 | B.2, B.2.2, B                                            |                              18 | 0.0193           |
| UK199          | Feb-26, Jun-08 |                   243 | B.1.5.5, B.1.5, B.1                                      |                               6 | 0.0398           |
| UK167          | Mar-06, Jun-07 |                   241 | B.1.66, B.1                                              |                               7 | 0.0482           |
| UK9            | Mar-09, May-15 |                   213 | B.1.13                                                   |                              30 | 0.0105           |
| UK3929         | Mar-06, Jun-03 |                   175 | B.1.1, B.1.1.3, B.1.1.4                                  |                              11 | 0.0385           |
| UK5741         | Mar-09, Jun-02 |                   161 | B.1                                                      |                              12 | 0.0261           |
| UK2735         | Mar-18, May-29 |                   142 | B.1.1                                                    |                              16 | 0.0183           |
| UK6            | Mar-06, May-13 |                   133 | B.1                                                      |                              32 | 0.0155           |
| UK15           | Feb-27, May-06 |                   128 | B.1.1                                                    |                              39 | 0.0106           |
| UK4            | Feb-28, Apr-29 |                   124 | B                                                        |                              46 | 0.0105           |
| UK63           | Mar-18, May-10 |                   121 | B.1.1                                                    |                              35 | 0.0125           |
| UK494          | Mar-19, May-05 |                   121 | B.1.p11                                                  |                              40 | 0.0096           |
| UK5561         | Feb-25, May-24 |                   119 | B.2, B.2.2                                               |                              21 | 0.0288           |
| UK565          | Mar-11, May-14 |                   102 | B.1.1                                                    |                              31 | 0.0186           |
| UK66           | Mar-18, May-20 |                    92 | B.1.1.8                                                  |                              25 | 0.0231           |
| UK28           | Mar-13, May-08 |                    89 | B.1.1.10                                                 |                              37 | 0.0172           |
| UK240          | Feb-25, May-08 |                    84 | B.2.5, B.2, B.3, B.2.1, B                                |                              37 | 0.0217           |
| UK5180         | Mar-07, May-09 |                    81 | B.1.1.7                                                  |                              36 | 0.0199           |
| UK370          | Mar-06, Jun-02 |                    81 | B.1.1.10                                                 |                              12 | 0.0421           |
| UK829          | Mar-03, Apr-29 |                    80 | B.2.5                                                    |                              46 | 0.0155           |
| UK51           | Mar-25, Jun-07 |                    72 | B.1.36                                                   |                               7 | 0.141            |
| UK319          | Mar-28, Jun-01 |                    71 | B.1                                                      |                              13 | 0.0714           |
| UK2906         | Mar-06, Jun-02 |                    68 | B.1                                                      |                              12 | 0.1027           |
| UK77           | Mar-11, May-20 |                    67 | B.2                                                      |                              25 | 0.0394           |
| UK501          | Mar-02, Jun-02 |                    66 | B.1                                                      |                              12 | 0.0996           |
| UK5498         | Mar-06, May-28 |                    66 | B.2, B                                                   |                              17 | 0.0588           |
| UK37           | Mar-17, May-04 |                    63 | B.1, B.1.30                                              |                              41 | 0.0183           |
| UK366          | Apr-04, Jun-03 |                    63 | B.1.1                                                    |                              11 | 0.088            |
| UK85           | Mar-09, Apr-27 |                    63 | B.3, B                                                   |                              48 | 0.0148           |
| UK509          | Apr-07, May-29 |                    62 | B.1.1                                                    |                              16 | 0.0533           |
| UK339          | Feb-23, Apr-16 |                    61 | B.3                                                      |                              59 | 0.0114           |
| UK384          | Feb-28, Apr-23 |                    60 | B.2, B.2.1                                               |                              52 | 0.0171           |
| UK31           | Mar-11, Apr-23 |                    60 | B.3                                                      |                              52 | 0.0131           |
| UK274          | Mar-06, May-21 |                    60 | B.3, B                                                   |                              24 | 0.0511           |
| UK36           | Mar-19, Jun-03 |                    59 | B.1                                                      |                              11 | 0.0169           |
| UK13           | Mar-13, May-13 |                    55 | B.1.1                                                    |                              32 | 0.0353           |
| UK476          | Mar-30, May-06 |                    55 | B.1.1                                                    |                              39 | 0.0176           |
| UK607          | Mar-02, May-18 |                    53 | B                                                        |                              27 | 0.0446           |
| UK120          | Feb-03, May-05 |                    52 | B.14, B                                                  |                              40 | 0.0354           |
| UK513          | Mar-12, Apr-29 |                    50 | B.1.p11                                                  |                              46 | 0.0213           |
| UK371          | Mar-12, May-09 |                    50 | B.1.1                                                    |                              36 | 0.0322           |
| UK448          | Apr-04, May-26 |                    47 | B.1.1                                                    |                              19 | 0.0582           |
| UK109          | Mar-12, Jun-08 |                    46 | B.1.5                                                    |                               6 | 0.0475           |
| UK5523         | May-01, Jun-01 |                    46 | B.1                                                      |                              13 | 0.053            |
| UK517          | Mar-02, Apr-30 |                    43 | B.1.1                                                    |                              45 | 0.0291           |
| UK89           | Mar-21, Jun-05 |                    42 | B.1.1, B.1.1.9                                           |                               9 | 0.1593           |
| UK61           | Mar-12, May-27 |                    41 | B.3                                                      |                              18 | 0.0102           |
| UK3126         | Apr-06, May-19 |                    41 | B.1.1                                                    |                              26 | 0.0413           |
| UK632          | Mar-23, Jun-04 |                    38 | B.1.1                                                    |                              10 | 0.0298           |
| UK376          | Mar-11, Apr-30 |                    38 | B.1.1.9                                                  |                              45 | 0.03             |
| UK497          | Mar-13, Jun-03 |                    38 | A.2                                                      |                              11 | 0.1818           |
| UK173          | Mar-14, May-19 |                    38 | B                                                        |                              26 | 0.0686           |
| UK275          | Mar-09, Apr-27 |                    38 | B.1.13                                                   |                              48 | 0.0222           |
| UK404          | Mar-01, Apr-19 |                    37 | B.1                                                      |                              56 | 0.0243           |
| UK276          | Mar-10, May-13 |                    37 | B.1.1                                                    |                              32 | 0.0526           |
| UK12           | Mar-12, May-07 |                    36 | B.1.p11                                                  |                              38 | 0.0409           |
| UK79           | Mar-24, May-05 |                    35 | B.1                                                      |                              40 | 0.0309           |
| UK355          | Mar-22, Jun-14 |                    35 | B.1.1                                                    |                               0 | active today     |
| UK131          | Mar-11, Apr-14 |                    34 | B.15                                                     |                              61 | 0.0151           |
| UK158          | Mar-23, Jun-03 |                    33 | B.1.1, B.1.1.2                                           |                              11 | 0.0205           |
| UK18           | Mar-11, Apr-14 |                    31 | B.1.1.7                                                  |                              61 | 0.0186           |
| UK1207         | Mar-23, May-12 |                    30 | B.1.1                                                    |                              33 | 0.0522           |
| UK41           | Feb-29, May-21 |                    30 | B.1                                                      |                              24 | 0.0813           |
| UK241          | Mar-22, Apr-16 |                    30 | B.1.5.3                                                  |                              59 | 0.0146           |
| UK119          | Mar-11, Apr-24 |                    27 | B.2.5                                                    |                              51 | 0.0254           |
| UK64           | Mar-12, May-05 |                    26 | B.1                                                      |                              40 | 0.0346           |
| UK101          | Mar-21, Apr-25 |                    26 | B.1.5                                                    |                              50 | 0.0269           |
| UK94           | Mar-12, Apr-19 |                    26 | B.2, B.2.1                                               |                              56 | 0.0271           |
| UK1721         | Mar-19, May-08 |                    26 | B.1                                                      |                              37 | 0.052            |
| UK23           | Mar-21, May-09 |                    25 | B.9                                                      |                              36 | 0.0567           |
| UK5649         | Mar-15, May-04 |                    24 | B.2.6                                                    |                              41 | 0.0469           |
| UK326          | Mar-22, May-22 |                    24 | B.1.1.10                                                 |                              23 | 0.1105           |
| UK164          | Apr-11, May-28 |                    24 | B.1                                                      |                              17 | 0.1225           |
| UK5549         | Mar-04, May-18 |                    24 | B.2.2                                                    |                              27 | 0.1068           |
| UK46           | Mar-02, May-08 |                    23 | B.2.1                                                    |                              37 | 0.0787           |
| UK5309         | Mar-20, May-30 |                    23 | B.1.1, B.1.1.10                                          |                              15 | 0.1893           |
| UK3021         | Mar-12, Jun-06 |                    23 | B.1                                                      |                               8 | 0.045            |
| UK2200         | Feb-28, May-20 |                    22 | B.1.5.6, B.1.5                                           |                              25 | 0.0349           |
| UK3692         | Mar-09, May-19 |                    22 | B.1.1                                                    |                              26 | 0.0975           |
| UK24           | Mar-14, Apr-10 |                    21 | B.2.1                                                    |                              65 | 0.0208           |
| UK174          | Mar-19, May-22 |                    21 | B.1.5                                                    |                              23 | 0.1391           |
| UK601          | Mar-13, May-04 |                    21 | B.10                                                     |                              41 | 0.0143           |
| UK2045         | Mar-17, May-09 |                    21 | B.1                                                      |                              36 | 0.0736           |
| UK394          | Mar-20, May-24 |                    21 | B.1.1                                                    |                              21 | 0.0317           |
| UK233          | May-25, Jun-08 |                    20 | B.1                                                      |                               6 | 0.1228           |
| UK75           | Mar-17, Apr-26 |                    20 | B.1, B.1.34                                              |                              49 | 0.043            |
| UK5503         | Mar-20, May-13 |                    20 | B.1                                                      |                              32 | 0.0888           |
| UK480          | Mar-23, May-18 |                    19 | B.1.1                                                    |                              27 | 0.1093           |
| UK1703         | Apr-02, May-01 |                    19 | B.1                                                      |                              44 | 0.0366           |
| UK203          | Mar-22, May-30 |                    19 | B.1.1                                                    |                              15 | 0.219            |
| UK4237         | Apr-02, Apr-20 |                    18 | B.1.1                                                    |                              55 | 0.0193           |
| UK2539         | Mar-24, May-14 |                    18 | B.1.1.5                                                  |                              31 | 0.0968           |
| UK146          | Mar-24, May-07 |                    18 | B.1.1                                                    |                              38 | 0.0643           |
| UK27           | Mar-05, May-21 |                    18 | B.1.1                                                    |                              24 | 0.1604           |
| UK86           | Mar-05, May-28 |                    18 | B.1, B.1.5                                               |                              17 | 0.0677           |
| UK462          | May-01, May-18 |                    17 | B.1                                                      |                              27 | 0.0757           |
| UK125          | Apr-03, May-29 |                    17 | B.1.1                                                    |                              16 | 0.2206           |
| UK491          | Mar-03, Apr-14 |                    16 | B.2, B.2.1, B                                            |                              61 | 0.0299           |
| UK161          | Mar-10, May-25 |                    16 | B.1.1                                                    |                              20 | 0.19             |
| UK71           | Mar-08, May-06 |                    16 | B                                                        |                              39 | 0.0946           |
| UK5300         | Apr-17, Jun-07 |                    16 | B.1.1                                                    |                               7 | 0.4554           |
| UK3781         | Mar-09, May-08 |                    16 | B.1.1                                                    |                              37 | 0.1081           |
| UK335          | Mar-07, Jun-05 |                    16 | B.1.1                                                    |                               9 | 0.5              |
| UK179          | Mar-26, May-07 |                    16 | B.1.1, B.1.1.p11                                         |                              38 | 0.0353           |
| UK5660         | Apr-25, May-08 |                    16 | B.1.1                                                    |                              37 | 0.0234           |
| UK47           | Mar-17, May-18 |                    15 | B.1.1                                                    |                              27 | 0.1209           |
| UK569          | Mar-23, May-12 |                    15 | B.1.1                                                    |                              33 | 0.1082           |
| UK34           | Feb-15, Apr-02 |                    15 | B.4                                                      |                              73 | 0.046            |
| UK1177         | Apr-22, May-29 |                    15 | B.1.1                                                    |                              16 | 0.1652           |
| UK1006         | Apr-02, May-03 |                    15 | B.1.1                                                    |                              42 | 0.0527           |
| UK134          | Mar-04, Apr-07 |                    15 | B.1                                                      |                              68 | 0.0278           |
| UK153          | Mar-13, Apr-14 |                    14 | B.2                                                      |                              61 | 0.0404           |
| UK38           | Mar-04, Apr-20 |                    14 | B.2.1                                                    |                              55 | 0.061            |
| UK5715         | Feb-13, Apr-22 |                    14 | B.2                                                      |                              53 | 0.093            |
| UK378          | Feb-15, Mar-05 |                    13 | B.1.1                                                    |                             101 | 0.0157           |
| UK186          | Apr-08, May-15 |                    13 | B                                                        |                              30 | 0.1256           |
| UK268          | Mar-23, Jun-04 |                    12 | B.1.1                                                    |                              10 | 0.4867           |
| UK604          | Mar-09, Mar-17 |                    12 | B.1.1                                                    |                              89 | 0.0077           |
| UK832          | Mar-09, Apr-26 |                    12 | A.5                                                      |                              49 | 0.0816           |
| UK49           | Mar-12, May-01 |                    12 | B.9                                                      |                              44 | 0.0874           |
| UK5663         | Apr-11, May-02 |                    12 | B.2                                                      |                              43 | 0.0444           |
| UK141          | Mar-22, Apr-24 |                    12 | B.1.1                                                    |                              51 | 0.0588           |
| UK408          | Apr-13, Jun-08 |                    12 | B.1.1                                                    |                               6 | 0.7778           |
| UK70           | Mar-06, Apr-18 |                    12 | B.2                                                      |                              57 | 0.0539           |
| UK5446         | May-05, May-16 |                    12 | B.1.1                                                    |                              29 | 0.0345           |
| UK507          | Mar-18, Apr-30 |                    12 | B.1.1.10                                                 |                              45 | 0.0869           |
| UK572          | Mar-16, Apr-11 |                    11 | B.2                                                      |                              64 | 0.0406           |
| UK193          | Mar-30, May-01 |                    11 | B.1.1                                                    |                              44 | 0.0661           |
| UK759          | Mar-28, Apr-27 |                    11 | B.1.1                                                    |                              48 | 0.0568           |
| UK132          | Mar-27, Apr-30 |                    11 | B.1                                                      |                              45 | 0.0687           |
| UK266          | Apr-06, Apr-30 |                    11 | B.1                                                      |                              45 | 0.0533           |
| UK566          | Apr-02, Apr-21 |                    11 | B.1.1, B.1.1.10                                          |                              54 | 0.0352           |
| UK445          | Mar-14, Apr-27 |                    11 | B.1.1                                                    |                              48 | 0.0917           |
| UK415          | Apr-19, May-06 |                    11 | B.1                                                      |                              39 | 0.0436           |
| UK317          | Mar-13, Apr-20 |                    11 | B.3                                                      |                              55 | 0.0288           |
| UK287          | Mar-28, Apr-24 |                    11 | B.1                                                      |                              51 | 0.0481           |
| UK523          | Apr-14, May-14 |                    11 | B.1.1                                                    |                              31 | 0.0968           |
| UK178          | Mar-14, Apr-29 |                    11 | B.1.1                                                    |                              46 | 0.0909           |
| UK553          | Feb-28, Apr-29 |                    11 | B.1                                                      |                              46 | 0.0884           |
| UK113          | Mar-22, Jun-02 |                    10 | B.1.1                                                    |                              12 | 0.6667           |
| UK291          | Mar-29, May-14 |                    10 | B.1.5                                                    |                              31 | 0.1649           |
| UK788          | Feb-28, Mar-05 |                    10 | B.4                                                      |                             101 | 0.0066           |
| UK242          | Mar-26, Apr-20 |                    10 | B.1.5                                                    |                              55 | 0.0505           |
| UK22           | Mar-02, Apr-21 |                    10 | B                                                        |                              54 | 0.1029           |
| UK527          | Mar-22, Apr-18 |                    10 | B.1                                                      |                              57 | 0.0351           |
| UK340          | Mar-23, May-17 |                     9 | B.1.1                                                    |                              28 | 0.2455           |
| UK454          | Mar-22, Apr-29 |                     9 | B.1.1                                                    |                              46 | 0.1033           |
| UK5653         | Mar-10, Apr-01 |                     9 | B.2.6                                                    |                              74 | 0.033            |
| UK59           | Mar-24, Apr-21 |                     9 | B.1                                                      |                              54 | 0.0648           |
| UK83           | Feb-29, Apr-08 |                     9 | B.1.1                                                    |                              67 | 0.0529           |
| UK5084         | Mar-29, Apr-16 |                     9 | B.1                                                      |                              59 | 0.0305           |
| UK202          | Mar-10, Jun-04 |                     9 | B.1.1                                                    |                              10 | 0.3909           |
| UK5307         | Mar-10, May-12 |                     9 | B.1.1                                                    |                              33 | 0.197            |
| UK342          | Apr-02, Apr-23 |                     8 | B.1.1                                                    |                              52 | 0.0577           |
| UK756          | Feb-27, Mar-05 |                     8 | B.1.1                                                    |                             101 | 0.0099           |
| UK739          | Mar-01, Mar-08 |                     8 | B.4                                                      |                              98 | 0.0102           |
| UK2888         | Apr-09, May-14 |                     8 | B.1.1                                                    |                              31 | 0.1613           |
| UK570          | Mar-24, Apr-29 |                     8 | B.1.1                                                    |                              46 | 0.1118           |
| UK284          | Apr-02, Apr-25 |                     8 | B.1.1                                                    |                              50 | 0.0657           |
| UK479          | Apr-01, Apr-27 |                     8 | B.1.1                                                    |                              48 | 0.0774           |
| UK116          | Mar-24, May-30 |                     8 | B.1                                                      |                              15 | 0.2233           |
| UK5308         | Apr-29, May-01 |                     8 | B.1.1                                                    |                              44 | 0.0065           |
| UK5348         | Mar-14, Apr-24 |                     8 | B.1.1                                                    |                              51 | 0.1148           |
| UK244          | Mar-12, Apr-06 |                     7 | B.1.1                                                    |                              69 | 0.0518           |
| UK520          | Mar-14, Apr-08 |                     7 | B.2, B.2.1                                               |                              67 | 0.0622           |
| UK584          | Mar-21, May-08 |                     7 | B.2, B.2.1                                               |                              37 | 0.2008           |
| UK5501         | Apr-16, Jun-01 |                     7 | B.1.12                                                   |                              13 | 0.5897           |
| UK490          | Apr-03, May-02 |                     7 | B.1.1                                                    |                              43 | 0.1124           |
| UK32           | Apr-10, May-01 |                     7 | B.1.1                                                    |                              44 | 0.0795           |
| UK390          | Mar-27, May-01 |                     7 | B.1.5                                                    |                              44 | 0.1326           |
| UK232          | Mar-04, Mar-30 |                     7 | B.1.1                                                    |                              76 | 0.057            |
| UK65           | Mar-07, Apr-21 |                     7 | B.1.1                                                    |                              54 | 0.119            |
| UK122          | Mar-23, May-07 |                     7 | B.1                                                      |                              38 | 0.1974           |
| UK755          | Mar-06, May-21 |                     7 | B.1.1                                                    |                              24 | 0.5278           |
| UK58           | Mar-17, Apr-09 |                     6 | B.1                                                      |                              66 | 0.0354           |
| UK5098         | Mar-16, May-27 |                     6 | B.1.8, B.1, B.1.p73                                      |                              18 | 0.0119           |
| UK40           | Mar-31, May-26 |                     6 | B.16                                                     |                              19 | 0.0228           |
| UK629          | Mar-23, Apr-13 |                     6 | B.1                                                      |                              62 | 0.0677           |
| UK263          | Mar-20, Apr-13 |                     6 | B.1.p11                                                  |                              62 | 0.0774           |
| UK320          | Apr-11, Jun-02 |                     6 | B.1                                                      |                              12 | 0.6667           |
| UK654          | Feb-27, Mar-08 |                     6 | B.2.5                                                    |                              98 | 0.0204           |
| UK799          | Mar-01, Mar-07 |                     6 | B.1                                                      |                              99 | 0.0121           |
| UK269          | Mar-25, Jun-02 |                     6 | B.1.1                                                    |                              12 | 1.15             |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NOTT     |             5 |
|  1 | CAMB     |             5 |
|  2 | NORW     |            10 |
|  3 | PORT     |            11 |
|  4 | BIRM     |            11 |
|  5 | LIVE     |            11 |
|  6 | SANG     |            14 |
|  7 | EXET     |            16 |
|  8 | SHEF     |            18 |
|  9 | NORT     |            19 |
| 10 | PHEC     |            31 |
| 11 | LOND     |            36 |
| 12 | OXON     |            66 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK107 |   UK42 |   UK5676 |   UK2913 |   UK2464 |   UK2916 |   UK72 |   UK199 |   UK167 |
|:------------------|------:|--------:|-------:|---------:|---------:|---------:|---------:|-------:|--------:|--------:|
| 2020-02-02        |     0 |       0 |      1 |        0 |        0 |        0 |        2 |      1 |       0 |       0 |
| 2020-02-09        |     0 |       1 |      0 |        1 |        0 |        0 |        1 |      0 |       0 |       0 |
| 2020-02-16        |     0 |       1 |      0 |        0 |        0 |        0 |        0 |      0 |       0 |       0 |
| 2020-02-23        |     1 |       5 |      3 |        2 |        0 |        0 |       10 |      2 |       1 |       0 |
| 2020-03-01        |     9 |       6 |     10 |        6 |        1 |        0 |       14 |      8 |       1 |       1 |
| 2020-03-08        |    20 |      16 |      8 |       12 |        4 |        3 |        7 |     12 |       3 |       6 |
| 2020-03-15        |    22 |      20 |     15 |       20 |        4 |        7 |        9 |     15 |       5 |       3 |
| 2020-03-22        |    33 |      25 |     19 |       16 |       10 |       12 |        8 |     16 |      11 |       9 |
| 2020-03-29        |    31 |      25 |     24 |       20 |       13 |       15 |       13 |     15 |      19 |      12 |
| 2020-04-05        |    36 |      21 |     23 |       14 |       14 |       14 |        9 |     13 |      17 |      17 |
| 2020-04-12        |    35 |      17 |     16 |        9 |       10 |       11 |        9 |      4 |      11 |      14 |
| 2020-04-19        |    35 |      15 |     17 |        6 |        8 |       11 |        8 |      3 |       5 |       9 |
| 2020-04-26        |    37 |       9 |     12 |        3 |        6 |        8 |        5 |      3 |       7 |       6 |
| 2020-05-03        |    40 |       4 |     10 |        2 |        2 |        4 |        1 |      3 |       5 |       6 |
| 2020-05-10        |    37 |       1 |      3 |        3 |        3 |        2 |        1 |      1 |       6 |       6 |
| 2020-05-17        |    36 |       1 |      2 |        0 |        2 |        2 |        0 |      0 |       2 |       6 |
| 2020-05-24        |    24 |       0 |      2 |        0 |        3 |        1 |        0 |      3 |       3 |       3 |
| 2020-05-31        |    24 |       1 |      4 |        0 |        3 |        1 |        1 |      0 |       2 |       3 |
| 2020-06-07        |    12 |       0 |      0 |        0 |        0 |        1 |        0 |      0 |       1 |       1 |
| 2020-06-14        |     1 |       0 |      0 |        0 |        0 |        0 |        0 |      0 |       0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




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
| 2020-03-01 |                            3 |                                4 |       7 |
| 2020-03-02 |                            1 |                                8 |       9 |
| 2020-03-03 |                            1 |                                5 |       6 |
| 2020-03-04 |                            0 |                                9 |       9 |
| 2020-03-05 |                            0 |                                4 |       4 |
| 2020-03-06 |                            3 |                                8 |      11 |
| 2020-03-07 |                            2 |                                6 |       8 |
| 2020-03-08 |                            2 |                                5 |       7 |
| 2020-03-09 |                            5 |                               14 |      19 |
| 2020-03-10 |                            4 |                                6 |      10 |
| 2020-03-11 |                            7 |                               15 |      22 |
| 2020-03-12 |                            9 |                               21 |      30 |
| 2020-03-13 |                            7 |                                7 |      14 |
| 2020-03-14 |                            2 |                                9 |      11 |
| 2020-03-15 |                            3 |                                3 |       6 |
| 2020-03-16 |                            2 |                                6 |       8 |
| 2020-03-17 |                            6 |                               13 |      19 |
| 2020-03-18 |                            8 |                               15 |      23 |
| 2020-03-19 |                            8 |                               10 |      18 |
| 2020-03-20 |                            6 |                               16 |      22 |
| 2020-03-21 |                            5 |                                9 |      14 |
| 2020-03-22 |                           10 |                               16 |      26 |
| 2020-03-23 |                            9 |                               21 |      30 |
| 2020-03-24 |                            7 |                               14 |      21 |
| 2020-03-25 |                           11 |                               10 |      21 |
| 2020-03-26 |                            8 |                               15 |      23 |
| 2020-03-27 |                            6 |                               11 |      17 |
| 2020-03-28 |                            9 |                               12 |      21 |
| 2020-03-29 |                           13 |                                8 |      21 |
| 2020-03-30 |                           12 |                               18 |      30 |
| 2020-03-31 |                           17 |                               15 |      32 |
| 2020-04-01 |                            9 |                                7 |      16 |
| 2020-04-02 |                           10 |                               13 |      23 |
| 2020-04-03 |                           10 |                                9 |      19 |
| 2020-04-04 |                            6 |                                7 |      13 |
| 2020-04-05 |                           13 |                                4 |      17 |
| 2020-04-06 |                            8 |                               12 |      20 |
| 2020-04-07 |                           15 |                                7 |      22 |
| 2020-04-08 |                            7 |                                4 |      11 |
| 2020-04-09 |                            5 |                                4 |       9 |
| 2020-04-10 |                            9 |                                3 |      12 |
| 2020-04-11 |                            4 |                                5 |       9 |
| 2020-04-12 |                            4 |                                0 |       4 |
| 2020-04-13 |                            7 |                                2 |       9 |
| 2020-04-14 |                            8 |                                4 |      12 |
| 2020-04-15 |                            7 |                                2 |       9 |
| 2020-04-16 |                           12 |                                3 |      15 |
| 2020-04-17 |                            1 |                                3 |       4 |
| 2020-04-18 |                            4 |                                4 |       8 |
| 2020-04-19 |                            4 |                                1 |       5 |
| 2020-04-20 |                            2 |                                2 |       4 |
| 2020-04-21 |                            8 |                                2 |      10 |
| 2020-04-22 |                            0 |                                1 |       1 |
| 2020-04-23 |                            3 |                                2 |       5 |
| 2020-04-24 |                            3 |                                0 |       3 |
| 2020-04-25 |                            2 |                                2 |       4 |
| 2020-04-26 |                            0 |                                1 |       1 |
| 2020-04-27 |                            1 |                                0 |       1 |
| 2020-04-28 |                            5 |                                1 |       6 |
| 2020-04-29 |                            2 |                                1 |       3 |
| 2020-05-01 |                            2 |                                2 |       4 |
| 2020-05-02 |                            2 |                                1 |       3 |
| 2020-05-03 |                            3 |                                0 |       3 |
| 2020-05-04 |                            4 |                                2 |       6 |
| 2020-05-05 |                            1 |                                1 |       2 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-07 |                            0 |                                1 |       1 |
| 2020-05-11 |                            2 |                                0 |       2 |
| 2020-05-12 |                            2 |                                0 |       2 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                2 |       3 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            1 |                                0 |       1 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-05-25 |                            0 |                                1 |       1 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-05-28 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-09 |                            1 |                                0 |       1 |

\pagebreak

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-02-03 |         5 |
| 2020-02-05 |         1 |
| 2020-02-08 |         2 |
| 2020-02-09 |         2 |
| 2020-02-13 |         2 |
| 2020-02-14 |         2 |
| 2020-02-15 |         2 |
| 2020-02-16 |         4 |
| 2020-02-18 |         1 |
| 2020-02-19 |         1 |
| 2020-02-20 |         1 |
| 2020-02-23 |         2 |
| 2020-02-24 |         4 |
| 2020-02-25 |         7 |
| 2020-02-26 |         6 |
| 2020-02-27 |        19 |
| 2020-02-28 |        24 |
| 2020-02-29 |        22 |
| 2020-03-01 |        51 |
| 2020-03-02 |        73 |
| 2020-03-03 |        91 |
| 2020-03-04 |       103 |
| 2020-03-05 |        81 |
| 2020-03-06 |        74 |
| 2020-03-07 |        44 |
| 2020-03-08 |        51 |
| 2020-03-09 |        71 |
| 2020-03-10 |        92 |
| 2020-03-11 |       145 |
| 2020-03-12 |       180 |
| 2020-03-13 |       104 |
| 2020-03-14 |        84 |
| 2020-03-15 |        65 |
| 2020-03-16 |        79 |
| 2020-03-17 |       119 |
| 2020-03-18 |       185 |
| 2020-03-19 |       151 |
| 2020-03-20 |       199 |
| 2020-03-21 |       206 |
| 2020-03-22 |       199 |
| 2020-03-23 |       345 |
| 2020-03-24 |       292 |
| 2020-03-25 |       290 |
| 2020-03-26 |       305 |
| 2020-03-27 |       302 |
| 2020-03-28 |       309 |
| 2020-03-29 |       348 |
| 2020-03-30 |       498 |
| 2020-03-31 |       455 |
| 2020-04-01 |       429 |
| 2020-04-02 |       429 |
| 2020-04-03 |       422 |
| 2020-04-04 |       345 |
| 2020-04-05 |       356 |
| 2020-04-06 |       439 |
| 2020-04-07 |       406 |
| 2020-04-08 |       379 |
| 2020-04-09 |       359 |
| 2020-04-10 |       328 |
| 2020-04-11 |       259 |
| 2020-04-12 |       211 |
| 2020-04-13 |       242 |
| 2020-04-14 |       311 |
| 2020-04-15 |       310 |
| 2020-04-16 |       354 |
| 2020-04-17 |       315 |
| 2020-04-18 |       235 |
| 2020-04-19 |       203 |
| 2020-04-20 |       266 |
| 2020-04-21 |       220 |
| 2020-04-22 |       170 |
| 2020-04-23 |       154 |
| 2020-04-24 |       110 |
| 2020-04-25 |        76 |
| 2020-04-26 |        97 |
| 2020-04-27 |       164 |
| 2020-04-28 |       126 |
| 2020-04-29 |       216 |
| 2020-04-30 |       183 |
| 2020-05-01 |       218 |
| 2020-05-02 |       118 |
| 2020-05-03 |        94 |
| 2020-05-04 |       179 |
| 2020-05-05 |       119 |
| 2020-05-06 |       143 |
| 2020-05-07 |       123 |
| 2020-05-08 |        79 |
| 2020-05-09 |        65 |
| 2020-05-10 |        73 |
| 2020-05-11 |       114 |
| 2020-05-12 |        77 |
| 2020-05-13 |        77 |
| 2020-05-14 |        54 |
| 2020-05-15 |        60 |
| 2020-05-16 |        44 |
| 2020-05-17 |        26 |
| 2020-05-18 |        69 |
| 2020-05-19 |        52 |
| 2020-05-20 |        32 |
| 2020-05-21 |        39 |
| 2020-05-22 |        35 |
| 2020-05-23 |        21 |
| 2020-05-24 |        20 |
| 2020-05-25 |        39 |
| 2020-05-26 |        43 |
| 2020-05-27 |        30 |
| 2020-05-28 |        35 |
| 2020-05-29 |        16 |
| 2020-05-30 |        11 |
| 2020-05-31 |        26 |
| 2020-06-01 |        41 |
| 2020-06-02 |        34 |
| 2020-06-03 |        27 |
| 2020-06-04 |        26 |
| 2020-06-05 |        13 |
| 2020-06-06 |         9 |
| 2020-06-07 |        12 |
| 2020-06-08 |        14 |
| 2020-06-09 |         2 |
| 2020-06-10 |        10 |
| 2020-06-11 |         1 |
| 2020-06-12 |         2 |
| 2020-06-13 |         1 |
| 2020-06-14 |         2 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                       | Country   |   Number of sequences | Sequence group   |
|:-----------------------------|:----------|----------------------:|:-----------------|
| BATH AND NORTH EAST SOMERSET | England   |                     0 | 0                |
| BEDFORDSHIRE                 | England   |                   449 | 400-500          |
| BERKSHIRE                    | England   |                    10 | 10-50            |
| BLACKBURN WITH DARWEN        | England   |                     0 | 0                |
| BLACKPOOL                    | England   |                     0 | 0                |
| BOLTON                       | England   |                     0 | 0                |
| BOURNEMOUTH                  | England   |                     0 | 0                |
| BRIGHTON AND HOVE            | England   |                     0 | 0                |
| BRISTOL                      | England   |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England   |                   400 | 400-500          |
| BURY                         | England   |                     0 | 0                |
| CAMBRIDGESHIRE               | England   |                   706 | >500             |
| CENTRAL BEDFORDSHIRE         | England   |                     0 | 0                |
| CHESHIRE                     | England   |                    43 | 10-50            |
| CORNWALL                     | England   |                    23 | 10-50            |
| CUMBRIA                      | England   |                    58 | 50-100           |
| DARLINGTON                   | England   |                     0 | 0                |
| DERBY                        | England   |                     0 | 0                |
| DERBYSHIRE                   | England   |                    28 | 10-50            |
| DEVON                        | England   |                   400 | 400-500          |
| DORSET                       | England   |                   183 | 150-200          |
| DURHAM                       | England   |                    21 | 10-50            |
| EAST RIDING OF YORKSHIRE     | England   |                    33 | 10-50            |
| ESSEX                        | England   |                  1375 | >500             |
| GATESHEAD                    | England   |                     0 | 0                |
| GLOUCESTERSHIRE              | England   |                   626 | >500             |
| GREATER LONDON               | England   |                  2368 | >500             |
| HALTON                       | England   |                     0 | 0                |
| HAMPSHIRE                    | England   |                   226 | 200-250          |
| HARTLEPOOL                   | England   |                     0 | 0                |
| HEREFORDSHIRE                | England   |                    39 | 10-50            |
| HERTFORDSHIRE                | England   |                  1003 | >500             |
| ISLE OF WIGHT                | England   |                     0 | 0                |
| ISLES OF SCILLY              | England   |                     0 | 0                |
| KENT                         | England   |                    29 | 10-50            |
| KINGSTON UPON HULL           | England   |                     0 | 0                |
| LANCASHIRE                   | England   |                    53 | 50-100           |
| LEICESTER                    | England   |                     0 | 0                |
| LEICESTERSHIRE               | England   |                     5 | 1-10             |
| LINCOLNSHIRE                 | England   |                    37 | 10-50            |
| LUTON                        | England   |                     0 | 0                |
| MANCHESTER                   | England   |                    30 | 10-50            |
| MEDWAY                       | England   |                     0 | 0                |
| MERSEYSIDE                   | England   |                   541 | >500             |
| MIDDLESBROUGH                | England   |                     0 | 0                |
| MILTON KEYNES                | England   |                     0 | 0                |
| NORFOLK                      | England   |                   607 | >500             |
| NORTH LINCOLNSHIRE           | England   |                     0 | 0                |
| NORTH SOMERSET               | England   |                     0 | 0                |
| NORTH YORKSHIRE              | England   |                    96 | 50-100           |
| NORTHAMPTONSHIRE             | England   |                    24 | 10-50            |
| NORTHUMBERLAND               | England   |                    12 | 10-50            |
| NOTTINGHAM                   | England   |                   662 | >500             |
| NOTTINGHAMSHIRE              | England   |                    58 | 50-100           |
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
| SOMERSET                     | England   |                   602 | >500             |
| SOUTH GLOUCESTERSHIRE        | England   |                     0 | 0                |
| SOUTH YORKSHIRE              | England   |                  1425 | >500             |
| SOUTHAMPTON                  | England   |                     0 | 0                |
| SOUTHEND-ON-SEA              | England   |                     0 | 0                |
| STAFFORDSHIRE                | England   |                    59 | 50-100           |
| STOCKPORT                    | England   |                     0 | 0                |
| STOCKTON-ON-TEES             | England   |                     0 | 0                |
| STOKE-ON-TRENT               | England   |                     0 | 0                |
| SUFFOLK                      | England   |                   569 | >500             |
| SURREY                       | England   |                    65 | 50-100           |
| SUSSEX                       | England   |                     1 | 1-10             |
| SWINDON                      | England   |                     0 | 0                |
| TAMESIDE                     | England   |                     0 | 0                |
| TELFORD AND WREKIN           | England   |                     0 | 0                |
| THURROCK                     | England   |                     0 | 0                |
| TORBAY                       | England   |                     0 | 0                |
| TRAFFORD                     | England   |                     0 | 0                |
| TYNE AND WEAR                | England   |                   106 | 100-150          |
| WARRINGTON                   | England   |                     0 | 0                |
| WARWICKSHIRE                 | England   |                    10 | 10-50            |
| WEST MIDLANDS                | England   |                   120 | 100-150          |
| WEST YORKSHIRE               | England   |                    20 | 10-50            |
| WIGAN                        | England   |                     0 | 0                |
| WILTSHIRE                    | England   |                   348 | 300-400          |
| WORCESTERSHIRE               | England   |                    12 | 10-50            |
| YORK                         | England   |                     0 | 0                |

\pagebreak






