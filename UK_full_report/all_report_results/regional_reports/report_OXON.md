







# Lineages report for OXON




This report gives summaries of UK specific lineages sequenced by OXON for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-06-10. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1259 sequences in the UK from the sequencing centre OXON have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6 and the maximum is 672


Sequences which were replicates or too error-prone were removed from this analysis.



161 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 8 that remain:
4 are pending extinction, ie last seen three weeks ago.
4 lineages have reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+------------------+----------+
| Lineage name   | England      | Date range     | Global lineage   | Total    |
+================+==============+================+==================+==========+
| UK5            | 340 (100.0%) | Mar-19, May-15 | B.1.1, B.1.1.10  | 340 taxa |
+----------------+--------------+----------------+------------------+----------+
| UK2039         | 127 (100.0%) | Mar-13, Jun-07 | B.1.1            | 127 taxa |
+----------------+--------------+----------------+------------------+----------+
| UK1951         | 44 (100.0%)  | Mar-21, May-07 | B.1.1.1, B.1.1   | 44 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1542         | 41 (100.0%)  | Mar-27, Apr-20 | B.1.1            | 41 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1278         | 33 (100.0%)  | Mar-23, Jun-05 | B.1.1            | 33 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1717         | 30 (100.0%)  | Apr-07, May-25 | B.1.1            | 30 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK175          | 27 (100.0%)  | Mar-30, May-01 | B.1              | 27 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK902          | 23 (100.0%)  | Apr-04, May-03 | B.1.1            | 23 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK109          | 23 (100.0%)  | Mar-20, May-06 | B.1.99, B.1      | 23 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK107          | 21 (100.0%)  | Mar-24, Apr-18 | B.2, B.2.1       | 21 taxa  |
+----------------+--------------+----------------+------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_OXON_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_OXON_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_OXON_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by OXON is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_OXON_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_OXON_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 847 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_OXON_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+------------------+----------+
| Lineage name   | England      | Date range     | Global lineage   | Total    |
+================+==============+================+==================+==========+
| UK5            | 340 (100.0%) | Mar-19, May-15 | B.1.1, B.1.1.10  | 340 taxa |
+----------------+--------------+----------------+------------------+----------+
| UK2039         | 127 (100.0%) | Mar-13, Jun-07 | B.1.1            | 127 taxa |
+----------------+--------------+----------------+------------------+----------+
| UK1951         | 44 (100.0%)  | Mar-21, May-07 | B.1.1.1, B.1.1   | 44 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1542         | 41 (100.0%)  | Mar-27, Apr-20 | B.1.1            | 41 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1278         | 33 (100.0%)  | Mar-23, Jun-05 | B.1.1            | 33 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1717         | 30 (100.0%)  | Apr-07, May-25 | B.1.1            | 30 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK175          | 27 (100.0%)  | Mar-30, May-01 | B.1              | 27 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK902          | 23 (100.0%)  | Apr-04, May-03 | B.1.1            | 23 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK109          | 23 (100.0%)  | Mar-20, May-06 | B.1.99, B.1      | 23 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK107          | 21 (100.0%)  | Mar-24, Apr-18 | B.2, B.2.1       | 21 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK315          | 18 (100.0%)  | Mar-12, Apr-15 | B.2.2            | 18 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1630         | 17 (100.0%)  | Mar-20, Apr-30 | B.1.1            | 17 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK263          | 14 (100.0%)  | Mar-13, Apr-13 | B.1              | 14 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK597          | 13 (100.0%)  | Mar-25, Apr-26 | B.1              | 13 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK9            | 13 (100.0%)  | Apr-04, May-03 | B.1.13, B.1      | 13 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1157         | 13 (100.0%)  | Apr-05, May-04 | B.1.1.7          | 13 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK2464         | 12 (100.0%)  | Apr-05, Apr-20 | B.1              | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK167          | 12 (100.0%)  | Mar-17, Apr-25 | B.1              | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK387          | 12 (100.0%)  | Mar-06, Apr-20 | B.1.21, B.1      | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK893          | 12 (100.0%)  | Apr-02, Apr-15 | B.1              | 12 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK962          | 11 (100.0%)  | Apr-02, Apr-22 | B.1.1            | 11 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK5498         | 11 (100.0%)  | Mar-09, Apr-20 | B.2              | 11 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK5741         | 11 (100.0%)  | Mar-30, May-03 | B.1              | 11 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK199          | 10 (100.0%)  | Apr-03, Apr-28 | B.1.5, B.1       | 10 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK629          | 10 (100.0%)  | Apr-01, May-24 | B.1              | 10 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK1126         | 10 (100.0%)  | Mar-25, Apr-30 | B.1.1            | 10 taxa  |
+----------------+--------------+----------------+------------------+----------+
| UK5676         | 9 (100.0%)   | Mar-17, Apr-17 | B.2              | 9 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK2913         | 9 (100.0%)   | Mar-23, May-25 | B.1.11, B.1      | 9 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK646          | 8 (100.0%)   | Apr-02, Apr-15 | B.1.1            | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK1091         | 8 (100.0%)   | Apr-07, Apr-27 | B.1.1.2, B.1.1   | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK72           | 8 (100.0%)   | Mar-22, Apr-24 | B                | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK366          | 8 (100.0%)   | Apr-11, Apr-24 | B.1              | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK1683         | 8 (100.0%)   | Mar-17, Apr-30 | B.1.1.1, B.1.1   | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK968          | 8 (100.0%)   | Apr-06, Jun-10 | B.1.1            | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK1153         | 8 (100.0%)   | Apr-05, May-01 | B.1.1            | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK600          | 8 (100.0%)   | Mar-11, Apr-08 | B.1.1, B.1       | 8 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK619          | 7 (100.0%)   | Apr-05, Apr-17 | B.1.1            | 7 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK945          | 7 (100.0%)   | Mar-25, Jun-06 | B.1.1            | 7 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK5525         | 7 (100.0%)   | Apr-16, Apr-29 | B.1              | 7 taxa   |
+----------------+--------------+----------------+------------------+----------+
| UK1037         | 6 (100.0%)   | Apr-05, May-01 | B.1.1            | 6 taxa   |
+----------------+--------------+----------------+------------------+----------+

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


| Week commencing   |   UK5 |   UK2039 |   UK1278 |   UK1717 |   UK629 |   UK2913 |   UK968 |   UK945 |
|:------------------|------:|---------:|---------:|---------:|--------:|---------:|--------:|--------:|
| 2020-03-08        |     0 |        1 |        0 |        0 |       0 |        0 |       0 |       0 |
| 2020-03-15        |     2 |        1 |        0 |        0 |       0 |        0 |       0 |       0 |
| 2020-03-22        |     3 |        1 |        1 |        0 |       0 |        1 |       0 |       1 |
| 2020-03-29        |     3 |        2 |        0 |        0 |       1 |        0 |       0 |       0 |
| 2020-04-05        |     4 |        2 |        2 |        1 |       2 |        1 |       2 |       1 |
| 2020-04-12        |     2 |        4 |        2 |        0 |       1 |        1 |       1 |       2 |
| 2020-04-19        |     3 |        3 |        2 |        0 |       0 |        1 |       1 |       0 |
| 2020-04-26        |     1 |        1 |        1 |        1 |       1 |        1 |       0 |       1 |
| 2020-05-03        |     1 |        1 |        0 |        2 |       1 |        0 |       1 |       0 |
| 2020-05-10        |     1 |        1 |        2 |        3 |       0 |        0 |       0 |       0 |
| 2020-05-17        |     0 |        1 |        1 |        3 |       0 |        0 |       0 |       0 |
| 2020-05-24        |     0 |        1 |        1 |        1 |       1 |        1 |       0 |       0 |
| 2020-05-31        |     0 |        0 |        1 |        0 |       0 |        0 |       0 |       1 |
| 2020-06-07        |     0 |        1 |        0 |        0 |       0 |        0 |       1 |       0 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-06 |                            0 |                                1 |       1 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-09 |                            0 |                                1 |       1 |
| 2020-03-10 |                            0 |                                1 |       1 |
| 2020-03-11 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                1 |       1 |
| 2020-03-13 |                            0 |                                2 |       2 |
| 2020-03-16 |                            1 |                                0 |       1 |
| 2020-03-17 |                            0 |                                3 |       3 |
| 2020-03-19 |                            1 |                                2 |       3 |
| 2020-03-20 |                            0 |                                2 |       2 |
| 2020-03-21 |                            1 |                                1 |       2 |
| 2020-03-22 |                            0 |                                1 |       1 |
| 2020-03-23 |                            6 |                                4 |      10 |
| 2020-03-24 |                            3 |                                4 |       7 |
| 2020-03-25 |                            0 |                                3 |       3 |
| 2020-03-26 |                            0 |                                1 |       1 |
| 2020-03-27 |                            0 |                                1 |       1 |
| 2020-03-28 |                            4 |                                0 |       4 |
| 2020-03-29 |                            5 |                                3 |       8 |
| 2020-03-30 |                            2 |                                3 |       5 |
| 2020-03-31 |                            1 |                                1 |       2 |
| 2020-04-01 |                            0 |                                1 |       1 |
| 2020-04-02 |                            0 |                                5 |       5 |
| 2020-04-03 |                            0 |                                4 |       4 |
| 2020-04-04 |                            7 |                                5 |      12 |
| 2020-04-05 |                            8 |                               10 |      18 |
| 2020-04-06 |                            8 |                                5 |      13 |
| 2020-04-07 |                            9 |                                7 |      16 |
| 2020-04-08 |                            6 |                                4 |      10 |
| 2020-04-09 |                            6 |                                3 |       9 |
| 2020-04-10 |                            6 |                                2 |       8 |
| 2020-04-11 |                            2 |                                1 |       3 |
| 2020-04-12 |                            2 |                                1 |       3 |
| 2020-04-13 |                            6 |                                1 |       7 |
| 2020-04-14 |                            2 |                                1 |       3 |
| 2020-04-15 |                            2 |                                0 |       2 |
| 2020-04-16 |                            4 |                                1 |       5 |
| 2020-04-17 |                            1 |                                0 |       1 |
| 2020-04-18 |                            1 |                                0 |       1 |
| 2020-04-19 |                            2 |                                1 |       3 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-21 |                            1 |                                0 |       1 |
| 2020-04-22 |                            3 |                                0 |       3 |
| 2020-04-23 |                            2 |                                0 |       2 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-04-26 |                            1 |                                0 |       1 |
| 2020-04-28 |                            2 |                                0 |       2 |
| 2020-05-02 |                            1 |                                0 |       1 |
| 2020-05-04 |                            1 |                                0 |       1 |
| 2020-05-26 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-06 |         1 |
| 2020-03-08 |         1 |
| 2020-03-09 |         1 |
| 2020-03-10 |         1 |
| 2020-03-11 |         3 |
| 2020-03-12 |         1 |
| 2020-03-13 |         3 |
| 2020-03-16 |         1 |
| 2020-03-17 |         4 |
| 2020-03-19 |         6 |
| 2020-03-20 |         7 |
| 2020-03-21 |         4 |
| 2020-03-22 |         2 |
| 2020-03-23 |        20 |
| 2020-03-24 |        19 |
| 2020-03-25 |         5 |
| 2020-03-26 |         1 |
| 2020-03-27 |        12 |
| 2020-03-28 |        11 |
| 2020-03-29 |        16 |
| 2020-03-30 |        26 |
| 2020-03-31 |        18 |
| 2020-04-01 |        12 |
| 2020-04-02 |        16 |
| 2020-04-03 |        15 |
| 2020-04-04 |        36 |
| 2020-04-05 |        79 |
| 2020-04-06 |        53 |
| 2020-04-07 |       115 |
| 2020-04-08 |        79 |
| 2020-04-09 |        52 |
| 2020-04-10 |        59 |
| 2020-04-11 |        25 |
| 2020-04-12 |        28 |
| 2020-04-13 |        48 |
| 2020-04-14 |        31 |
| 2020-04-15 |        34 |
| 2020-04-16 |        32 |
| 2020-04-17 |        40 |
| 2020-04-18 |        32 |
| 2020-04-19 |        32 |
| 2020-04-20 |        33 |
| 2020-04-21 |        24 |
| 2020-04-22 |        17 |
| 2020-04-23 |        34 |
| 2020-04-24 |        19 |
| 2020-04-25 |        15 |
| 2020-04-26 |        15 |
| 2020-04-27 |        14 |
| 2020-04-28 |        14 |
| 2020-04-29 |         4 |
| 2020-04-30 |         8 |
| 2020-05-01 |         8 |
| 2020-05-02 |         7 |
| 2020-05-03 |         8 |
| 2020-05-04 |         8 |
| 2020-05-05 |         6 |
| 2020-05-06 |         6 |
| 2020-05-07 |         2 |
| 2020-05-08 |         2 |
| 2020-05-10 |         1 |
| 2020-05-12 |         4 |
| 2020-05-14 |         3 |
| 2020-05-15 |         1 |
| 2020-05-16 |         2 |
| 2020-05-17 |         2 |
| 2020-05-18 |         1 |
| 2020-05-19 |         2 |
| 2020-05-20 |         3 |
| 2020-05-21 |         1 |
| 2020-05-22 |         2 |
| 2020-05-24 |         2 |
| 2020-05-25 |         2 |
| 2020-05-26 |         4 |
| 2020-06-05 |         1 |
| 2020-06-06 |         1 |
| 2020-06-07 |         1 |
| 2020-06-10 |         1 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country   |   Number of sequences | Sequence group   |
|:-----------------|:----------|----------------------:|:-----------------|
| BERKSHIRE        | England   |                    17 | 10-100           |
| BUCKINGHAMSHIRE  | England   |                    11 | 10-100           |
| GLOUCESTERSHIRE  | England   |                     1 | 1-10             |
| GREATER LONDON   | England   |                     1 | 1-10             |
| HAMPSHIRE        | England   |                   283 | 200-300          |
| HERTFORDSHIRE    | England   |                     2 | 1-10             |
| ISLE OF WIGHT    | England   |                     1 | 1-10             |
| NORTHAMPTONSHIRE | England   |                     1 | 1-10             |
| OXFORDSHIRE      | England   |                    87 | 10-100           |
| SOMERSET         | England   |                     1 | 1-10             |
| SURREY           | England   |                     2 | 1-10             |
| SUSSEX           | England   |                     3 | 1-10             |
| WILTSHIRE        | England   |                     2 | 1-10             |

<div style="page-break-after: always"></div>






