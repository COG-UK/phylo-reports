







# Lineages report for CAMB




This report gives summaries of UK specific lineages sequenced by CAMB for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-08-19. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1528 sequences in the UK from the sequencing centre CAMB have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 11 and the maximum is 796


Sequences which were replicates or too error-prone were removed from this analysis.



195 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 5 that remain:
2 lineages have gone quiet, ie haven't been seen this week.
3 lineages have reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+-------------------------------------+----------+
| Lineage name   | England      | Date range     | Global lineage                      | Total    |
+================+==============+================+=====================================+==========+
| UK5            | 457 (100.0%) | Mar-15, Aug-17 | B.1.1.10, B.1.1                     | 457 taxa |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1205         | 79 (100.0%)  | Mar-13, Jul-10 | B.1.1.3, B.1.1.1, B.1.1             | 79 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK175          | 76 (100.0%)  | Mar-16, Aug-12 | B.1.35, B.1.5, B.1, B.1.76, B.1.105 | 76 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK107          | 62 (100.0%)  | Mar-13, May-04 | B.2, B.2.1, B                       | 62 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1535         | 37 (100.0%)  | Mar-31, May-18 | B.1.1.3, B.1.1                      | 37 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1951         | 36 (100.0%)  | Apr-02, Jun-18 | B.1.1.1                             | 36 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5676         | 35 (100.0%)  | Mar-14, Jul-22 | B.2, B.2.9                          | 35 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1126         | 33 (100.0%)  | Mar-28, May-13 | B.1.1                               | 33 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK439          | 30 (100.0%)  | Apr-01, May-20 | B.1, B.1.66                         | 30 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2464         | 25 (100.0%)  | Mar-17, May-11 | B.1                                 | 25 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_CAMB_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


```
---------------------------------------------------------------------------NameError
Traceback (most recent call last)<ipython-input-1-2620455843ef> in
<module>
      2     lag_dict, lags = dp.sequencing_centre_lags(taxa, sc_dict,
current_date, country)
      3 elif sequencing_centre != "":
----> 4     print("The lag for this sequencing centre is " +
str(lags[sequencing_centre]) + " days")
NameError: name 'lags' is not defined
```



The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](figures/report_CAMB_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_CAMB_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by CAMB is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_CAMB_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_CAMB_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 45 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_CAMB_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+-------------------------------------+----------+
| Lineage name   | England      | Date range     | Global lineage                      | Total    |
+================+==============+================+=====================================+==========+
| UK5            | 457 (100.0%) | Mar-15, Aug-17 | B.1.1.10, B.1.1                     | 457 taxa |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1205         | 79 (100.0%)  | Mar-13, Jul-10 | B.1.1.3, B.1.1.1, B.1.1             | 79 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK175          | 76 (100.0%)  | Mar-16, Aug-12 | B.1.35, B.1.5, B.1, B.1.76, B.1.105 | 76 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK107          | 62 (100.0%)  | Mar-13, May-04 | B.2, B.2.1, B                       | 62 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1535         | 37 (100.0%)  | Mar-31, May-18 | B.1.1.3, B.1.1                      | 37 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1951         | 36 (100.0%)  | Apr-02, Jun-18 | B.1.1.1                             | 36 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5676         | 35 (100.0%)  | Mar-14, Jul-22 | B.2, B.2.9                          | 35 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1126         | 33 (100.0%)  | Mar-28, May-13 | B.1.1                               | 33 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK439          | 30 (100.0%)  | Apr-01, May-20 | B.1, B.1.66                         | 30 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2464         | 25 (100.0%)  | Mar-17, May-11 | B.1                                 | 25 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK494          | 24 (100.0%)  | Mar-20, Jun-30 | B.1.104                             | 24 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2913         | 23 (100.0%)  | Mar-29, May-31 | B.1, B.1.11                         | 23 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2916         | 21 (100.0%)  | Mar-17, May-08 | B.1                                 | 21 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK945          | 21 (100.0%)  | Mar-31, Aug-19 | B.1.1                               | 21 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1051         | 21 (100.0%)  | Apr-08, May-21 | B.1.1                               | 21 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1140         | 20 (100.0%)  | Apr-04, May-26 | B.1.1                               | 20 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK2111         | 20 (100.0%)  | Apr-14, Jul-07 | B.1.1                               | 20 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1215         | 19 (100.0%)  | Mar-28, Jun-10 | B.1.1.1, B.1.1                      | 19 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK51           | 16 (100.0%)  | Mar-31, Jul-01 | B.1, B.1.36                         | 16 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5741         | 15 (100.0%)  | Mar-17, May-22 | B.1                                 | 15 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK9            | 11 (100.0%)  | Mar-28, May-06 | B.1, B.1.13                         | 11 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1060         | 10 (100.0%)  | Mar-16, May-18 | B.1.1.10, B.1.1                     | 10 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1919         | 10 (100.0%)  | Mar-30, Apr-29 | B.1.1                               | 10 taxa  |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5503         | 9 (100.0%)   | Apr-15, Jun-12 | B.1                                 | 9 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK199          | 9 (100.0%)   | Mar-16, Jun-15 | B.1, B.1.5                          | 9 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK37           | 9 (100.0%)   | Mar-29, May-03 | B.1.30, B.1                         | 9 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK5498         | 9 (100.0%)   | Mar-18, Jun-26 | B.2                                 | 9 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK72           | 8 (100.0%)   | Mar-17, May-27 | B                                   | 8 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1617         | 8 (100.0%)   | Apr-02, Apr-22 | B.1.1                               | 8 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK274          | 8 (100.0%)   | Mar-19, May-20 | B.3                                 | 8 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK6            | 8 (100.0%)   | Mar-19, May-01 | B.1.93, B.1.75                      | 8 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1195         | 7 (100.0%)   | Aug-13, Aug-19 | B.1.1                               | 7 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1148         | 6 (100.0%)   | May-11, Aug-06 | B.1.1                               | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK174          | 6 (100.0%)   | Apr-20, May-25 | B.1, B.1.5                          | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK336          | 6 (100.0%)   | Mar-29, Apr-15 | B.1, B.1.93                         | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK678          | 6 (100.0%)   | Apr-10, May-25 | B.1.1                               | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK167          | 6 (100.0%)   | Apr-13, May-11 | B.1                                 | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK1157         | 6 (100.0%)   | Apr-09, Apr-28 | B.1.1.7                             | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK829          | 6 (100.0%)   | Mar-16, May-07 | B.2                                 | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+
| UK719          | 6 (100.0%)   | Apr-04, Jun-11 | B.1.1                               | 6 taxa   |
+----------------+--------------+----------------+-------------------------------------+----------+

<div style="page-break-after: always"></div>

**Table S2** Raw data for figure two showing lags between the most recent sequence and current date for each sequencing centre



---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-9cc5d2177dab> in <module>
      1 if not pillar2:
----> 2     lag_df = pd.DataFrame(lag_dict)
      3     print(lag_df.to_markdown())
      4 else:
      5     print("Table S2 is not appropriate for this report and so has been omitted.")
NameError: name 'lag_dict' is not defined

<div style="page-break-after: always"></div>

**Table S3** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK5 |   UK175 |   UK945 |   UK1195 |   UK1148 |
|:------------------|------:|--------:|--------:|---------:|---------:|
| 2020-03-15        |     6 |       4 |       0 |        0 |        0 |
| 2020-03-22        |     4 |       2 |       0 |        0 |        0 |
| 2020-03-29        |     7 |       6 |       1 |        0 |        0 |
| 2020-04-05        |     9 |       4 |       1 |        0 |        0 |
| 2020-04-12        |     7 |       2 |       2 |        0 |        0 |
| 2020-04-19        |     8 |       3 |       2 |        0 |        0 |
| 2020-04-26        |     7 |       4 |       2 |        0 |        0 |
| 2020-05-03        |     7 |       3 |       1 |        0 |        0 |
| 2020-05-10        |     6 |       1 |       2 |        0 |        1 |
| 2020-05-17        |     4 |       1 |       1 |        0 |        1 |
| 2020-05-24        |     4 |       1 |       1 |        0 |        0 |
| 2020-05-31        |     4 |       4 |       0 |        0 |        0 |
| 2020-06-07        |     2 |       1 |       0 |        0 |        0 |
| 2020-06-14        |     2 |       0 |       0 |        0 |        0 |
| 2020-06-21        |     2 |       1 |       0 |        0 |        0 |
| 2020-06-28        |     2 |       0 |       0 |        0 |        0 |
| 2020-07-12        |     0 |       0 |       1 |        0 |        0 |
| 2020-07-19        |     0 |       1 |       0 |        0 |        0 |
| 2020-08-02        |     0 |       0 |       0 |        0 |        1 |
| 2020-08-09        |     0 |       1 |       0 |        2 |        0 |
| 2020-08-16        |     2 |       0 |       1 |        1 |        0 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-13 |                            1 |                                2 |       3 |
| 2020-03-14 |                            0 |                                1 |       1 |
| 2020-03-15 |                            1 |                                1 |       2 |
| 2020-03-16 |                            1 |                                6 |       7 |
| 2020-03-17 |                            8 |                                6 |      14 |
| 2020-03-18 |                            9 |                                7 |      16 |
| 2020-03-19 |                            4 |                                3 |       7 |
| 2020-03-20 |                            4 |                                1 |       5 |
| 2020-03-26 |                            2 |                                3 |       5 |
| 2020-03-27 |                            1 |                                3 |       4 |
| 2020-03-28 |                            1 |                                5 |       6 |
| 2020-03-29 |                            7 |                                5 |      12 |
| 2020-03-30 |                            2 |                                1 |       3 |
| 2020-03-31 |                           11 |                               10 |      21 |
| 2020-04-01 |                            3 |                                3 |       6 |
| 2020-04-02 |                            0 |                                4 |       4 |
| 2020-04-03 |                            1 |                                0 |       1 |
| 2020-04-04 |                            3 |                                3 |       6 |
| 2020-04-05 |                            0 |                                1 |       1 |
| 2020-04-06 |                            4 |                                3 |       7 |
| 2020-04-07 |                            2 |                                1 |       3 |
| 2020-04-08 |                            4 |                                4 |       8 |
| 2020-04-09 |                            1 |                                2 |       3 |
| 2020-04-10 |                            0 |                                1 |       1 |
| 2020-04-11 |                            0 |                                2 |       2 |
| 2020-04-12 |                            2 |                                0 |       2 |
| 2020-04-13 |                            2 |                                2 |       4 |
| 2020-04-14 |                            3 |                                1 |       4 |
| 2020-04-15 |                            3 |                                2 |       5 |
| 2020-04-16 |                            1 |                                0 |       1 |
| 2020-04-17 |                            3 |                                1 |       4 |
| 2020-04-18 |                            2 |                                1 |       3 |
| 2020-04-20 |                            0 |                                1 |       1 |
| 2020-04-21 |                            6 |                                2 |       8 |
| 2020-04-22 |                            1 |                                3 |       4 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-04-26 |                            1 |                                1 |       2 |
| 2020-04-27 |                            4 |                                1 |       5 |
| 2020-04-28 |                            0 |                                2 |       2 |
| 2020-04-29 |                            0 |                                2 |       2 |
| 2020-04-30 |                            0 |                                1 |       1 |
| 2020-05-01 |                            3 |                                1 |       4 |
| 2020-05-02 |                            1 |                                0 |       1 |
| 2020-05-03 |                            1 |                                0 |       1 |
| 2020-05-04 |                            3 |                                0 |       3 |
| 2020-05-05 |                            6 |                                0 |       6 |
| 2020-05-06 |                            2 |                                1 |       3 |
| 2020-05-07 |                            1 |                                1 |       2 |
| 2020-05-10 |                            2 |                                0 |       2 |
| 2020-05-11 |                            0 |                                1 |       1 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-17 |                            1 |                                0 |       1 |
| 2020-05-18 |                            2 |                                0 |       2 |
| 2020-05-22 |                            1 |                                0 |       1 |
| 2020-05-23 |                            2 |                                0 |       2 |
| 2020-05-25 |                            0 |                                1 |       1 |
| 2020-05-26 |                            1 |                                0 |       1 |
| 2020-07-27 |                            1 |                                0 |       1 |
| 2020-07-29 |                            1 |                                0 |       1 |
| 2020-08-06 |                            1 |                                0 |       1 |
| 2020-08-13 |                            0 |                                1 |       1 |
| 2020-08-17 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-13 |         4 |
| 2020-03-14 |         2 |
| 2020-03-15 |         3 |
| 2020-03-16 |         8 |
| 2020-03-17 |        25 |
| 2020-03-18 |        29 |
| 2020-03-19 |        14 |
| 2020-03-20 |        20 |
| 2020-03-21 |         1 |
| 2020-03-22 |         2 |
| 2020-03-24 |         1 |
| 2020-03-26 |        11 |
| 2020-03-27 |        14 |
| 2020-03-28 |        16 |
| 2020-03-29 |        22 |
| 2020-03-30 |        24 |
| 2020-03-31 |        42 |
| 2020-04-01 |        27 |
| 2020-04-02 |        15 |
| 2020-04-03 |        12 |
| 2020-04-04 |        19 |
| 2020-04-05 |        32 |
| 2020-04-06 |        33 |
| 2020-04-07 |        31 |
| 2020-04-08 |        30 |
| 2020-04-09 |        21 |
| 2020-04-10 |        17 |
| 2020-04-11 |        25 |
| 2020-04-12 |        28 |
| 2020-04-13 |        27 |
| 2020-04-14 |        25 |
| 2020-04-15 |        23 |
| 2020-04-16 |        25 |
| 2020-04-17 |        32 |
| 2020-04-18 |        16 |
| 2020-04-19 |        18 |
| 2020-04-20 |        33 |
| 2020-04-21 |        35 |
| 2020-04-22 |        30 |
| 2020-04-23 |        14 |
| 2020-04-24 |        10 |
| 2020-04-25 |        17 |
| 2020-04-26 |        26 |
| 2020-04-27 |        41 |
| 2020-04-28 |        26 |
| 2020-04-29 |        25 |
| 2020-04-30 |        22 |
| 2020-05-01 |        34 |
| 2020-05-02 |        14 |
| 2020-05-03 |         7 |
| 2020-05-04 |        21 |
| 2020-05-05 |        14 |
| 2020-05-06 |        23 |
| 2020-05-07 |        31 |
| 2020-05-08 |        12 |
| 2020-05-09 |        13 |
| 2020-05-10 |         9 |
| 2020-05-11 |        50 |
| 2020-05-12 |        17 |
| 2020-05-13 |        20 |
| 2020-05-14 |        10 |
| 2020-05-15 |        11 |
| 2020-05-16 |         4 |
| 2020-05-17 |         3 |
| 2020-05-18 |        31 |
| 2020-05-19 |        26 |
| 2020-05-20 |        11 |
| 2020-05-21 |         7 |
| 2020-05-22 |        11 |
| 2020-05-23 |         5 |
| 2020-05-24 |         4 |
| 2020-05-25 |        19 |
| 2020-05-26 |        10 |
| 2020-05-27 |        10 |
| 2020-05-28 |         6 |
| 2020-05-29 |         2 |
| 2020-05-30 |         2 |
| 2020-05-31 |         5 |
| 2020-06-01 |         8 |
| 2020-06-02 |         8 |
| 2020-06-03 |         3 |
| 2020-06-04 |         6 |
| 2020-06-05 |         2 |
| 2020-06-07 |         3 |
| 2020-06-08 |         3 |
| 2020-06-09 |         1 |
| 2020-06-10 |        11 |
| 2020-06-11 |         2 |
| 2020-06-12 |         3 |
| 2020-06-13 |         2 |
| 2020-06-14 |         1 |
| 2020-06-15 |         1 |
| 2020-06-16 |         5 |
| 2020-06-17 |         4 |
| 2020-06-18 |         9 |
| 2020-06-19 |         1 |
| 2020-06-21 |         2 |
| 2020-06-22 |         2 |
| 2020-06-23 |         1 |
| 2020-06-25 |         1 |
| 2020-06-26 |         1 |
| 2020-06-29 |         3 |
| 2020-06-30 |         2 |
| 2020-07-01 |         2 |
| 2020-07-07 |         1 |
| 2020-07-10 |         1 |
| 2020-07-16 |         1 |
| 2020-07-22 |         1 |
| 2020-07-25 |         1 |
| 2020-07-27 |         1 |
| 2020-07-29 |         1 |
| 2020-08-06 |         3 |
| 2020-08-12 |         1 |
| 2020-08-13 |         6 |
| 2020-08-17 |         7 |
| 2020-08-19 |         2 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country   |   Number of sequences | Sequence group   |
|:-----------------|:----------|----------------------:|:-----------------|
| BEDFORDSHIRE     | England   |                    47 | 10-100           |
| BUCKINGHAMSHIRE  | England   |                    70 | 10-100           |
| CAMBRIDGESHIRE   | England   |                   517 | 500-600          |
| ESSEX            | England   |                   344 | 300-400          |
| GREATER LONDON   | England   |                   108 | 100-200          |
| HERTFORDSHIRE    | England   |                   214 | 200-300          |
| NORFOLK          | England   |                     6 | 1-10             |
| NORTHAMPTONSHIRE | England   |                     4 | 1-10             |
| NOTTINGHAMSHIRE  | England   |                     2 | 1-10             |
| OXFORDSHIRE      | England   |                     1 | 1-10             |
| STAFFORDSHIRE    | England   |                     1 | 1-10             |
| SUFFOLK          | England   |                   169 | 100-200          |

<div style="page-break-after: always"></div>






