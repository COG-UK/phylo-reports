
# UK lineages summary report








This report gives summaries of lineages sampled in England for week 2020-05-29. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-23. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
13522 sequences from England have been included in this analysis.
4680 lineages have been recorded, 3565 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 4822 and the maximum is 7104


Sequences which were replicates or too error-prone were removed from this analysis.



4356 are lineages which were sampled less than five times in England, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 324 that remain:
125 are pending extinction, ie last seen three weeks ago.
136 have not been seen for more than one month, and so are viewed as extinct, but will continue to be monitored.
36 lineages have gone quiet, ie haven't been seen this week.
9 lineages have reactivated.
18 lineages have been continuously circulating.


The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lienages is found in the appendix, along with the raw data for all of the other figures.

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Date range     |   Number of sequences | Global lineage      |   Time since last sample (days) |   Activity score |
|:---------------|:---------------|----------------------:|:--------------------|--------------------------------:|-----------------:|
| UK5            | Mar-03, May-22 |                  1000 | B.1.1.1, B.1.1, B.1 |                               1 |           0.0668 |
| UK701          | Feb-03, May-10 |                   244 | B.1, B.1.p11        |                              13 |           0.0248 |
| UK2464         | Mar-09, May-11 |                   240 | B.1.p11             |                              12 |           0.0145 |
| UK9            | Mar-09, May-05 |                   199 | B.1.13              |                              18 |           0.0159 |
| UK4            | Feb-28, May-01 |                   138 | B                   |                              22 |           0.019  |
| UK19           | Mar-09, May-10 |                   137 | B.1                 |                              13 |           0.022  |
| UK6            | Mar-06, May-13 |                   112 | B.1                 |                              10 |           0.0591 |
| UK494          | Mar-20, May-05 |                   105 | B.1.p11             |                              18 |           0.0241 |
| UK63           | Mar-18, May-05 |                   103 | B.1.1               |                              18 |           0.0254 |
| UK36           | Mar-19, May-12 |                    81 | B.1                 |                              11 |           0.0167 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 


![Number of sequences sampled in a lineage by country](UK_full_report/adm1_reports/England/figures/England_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](UK_full_report/adm1_reports/England/figures/England_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](UK_full_report/adm1_reports/England/figures/England_geog_plot_1.png){#geog_plot }







These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](UK_full_report/adm1_reports/England/figures/England_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 



NB the lineage may have started anywhere in the UK, but has been recorded at least once in England



![Lineage starts per week, split by singletons and non-singletons](UK_full_report/adm1_reports/England/figures/England_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](UK_full_report/adm1_reports/England/figures/England_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.



![Map showing the number of sequences sampled by adm2 region](UK_full_report/adm1_reports/England/figures/England_map_1.png){#map }




There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Date range     |   Number of sequences | Global lineage      |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:--------------------|--------------------------------:|:-----------------|
| UK5            | Mar-03, May-22 |                  1000 | B.1.1.1, B.1.1, B.1 |                               1 | 0.0668           |
| UK701          | Feb-03, May-10 |                   244 | B.1, B.1.p11        |                              13 | 0.0248           |
| UK2464         | Mar-09, May-11 |                   240 | B.1.p11             |                              12 | 0.0145           |
| UK9            | Mar-09, May-05 |                   199 | B.1.13              |                              18 | 0.0159           |
| UK4            | Feb-28, May-01 |                   138 | B                   |                              22 | 0.019            |
| UK19           | Mar-09, May-10 |                   137 | B.1                 |                              13 | 0.022            |
| UK6            | Mar-06, May-13 |                   112 | B.1                 |                              10 | 0.0591           |
| UK494          | Mar-20, May-05 |                   105 | B.1.p11             |                              18 | 0.0241           |
| UK63           | Mar-18, May-05 |                   103 | B.1.1               |                              18 | 0.0254           |
| UK36           | Mar-19, May-12 |                    81 | B.1                 |                              11 | 0.0167           |
| UK371          | Mar-12, May-19 |                    79 | B.1.1               |                               4 | 0.2179           |
| UK77           | Mar-11, May-20 |                    74 | B.2, B.2.4          |                               3 | 0.303            |
| UK177          | Mar-27, May-02 |                    73 | B.1.1               |                              21 | 0.0238           |
| UK26           | Mar-18, May-18 |                    73 | B.1.1.3             |                               5 | 0.1694           |
| UK31           | Mar-21, May-08 |                    71 | B.1                 |                              15 | 0.0457           |
| UK107          | Mar-15, Apr-21 |                    68 | B.2.5, B.2, B.2.1   |                              32 | 0.0173           |
| UK66           | Mar-18, May-01 |                    68 | B.1.1.8             |                              22 | 0.25             |
| UK89           | Mar-11, May-17 |                    64 | B.1.1.9             |                               6 | 0.1718           |
| UK200          | Apr-08, May-14 |                    62 | B.1.p11             |                               9 | 0.0656           |
| UK194          | Mar-19, Apr-24 |                    61 | B.1.1               |                              29 | 0.0207           |
| UK343          | Mar-28, Apr-24 |                    60 | B.1                 |                              29 | 0.0158           |
| UK37           | Mar-17, May-04 |                    60 | B.1, B.1.30         |                              19 | 0.0414           |
| UK233          | Apr-08, May-13 |                    59 | B.1.1               |                              10 | 0.0603           |
| UK274          | Mar-06, May-11 |                    59 | B.3, B              |                              12 | 0.0902           |
| UK115          | Mar-15, Apr-20 |                    58 | B.2.1               |                              33 | 0.0188           |
| UK476          | Mar-31, May-06 |                    56 | B.1.1               |                              17 | 0.0385           |
| UK112          | Mar-15, May-04 |                    55 | B.1.1.p11, B.1.1    |                              19 | 0.0487           |
| UK632          | Mar-23, May-17 |                    54 | B.1.1               |                               6 | 0.0611           |
| UK204          | Apr-07, May-12 |                    54 | B.1.1               |                              11 | 0.06             |
| UK5322         | Mar-24, May-13 |                    53 | B.1.1               |                              10 | 0.0689           |
| UK199          | Apr-08, May-17 |                    52 | B.1.5.5             |                               6 | 0.1275           |
| UK62           | Mar-12, Apr-23 |                    52 | B.3                 |                              30 | 0.0259           |
| UK51           | Mar-25, May-19 |                    50 | B.1.36              |                               4 | 0.2634           |
| UK33           | Mar-21, May-15 |                    50 | B.1.1               |                               8 | 0.1348           |
| UK3            | Feb-24, May-10 |                    48 | B.1                 |                              13 | 0.1244           |
| UK94           | Mar-12, Apr-19 |                    47 | B.2, B.2.1          |                              34 | 0.0243           |
| UK11           | Mar-06, Apr-11 |                    46 | B.1                 |                              42 | 0.0181           |
| UK13           | Mar-13, May-13 |                    46 | B.1.1               |                              10 | 0.1356           |
| UK28           | Mar-13, May-01 |                    45 | B.1.1.10            |                              22 | 0.0506           |
| UK238          | Mar-19, May-03 |                    44 | B.1.1               |                              20 | 0.0523           |
| UK513          | Mar-12, Apr-29 |                    43 | B.1.p11             |                              24 | 0.0476           |
| UK8            | Mar-03, May-01 |                    38 | B                   |                              22 | 0.0654           |
| UK23           | Mar-12, May-02 |                    37 | B, B.9              |                              21 | 0.0656           |
| UK214          | Mar-14, May-13 |                    37 | B.1.1               |                              10 | 0.1622           |
| UK2240         | Mar-01, Apr-19 |                    37 | B.1                 |                              34 | 0.0379           |
| UK128          | Apr-03, May-23 |                    37 | B.1.1               |                               0 | active today     |
| UK283          | Mar-25, May-04 |                    36 | B.1.1               |                              19 | 0.0602           |
| UK12           | Mar-12, May-07 |                    36 | B.1.p11             |                              16 | 0.1148           |
| UK346          | Mar-16, Apr-19 |                    36 | B.1.72, B.1         |                              34 | 0.0286           |
| UK57           | Mar-20, May-04 |                    35 | B.1.1               |                              19 | 0.0697           |
| UK18           | Mar-11, May-03 |                    34 | B.1.1.7             |                              20 | 0.0803           |
| UK147          | Apr-04, May-22 |                    34 | B.1.1               |                               1 | 1.4118           |
| UK131          | Mar-11, Apr-14 |                    34 | B.15                |                              39 | 0.0229           |
| UK138          | Mar-23, Apr-26 |                    33 | B.2.1               |                              27 | 0.0394           |
| UK167          | Mar-29, May-21 |                    31 | B.1.66, B.1         |                               2 | 0.8833           |
| UK173          | Mar-16, May-06 |                    31 | B                   |                              17 | 0.1              |
| UK5672         | Mar-20, May-13 |                    30 | B.2                 |                              10 | 0.1862           |
| UK300          | Mar-28, May-04 |                    30 | B.1.1               |                              19 | 0.0672           |
| UK79           | Mar-24, May-05 |                    30 | B.1                 |                              18 | 0.0805           |
| UK1845         | Mar-01, Apr-07 |                    30 | B                   |                              46 | 0.0296           |
| UK241          | Mar-22, Apr-16 |                    29 | B.1.5.3             |                              37 | 0.0241           |
| UK183          | Mar-29, Apr-28 |                    28 | B.1.1               |                              25 | 0.0444           |
| UK116          | Feb-25, Apr-01 |                    28 | B.2.1               |                              52 | 0.0256           |
| UK95           | Mar-10, May-03 |                    28 | B.2.1               |                              20 | 0.0964           |
| UK565          | Mar-31, May-13 |                    26 | B.1.1               |                              10 | 0.172            |
| UK351          | Apr-13, May-17 |                    26 | B.1.1, B.1.1.10     |                               6 | 0.2267           |
| UK53           | Mar-26, May-22 |                    26 | B.1.1.4             |                               1 | 1.1633           |
| UK144          | Mar-05, Apr-07 |                    26 | B.2.1               |                              46 | 0.0287           |
| UK158          | Mar-23, Apr-19 |                    25 | B.1.1, B.1.1.2      |                              34 | 0.0123           |
| UK92           | Mar-23, Apr-28 |                    25 | B.1.1               |                              25 | 0.06             |
| UK41           | Mar-01, Apr-15 |                    25 | B.1                 |                              38 | 0.0664           |
| UK46           | Mar-02, May-08 |                    25 | B.2.1               |                              15 | 0.1787           |
| UK5675         | Mar-03, Apr-10 |                    25 | B.2                 |                              43 | 0.0327           |
| UK64           | Mar-12, Apr-17 |                    24 | B.1                 |                              36 | 0.0369           |
| UK81           | Mar-19, Apr-27 |                    24 | B.1.1               |                              26 | 0.0625           |
| UK56           | Mar-20, May-06 |                    24 | B.1.1               |                              17 | 0.1202           |
| UK119          | Mar-11, Apr-16 |                    23 | B.2.5               |                              37 | 0.0324           |
| UK109          | Mar-21, May-01 |                    23 | B.1.5               |                              22 | 0.0745           |
| UK235          | Mar-21, May-04 |                    23 | B.1.1               |                              19 | 0.1053           |
| UK103          | Mar-20, May-20 |                    23 | B.1.1               |                               3 | 0.9242           |
| UK326          | Mar-22, May-22 |                    23 | B.1.1.10            |                               1 | 2.7727           |
| UK101          | Mar-21, Apr-27 |                    22 | B.1.5               |                              26 | 0.0647           |
| UK61           | Mar-12, Apr-21 |                    22 | B.3                 |                              32 | 0.0065           |
| UK2200         | Feb-28, May-04 |                    22 | B.1.5.6, B.1.5      |                              19 | 0.0418           |
| UK5649         | Mar-15, May-01 |                    22 | B.2.6               |                              22 | 0.089            |
| UK30           | Mar-15, May-15 |                    22 | B.1.1               |                               8 | 0.3631           |
| UK114          | Mar-16, Apr-21 |                    22 | B.1.1               |                              32 | 0.0536           |
| UK279          | Mar-26, Apr-25 |                    22 | B.1.1               |                              28 | 0.051            |
| UK74           | Mar-12, Apr-16 |                    21 | B.1                 |                              37 | 0.0224           |
| UK5549         | Mar-04, May-10 |                    21 | B.2.2               |                              13 | 0.2241           |
| UK384          | Mar-14, Apr-02 |                    21 | B.2.1               |                              51 | 0.0186           |
| UK174          | Mar-19, May-22 |                    21 | B.1.5               |                               1 | 3.2              |
| UK135          | Apr-01, May-14 |                    21 | B.1.p11             |                               9 | 0.2389           |
| UK113          | Mar-22, May-19 |                    21 | B.1.1               |                               4 | 0.725            |
| UK293          | Mar-24, Apr-28 |                    20 | B.1                 |                              25 | 0.0737           |
| UK75           | Mar-17, Apr-26 |                    20 | B.1, B.1.34         |                              27 | 0.078            |
| UK24           | Mar-18, Apr-30 |                    20 | B.1.1, B.1.1.10     |                              23 | 0.0984           |
| UK291          | Mar-13, Apr-05 |                    20 | B.2.1               |                              48 | 0.024            |
| UK514          | Mar-30, Apr-13 |                    19 | B.1.1               |                              40 | 0.0194           |
| UK419          | Mar-30, May-02 |                    19 | B.1.1               |                              21 | 0.0873           |
| UK403          | Mar-23, May-04 |                    19 | B.1.1               |                              19 | 0.1228           |
| UK307          | Mar-28, May-04 |                    19 | B.1.1               |                              19 | 0.1082           |
| UK5309         | Mar-20, Apr-29 |                    18 | B.1.1, B.1.1.10     |                              24 | 0.0833           |
| UK117          | Feb-28, Apr-04 |                    18 | B.2.1               |                              49 | 0.0432           |
| UK248          | Apr-08, May-11 |                    18 | B.1.1               |                              12 | 0.1618           |
| UK193          | Apr-07, May-01 |                    18 | B.1.1               |                              22 | 0.0505           |
| UK143          | Mar-14, Apr-16 |                    18 | B.2.1               |                              37 | 0.0525           |
| UK72           | Mar-13, May-04 |                    18 | B.10                |                              19 | 0.0374           |
| UK444          | Mar-24, Apr-17 |                    16 | B.1.1               |                              36 | 0.1161           |
| UK86           | Mar-05, Apr-10 |                    16 | B.1                 |                              43 | 0.0568           |
| UK888          | Apr-05, May-01 |                    16 | B.1.1               |                              22 | 0.0788           |
| UK195          | Mar-29, May-03 |                    16 | B.1.1               |                              20 | 0.1167           |
| UK67           | Mar-25, May-21 |                    16 | B.1.1               |                               2 | 1.9              |
| UK134          | Mar-04, Apr-07 |                    15 | B.1                 |                              46 | 0.0411           |
| UK374          | Apr-01, Apr-20 |                    15 | B.1.1               |                              33 | 0.0411           |
| UK2045         | Mar-17, Apr-29 |                    15 | B.1, B              |                              24 | 0.128            |
| UK5084         | Mar-23, Apr-16 |                    15 | B.2.1, B.1, B.1.p11 |                              37 | 0.0405           |
| UK146          | Mar-24, May-07 |                    14 | B.1.1               |                              16 | 0.1964           |
| UK5409         | Mar-22, Apr-19 |                    14 | B.1.1               |                              34 | 0.0633           |
| UK236          | Mar-27, Apr-22 |                    14 | B.1.1               |                              31 | 0.0599           |
| UK254          | Mar-20, Apr-14 |                    14 | B.1.1               |                              39 | 0.0493           |
| UK249          | Apr-01, Apr-25 |                    14 | B.1.1               |                              28 | 0.0638           |
| UK5180         | Apr-04, Apr-24 |                    14 | B.1.1.7             |                              29 | 0.0531           |
| UK722          | Mar-31, May-05 |                    14 | B.1.1               |                              18 | 0.1496           |
| UK179          | Mar-26, Apr-18 |                    14 | B.1.1.p11           |                              35 | 0.0584           |
| UK276          | Mar-18, May-04 |                    14 | B.1.1               |                              19 | 0.1903           |
| UK376          | Apr-08, May-08 |                    14 | B.1.1               |                              15 | 0.1538           |
| UK726          | Mar-30, May-04 |                    14 | B.1                 |                              19 | 0.1417           |
| UK153          | Mar-13, Apr-14 |                    14 | B.2                 |                              39 | 0.0631           |
| UK45           | Mar-02, Apr-15 |                    14 | B.1.1               |                              38 | 0.0606           |
| UK253          | Apr-03, May-03 |                    14 | B.1.1               |                              20 | 0.1154           |
| UK378          | Feb-15, Mar-05 |                    13 | B.1.1               |                              79 | 0.02             |
| UK34           | Feb-15, Apr-02 |                    13 | B.4                 |                              51 | 0.0768           |
| UK278          | Apr-10, May-07 |                    13 | B.1.1               |                              16 | 0.1406           |
| UK5260         | Mar-29, May-02 |                    13 | B.1.1               |                              21 | 0.1349           |
| UK637          | Mar-28, May-01 |                    13 | B.1.1               |                              22 | 0.1288           |
| UK71           | Mar-08, Apr-30 |                    13 | B                   |                              23 | 0.1773           |
| UK5498         | Apr-01, Apr-20 |                    13 | B.2                 |                              33 | 0.0653           |
| UK354          | Mar-18, Apr-07 |                    13 | B.1.1               |                              46 | 0.0362           |
| UK308          | Apr-09, May-18 |                    13 | B.1.1               |                               5 | 0.65             |
| UK397          | Mar-28, Apr-14 |                    13 | B.1.1.13            |                              39 | 0.0311           |
| UK501          | Apr-03, Apr-22 |                    13 | B.1, B              |                              31 | 0.0511           |
| UK604          | Mar-09, Mar-12 |                    12 | B.1.1               |                              72 | 0.0103           |
| UK126          | Mar-29, May-03 |                    12 | B.1.1               |                              20 | 0.1591           |
| UK5715         | Feb-13, Apr-05 |                    12 | B.2                 |                              48 | 0.1855           |
| UK168          | Mar-16, Apr-16 |                    12 | B.2.1               |                              37 | 0.0762           |
| UK347          | Mar-13, Apr-02 |                    12 | B.1                 |                              51 | 0.0357           |
| UK694          | Mar-06, Mar-14 |                    12 | B                   |                              70 | 0.0104           |
| UK203          | Apr-01, May-17 |                    12 | B.1.1               |                               6 | 0.5222           |
| UK329          | Apr-11, May-09 |                    12 | B.1.1               |                              14 | 0.1818           |
| UK511          | Apr-05, May-06 |                    12 | B.1.1               |                              17 | 0.1658           |
| UK186          | Apr-08, May-15 |                    12 | B                   |                               8 | 0.5104           |
| UK269          | Apr-03, May-06 |                    12 | B.1.1               |                              17 | 0.1513           |
| UK479          | Mar-30, May-12 |                    12 | B.1.1               |                              11 | 0.3554           |
| UK148          | Apr-02, May-13 |                    12 | B.1.1               |                              10 | 0.3727           |
| UK240          | Mar-16, Apr-11 |                    11 | B.2                 |                              42 | 0.0619           |
| UK141          | Mar-22, Apr-24 |                    11 | B.1.1               |                              29 | 0.1138           |
| UK1018         | Apr-20, Apr-21 |                    11 | B.1.1               |                              32 | 0.0031           |
| UK415          | Apr-19, May-06 |                    11 | B.1                 |                              17 | 0.1              |
| UK180          | Mar-30, May-01 |                    11 | B.1.1               |                              22 | 0.1322           |
| UK428          | Mar-20, Apr-06 |                    11 | B.2, B.2.1          |                              47 | 0.0362           |
| UK163          | Mar-27, Apr-16 |                    11 | B.1.1               |                              37 | 0.1156           |
| UK47           | Mar-17, Apr-13 |                    11 | B.1.1               |                              40 | 0.045            |
| UK368          | Mar-18, May-01 |                    11 | B.1                 |                              22 | 0.2              |
| UK532          | Apr-04, May-09 |                    11 | B.1.1               |                              14 | 0.25             |
| UK441          | Apr-04, May-01 |                    11 | B.1.1               |                              22 | 0.0944           |
| UK251          | Mar-17, May-02 |                    11 | B.1.1               |                              21 | 0.1991           |
| UK266          | Apr-06, Apr-30 |                    11 | B.1                 |                              23 | 0.1043           |
| UK54           | Mar-18, Apr-30 |                    11 | B.1.1.10            |                              23 | 0.187            |
| UK5339         | Apr-15, Apr-29 |                    11 | B.1.1               |                              24 | 0.0583           |
| UK111          | Mar-25, May-01 |                    11 | B.1.1               |                              22 | 0.1529           |
| UK759          | Mar-28, Apr-04 |                    11 | B.1.1               |                              49 | 0.0143           |
| UK255          | Mar-26, Apr-20 |                    10 | B.1.1               |                              33 | 0.0758           |
| UK22           | Mar-02, Apr-21 |                    10 | B                   |                              32 | 0.1736           |
| UK132          | Mar-27, Apr-30 |                    10 | B.1                 |                              23 | 0.1232           |
| UK42           | Mar-28, Apr-28 |                    10 | B.1, B.1.35         |                              25 | 0.0307           |
| UK687          | Feb-28, Mar-08 |                    10 | B.2, B.2.1          |                              76 | 0.0132           |
| UK125          | Mar-27, May-10 |                    10 | B.1.1               |                              13 | 0.3761           |
| UK219          | Mar-26, May-02 |                    10 | B.1.1               |                              21 | 0.1468           |
| UK123          | Mar-23, May-01 |                    10 | B.1                 |                              22 | 0.197            |
| UK178          | Mar-14, Apr-13 |                    10 | B.1.1               |                              40 | 0.0833           |
| UK155          | Feb-27, Mar-24 |                    10 | B.1                 |                              60 | 0.1833           |
| UK38           | Mar-04, Apr-20 |                    10 | B.2.1               |                              33 | 0.1648           |
| UK171          | Mar-13, Apr-13 |                    10 | B.2, B.2.1          |                              40 | 0.0861           |
| UK220          | Mar-27, Apr-22 |                    10 | B.1.1               |                              31 | 0.0932           |
| UK201          | Mar-29, May-03 |                    10 | B.1                 |                              20 | 0.1944           |
| UK909          | Apr-13, Apr-20 |                    10 | B.1                 |                              33 | 0.0236           |
| UK78           | Mar-29, May-14 |                    10 | B.1.5               |                               9 | 0.5679           |
| UK242          | Mar-26, Apr-20 |                    10 | B.1.5               |                              33 | 0.0842           |
| UK564          | Apr-03, May-02 |                     9 | B.1.1               |                              21 | 0.1726           |
| UK802          | Mar-21, Apr-22 |                     9 | B.1                 |                              31 | 0.129            |
| UK541          | Apr-01, May-02 |                     9 | B.1.1               |                              21 | 0.1845           |
| UK569          | Mar-23, Apr-10 |                     9 | B.1.1               |                              43 | 0.0523           |
| UK5423         | Apr-23, May-04 |                     9 | B.1.1               |                              19 | 0.0724           |
| UK5338         | Apr-29, May-02 |                     9 | B.1.1               |                              21 | 0.0179           |
| UK2258         | Mar-25, May-07 |                     9 | B.1.5, B.1          |                              16 | 0.3359           |
| UK142          | Mar-15, Apr-17 |                     9 | B.2.1               |                              36 | 0.1146           |
| UK432          | Mar-24, Apr-09 |                     9 | B.3                 |                              44 | 0.0455           |
| UK237          | Mar-31, May-16 |                     9 | B.1.1               |                               7 | 0.8214           |
| UK312          | Mar-01, Mar-23 |                     9 | B.1.1               |                              61 | 0.0451           |
| UK190          | Mar-01, Mar-30 |                     9 | B.1                 |                              54 | 0.0671           |
| UK5685         | Mar-17, Apr-13 |                     9 | B.2                 |                              40 | 0.0614           |
| UK5663         | Apr-11, Apr-30 |                     9 | B.2                 |                              23 | 0.1033           |
| UK90           | Mar-29, May-06 |                     9 | B.1.1               |                              17 | 0.2794           |
| UK91           | Mar-28, May-06 |                     9 | B.1.1               |                              17 | 0.2868           |
| UK1737         | Mar-11, Apr-14 |                     9 | B.1                 |                              39 | 0.0969           |
| UK5673         | Mar-19, May-01 |                     9 | B.2                 |                              22 | 0.2443           |
| UK297          | Apr-09, May-15 |                     9 | B.1.p11             |                               8 | 0.5625           |
| UK645          | Mar-29, Apr-08 |                     9 | B.2.1               |                              45 | 0.0278           |
| UK1013         | Apr-15, Apr-16 |                     8 | B.1.1               |                              37 | 0.0039           |
| UK311          | Mar-20, Apr-11 |                     8 | B.1.1               |                              42 | 0.0748           |
| UK70           | Mar-06, Apr-16 |                     8 | B.2                 |                              37 | 0.1108           |
| UK5707         | Mar-18, Apr-14 |                     8 | B.2                 |                              39 | 0.0989           |
| UK252          | Apr-04, Apr-29 |                     8 | B.1.1               |                              24 | 0.1488           |
| UK318          | Mar-20, Apr-10 |                     8 | B                   |                              43 | 0.0698           |
| UK129          | Mar-23, Apr-29 |                     8 | B.1.1               |                              24 | 0.1927           |
| UK480          | Mar-27, May-19 |                     8 | B.1.1.10, B.1.1     |                               4 | 1.8929           |
| UK287          | Mar-28, Apr-18 |                     8 | B.1                 |                              35 | 0.0657           |
| UK223          | Mar-10, Apr-06 |                     8 | B.2.1               |                              47 | 0.0821           |
| UK306          | Mar-26, Apr-10 |                     8 | B.1.1               |                              43 | 0.0436           |
| UK341          | Mar-23, Apr-12 |                     8 | B.1                 |                              41 | 0.0697           |
| UK324          | Mar-31, Apr-21 |                     8 | B.1.1               |                              32 | 0.0938           |
| UK335          | Mar-25, Apr-15 |                     8 | B.2.1               |                              38 | 0.0789           |
| UK1849         | Apr-11, Apr-29 |                     8 | B.1.1               |                              24 | 0.1071           |
| UK733          | Mar-10, Apr-22 |                     8 | B.2.1               |                              31 | 0.1982           |
| UK739          | Mar-01, Mar-08 |                     8 | B.4                 |                              76 | 0.0132           |
| UK5563         | Apr-11, Apr-22 |                     8 | B.2.2               |                              31 | 0.0507           |
| UK83           | Feb-29, Apr-08 |                     8 | B.1.1               |                              45 | 0.0867           |
| UK5505         | Mar-23, Apr-21 |                     8 | B.2, B.1            |                              32 | 0.1295           |
| UK352          | Apr-11, May-03 |                     8 | B.1.1               |                              20 | 0.1571           |
| UK5557         | Mar-11, May-07 |                     8 | B.2.2               |                              16 | 0.4028           |
| UK788          | Feb-28, Mar-05 |                     8 | B.4                 |                              79 | 0.0108           |
| UK756          | Feb-27, Mar-05 |                     8 | B.1.1               |                              79 | 0.0127           |
| UK5308         | Apr-29, May-01 |                     8 | B.1.1               |                              22 | 0.013            |
| UK574          | Mar-30, Apr-29 |                     8 | B.1.1               |                              24 | 0.1786           |
| UK3875         | Apr-08, May-12 |                     8 | B.1.1               |                              11 | 0.4416           |
| UK182          | Mar-29, May-02 |                     8 | B.1.1               |                              21 | 0.2313           |
| UK5178         | Mar-21, Apr-17 |                     8 | B.1.1.7             |                              36 | 0.1071           |
| UK244          | Mar-12, Apr-30 |                     8 | B.1.1               |                              23 | 0.2663           |
| UK634          | Mar-30, Apr-18 |                     7 | B.1.1               |                              35 | 0.0905           |
| UK487          | Mar-24, Apr-08 |                     7 | B.1.1               |                              45 | 0.0556           |
| UK213          | Mar-18, Apr-17 |                     7 | B.1.1               |                              36 | 0.1389           |
| UK510          | Apr-02, Apr-16 |                     7 | B.1.1               |                              37 | 0.0631           |
| UK5307         | Mar-10, May-12 |                     7 | B.1.1               |                              11 | 0.7386           |
| UK913          | Apr-03, Apr-29 |                     7 | B.1                 |                              24 | 0.1806           |
| UK188          | Mar-07, Apr-15 |                     7 | B.1                 |                              38 | 0.1466           |
| UK232          | Mar-04, Mar-30 |                     7 | B.1.1               |                              54 | 0.0802           |
| UK29           | Mar-09, Apr-30 |                     7 | B.1.1               |                              23 | 0.3768           |
| UK49           | Mar-19, May-11 |                     7 | B.2.1               |                              12 | 0.7361           |
| UK309          | Apr-01, May-17 |                     7 | B.1.1               |                               6 | 1.2778           |
| UK692          | Mar-04, Apr-03 |                     7 | B.2, B, B.2.1       |                              50 | 0.1              |
| UK540          | Apr-09, Apr-22 |                     7 | B.1.1, B.1.1.p15    |                              31 | 0.0699           |
| UK5174         | Mar-26, Apr-07 |                     7 | B.1.1.7             |                              46 | 0.0373           |
| UK1006         | Apr-04, Apr-29 |                     7 | B.1.1               |                              24 | 0.1736           |
| UK206          | Mar-22, Apr-19 |                     7 | B.2.1               |                              34 | 0.1373           |
| UK65           | Mar-07, Apr-17 |                     7 | B.1.1               |                              36 | 0.1627           |
| UK69           | Mar-04, Apr-14 |                     7 | B.2.1               |                              39 | 0.1502           |
| UK5261         | Mar-29, May-01 |                     7 | B.1.1               |                              22 | 0.25             |
| UK317          | Mar-26, Apr-16 |                     7 | B.3                 |                              37 | 0.0946           |
| UK390          | Mar-27, May-01 |                     7 | B.1.5               |                              22 | 0.2652           |
| UK14           | Mar-04, Apr-01 |                     7 | B                   |                              52 | 0.067            |
| UK629          | Mar-23, Apr-13 |                     7 | B.1                 |                              40 | 0.0875           |
| UK5112         | Mar-20, May-08 |                     7 | B.1, B.2.1          |                              15 | 0.5444           |
| UK5177         | Mar-27, Apr-11 |                     7 | B.1.1.7             |                              42 | 0.0595           |
| UK268          | Mar-23, Apr-16 |                     7 | B.1.1               |                              37 | 0.0649           |
| UK217          | Apr-04, May-18 |                     7 | B.1.1               |                               5 | 1.4667           |
| UK331          | Mar-31, May-01 |                     7 | B.1.1               |                              22 | 0.2348           |
| UK32           | Mar-11, May-01 |                     7 | B.1.1               |                              22 | 0.3864           |
| UK2557         | Apr-01, May-13 |                     7 | B.1.p11             |                              10 | 0.325            |
| UK806          | Apr-04, Apr-27 |                     7 | B.1.1.10            |                              26 | 0.1474           |
| UK682          | Mar-21, Mar-30 |                     6 | B.2, B.2.1          |                              54 | 0.0333           |
| UK647          | Mar-21, Mar-27 |                     6 | B.2, B.2.1          |                              57 | 0.0292           |
| UK270          | Mar-13, Apr-09 |                     6 | B.3                 |                              44 | 0.1227           |
| UK5666         | Mar-13, Apr-05 |                     6 | B.2                 |                              48 | 0.0958           |
| UK755          | Mar-06, May-21 |                     6 | B.1.1               |                               2 | 7.6              |
| UK544          | Mar-24, Apr-06 |                     6 | B.2.1               |                              47 | 0.0553           |
| UK654          | Feb-27, Mar-08 |                     6 | B.2.5               |                              76 | 0.0263           |
| UK716          | Mar-31, Apr-08 |                     6 | B.1.1               |                              45 | 0.0356           |
| UK440          | Mar-28, Apr-13 |                     6 | B.1.1.10            |                              40 | 0.08             |
| UK517          | Mar-29, Apr-12 |                     6 | B.1.1               |                              41 | 0.0683           |
| UK799          | Mar-01, Mar-07 |                     6 | B.1                 |                              77 | 0.0156           |
| UK5581         | Mar-11, Apr-08 |                     6 | B.2.2               |                              45 | 0.1244           |
| UK1023         | Apr-07, Apr-16 |                     6 | B.1.1               |                              37 | 0.0486           |
| UK673          | Mar-28, May-18 |                     6 | B.1.1               |                               5 | 2.04             |
| UK68           | Mar-20, Apr-30 |                     6 | B.1.1               |                              23 | 0.3565           |
| UK263          | Mar-20, Apr-13 |                     6 | B.1.p11             |                              40 | 0.12             |
| UK849          | Apr-16, May-07 |                     6 | B.1.1               |                              16 | 0.2625           |
| UK325          | Apr-10, May-01 |                     6 | B.1.1               |                              22 | 0.1909           |
| UK110          | Mar-24, Apr-29 |                     6 | B.1                 |                              24 | 0.3              |
| UK542          | Apr-01, Apr-14 |                     6 | B.1                 |                              39 | 0.0667           |
| UK16           | Apr-16, May-06 |                     6 | B.1.1               |                              17 | 0.2353           |
| UK435          | Apr-03, Apr-23 |                     6 | B.1.5               |                              30 | 0.1333           |
| UK302          | Mar-25, May-03 |                     6 | B.1.1               |                              20 | 0.39             |
| UK161          | Mar-10, May-03 |                     6 | B.1.1               |                              20 | 0.27             |
| UK372          | Apr-16, May-05 |                     6 | B.1.1               |                              18 | 0.2111           |
| UK497          | Mar-27, Apr-27 |                     6 | A.2                 |                              26 | 0.2385           |
| UK1344         | Apr-20, May-08 |                     6 | B                   |                              15 | 0.24             |
| UK58           | Mar-17, Apr-09 |                     6 | B.1                 |                              44 | 0.053            |
| UK15           | Mar-06, Apr-30 |                     6 | B.1.1               |                              23 | 0.2657           |
| UK5378         | Mar-23, May-01 |                     6 | B.1.1               |                              22 | 0.1043           |
| UK157          | Mar-29, May-16 |                     6 | B.1                 |                               7 | 1.3714           |
| UK746          | Mar-31, Apr-14 |                     6 | B.1.5               |                              39 | 0.0718           |
| UK247          | Apr-04, May-15 |                     6 | B.1.1               |                               8 | 1.025            |
| UK202          | Mar-10, Apr-30 |                     6 | B.1.1               |                              23 | 0.2149           |
| UK5703         | Mar-06, Apr-07 |                     6 | B.2                 |                              46 | 0.1429           |
| UK489          | Mar-23, Apr-07 |                     6 | B.2.1               |                              46 | 0.0652           |
| UK481          | Mar-30, Apr-14 |                     6 | B.1.1               |                              39 | 0.0769           |
| UK659          | Mar-21, Mar-30 |                     6 | B                   |                              54 | 0.0333           |
| UK447          | Apr-05, Apr-21 |                     6 | B.1.1               |                              32 | 0.1              |
| UK284          | Apr-02, Apr-25 |                     6 | B.1.1               |                              28 | 0.1643           |
| UK512          | Mar-30, Apr-13 |                     6 | B.1.1               |                              40 | 0.07             |
| UK570          | Apr-05, Apr-17 |                     6 | B.1.1               |                              36 | 0.0667           |
| UK102          | Mar-10, Apr-16 |                     6 | B.1                 |                              37 | 0.2              |
| UK735          | Mar-13, Apr-16 |                     6 | B.3                 |                              37 | 0.1838           |
| UK5486         | Mar-11, May-20 |                     6 | B.2, B.1.1          |                               3 | 4.6667           |
| UK280          | Mar-30, Apr-15 |                     6 | B.1.1               |                              38 | 0.0842           |
| UK680          | Apr-05, Apr-14 |                     6 | B.1                 |                              39 | 0.0462           |
| UK330          | Mar-23, Apr-13 |                     6 | B.1.1               |                              40 | 0.0875           |
| UK40           | Mar-31, Apr-20 |                     6 | B.16                |                              33 | 0.041            |
| UK1174         | Apr-02, May-12 |                     6 | B.1.1               |                              11 | 0.6833           |
| UK313          | Mar-23, Apr-14 |                     6 | B.1.1               |                              39 | 0.1128           |
| UK989          | Mar-21, Apr-19 |                     6 | B.1                 |                              34 | 0.1706           |
| UK27           | Mar-08, Apr-26 |                     6 | B.1.1               |                              27 | 0.363            |
| UK857          | Mar-24, Mar-29 |                     6 | B.2.1               |                              55 | 0.0182           |

\pagebreak

**Table S2** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK701 |   UK2464 |   UK9 |   UK4 |   UK19 |   UK6 |   UK494 |   UK63 |   UK36 |
|:------------------|------:|--------:|---------:|------:|------:|-------:|------:|--------:|-------:|-------:|
| 2020-02-02        |     0 |       2 |        0 |     0 |     0 |      0 |     0 |       0 |      0 |      0 |
| 2020-02-09        |     0 |       1 |        0 |     0 |     0 |      0 |     0 |       0 |      0 |      0 |
| 2020-02-23        |     0 |      10 |        0 |     0 |     1 |      0 |     0 |       0 |      0 |      0 |
| 2020-03-01        |     3 |      13 |        0 |     0 |     6 |      0 |     1 |       0 |      0 |      0 |
| 2020-03-08        |    13 |       8 |        3 |     2 |     4 |      2 |     1 |       0 |      0 |      0 |
| 2020-03-15        |    11 |       9 |        7 |     4 |     7 |      3 |     3 |       2 |      2 |      1 |
| 2020-03-22        |    16 |       7 |       10 |     7 |    11 |      6 |     2 |       4 |      4 |      2 |
| 2020-03-29        |    21 |      10 |       14 |    13 |    10 |     10 |     5 |       8 |      9 |      6 |
| 2020-04-05        |    23 |      10 |       13 |    10 |     6 |      9 |     6 |       6 |      7 |      4 |
| 2020-04-12        |    21 |      11 |        9 |     8 |     3 |      7 |     6 |       6 |      8 |      6 |
| 2020-04-19        |    17 |       5 |        6 |     1 |     2 |      4 |     7 |       3 |      1 |      3 |
| 2020-04-26        |    22 |       4 |        7 |     2 |     1 |      4 |     5 |       3 |      2 |      2 |
| 2020-05-03        |    11 |       1 |        4 |     1 |     0 |      1 |     4 |       2 |      2 |      2 |
| 2020-05-10        |     7 |       1 |        1 |     0 |     0 |      1 |     1 |       0 |      0 |      2 |
| 2020-05-17        |     5 |       0 |        0 |     0 |     0 |      0 |     0 |       0 |      0 |      0 |

\pagebreak


Table S3 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S4** Raw data for figure six showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
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
| 2020-02-27 |                            6 |                                3 |       9 |
| 2020-02-28 |                            4 |                                6 |      10 |
| 2020-02-29 |                            9 |                                1 |      10 |
| 2020-03-01 |                           17 |                                9 |      26 |
| 2020-03-02 |                           39 |                                3 |      42 |
| 2020-03-03 |                           33 |                               11 |      44 |
| 2020-03-04 |                           35 |                               15 |      50 |
| 2020-03-05 |                           41 |                                6 |      47 |
| 2020-03-06 |                           35 |                               16 |      51 |
| 2020-03-07 |                           18 |                                7 |      25 |
| 2020-03-08 |                           24 |                               10 |      34 |
| 2020-03-09 |                           38 |                               13 |      51 |
| 2020-03-10 |                           46 |                               23 |      69 |
| 2020-03-11 |                           73 |                               30 |     103 |
| 2020-03-12 |                           92 |                               28 |     120 |
| 2020-03-13 |                           40 |                               28 |      68 |
| 2020-03-14 |                           36 |                               19 |      55 |
| 2020-03-15 |                           26 |                               12 |      38 |
| 2020-03-16 |                           31 |                               23 |      54 |
| 2020-03-17 |                           39 |                               30 |      69 |
| 2020-03-18 |                           65 |                               45 |     110 |
| 2020-03-19 |                           54 |                               35 |      89 |
| 2020-03-20 |                           70 |                               43 |     113 |
| 2020-03-21 |                           72 |                               40 |     112 |
| 2020-03-22 |                           70 |                               28 |      98 |
| 2020-03-23 |                          119 |                               56 |     175 |
| 2020-03-24 |                          113 |                               37 |     150 |
| 2020-03-25 |                           88 |                               46 |     134 |
| 2020-03-26 |                          104 |                               49 |     153 |
| 2020-03-27 |                           89 |                               53 |     142 |
| 2020-03-28 |                           98 |                               38 |     136 |
| 2020-03-29 |                          106 |                               40 |     146 |
| 2020-03-30 |                          145 |                               47 |     192 |
| 2020-03-31 |                          119 |                               47 |     166 |
| 2020-04-01 |                          114 |                               38 |     152 |
| 2020-04-02 |                          109 |                               37 |     146 |
| 2020-04-03 |                          105 |                               31 |     136 |
| 2020-04-04 |                           78 |                               39 |     117 |
| 2020-04-05 |                           89 |                               17 |     106 |
| 2020-04-06 |                          108 |                               16 |     124 |
| 2020-04-07 |                           97 |                               20 |     117 |
| 2020-04-08 |                           71 |                               21 |      92 |
| 2020-04-09 |                           50 |                               12 |      62 |
| 2020-04-10 |                           61 |                               11 |      72 |
| 2020-04-11 |                           48 |                               15 |      63 |
| 2020-04-12 |                           36 |                                5 |      41 |
| 2020-04-13 |                           40 |                                8 |      48 |
| 2020-04-14 |                           50 |                               13 |      63 |
| 2020-04-15 |                           45 |                               10 |      55 |
| 2020-04-16 |                           45 |                               10 |      55 |
| 2020-04-17 |                           42 |                                8 |      50 |
| 2020-04-18 |                           16 |                                3 |      19 |
| 2020-04-19 |                           20 |                                4 |      24 |
| 2020-04-20 |                           24 |                                5 |      29 |
| 2020-04-21 |                           19 |                                2 |      21 |
| 2020-04-22 |                            6 |                                7 |      13 |
| 2020-04-23 |                            7 |                                2 |       9 |
| 2020-04-24 |                            4 |                                1 |       5 |
| 2020-04-25 |                            7 |                                0 |       7 |
| 2020-04-26 |                            6 |                                0 |       6 |
| 2020-04-27 |                           12 |                                3 |      15 |
| 2020-04-28 |                            5 |                                1 |       6 |
| 2020-04-29 |                           13 |                                3 |      16 |
| 2020-04-30 |                           10 |                                3 |      13 |
| 2020-05-01 |                           15 |                                1 |      16 |
| 2020-05-02 |                            3 |                                2 |       5 |
| 2020-05-03 |                            5 |                                0 |       5 |
| 2020-05-04 |                            7 |                                1 |       8 |
| 2020-05-05 |                            8 |                                1 |       9 |
| 2020-05-06 |                            3 |                                0 |       3 |
| 2020-05-07 |                            3 |                                1 |       4 |
| 2020-05-08 |                            2 |                                0 |       2 |
| 2020-05-09 |                            1 |                                2 |       3 |
| 2020-05-10 |                            2 |                                0 |       2 |
| 2020-05-11 |                            5 |                                1 |       6 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-13 |                            3 |                                0 |       3 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-18 |                            1 |                                0 |       1 |
| 2020-05-21 |                            1 |                                0 |       1 |

\pagebreak

**Table S5** Raw data for figure seven showing the number of sequences taken over time.


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
| 2020-03-02 |        72 |
| 2020-03-03 |        91 |
| 2020-03-04 |       102 |
| 2020-03-05 |        81 |
| 2020-03-06 |        74 |
| 2020-03-07 |        43 |
| 2020-03-08 |        50 |
| 2020-03-09 |        71 |
| 2020-03-10 |        89 |
| 2020-03-11 |       145 |
| 2020-03-12 |       179 |
| 2020-03-13 |       102 |
| 2020-03-14 |        83 |
| 2020-03-15 |        64 |
| 2020-03-16 |        79 |
| 2020-03-17 |       118 |
| 2020-03-18 |       184 |
| 2020-03-19 |       141 |
| 2020-03-20 |       194 |
| 2020-03-21 |       203 |
| 2020-03-22 |       193 |
| 2020-03-23 |       332 |
| 2020-03-24 |       285 |
| 2020-03-25 |       276 |
| 2020-03-26 |       299 |
| 2020-03-27 |       292 |
| 2020-03-28 |       299 |
| 2020-03-29 |       339 |
| 2020-03-30 |       481 |
| 2020-03-31 |       442 |
| 2020-04-01 |       402 |
| 2020-04-02 |       413 |
| 2020-04-03 |       416 |
| 2020-04-04 |       336 |
| 2020-04-05 |       346 |
| 2020-04-06 |       428 |
| 2020-04-07 |       396 |
| 2020-04-08 |       344 |
| 2020-04-09 |       293 |
| 2020-04-10 |       303 |
| 2020-04-11 |       256 |
| 2020-04-12 |       206 |
| 2020-04-13 |       239 |
| 2020-04-14 |       309 |
| 2020-04-15 |       302 |
| 2020-04-16 |       283 |
| 2020-04-17 |       213 |
| 2020-04-18 |       109 |
| 2020-04-19 |       139 |
| 2020-04-20 |       151 |
| 2020-04-21 |       111 |
| 2020-04-22 |       121 |
| 2020-04-23 |        82 |
| 2020-04-24 |        48 |
| 2020-04-25 |        48 |
| 2020-04-26 |        77 |
| 2020-04-27 |       127 |
| 2020-04-28 |        81 |
| 2020-04-29 |       163 |
| 2020-04-30 |       156 |
| 2020-05-01 |       200 |
| 2020-05-02 |        98 |
| 2020-05-03 |        61 |
| 2020-05-04 |       111 |
| 2020-05-05 |        68 |
| 2020-05-06 |        77 |
| 2020-05-07 |        75 |
| 2020-05-08 |        41 |
| 2020-05-09 |        40 |
| 2020-05-10 |        36 |
| 2020-05-11 |        66 |
| 2020-05-12 |        38 |
| 2020-05-13 |        39 |
| 2020-05-14 |        14 |
| 2020-05-15 |        16 |
| 2020-05-16 |         7 |
| 2020-05-17 |        10 |
| 2020-05-18 |        21 |
| 2020-05-19 |        21 |
| 2020-05-20 |         7 |
| 2020-05-21 |         7 |
| 2020-05-22 |         8 |
| 2020-05-23 |         2 |

\pagebreak

**Table S6** Raw data for the map with the number of sequences assigned to each admin2 region.


| Admin2                       | Country   |   Number of sequences | Sequence group   |
|:-----------------------------|:----------|----------------------:|:-----------------|
| BATH AND NORTH EAST SOMERSET | England   |                     0 | 0                |
| BEDFORDSHIRE                 | England   |                   417 | 400-500          |
| BERKSHIRE                    | England   |                     7 | 1-10             |
| BLACKBURN WITH DARWEN        | England   |                     0 | 0                |
| BLACKPOOL                    | England   |                     0 | 0                |
| BOLTON                       | England   |                     0 | 0                |
| BOURNEMOUTH                  | England   |                     0 | 0                |
| BRIGHTON AND HOVE            | England   |                     0 | 0                |
| BRISTOL                      | England   |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England   |                   348 | 300-400          |
| BURY                         | England   |                     0 | 0                |
| CAMBRIDGESHIRE               | England   |                   656 | >500             |
| CENTRAL BEDFORDSHIRE         | England   |                     0 | 0                |
| CHESHIRE                     | England   |                    10 | 10-50            |
| CORNWALL                     | England   |                    20 | 10-50            |
| CUMBRIA                      | England   |                    31 | 10-50            |
| DARLINGTON                   | England   |                     0 | 0                |
| DERBY                        | England   |                     0 | 0                |
| DERBYSHIRE                   | England   |                    25 | 10-50            |
| DEVON                        | England   |                   283 | 250-300          |
| DORSET                       | England   |                   159 | 150-200          |
| DURHAM                       | England   |                     3 | 1-10             |
| EAST RIDING OF YORKSHIRE     | England   |                    31 | 10-50            |
| ESSEX                        | England   |                  1189 | >500             |
| GATESHEAD                    | England   |                     0 | 0                |
| GLOUCESTERSHIRE              | England   |                   452 | 400-500          |
| GREATER LONDON               | England   |                  2273 | >500             |
| HALTON                       | England   |                     0 | 0                |
| HAMPSHIRE                    | England   |                    95 | 50-100           |
| HARTLEPOOL                   | England   |                     0 | 0                |
| HEREFORDSHIRE                | England   |                     4 | 1-10             |
| HERTFORDSHIRE                | England   |                   928 | >500             |
| ISLE OF WIGHT                | England   |                     0 | 0                |
| ISLES OF SCILLY              | England   |                     0 | 0                |
| KENT                         | England   |                    28 | 10-50            |
| KINGSTON UPON HULL           | England   |                     0 | 0                |
| LANCASHIRE                   | England   |                     6 | 1-10             |
| LEICESTER                    | England   |                     0 | 0                |
| LEICESTERSHIRE               | England   |                     5 | 1-10             |
| LINCOLNSHIRE                 | England   |                    16 | 10-50            |
| LUTON                        | England   |                     0 | 0                |
| MANCHESTER                   | England   |                    30 | 10-50            |
| MEDWAY                       | England   |                     0 | 0                |
| MERSEYSIDE                   | England   |                    59 | 50-100           |
| MIDDLESBROUGH                | England   |                     0 | 0                |
| MILTON KEYNES                | England   |                     0 | 0                |
| NORFOLK                      | England   |                   498 | 400-500          |
| NORTH LINCOLNSHIRE           | England   |                     0 | 0                |
| NORTH SOMERSET               | England   |                     0 | 0                |
| NORTH YORKSHIRE              | England   |                    53 | 50-100           |
| NORTHAMPTONSHIRE             | England   |                    22 | 10-50            |
| NORTHUMBERLAND               | England   |                     2 | 1-10             |
| NOTTINGHAM                   | England   |                   559 | >500             |
| NOTTINGHAMSHIRE              | England   |                    58 | 50-100           |
| OLDHAM                       | England   |                     0 | 0                |
| OXFORDSHIRE                  | England   |                    97 | 50-100           |
| PETERBOROUGH                 | England   |                     0 | 0                |
| PLYMOUTH                     | England   |                     1 | 1-10             |
| POOLE                        | England   |                     0 | 0                |
| PORTSMOUTH                   | England   |                     0 | 0                |
| REDCAR AND CLEVELAND         | England   |                     0 | 0                |
| ROCHDALE                     | England   |                     0 | 0                |
| RUTLAND                      | England   |                     0 | 0                |
| SALFORD                      | England   |                     0 | 0                |
| SHROPSHIRE                   | England   |                     1 | 1-10             |
| SOMERSET                     | England   |                   338 | 300-400          |
| SOUTH GLOUCESTERSHIRE        | England   |                     0 | 0                |
| SOUTH YORKSHIRE              | England   |                  1165 | >500             |
| SOUTHAMPTON                  | England   |                     0 | 0                |
| SOUTHEND-ON-SEA              | England   |                     0 | 0                |
| STAFFORDSHIRE                | England   |                    28 | 10-50            |
| STOCKPORT                    | England   |                     0 | 0                |
| STOCKTON-ON-TEES             | England   |                     0 | 0                |
| STOKE-ON-TRENT               | England   |                     0 | 0                |
| SUFFOLK                      | England   |                   484 | 400-500          |
| SURREY                       | England   |                    60 | 50-100           |
| SUSSEX                       | England   |                     1 | 1-10             |
| SWINDON                      | England   |                     0 | 0                |
| TAMESIDE                     | England   |                     0 | 0                |
| TELFORD AND WREKIN           | England   |                     0 | 0                |
| THURROCK                     | England   |                     0 | 0                |
| TORBAY                       | England   |                     0 | 0                |
| TRAFFORD                     | England   |                     0 | 0                |
| TYNE AND WEAR                | England   |                    38 | 10-50            |
| WARRINGTON                   | England   |                     0 | 0                |
| WARWICKSHIRE                 | England   |                    10 | 10-50            |
| WEST MIDLANDS                | England   |                    89 | 50-100           |
| WEST YORKSHIRE               | England   |                    20 | 10-50            |
| WIGAN                        | England   |                     0 | 0                |
| WILTSHIRE                    | England   |                   243 | 200-250          |
| WORCESTERSHIRE               | England   |                     7 | 1-10             |
| YORK                         | England   |                     0 | 0                |

\pagebreak






