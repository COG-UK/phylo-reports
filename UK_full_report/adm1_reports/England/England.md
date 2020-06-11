







# Lineages report for England




This report gives summaries of lineages sampled in England for week 2020-06-05. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-02. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
13984 sequences from England have been included in this analysis.
4592 lineages have been recorded, 3446 of which only contain one sequence.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 4777 and the maximum is 6858


Sequences which were replicates or too error-prone were removed from this analysis.



4467 are lineages which were sampled less than five times in England, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 125 that remain:
82 are pending extinction, ie last seen three weeks ago.
30 lineages have gone quiet, ie haven't been seen this week.
4 lineages have reactivated.
9 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | Date range     |   Number of sequences | Global lineage   |   Time since last sample (days) |   Activity score |
|:---------------|:---------------|----------------------:|:-----------------|--------------------------------:|-----------------:|
| UK5            | Mar-03, May-31 |                  1096 | B.1.1.1, B.1.1   |                               2 |           0.0339 |
| UK2464         | Mar-09, May-25 |                   255 | B.1.p11          |                               8 |           0.0222 |
| UK2916         | Feb-03, May-10 |                   253 | B.1.p11, B.1     |                              23 |           0.0132 |
| UK9            | Mar-09, May-15 |                   201 | B.1.13           |                              18 |           0.0185 |
| UK4            | Feb-28, May-18 |                   169 | B                |                              15 |           0.0287 |
| UK494          | Mar-20, May-05 |                   106 | B.1.p11          |                              28 |           0.0152 |
| UK2913         | Mar-10, May-12 |                    99 | B.1.p11          |                              21 |           0.0231 |
| UK6            | Mar-17, May-13 |                    94 | B.1              |                              20 |           0.0306 |
| UK19           | Mar-09, May-15 |                    93 | B.1              |                              18 |           0.0199 |
| UK63           | Mar-18, May-05 |                    90 | B.1.1            |                              28 |           0.019  |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](UK_full_report/results/figures/England_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](UK_full_report/results/figures/England_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](UK_full_report/results/figures/England_geog_plot_1.png){#geog_plot }










These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](UK_full_report/results/figures/England_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 



NB the lineage may have started anywhere in the UK, but has been recorded at least once in England



![Lineage starts per week, split by singletons and non-singletons](UK_full_report/results/figures/England_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](UK_full_report/results/figures/England_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





![Map showing the number of sequences sampled by adm2 region](UK_full_report/results/figures/England_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | Date range     |   Number of sequences | Global lineage    |   Time since last sample (days) | Activity score   |
|:---------------|:---------------|----------------------:|:------------------|--------------------------------:|:-----------------|
| UK5            | Mar-03, May-31 |                  1096 | B.1.1.1, B.1.1    |                               2 | 0.0339           |
| UK2464         | Mar-09, May-25 |                   255 | B.1.p11           |                               8 | 0.0222           |
| UK2916         | Feb-03, May-10 |                   253 | B.1.p11, B.1      |                              23 | 0.0132           |
| UK9            | Mar-09, May-15 |                   201 | B.1.13            |                              18 | 0.0185           |
| UK4            | Feb-28, May-18 |                   169 | B                 |                              15 | 0.0287           |
| UK494          | Mar-20, May-05 |                   106 | B.1.p11           |                              28 | 0.0152           |
| UK2913         | Mar-10, May-12 |                    99 | B.1.p11           |                              21 | 0.0231           |
| UK6            | Mar-17, May-13 |                    94 | B.1               |                              20 | 0.0306           |
| UK19           | Mar-09, May-15 |                    93 | B.1               |                              18 | 0.0199           |
| UK63           | Mar-18, May-05 |                    90 | B.1.1             |                              28 | 0.019            |
| UK36           | Mar-19, May-21 |                    83 | B.1               |                              12 | 0.0161           |
| UK177          | Mar-27, May-12 |                    79 | B.1.1             |                              21 | 0.0281           |
| UK371          | Mar-12, May-19 |                    77 | B.1.1             |                              14 | 0.0631           |
| UK200          | Apr-08, May-18 |                    76 | B.1.p11           |                              15 | 0.0356           |
| UK77           | Mar-11, May-20 |                    74 | B.2, B.2.4        |                              13 | 0.069            |
| UK26           | Mar-18, May-20 |                    74 | B.1.1.3           |                              13 | 0.0664           |
| UK89           | Mar-11, May-28 |                    72 | B.1.1.9           |                               5 | 0.2108           |
| UK632          | Mar-23, Jun-02 |                    71 | B.1.1             |                               0 | active today     |
| UK107          | Mar-15, Apr-21 |                    68 | B.2.5, B.2, B.2.1 |                              42 | 0.0131           |
| UK66           | Mar-18, May-20 |                    68 | B.1.1.8           |                              13 | 0.0577           |
| UK194          | Mar-19, Apr-24 |                    64 | B.1.1             |                              39 | 0.0147           |
| UK343          | Mar-28, May-15 |                    64 | B.1               |                              18 | 0.0423           |
| UK274          | Mar-06, May-21 |                    62 | B.3, B            |                              12 | 0.099            |
| UK37           | Mar-17, May-04 |                    60 | B.1.30, B.1       |                              29 | 0.0271           |
| UK204          | Apr-07, May-12 |                    60 | B.1.1             |                              21 | 0.0282           |
| UK199          | Apr-08, May-21 |                    59 | B.1.5.5           |                              12 | 0.0618           |
| UK339          | Feb-23, Apr-16 |                    59 | B.3               |                              47 | 0.015            |
| UK115          | Mar-15, Apr-20 |                    58 | B.2.1             |                              43 | 0.0144           |
| UK51           | Mar-25, May-26 |                    57 | B.1.36            |                               7 | 0.1497           |
| UK2735         | Mar-24, May-15 |                    57 | B.1.1             |                              18 | 0.0358           |
| UK476          | Mar-31, May-06 |                    56 | B.1.1             |                              27 | 0.0242           |
| UK112          | Mar-15, May-04 |                    56 | B.1.1.p11, B.1.1  |                              29 | 0.0313           |
| UK56           | Mar-20, Jun-02 |                    52 | B.1.1             |                               0 | active today     |
| UK214          | Mar-06, May-21 |                    52 | B.1.1             |                              12 | 0.1195           |
| UK3            | Feb-24, May-25 |                    49 | B.1               |                               8 | 0.237            |
| UK13           | Mar-13, May-13 |                    47 | B.1.1             |                              20 | 0.0663           |
| UK94           | Mar-12, Apr-19 |                    47 | B.2, B.2.1        |                              44 | 0.0188           |
| UK238          | Mar-19, May-07 |                    47 | B.1.1             |                              26 | 0.041            |
| UK28           | Mar-13, May-01 |                    45 | B.1.1.10          |                              32 | 0.0348           |
| UK513          | Mar-12, Apr-29 |                    43 | B.1.p11           |                              34 | 0.0336           |
| UK5672         | Mar-19, May-13 |                    43 | B.2               |                              20 | 0.064            |
| UK233          | Apr-08, May-21 |                    41 | B.1.1             |                              12 | 0.0896           |
| UK128          | Apr-03, May-27 |                    40 | B.1.1             |                               6 | 0.2308           |
| UK8            | Mar-03, May-01 |                    38 | B                 |                              32 | 0.045            |
| UK62           | Mar-12, Apr-23 |                    38 | B.3               |                              40 | 0.0262           |
| UK31           | Mar-21, May-06 |                    37 | B.1               |                              27 | 0.0473           |
| UK23           | Mar-12, May-02 |                    37 | B, B.9            |                              31 | 0.0445           |
| UK346          | Mar-16, Apr-19 |                    36 | B.1.72, B.1       |                              44 | 0.0221           |
| UK276          | Mar-18, May-01 |                    36 | B.1.1             |                              32 | 0.0393           |
| UK190          | Mar-01, Apr-19 |                    36 | B.1               |                              44 | 0.0318           |
| UK147          | Apr-04, May-26 |                    36 | B.1.1             |                               7 | 0.2122           |
| UK283          | Mar-25, May-04 |                    35 | B.1.1             |                              29 | 0.0406           |
| UK18           | Mar-11, May-27 |                    35 | B.1.1.7           |                               6 | 0.3775           |
| UK12           | Mar-12, May-07 |                    35 | B.1.p11           |                              26 | 0.0615           |
| UK3035         | Mar-24, May-18 |                    35 | B.1               |                              15 | 0.1078           |
| UK131          | Mar-11, Apr-14 |                    34 | B.15              |                              49 | 0.0183           |
| UK138          | Mar-23, Apr-26 |                    33 | B.2.1             |                              37 | 0.0287           |
| UK3019         | Mar-06, May-07 |                    33 | B.1               |                              26 | 0.0662           |
| UK5660         | Apr-11, May-10 |                    33 | B.1.1             |                              23 | 0.0764           |
| UK173          | Mar-16, May-19 |                    32 | B                 |                              14 | 0.1475           |
| UK167          | Mar-29, May-21 |                    31 | B.1.66, B.1       |                              12 | 0.1472           |
| UK79           | Mar-24, May-05 |                    30 | B.1               |                              28 | 0.0517           |
| UK95           | Mar-10, May-07 |                    30 | B.2.1             |                              26 | 0.0744           |
| UK113          | Mar-22, May-30 |                    28 | B.1.1             |                               3 | 0.8519           |
| UK241          | Mar-22, Apr-16 |                    28 | B.1.5.3           |                              47 | 0.0197           |
| UK116          | Feb-25, Apr-01 |                    28 | B.2.1             |                              62 | 0.0215           |
| UK300          | Mar-28, May-04 |                    27 | B.1.1             |                              29 | 0.0491           |
| UK5741         | Mar-01, Apr-19 |                    27 | B.2, B.1          |                              44 | 0.0398           |
| UK351          | Apr-13, May-21 |                    27 | B.1.1.10, B.1.1   |                              12 | 0.1218           |
| UK53           | Mar-26, May-22 |                    27 | B.1.1.4           |                              11 | 0.096            |
| UK144          | Mar-05, Apr-07 |                    26 | B.2.1             |                              56 | 0.0236           |
| UK565          | Mar-31, May-13 |                    26 | B.1.1             |                              20 | 0.086            |
| UK183          | Mar-29, Apr-23 |                    26 | B.1.1             |                              40 | 0.025            |
| UK33           | Mar-30, May-12 |                    25 | B.1.1             |                              21 | 0.0853           |
| UK114          | Mar-16, May-25 |                    25 | B.1.1             |                               8 | 0.3646           |
| UK64           | Mar-12, May-05 |                    25 | B.1               |                              28 | 0.0536           |
| UK57           | Apr-05, Apr-28 |                    25 | B.1.1             |                              35 | 0.0274           |
| UK5675         | Mar-03, May-06 |                    25 | B.2               |                              27 | 0.0847           |
| UK235          | Mar-21, May-04 |                    25 | B.1.1             |                              29 | 0.0632           |
| UK81           | Mar-19, Apr-27 |                    24 | B.1.1             |                              36 | 0.0451           |
| UK119          | Mar-11, Apr-16 |                    24 | B.2.5             |                              47 | 0.0247           |
| UK103          | Mar-20, May-27 |                    24 | B.1.1             |                               6 | 0.4928           |
| UK248          | Apr-08, May-16 |                    24 | B.1.1             |                              17 | 0.086            |
| UK158          | Mar-23, May-17 |                    24 | B.1.1.2, B.1.1    |                              16 | 0.0168           |
| UK101          | Mar-21, Apr-27 |                    23 | B.1.5             |                              36 | 0.0447           |
| UK92           | Mar-23, Apr-30 |                    23 | B.1.1             |                              33 | 0.0501           |
| UK326          | Mar-22, May-22 |                    23 | B.1.1.10          |                              11 | 0.2521           |
| UK109          | Mar-21, May-01 |                    23 | B.1.5             |                              32 | 0.0512           |
| UK3021         | Mar-12, May-16 |                    23 | B.1               |                              17 | 0.0237           |
| UK5649         | Mar-15, May-11 |                    23 | B.2.6, B.1.1      |                              22 | 0.1036           |
| UK24           | Mar-18, May-04 |                    22 | B.1.1.10, B.1.1   |                              29 | 0.0772           |
| UK30           | Mar-15, May-15 |                    22 | B.1.1             |                              18 | 0.1614           |
| UK2200         | Feb-28, May-05 |                    22 | B.1.5, B.1.5.6    |                              28 | 0.0263           |
| UK61           | Mar-12, May-15 |                    22 | B.3               |                              18 | 0.0093           |
| UK5549         | Mar-04, May-18 |                    22 | B.2.2             |                              15 | 0.2              |
| UK279          | Mar-26, Apr-25 |                    22 | B.1.1             |                              38 | 0.0376           |
| UK174          | Mar-19, May-22 |                    21 | B.1.5             |                              11 | 0.2909           |
| UK722          | Mar-23, May-18 |                    21 | B.1.1             |                              15 | 0.1867           |
| UK384          | Mar-14, Apr-02 |                    21 | B.2.1             |                              61 | 0.0156           |
| UK135          | Apr-01, May-14 |                    21 | B.1.p11           |                              19 | 0.1132           |
| UK72           | Mar-13, May-04 |                    20 | B.10              |                              29 | 0.023            |
| UK307          | Mar-28, May-04 |                    20 | B.1.1             |                              29 | 0.0672           |
| UK75           | Mar-17, Apr-26 |                    20 | B.1.34, B.1       |                              37 | 0.0569           |
| UK293          | Mar-24, Apr-28 |                    20 | B.1               |                              35 | 0.0526           |
| UK419          | Mar-30, May-02 |                    19 | B.1.1             |                              31 | 0.0591           |
| UK219          | Mar-26, May-02 |                    19 | B.1.1             |                              31 | 0.0628           |
| UK514          | Mar-30, Apr-13 |                    19 | B.1.1             |                              50 | 0.0156           |
| UK291          | Mar-13, Apr-05 |                    19 | B.2.1             |                              58 | 0.0209           |
| UK2013         | Mar-15, Apr-26 |                    19 | B.1               |                              37 | 0.0597           |
| UK126          | Mar-29, May-03 |                    18 | B.1.1             |                              30 | 0.0686           |
| UK1764         | Mar-14, Apr-19 |                    18 | B.3               |                              44 | 0.0481           |
| UK117          | Feb-28, Apr-04 |                    18 | B.2.1             |                              59 | 0.0359           |
| UK376          | Apr-04, May-08 |                    17 | B.1.1             |                              25 | 0.085            |
| UK2045         | Mar-17, May-09 |                    17 | B, B.1            |                              24 | 0.138            |
| UK4442         | May-10, May-24 |                    17 | B.1.1             |                               9 | 0.0972           |
| UK888          | Apr-05, May-04 |                    17 | B.1.1             |                              29 | 0.0588           |
| UK5309         | Mar-20, Apr-29 |                    17 | B.1.1.10, B.1.1   |                              34 | 0.0619           |
| UK143          | Mar-14, Apr-16 |                    17 | B.2.1             |                              47 | 0.0439           |
| UK29           | Mar-09, May-08 |                    17 | B.1.1             |                              25 | 0.15             |
| UK403          | Mar-23, Apr-15 |                    17 | B.1.1             |                              48 | 0.0299           |
| UK41           | Mar-01, Apr-24 |                    17 | B.1               |                              39 | 0.0729           |
| UK195          | Mar-29, May-03 |                    16 | B.1.1             |                              30 | 0.0778           |
| UK67           | Mar-25, May-21 |                    16 | B.1.1             |                              12 | 0.3167           |
| UK5084         | Mar-29, Apr-18 |                    16 | B.1               |                              45 | 0.0261           |
| UK86           | Mar-05, May-14 |                    16 | B.1               |                              19 | 0.0722           |
| UK397          | Mar-28, Apr-18 |                    16 | B.1.1.13, B.1.1   |                              45 | 0.0311           |
| UK46           | Mar-02, May-08 |                    16 | B.2.1             |                              25 | 0.1675           |
| UK374          | Apr-01, Apr-20 |                    15 | B.1.1             |                              43 | 0.0316           |
| UK5715         | Feb-13, Apr-22 |                    15 | B.2, B.1.1        |                              41 | 0.1122           |
| UK134          | Mar-04, Apr-07 |                    15 | B.1               |                              56 | 0.0337           |
| UK1849         | Apr-07, Apr-20 |                    15 | B.1.1             |                              43 | 0.0216           |
| UK5713         | Mar-26, Apr-14 |                    14 | B.2, B.1.1        |                              49 | 0.0298           |
| UK5180         | Apr-04, Apr-24 |                    14 | B.1.1.7           |                              39 | 0.0394           |
| UK253          | Apr-03, May-03 |                    14 | B.1.1             |                              30 | 0.0769           |
| UK354          | Mar-18, Apr-11 |                    14 | B.1.1             |                              52 | 0.033            |
| UK501          | Apr-03, Apr-29 |                    14 | B, B.1            |                              34 | 0.0588           |
| UK569          | Mar-23, May-12 |                    14 | B.1.1             |                              21 | 0.1832           |
| UK146          | Mar-24, May-07 |                    14 | B.1.1             |                              26 | 0.1209           |
| UK254          | Mar-20, Apr-14 |                    14 | B.1.1             |                              49 | 0.0392           |
| UK726          | Mar-30, May-04 |                    14 | B.1               |                              29 | 0.0928           |
| UK505          | Mar-21, May-15 |                    14 | B.1.1.p11, B.1.1  |                              18 | 0.235            |
| UK153          | Mar-13, Apr-14 |                    14 | B.2               |                              49 | 0.0502           |
| UK278          | Apr-10, May-06 |                    14 | B.1.1             |                              27 | 0.0741           |
| UK249          | Apr-01, Apr-25 |                    14 | B.1.1             |                              38 | 0.0439           |
| UK236          | Mar-27, Apr-22 |                    14 | B.1.1             |                              41 | 0.0453           |
| UK179          | Mar-26, May-07 |                    14 | B.1.1.p11         |                              26 | 0.053            |
| UK5214         | Mar-20, May-04 |                    14 | B.1.1             |                              29 | 0.1194           |
| UK5260         | Mar-29, May-02 |                    13 | B.1.1             |                              31 | 0.0914           |
| UK378          | Feb-15, Mar-05 |                    13 | B.1.1             |                              89 | 0.0178           |
| UK308          | Apr-09, May-18 |                    13 | B.1.1             |                              15 | 0.2167           |
| UK5663         | Apr-11, May-02 |                    13 | B.2, B.1.1        |                              31 | 0.0565           |
| UK34           | Feb-15, Apr-02 |                    13 | B.4               |                              61 | 0.0642           |
| UK637          | Mar-28, May-01 |                    13 | B.1.1             |                              32 | 0.0885           |
| UK5498         | Apr-01, Apr-20 |                    13 | B.2               |                              43 | 0.0368           |
| UK247          | Apr-04, May-27 |                    13 | B.1.1             |                               6 | 0.7361           |
| UK45           | Mar-02, Apr-16 |                    13 | B.1.1             |                              47 | 0.0563           |
| UK148          | Apr-02, May-13 |                    12 | B.1.1             |                              20 | 0.1864           |
| UK806          | Apr-04, May-08 |                    12 | B.1.1.10          |                              25 | 0.1236           |
| UK694          | Mar-06, Mar-14 |                    12 | B                 |                              80 | 0.0091           |
| UK186          | Apr-08, May-15 |                    12 | B                 |                              18 | 0.2269           |
| UK347          | Mar-13, Apr-02 |                    12 | B.1               |                              61 | 0.0298           |
| UK111          | Mar-25, May-18 |                    12 | B.1.1             |                              15 | 0.3273           |
| UK604          | Mar-09, Mar-17 |                    12 | B.1.1             |                              77 | 0.0089           |
| UK71           | Mar-08, Apr-30 |                    12 | B                 |                              33 | 0.1338           |
| UK269          | Apr-04, May-06 |                    12 | B.1.1             |                              27 | 0.0784           |
| UK266          | Apr-06, Apr-30 |                    12 | B.1               |                              33 | 0.0661           |
| UK5505         | Mar-29, May-01 |                    12 | B.1               |                              32 | 0.0938           |
| UK689          | Mar-05, Apr-07 |                    12 | B.2, B.2.1        |                              56 | 0.0491           |
| UK47           | Mar-17, May-18 |                    12 | B.1.1             |                              15 | 0.2431           |
| UK180          | Mar-30, May-01 |                    11 | B.1.1             |                              32 | 0.0909           |
| UK5703         | Mar-06, Apr-15 |                    11 | B.2, B.1.1        |                              48 | 0.0758           |
| UK5409         | Mar-27, Apr-19 |                    11 | B.1.1             |                              44 | 0.0523           |
| UK759          | Mar-28, Apr-27 |                    11 | B.1.1             |                              36 | 0.0694           |
| UK329          | Apr-11, May-09 |                    11 | B.1.1             |                              24 | 0.1736           |
| UK54           | Mar-18, Apr-30 |                    11 | B.1.1.10          |                              33 | 0.1303           |
| UK368          | Mar-18, May-01 |                    11 | B.1               |                              32 | 0.1375           |
| UK415          | Apr-19, May-06 |                    11 | B.1               |                              27 | 0.063            |
| UK441          | Apr-04, May-01 |                    11 | B.1.1             |                              32 | 0.0649           |
| UK428          | Mar-20, Apr-06 |                    11 | B.2, B.2.1        |                              57 | 0.0298           |
| UK240          | Mar-16, Apr-11 |                    11 | B.2               |                              52 | 0.05             |
| UK511          | Apr-05, May-06 |                    11 | B.1.1             |                              27 | 0.1148           |
| UK5339         | Apr-15, Apr-29 |                    11 | B.1.1             |                              34 | 0.0412           |
| UK1018         | Apr-20, Apr-21 |                    11 | B.1.1             |                              42 | 0.0024           |
| UK251          | Mar-17, May-02 |                    11 | B.1.1             |                              31 | 0.1349           |
| UK141          | Mar-22, Apr-24 |                    11 | B.1.1             |                              39 | 0.0846           |
| UK163          | Mar-27, May-03 |                    11 | B.1.1             |                              30 | 0.0949           |
| UK132          | Mar-27, Apr-30 |                    10 | B.1               |                              33 | 0.0859           |
| UK22           | Mar-02, Apr-21 |                    10 | B                 |                              42 | 0.1323           |
| UK297          | Apr-09, May-26 |                    10 | B.1.p11           |                               7 | 0.746            |
| UK171          | Mar-13, Apr-13 |                    10 | B.2, B.2.1        |                              50 | 0.0689           |
| UK687          | Feb-28, Mar-08 |                    10 | B.2, B.2.1        |                              86 | 0.0116           |
| UK255          | Mar-26, Apr-20 |                    10 | B.1.1             |                              43 | 0.0581           |
| UK125          | Apr-22, May-20 |                    10 | B.1.1             |                              13 | 0.2393           |
| UK42           | Mar-28, May-16 |                    10 | B.1.35, B.1       |                              17 | 0.028            |
| UK123          | Mar-23, May-01 |                    10 | B.1               |                              32 | 0.1354           |
| UK38           | Mar-04, May-11 |                    10 | B.2.1             |                              22 | 0.1627           |
| UK78           | Mar-29, May-14 |                    10 | B.1.5             |                              19 | 0.269            |
| UK91           | Mar-28, May-06 |                    10 | B.1.1             |                              27 | 0.1605           |
| UK201          | Mar-29, May-13 |                    10 | B.1               |                              20 | 0.25             |
| UK2906         | Apr-08, May-22 |                    10 | B.1               |                              11 | 0.4545           |
| UK541          | Apr-01, May-20 |                    10 | B.1.1             |                              13 | 0.4188           |
| UK242          | Mar-26, Apr-20 |                    10 | B.1.5             |                              43 | 0.0646           |
| UK5543         | Mar-10, Apr-29 |                    10 | B.2.1             |                              34 | 0.1634           |
| UK161          | Mar-10, May-25 |                    10 | B.1.1             |                               8 | 0.6786           |
| UK5707         | Mar-18, Apr-16 |                     9 | B.2, B.1.1        |                              47 | 0.0617           |
| UK645          | Mar-29, Apr-08 |                     9 | B.2.1             |                              55 | 0.0227           |
| UK178          | Mar-14, Apr-13 |                     9 | B.1.1             |                              50 | 0.075            |
| UK312          | Mar-01, Mar-23 |                     9 | B.1.1             |                              71 | 0.0387           |
| UK49           | Mar-19, Jun-02 |                     9 | B.2.1             |                               0 | active today     |
| UK168          | Mar-16, Apr-16 |                     9 | B.2.1             |                              47 | 0.0824           |
| UK311          | Mar-20, Apr-11 |                     9 | B.1.1             |                              52 | 0.0529           |
| UK802          | Mar-21, Apr-22 |                     9 | B.1               |                              41 | 0.0976           |
| UK564          | Apr-03, May-02 |                     9 | B.1.1             |                              31 | 0.1169           |
| UK203          | Apr-01, May-17 |                     9 | B.1.1             |                              16 | 0.2448           |
| UK913          | Apr-03, May-04 |                     9 | B.1               |                              29 | 0.1336           |
| UK5423         | Apr-23, May-04 |                     9 | B.1.1             |                              29 | 0.1073           |
| UK432          | Mar-24, Apr-09 |                     9 | B.3               |                              54 | 0.037            |
| UK237          | Mar-31, May-16 |                     9 | B.1.1             |                              17 | 0.3382           |
| UK5338         | Apr-29, May-02 |                     9 | B.1.1             |                              31 | 0.0121           |
| UK5685         | Mar-17, May-03 |                     9 | B.2               |                              30 | 0.1306           |
| UK5308         | Apr-29, May-01 |                     9 | B.1.1             |                              32 | 0.0078           |
| UK3875         | Apr-08, May-12 |                     8 | B.1.1             |                              21 | 0.2313           |
| UK733          | Mar-10, Apr-22 |                     8 | B.2.1             |                              41 | 0.1498           |
| UK244          | Mar-12, Apr-30 |                     8 | B.1.1             |                              33 | 0.1856           |
| UK318          | Mar-20, Apr-10 |                     8 | B                 |                              53 | 0.0566           |
| UK1013         | Apr-15, Apr-16 |                     8 | B.1.1             |                              47 | 0.003            |
| UK5178         | Mar-21, Apr-17 |                     8 | B.1.1.7           |                              46 | 0.0839           |
| UK306          | Mar-26, Apr-10 |                     8 | B.1.1             |                              53 | 0.0354           |
| UK252          | Apr-04, Apr-29 |                     8 | B.1.1             |                              34 | 0.105            |
| UK5307         | Mar-10, May-12 |                     8 | B.1.1             |                              21 | 0.3869           |
| UK335          | Mar-25, Apr-15 |                     8 | B.2.1             |                              48 | 0.0625           |
| UK70           | Mar-06, Apr-16 |                     8 | B.2               |                              47 | 0.0872           |
| UK2918         | Mar-02, Apr-27 |                     8 | B.1               |                              36 | 0.1111           |
| UK83           | Feb-29, Apr-08 |                     8 | B.1.1             |                              55 | 0.0709           |
| UK341          | Mar-23, Apr-12 |                     8 | B.1               |                              51 | 0.056            |
| UK193          | Apr-08, May-13 |                     8 | B.1.1             |                              20 | 0.0913           |
| UK756          | Feb-27, Mar-05 |                     8 | B.1.1             |                              89 | 0.0112           |
| UK739          | Mar-01, Mar-08 |                     8 | B.4               |                              86 | 0.0116           |
| UK5563         | Apr-11, Apr-22 |                     8 | B.2.2             |                              41 | 0.0383           |
| UK142          | Mar-15, Apr-01 |                     8 | B.2.1             |                              62 | 0.0392           |
| UK220          | Mar-27, Apr-11 |                     8 | B.1.1             |                              52 | 0.0412           |
| UK788          | Feb-28, Mar-05 |                     8 | B.4               |                              89 | 0.0096           |
| UK5557         | Mar-11, May-13 |                     8 | B.2.2             |                              20 | 0.35             |
| UK532          | Apr-04, Apr-17 |                     8 | B.1.1             |                              46 | 0.0404           |
| UK574          | Mar-30, Apr-29 |                     8 | B.1.1             |                              34 | 0.1261           |
| UK287          | Mar-28, Apr-18 |                     8 | B.1               |                              45 | 0.0511           |
| UK480          | Apr-02, May-27 |                     8 | B.1.1             |                               6 | 1.3095           |
| UK223          | Mar-10, Apr-06 |                     8 | B.2.1             |                              57 | 0.0677           |
| UK232          | Mar-04, Mar-30 |                     7 | B.1.1             |                              64 | 0.0677           |
| UK510          | Apr-02, Apr-16 |                     7 | B.1.1             |                              47 | 0.0496           |
| UK634          | Mar-30, Apr-18 |                     7 | B.1.1             |                              45 | 0.0704           |
| UK372          | Apr-16, May-13 |                     7 | B.1.1             |                              20 | 0.225            |
| UK65           | Mar-07, Apr-17 |                     7 | B.1.1             |                              46 | 0.1273           |
| UK280          | Mar-31, May-06 |                     7 | B.1.1             |                              27 | 0.2222           |
| UK540          | Apr-09, Apr-22 |                     7 | B.1.1.p15, B.1.1  |                              41 | 0.0528           |
| UK15           | Mar-06, May-06 |                     7 | B.1.1             |                              27 | 0.2259           |
| UK3323         | Mar-26, Apr-28 |                     7 | B.1.1             |                              35 | 0.1571           |
| UK534          | Apr-13, May-13 |                     7 | B.1.1             |                              20 | 0.2143           |
| UK5523         | May-01, May-23 |                     7 | B.1               |                              10 | 0.3667           |
| UK487          | Mar-24, Apr-08 |                     7 | B.1.1             |                              55 | 0.039            |
| UK629          | Mar-23, Apr-13 |                     7 | B.1               |                              50 | 0.07             |
| UK5300         | Apr-17, May-06 |                     7 | B.1.1             |                              27 | 0.1173           |
| UK129          | Mar-23, Apr-29 |                     7 | B.1.1             |                              34 | 0.1555           |
| UK5261         | Mar-29, May-01 |                     7 | B.1.1             |                              32 | 0.1473           |
| UK692          | Mar-04, Apr-03 |                     7 | B, B.2, B.2.1     |                              60 | 0.0833           |
| UK206          | Mar-22, Apr-19 |                     7 | B.2.1             |                              44 | 0.1061           |
| UK268          | Mar-23, Apr-16 |                     7 | B.1.1             |                              47 | 0.0511           |
| UK317          | Mar-26, Apr-16 |                     7 | B.3               |                              47 | 0.0745           |
| UK390          | Mar-27, May-01 |                     7 | B.1.5             |                              32 | 0.1823           |
| UK352          | Apr-11, May-03 |                     7 | B.1.1             |                              30 | 0.1222           |
| UK2258         | Mar-23, May-07 |                     7 | B.1               |                              26 | 0.2885           |
| UK5708         | Mar-30, May-01 |                     7 | B.1.1             |                              32 | 0.1429           |
| UK69           | Mar-04, Apr-14 |                     7 | B.2.1             |                              49 | 0.1195           |
| UK5177         | Mar-27, Apr-11 |                     7 | B.1.1.7           |                              52 | 0.0481           |
| UK289          | Mar-25, Apr-16 |                     7 | B.2.1             |                              47 | 0.078            |
| UK5174         | Mar-26, Apr-07 |                     7 | B.1.1.7           |                              56 | 0.0306           |
| UK309          | Apr-01, May-17 |                     7 | B.1.1             |                              16 | 0.4792           |
| UK182          | Apr-03, May-02 |                     7 | B.1.1             |                              31 | 0.1559           |
| UK1006         | Apr-04, Apr-29 |                     7 | B.1.1             |                              34 | 0.1225           |
| UK213          | Mar-18, Apr-17 |                     7 | B.1.1             |                              46 | 0.1087           |
| UK654          | Feb-27, Mar-08 |                     6 | B.2.5             |                              86 | 0.0233           |
| UK542          | Apr-01, Apr-14 |                     6 | B.1               |                              49 | 0.0531           |
| UK5581         | Mar-11, Apr-08 |                     6 | B.2.2             |                              55 | 0.1018           |
| UK196          | Mar-18, Apr-17 |                     6 | B.2.1             |                              46 | 0.1304           |
| UK647          | Mar-21, Mar-27 |                     6 | B.2, B.2.1        |                              67 | 0.0249           |
| UK110          | Mar-24, Apr-29 |                     6 | B.1               |                              34 | 0.2118           |
| UK1244         | May-01, May-11 |                     6 | B.1.1             |                              22 | 0.0909           |
| UK544          | Mar-24, Apr-06 |                     6 | B.2.1             |                              57 | 0.0456           |
| UK5780         | Mar-14, Mar-29 |                     6 | B.2, B.2.1        |                              65 | 0.0462           |
| UK5666         | Mar-13, May-10 |                     6 | B.2               |                              23 | 0.4203           |
| UK520          | Mar-14, Mar-28 |                     6 | B.2, B.2.1        |                              66 | 0.0424           |
| UK58           | Mar-17, Apr-24 |                     6 | B.1               |                              39 | 0.0689           |
| UK793          | Apr-08, May-21 |                     6 | B.1, B.1.5        |                              12 | 0.7167           |
| UK799          | Mar-01, Mar-07 |                     6 | B.1               |                              87 | 0.0138           |
| UK5297         | Mar-30, Apr-04 |                     6 | B.1.1             |                              59 | 0.0169           |
| UK5743         | Mar-21, Apr-06 |                     6 | B.2, B.1          |                              57 | 0.0561           |
| UK5903         | Mar-25, Apr-18 |                     6 | B.2               |                              45 | 0.1067           |
| UK5486         | May-01, May-28 |                     6 | B.2               |                               5 | 1.08             |
| UK673          | Mar-28, May-18 |                     6 | B.1.1             |                              15 | 0.68             |
| UK435          | Apr-03, Apr-23 |                     6 | B.1.5             |                              40 | 0.1              |
| UK413          | Mar-06, Apr-03 |                     6 | B                 |                              60 | 0.0933           |
| UK746          | Mar-31, Apr-14 |                     6 | B.1.5             |                              49 | 0.0571           |
| UK331          | Mar-31, May-01 |                     6 | B.1.1             |                              32 | 0.1938           |
| UK40           | Mar-31, May-12 |                     6 | B.16              |                              21 | 0.0201           |
| UK394          | Mar-20, May-24 |                     6 | B.1.1             |                               9 | 0.2698           |
| UK330          | Mar-23, Apr-13 |                     6 | B.1.1             |                              50 | 0.084            |
| UK488          | Mar-31, Apr-15 |                     6 | B.1               |                              48 | 0.0625           |
| UK1344         | Apr-20, May-08 |                     6 | B                 |                              25 | 0.144            |
| UK517          | Mar-29, Apr-12 |                     6 | B.1.1             |                              51 | 0.0549           |
| UK1023         | Apr-07, Apr-16 |                     6 | B.1.1             |                              47 | 0.0383           |
| UK5648         | Mar-08, May-19 |                     6 | B.2, B.1.1        |                              14 | 1.0286           |
| UK570          | Apr-05, Apr-17 |                     6 | B.1.1             |                              46 | 0.0522           |
| UK566          | Apr-03, Apr-15 |                     6 | B.1.1.10          |                              48 | 0.05             |
| UK481          | Mar-30, Apr-14 |                     6 | B.1.1             |                              49 | 0.0612           |
| UK157          | Apr-11, Jun-02 |                     6 | B.1               |                               0 | active today     |
| UK313          | Mar-23, Apr-14 |                     6 | B.1.1             |                              49 | 0.0898           |
| UK102          | Mar-10, Apr-16 |                     6 | B.1               |                              47 | 0.1574           |
| UK68           | Mar-20, Apr-30 |                     6 | B.1.1             |                              33 | 0.2485           |
| UK755          | Mar-06, May-21 |                     6 | B.1.1             |                              12 | 1.2667           |
| UK5650         | Mar-08, May-22 |                     6 | B.2.6, B.1.1      |                              11 | 1.3636           |
| UK443          | Mar-31, May-14 |                     6 | B.1.1             |                              19 | 0.4632           |
| UK512          | Mar-30, Apr-13 |                     6 | B.1.1             |                              50 | 0.056            |
| UK284          | Apr-02, Apr-25 |                     6 | B.1.1             |                              38 | 0.1211           |
| UK447          | Apr-05, Apr-21 |                     6 | B.1.1             |                              42 | 0.0762           |
| UK27           | Mar-08, Apr-26 |                     6 | B.1.1             |                              37 | 0.2649           |
| UK4237         | Apr-15, Apr-15 |                     6 | B.1.1             |                              48 | 0.0              |
| UK659          | Mar-21, Mar-30 |                     6 | B                 |                              64 | 0.0281           |
| UK489          | Mar-23, Apr-07 |                     6 | B.2.1             |                              56 | 0.0536           |
| UK4399         | Mar-08, Apr-16 |                     6 | B.1.1             |                              47 | 0.1383           |
| UK670          | Mar-28, May-07 |                     6 | B.1.1             |                              26 | 0.2564           |
| UK3126         | Apr-06, May-04 |                     6 | B.1.1             |                              29 | 0.1931           |
| UK202          | Mar-10, May-05 |                     6 | B.1.1             |                              28 | 0.1538           |
| UK263          | Mar-20, Apr-13 |                     6 | B.1.p11           |                              50 | 0.096            |
| UK16           | Apr-16, May-06 |                     6 | B.1.1             |                              27 | 0.1481           |
| UK188          | Mar-07, Apr-08 |                     6 | B.1               |                              55 | 0.0727           |
| UK682          | Mar-21, Mar-31 |                     6 | B.2, B.2.1        |                              63 | 0.0265           |
| UK440          | Mar-28, Apr-13 |                     6 | B.1.1.10          |                              50 | 0.064            |
| UK680          | Apr-05, Apr-14 |                     6 | B.1               |                              49 | 0.0367           |
| UK857          | Mar-24, Mar-29 |                     6 | B.2.1             |                              65 | 0.0154           |

\pagebreak

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre


|    | Centre   |   Lag in days |
|---:|:---------|--------------:|
|  0 | NOTT     |             3 |
|  1 | CAMB     |             6 |
|  2 | PORT     |            11 |
|  3 | SANG     |            11 |
|  4 | BIRM     |            12 |
|  5 | SHEF     |            14 |
|  6 | NORW     |            15 |
|  7 | PHEC     |            17 |
|  8 | LIVE     |            21 |
|  9 | LOND     |            22 |
| 10 | NORT     |            22 |
| 11 | EXET     |            23 |
| 12 | OXON     |            52 |

\pagebreak

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK2464 |   UK2916 |   UK9 |   UK4 |   UK2913 |   UK6 |   UK19 |   UK36 |   UK177 |
|:------------------|------:|---------:|---------:|------:|------:|---------:|------:|-------:|-------:|--------:|
| 2020-02-02        |     0 |        0 |        2 |     0 |     0 |        0 |     0 |      0 |      0 |       0 |
| 2020-02-09        |     0 |        0 |        1 |     0 |     0 |        0 |     0 |      0 |      0 |       0 |
| 2020-02-23        |     0 |        0 |       10 |     0 |     1 |        0 |     0 |      0 |      0 |       0 |
| 2020-03-01        |     3 |        0 |       14 |     0 |     7 |        0 |     0 |      0 |      0 |       0 |
| 2020-03-08        |    13 |        3 |        8 |     2 |     5 |        2 |     0 |      2 |      0 |       0 |
| 2020-03-15        |    11 |        7 |        9 |     4 |     7 |        3 |     2 |      3 |      1 |       0 |
| 2020-03-22        |    16 |       10 |        8 |     7 |    14 |        8 |     1 |      5 |      2 |       1 |
| 2020-03-29        |    21 |       14 |       10 |    13 |    12 |        8 |     5 |      6 |      6 |       5 |
| 2020-04-05        |    23 |       14 |       11 |    10 |     6 |        9 |     5 |      8 |      4 |       8 |
| 2020-04-12        |    21 |        9 |       10 |     8 |     3 |        6 |     5 |      4 |      6 |       6 |
| 2020-04-19        |    17 |        7 |        5 |     1 |     2 |        2 |     6 |      4 |      3 |       2 |
| 2020-04-26        |    22 |        7 |        4 |     2 |     1 |        3 |     5 |      3 |      2 |       5 |
| 2020-05-03        |    12 |        4 |        2 |     1 |     0 |        0 |     3 |      1 |      2 |       3 |
| 2020-05-10        |    11 |        2 |        1 |     1 |     0 |        0 |     1 |      1 |      3 |       1 |
| 2020-05-17        |    12 |        1 |        0 |     0 |     1 |        0 |     0 |      0 |      1 |       0 |
| 2020-05-24        |     6 |        1 |        0 |     0 |     0 |        0 |     0 |      0 |      0 |       0 |
| 2020-05-31        |     1 |        0 |        0 |     0 |     0 |        0 |     0 |      0 |      0 |       0 |

\pagebreak


Table S4 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
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
| 2020-02-27 |                            6 |                                2 |       8 |
| 2020-02-28 |                            4 |                                6 |      10 |
| 2020-02-29 |                            9 |                                1 |      10 |
| 2020-03-01 |                           13 |                               10 |      23 |
| 2020-03-02 |                           35 |                               10 |      45 |
| 2020-03-03 |                           30 |                               14 |      44 |
| 2020-03-04 |                           32 |                               17 |      49 |
| 2020-03-05 |                           35 |                               12 |      47 |
| 2020-03-06 |                           30 |                               22 |      52 |
| 2020-03-07 |                           18 |                                6 |      24 |
| 2020-03-08 |                           24 |                               12 |      36 |
| 2020-03-09 |                           34 |                               14 |      48 |
| 2020-03-10 |                           40 |                               28 |      68 |
| 2020-03-11 |                           65 |                               34 |      99 |
| 2020-03-12 |                           83 |                               38 |     121 |
| 2020-03-13 |                           36 |                               27 |      63 |
| 2020-03-14 |                           33 |                               21 |      54 |
| 2020-03-15 |                           25 |                               17 |      42 |
| 2020-03-16 |                           29 |                               19 |      48 |
| 2020-03-17 |                           32 |                               30 |      62 |
| 2020-03-18 |                           60 |                               44 |     104 |
| 2020-03-19 |                           50 |                               29 |      79 |
| 2020-03-20 |                           61 |                               42 |     103 |
| 2020-03-21 |                           62 |                               35 |      97 |
| 2020-03-22 |                           67 |                               26 |      93 |
| 2020-03-23 |                          110 |                               47 |     157 |
| 2020-03-24 |                          108 |                               29 |     137 |
| 2020-03-25 |                           93 |                               36 |     129 |
| 2020-03-26 |                           89 |                               45 |     134 |
| 2020-03-27 |                           91 |                               40 |     131 |
| 2020-03-28 |                           97 |                               39 |     136 |
| 2020-03-29 |                          101 |                               40 |     141 |
| 2020-03-30 |                          136 |                               49 |     185 |
| 2020-03-31 |                          117 |                               48 |     165 |
| 2020-04-01 |                          112 |                               32 |     144 |
| 2020-04-02 |                          117 |                               38 |     155 |
| 2020-04-03 |                          105 |                               29 |     134 |
| 2020-04-04 |                           82 |                               31 |     113 |
| 2020-04-05 |                           89 |                               18 |     107 |
| 2020-04-06 |                          112 |                               21 |     133 |
| 2020-04-07 |                           95 |                               19 |     114 |
| 2020-04-08 |                           71 |                               22 |      93 |
| 2020-04-09 |                           55 |                               12 |      67 |
| 2020-04-10 |                           66 |                                9 |      75 |
| 2020-04-11 |                           45 |                               13 |      58 |
| 2020-04-12 |                           37 |                                6 |      43 |
| 2020-04-13 |                           34 |                                9 |      43 |
| 2020-04-14 |                           48 |                               14 |      62 |
| 2020-04-15 |                           47 |                               12 |      59 |
| 2020-04-16 |                           45 |                               10 |      55 |
| 2020-04-17 |                           44 |                                9 |      53 |
| 2020-04-18 |                           17 |                                7 |      24 |
| 2020-04-19 |                           21 |                                4 |      25 |
| 2020-04-20 |                           20 |                                5 |      25 |
| 2020-04-21 |                           19 |                                1 |      20 |
| 2020-04-22 |                            6 |                                7 |      13 |
| 2020-04-23 |                            9 |                                0 |       9 |
| 2020-04-24 |                            6 |                                1 |       7 |
| 2020-04-25 |                            7 |                                1 |       8 |
| 2020-04-26 |                            6 |                                1 |       7 |
| 2020-04-27 |                           10 |                                4 |      14 |
| 2020-04-28 |                            8 |                                2 |      10 |
| 2020-04-29 |                           15 |                                5 |      20 |
| 2020-04-30 |                           12 |                                4 |      16 |
| 2020-05-01 |                           22 |                                7 |      29 |
| 2020-05-02 |                            5 |                                2 |       7 |
| 2020-05-03 |                            6 |                                0 |       6 |
| 2020-05-04 |                           12 |                                2 |      14 |
| 2020-05-05 |                            9 |                                0 |       9 |
| 2020-05-06 |                            8 |                                1 |       9 |
| 2020-05-07 |                            4 |                                2 |       6 |
| 2020-05-08 |                            3 |                                0 |       3 |
| 2020-05-09 |                            1 |                                0 |       1 |
| 2020-05-10 |                            3 |                                1 |       4 |
| 2020-05-11 |                            5 |                                1 |       6 |
| 2020-05-13 |                            0 |                                1 |       1 |
| 2020-05-14 |                            2 |                                2 |       4 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            1 |                                0 |       1 |
| 2020-05-18 |                            2 |                                0 |       2 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-05-21 |                            1 |                                0 |       1 |

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
| 2020-03-19 |       142 |
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
| 2020-03-30 |       482 |
| 2020-03-31 |       441 |
| 2020-04-01 |       401 |
| 2020-04-02 |       414 |
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
| 2020-04-16 |       286 |
| 2020-04-17 |       219 |
| 2020-04-18 |       137 |
| 2020-04-19 |       155 |
| 2020-04-20 |       153 |
| 2020-04-21 |       113 |
| 2020-04-22 |       122 |
| 2020-04-23 |        86 |
| 2020-04-24 |        49 |
| 2020-04-25 |        50 |
| 2020-04-26 |        80 |
| 2020-04-27 |       125 |
| 2020-04-28 |       102 |
| 2020-04-29 |       190 |
| 2020-04-30 |       170 |
| 2020-05-01 |       205 |
| 2020-05-02 |       106 |
| 2020-05-03 |        68 |
| 2020-05-04 |       115 |
| 2020-05-05 |        75 |
| 2020-05-06 |        86 |
| 2020-05-07 |        87 |
| 2020-05-08 |        44 |
| 2020-05-09 |        43 |
| 2020-05-10 |        41 |
| 2020-05-11 |        82 |
| 2020-05-12 |        56 |
| 2020-05-13 |        49 |
| 2020-05-14 |        31 |
| 2020-05-15 |        22 |
| 2020-05-16 |        15 |
| 2020-05-17 |        14 |
| 2020-05-18 |        44 |
| 2020-05-19 |        42 |
| 2020-05-20 |        28 |
| 2020-05-21 |        32 |
| 2020-05-22 |        26 |
| 2020-05-23 |        11 |
| 2020-05-24 |         9 |
| 2020-05-25 |        13 |
| 2020-05-26 |        11 |
| 2020-05-27 |         9 |
| 2020-05-28 |        11 |
| 2020-05-29 |         4 |
| 2020-05-30 |         5 |
| 2020-05-31 |         4 |
| 2020-06-01 |         3 |
| 2020-06-02 |         5 |

\pagebreak

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                       | Country   |   Number of sequences | Sequence group   |
|:-----------------------------|:----------|----------------------:|:-----------------|
| BATH AND NORTH EAST SOMERSET | England   |                     0 | 0                |
| BEDFORDSHIRE                 | England   |                   418 | 400-500          |
| BERKSHIRE                    | England   |                     8 | 1-10             |
| BLACKBURN WITH DARWEN        | England   |                     0 | 0                |
| BLACKPOOL                    | England   |                     0 | 0                |
| BOLTON                       | England   |                     0 | 0                |
| BOURNEMOUTH                  | England   |                     0 | 0                |
| BRIGHTON AND HOVE            | England   |                     0 | 0                |
| BRISTOL                      | England   |                    18 | 10-50            |
| BUCKINGHAMSHIRE              | England   |                   349 | 300-400          |
| BURY                         | England   |                     0 | 0                |
| CAMBRIDGESHIRE               | England   |                   668 | >500             |
| CENTRAL BEDFORDSHIRE         | England   |                     0 | 0                |
| CHESHIRE                     | England   |                    12 | 10-50            |
| CORNWALL                     | England   |                    20 | 10-50            |
| CUMBRIA                      | England   |                    32 | 10-50            |
| DARLINGTON                   | England   |                     0 | 0                |
| DERBY                        | England   |                     0 | 0                |
| DERBYSHIRE                   | England   |                    25 | 10-50            |
| DEVON                        | England   |                   283 | 250-300          |
| DORSET                       | England   |                   159 | 150-200          |
| DURHAM                       | England   |                     6 | 1-10             |
| EAST RIDING OF YORKSHIRE     | England   |                    33 | 10-50            |
| ESSEX                        | England   |                  1209 | >500             |
| GATESHEAD                    | England   |                     0 | 0                |
| GLOUCESTERSHIRE              | England   |                   456 | 400-500          |
| GREATER LONDON               | England   |                  2312 | >500             |
| HALTON                       | England   |                     0 | 0                |
| HAMPSHIRE                    | England   |                   122 | 100-150          |
| HARTLEPOOL                   | England   |                     0 | 0                |
| HEREFORDSHIRE                | England   |                     4 | 1-10             |
| HERTFORDSHIRE                | England   |                   933 | >500             |
| ISLE OF WIGHT                | England   |                     0 | 0                |
| ISLES OF SCILLY              | England   |                     0 | 0                |
| KENT                         | England   |                    29 | 10-50            |
| KINGSTON UPON HULL           | England   |                     0 | 0                |
| LANCASHIRE                   | England   |                     8 | 1-10             |
| LEICESTER                    | England   |                     0 | 0                |
| LEICESTERSHIRE               | England   |                     5 | 1-10             |
| LINCOLNSHIRE                 | England   |                    16 | 10-50            |
| LUTON                        | England   |                     0 | 0                |
| MANCHESTER                   | England   |                    30 | 10-50            |
| MEDWAY                       | England   |                     0 | 0                |
| MERSEYSIDE                   | England   |                    59 | 50-100           |
| MIDDLESBROUGH                | England   |                     0 | 0                |
| MILTON KEYNES                | England   |                     0 | 0                |
| NORFOLK                      | England   |                   559 | >500             |
| NORTH LINCOLNSHIRE           | England   |                     0 | 0                |
| NORTH SOMERSET               | England   |                     0 | 0                |
| NORTH YORKSHIRE              | England   |                    63 | 50-100           |
| NORTHAMPTONSHIRE             | England   |                    22 | 10-50            |
| NORTHUMBERLAND               | England   |                     4 | 1-10             |
| NOTTINGHAM                   | England   |                   634 | >500             |
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
| SOMERSET                     | England   |                   356 | 300-400          |
| SOUTH GLOUCESTERSHIRE        | England   |                     0 | 0                |
| SOUTH YORKSHIRE              | England   |                  1250 | >500             |
| SOUTHAMPTON                  | England   |                     0 | 0                |
| SOUTHEND-ON-SEA              | England   |                     0 | 0                |
| STAFFORDSHIRE                | England   |                    49 | 10-50            |
| STOCKPORT                    | England   |                     0 | 0                |
| STOCKTON-ON-TEES             | England   |                     0 | 0                |
| STOKE-ON-TRENT               | England   |                     0 | 0                |
| SUFFOLK                      | England   |                   503 | >500             |
| SURREY                       | England   |                    64 | 50-100           |
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
| WEST MIDLANDS                | England   |                    95 | 50-100           |
| WEST YORKSHIRE               | England   |                    20 | 10-50            |
| WIGAN                        | England   |                     0 | 0                |
| WILTSHIRE                    | England   |                   245 | 200-250          |
| WORCESTERSHIRE               | England   |                    12 | 10-50            |
| YORK                         | England   |                     0 | 0                |

\pagebreak






