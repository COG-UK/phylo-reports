







# Lineages report for GLAS




This report gives summaries of UK specific lineages sequenced by GLAS for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-08-31. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
2594 sequences in the UK from the sequencing centre GLAS have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 28 and the maximum is 670


Sequences which were replicates or too error-prone were removed from this analysis.



150 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 5 that remain:
5 lineages have reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| Lineage name   | Scotland     | England   | Date range     | Global lineage                      | Total    |
+================+==============+===========+================+=====================================+==========+
| UK175          | 533 (100.0%) | 0 (0%)    | Mar-01, Jun-20 | B.6, B.1, B.1.35, B.1.5             | 533 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK336          | 308 (100.0%) | 0 (0%)    | Mar-20, Jul-22 | B.1, B.1.93                         | 308 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK5            | 190 (100.0%) | 0 (0%)    | Feb-28, Aug-31 | B.1.1, B.1.1.10, B.1.1.13, B.1.1.14 | 190 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK40           | 181 (100.0%) | 0 (0%)    | Mar-13, Jun-23 | B.16, B                             | 181 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK39           | 144 (100.0%) | 0 (0%)    | Mar-12, May-29 | A.2                                 | 144 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK5676         | 98 (100.0%)  | 0 (0%)    | Mar-12, May-27 | B.2                                 | 98 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK191          | 83 (100.0%)  | 0 (0%)    | Mar-22, Jun-19 | B.1, B.1.77                         | 83 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2464         | 80 (100.0%)  | 0 (0%)    | Mar-19, May-22 | B.1.90, B.1.11, B.1, B.1.5          | 80 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2913         | 75 (100.0%)  | 0 (0%)    | Mar-25, May-19 | B.1.11, B.1, B.1.5                  | 75 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK100          | 53 (100.0%)  | 0 (0%)    | Apr-06, Jun-01 | B.1.101, B.1                        | 53 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_GLAS_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_GLAS_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_GLAS_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by GLAS is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_GLAS_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_GLAS_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
All sequences have been assigned clean adm2 data this week.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_GLAS_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| Lineage name   | Scotland     | England   | Date range     | Global lineage                      | Total    |
+================+==============+===========+================+=====================================+==========+
| UK175          | 533 (100.0%) | 0 (0%)    | Mar-01, Jun-20 | B.6, B.1, B.1.35, B.1.5             | 533 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK336          | 308 (100.0%) | 0 (0%)    | Mar-20, Jul-22 | B.1, B.1.93                         | 308 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK5            | 190 (100.0%) | 0 (0%)    | Feb-28, Aug-31 | B.1.1, B.1.1.10, B.1.1.13, B.1.1.14 | 190 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK40           | 181 (100.0%) | 0 (0%)    | Mar-13, Jun-23 | B.16, B                             | 181 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK39           | 144 (100.0%) | 0 (0%)    | Mar-12, May-29 | A.2                                 | 144 taxa |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK5676         | 98 (100.0%)  | 0 (0%)    | Mar-12, May-27 | B.2                                 | 98 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK191          | 83 (100.0%)  | 0 (0%)    | Mar-22, Jun-19 | B.1, B.1.77                         | 83 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2464         | 80 (100.0%)  | 0 (0%)    | Mar-19, May-22 | B.1.90, B.1.11, B.1, B.1.5          | 80 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2913         | 75 (100.0%)  | 0 (0%)    | Mar-25, May-19 | B.1.11, B.1, B.1.5                  | 75 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK100          | 53 (100.0%)  | 0 (0%)    | Apr-06, Jun-01 | B.1.101, B.1                        | 53 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK87           | 33 (100.0%)  | 0 (0%)    | Mar-13, Apr-24 | B.1, B.1.70                         | 33 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1951         | 31 (96.88%)  | 1 (3.12%) | Mar-13, Jul-13 | B.1.1.1                             | 32 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK600          | 30 (100.0%)  | 0 (0%)    | Mar-09, Apr-30 | B.1.1                               | 30 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1487         | 29 (100.0%)  | 0 (0%)    | Mar-17, Apr-26 | B.1.5                               | 29 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK407          | 27 (100.0%)  | 0 (0%)    | Aug-29, Aug-31 | B.1, B.1.79                         | 27 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK107          | 27 (100.0%)  | 0 (0%)    | Mar-09, Jun-02 | B.2.1                               | 27 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK199          | 27 (100.0%)  | 0 (0%)    | Mar-05, May-25 | B.1, B.1.5                          | 27 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1683         | 26 (100.0%)  | 0 (0%)    | Mar-16, May-21 | B.1.1, B.1.1.1                      | 26 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1684         | 21 (100.0%)  | 0 (0%)    | Mar-18, May-21 | B.1.1, B.1.1.1                      | 21 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK501          | 21 (100.0%)  | 0 (0%)    | Mar-19, Jun-18 | B.1                                 | 21 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK72           | 18 (100.0%)  | 0 (0%)    | Mar-07, Apr-24 | B                                   | 18 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK14           | 18 (100.0%)  | 0 (0%)    | Mar-14, Apr-12 | B                                   | 18 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK261          | 17 (100.0%)  | 0 (0%)    | Mar-19, Apr-15 | A.3                                 | 17 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK502          | 16 (100.0%)  | 0 (0%)    | Mar-06, Mar-20 | B.1.69                              | 16 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1332         | 15 (100.0%)  | 0 (0%)    | Mar-31, May-19 | B.1.5                               | 15 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1418         | 15 (100.0%)  | 0 (0%)    | Apr-08, Jul-09 | B.1.5                               | 15 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1040         | 14 (100.0%)  | 0 (0%)    | Mar-21, May-06 | B.1.1, B.1.1.20                     | 14 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK44           | 13 (100.0%)  | 0 (0%)    | Mar-17, Apr-13 | B                                   | 13 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK58           | 13 (100.0%)  | 0 (0%)    | Mar-12, Apr-24 | B.1                                 | 13 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1186         | 13 (100.0%)  | 0 (0%)    | Aug-24, Aug-31 | B.1, B.1.79                         | 13 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK312          | 13 (100.0%)  | 0 (0%)    | Aug-10, Aug-31 | B.1                                 | 13 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2200         | 12 (100.0%)  | 0 (0%)    | Mar-31, May-04 | B.1, B.1.5                          | 12 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK669          | 12 (100.0%)  | 0 (0%)    | Apr-15, May-21 | B.1.1                               | 12 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK120          | 11 (100.0%)  | 0 (0%)    | Mar-02, Apr-16 | B                                   | 11 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1346         | 11 (100.0%)  | 0 (0%)    | Mar-08, Apr-08 | B.1.1                               | 11 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK43           | 10 (100.0%)  | 0 (0%)    | Mar-23, Apr-22 | A.5                                 | 10 taxa  |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK719          | 9 (100.0%)   | 0 (0%)    | Mar-13, May-26 | B.1.1                               | 9 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1034         | 9 (100.0%)   | 0 (0%)    | Apr-22, May-27 | B.1.1.28                            | 9 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2022         | 8 (100.0%)   | 0 (0%)    | Aug-30, Aug-31 | B.1.1                               | 8 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK917          | 7 (100.0%)   | 0 (0%)    | Apr-06, Apr-25 | B.1.1                               | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1230         | 7 (100.0%)   | 0 (0%)    | Apr-01, May-13 | B.1.1                               | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK601          | 7 (100.0%)   | 0 (0%)    | Mar-14, Apr-01 | B.10                                | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK267          | 7 (100.0%)   | 0 (0%)    | Mar-19, May-27 | B.2                                 | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK167          | 7 (100.0%)   | 0 (0%)    | Mar-12, Apr-14 | B.1                                 | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK945          | 7 (100.0%)   | 0 (0%)    | Apr-08, Apr-17 | B.1.1                               | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1060         | 7 (100.0%)   | 0 (0%)    | Mar-13, May-07 | B.1.1                               | 7 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK2916         | 6 (100.0%)   | 0 (0%)    | Mar-03, Apr-04 | B.1                                 | 6 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK187          | 6 (100.0%)   | 0 (0%)    | Apr-04, Apr-24 | B.1                                 | 6 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+
| UK1964         | 6 (100.0%)   | 0 (0%)    | Mar-29, Jun-17 | B.1.1.14, B.1.1                     | 6 taxa   |
+----------------+--------------+-----------+----------------+-------------------------------------+----------+

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


| Week commencing   |   UK5 |   UK407 |   UK1186 |   UK312 |   UK2022 |
|:------------------|------:|--------:|---------:|--------:|---------:|
| 2020-02-23        |     1 |       0 |        0 |       0 |        0 |
| 2020-03-08        |     2 |       0 |        0 |       0 |        0 |
| 2020-03-15        |     3 |       0 |        0 |       0 |        0 |
| 2020-03-22        |     7 |       0 |        0 |       0 |        0 |
| 2020-03-29        |     5 |       0 |        0 |       0 |        0 |
| 2020-04-05        |    10 |       0 |        0 |       0 |        0 |
| 2020-04-12        |    10 |       0 |        0 |       0 |        0 |
| 2020-04-19        |     8 |       0 |        0 |       0 |        0 |
| 2020-04-26        |     5 |       0 |        0 |       0 |        0 |
| 2020-05-03        |     3 |       0 |        0 |       0 |        0 |
| 2020-05-10        |     3 |       0 |        0 |       0 |        0 |
| 2020-05-17        |     4 |       0 |        0 |       0 |        0 |
| 2020-05-24        |     4 |       0 |        0 |       0 |        0 |
| 2020-05-31        |     3 |       0 |        0 |       0 |        0 |
| 2020-06-07        |     2 |       0 |        0 |       0 |        0 |
| 2020-06-14        |     2 |       0 |        0 |       0 |        0 |
| 2020-06-21        |     1 |       0 |        0 |       0 |        0 |
| 2020-08-09        |     0 |       0 |        0 |       2 |        0 |
| 2020-08-23        |     4 |       5 |        3 |       4 |        0 |
| 2020-08-30        |     1 |       4 |        2 |       3 |        2 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-02-28 |                            0 |                                1 |       1 |
| 2020-03-01 |                            0 |                                1 |       1 |
| 2020-03-02 |                            0 |                                1 |       1 |
| 2020-03-03 |                            0 |                                2 |       2 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-06 |                            0 |                                1 |       1 |
| 2020-03-07 |                            1 |                                1 |       2 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-09 |                            1 |                                3 |       4 |
| 2020-03-10 |                            1 |                                0 |       1 |
| 2020-03-11 |                            1 |                                0 |       1 |
| 2020-03-12 |                            2 |                                7 |       9 |
| 2020-03-13 |                            3 |                                8 |      11 |
| 2020-03-14 |                            0 |                                4 |       4 |
| 2020-03-15 |                            1 |                                0 |       1 |
| 2020-03-16 |                            3 |                                1 |       4 |
| 2020-03-17 |                            4 |                                4 |       8 |
| 2020-03-18 |                            1 |                                2 |       3 |
| 2020-03-19 |                            2 |                                7 |       9 |
| 2020-03-20 |                            3 |                                3 |       6 |
| 2020-03-21 |                            3 |                                2 |       5 |
| 2020-03-22 |                            0 |                                1 |       1 |
| 2020-03-23 |                            2 |                                2 |       4 |
| 2020-03-24 |                            1 |                                0 |       1 |
| 2020-03-25 |                            3 |                                1 |       4 |
| 2020-03-26 |                            2 |                                2 |       4 |
| 2020-03-27 |                            4 |                                1 |       5 |
| 2020-03-28 |                            1 |                                0 |       1 |
| 2020-03-29 |                            4 |                                4 |       8 |
| 2020-03-30 |                            1 |                                0 |       1 |
| 2020-03-31 |                            0 |                                5 |       5 |
| 2020-04-01 |                            2 |                                2 |       4 |
| 2020-04-02 |                            1 |                                1 |       2 |
| 2020-04-03 |                            2 |                                1 |       3 |
| 2020-04-04 |                            2 |                                2 |       4 |
| 2020-04-05 |                            0 |                                1 |       1 |
| 2020-04-06 |                            1 |                                2 |       3 |
| 2020-04-07 |                            3 |                                0 |       3 |
| 2020-04-08 |                            4 |                                2 |       6 |
| 2020-04-09 |                            3 |                                1 |       4 |
| 2020-04-10 |                            1 |                                0 |       1 |
| 2020-04-11 |                            1 |                                1 |       2 |
| 2020-04-12 |                            4 |                                1 |       5 |
| 2020-04-14 |                            0 |                                1 |       1 |
| 2020-04-15 |                            2 |                                3 |       5 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            1 |                                1 |       2 |
| 2020-04-20 |                            0 |                                2 |       2 |
| 2020-04-21 |                            0 |                                2 |       2 |
| 2020-04-22 |                            1 |                                4 |       5 |
| 2020-04-23 |                            1 |                                0 |       1 |
| 2020-04-26 |                            0 |                                1 |       1 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-09 |                            1 |                                0 |       1 |
| 2020-05-12 |                            0 |                                1 |       1 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                0 |       1 |
| 2020-05-23 |                            1 |                                0 |       1 |
| 2020-05-28 |                            1 |                                0 |       1 |
| 2020-06-03 |                            1 |                                0 |       1 |
| 2020-06-10 |                            1 |                                0 |       1 |
| 2020-06-18 |                            2 |                                0 |       2 |
| 2020-07-25 |                            0 |                                1 |       1 |
| 2020-08-03 |                            1 |                                0 |       1 |
| 2020-08-09 |                            1 |                                0 |       1 |
| 2020-08-10 |                            0 |                                2 |       2 |
| 2020-08-22 |                            0 |                                1 |       1 |
| 2020-08-24 |                            0 |                                1 |       1 |
| 2020-08-25 |                            2 |                                0 |       2 |
| 2020-08-29 |                            1 |                                4 |       5 |
| 2020-08-30 |                            1 |                                3 |       4 |
| 2020-08-31 |                            0 |                                1 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Scotland |
|:-----------|----------:|-----------:|
| 2020-02-28 |         0 |          1 |
| 2020-03-01 |         0 |          1 |
| 2020-03-02 |         0 |          1 |
| 2020-03-03 |         0 |          2 |
| 2020-03-04 |         0 |          3 |
| 2020-03-05 |         0 |          2 |
| 2020-03-06 |         0 |          5 |
| 2020-03-07 |         0 |          3 |
| 2020-03-08 |         0 |          1 |
| 2020-03-09 |         0 |          8 |
| 2020-03-10 |         0 |          4 |
| 2020-03-11 |         0 |          2 |
| 2020-03-12 |         0 |         24 |
| 2020-03-13 |         0 |         41 |
| 2020-03-14 |         0 |         12 |
| 2020-03-15 |         0 |          6 |
| 2020-03-16 |         0 |         17 |
| 2020-03-17 |         0 |         28 |
| 2020-03-18 |         0 |         18 |
| 2020-03-19 |         0 |         26 |
| 2020-03-20 |         0 |         22 |
| 2020-03-21 |         0 |         18 |
| 2020-03-22 |         0 |         14 |
| 2020-03-23 |         0 |         31 |
| 2020-03-24 |         0 |         16 |
| 2020-03-25 |         0 |         24 |
| 2020-03-26 |         0 |         36 |
| 2020-03-27 |         0 |         41 |
| 2020-03-28 |         0 |         27 |
| 2020-03-29 |         0 |         35 |
| 2020-03-30 |         0 |         25 |
| 2020-03-31 |         0 |         52 |
| 2020-04-01 |         0 |         66 |
| 2020-04-02 |         0 |         30 |
| 2020-04-03 |         0 |         43 |
| 2020-04-04 |         0 |         22 |
| 2020-04-05 |         0 |         30 |
| 2020-04-06 |         0 |         20 |
| 2020-04-07 |         0 |         29 |
| 2020-04-08 |         0 |         70 |
| 2020-04-09 |         0 |         59 |
| 2020-04-10 |         0 |         75 |
| 2020-04-11 |         0 |         58 |
| 2020-04-12 |         0 |         67 |
| 2020-04-13 |         0 |         77 |
| 2020-04-14 |         0 |         70 |
| 2020-04-15 |         0 |         76 |
| 2020-04-16 |         0 |         85 |
| 2020-04-17 |         0 |         60 |
| 2020-04-18 |         0 |         51 |
| 2020-04-19 |         0 |          7 |
| 2020-04-20 |         0 |         47 |
| 2020-04-21 |         0 |         83 |
| 2020-04-22 |         0 |         82 |
| 2020-04-23 |         0 |         61 |
| 2020-04-24 |         0 |         59 |
| 2020-04-25 |         0 |         38 |
| 2020-04-26 |         0 |         30 |
| 2020-04-27 |         0 |         22 |
| 2020-04-28 |         0 |         21 |
| 2020-04-29 |         0 |          7 |
| 2020-04-30 |         0 |         10 |
| 2020-05-01 |         0 |         27 |
| 2020-05-02 |         0 |         13 |
| 2020-05-03 |         0 |          8 |
| 2020-05-04 |         0 |          7 |
| 2020-05-05 |         0 |          9 |
| 2020-05-06 |         0 |         17 |
| 2020-05-07 |         0 |         35 |
| 2020-05-08 |         0 |         14 |
| 2020-05-09 |         0 |         18 |
| 2020-05-10 |         0 |         16 |
| 2020-05-11 |         0 |         19 |
| 2020-05-12 |         0 |         20 |
| 2020-05-13 |         0 |         18 |
| 2020-05-14 |         0 |         15 |
| 2020-05-15 |         0 |         11 |
| 2020-05-16 |         0 |         15 |
| 2020-05-17 |         0 |          7 |
| 2020-05-18 |         0 |         22 |
| 2020-05-19 |         0 |         23 |
| 2020-05-20 |         0 |          9 |
| 2020-05-21 |         0 |         17 |
| 2020-05-22 |         0 |         15 |
| 2020-05-23 |         0 |          4 |
| 2020-05-24 |         0 |          6 |
| 2020-05-25 |         0 |         15 |
| 2020-05-26 |         0 |          8 |
| 2020-05-27 |         0 |         10 |
| 2020-05-28 |         0 |          5 |
| 2020-05-29 |         0 |          1 |
| 2020-05-30 |         0 |          5 |
| 2020-05-31 |         0 |          7 |
| 2020-06-01 |         0 |          4 |
| 2020-06-02 |         0 |          7 |
| 2020-06-03 |         0 |          3 |
| 2020-06-04 |         0 |          2 |
| 2020-06-05 |         0 |          6 |
| 2020-06-06 |         0 |          3 |
| 2020-06-07 |         0 |          1 |
| 2020-06-08 |         0 |          2 |
| 2020-06-09 |         0 |          6 |
| 2020-06-10 |         0 |          3 |
| 2020-06-11 |         0 |          2 |
| 2020-06-12 |         0 |          1 |
| 2020-06-14 |         0 |          1 |
| 2020-06-15 |         0 |          3 |
| 2020-06-16 |         0 |          2 |
| 2020-06-17 |         0 |          3 |
| 2020-06-18 |         0 |          3 |
| 2020-06-19 |         0 |          1 |
| 2020-06-20 |         0 |          1 |
| 2020-06-21 |         0 |          1 |
| 2020-06-23 |         0 |          1 |
| 2020-06-24 |         0 |          1 |
| 2020-06-26 |         0 |          2 |
| 2020-06-27 |         0 |          1 |
| 2020-06-28 |         0 |          1 |
| 2020-06-30 |         1 |          1 |
| 2020-07-03 |         0 |          6 |
| 2020-07-04 |         0 |          1 |
| 2020-07-09 |         0 |          1 |
| 2020-07-13 |         0 |          1 |
| 2020-07-22 |         0 |          1 |
| 2020-07-25 |         0 |          1 |
| 2020-07-29 |         0 |          3 |
| 2020-08-03 |         0 |          1 |
| 2020-08-05 |         0 |          1 |
| 2020-08-09 |         0 |          1 |
| 2020-08-10 |         0 |          2 |
| 2020-08-14 |         0 |          1 |
| 2020-08-17 |         0 |          1 |
| 2020-08-22 |         0 |          2 |
| 2020-08-24 |         0 |          2 |
| 2020-08-25 |         0 |          3 |
| 2020-08-27 |         0 |          1 |
| 2020-08-29 |         0 |         31 |
| 2020-08-30 |         0 |         27 |
| 2020-08-31 |         0 |         27 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country   |   Number of sequences | Sequence group   |
|:-----------------------|:----------|----------------------:|:-----------------|
| ABERDEEN               | Scotland  |                    21 | 10-100           |
| ABERDEENSHIRE          | Scotland  |                     1 | 1-10             |
| ANGUS                  | Scotland  |                     1 | 1-10             |
| ARGYLL AND BUTE        | Scotland  |                    26 | 10-100           |
| CLACKMANNANSHIRE       | Scotland  |                     1 | 1-10             |
| CUMBRIA                | England   |                     1 | 1-10             |
| DUMFRIES AND GALLOWAY  | Scotland  |                    61 | 10-100           |
| DUNDEE                 | Scotland  |                    12 | 10-100           |
| EAST AYRSHIRE          | Scotland  |                    65 | 10-100           |
| EAST DUNBARTONSHIRE    | Scotland  |                   102 | 100-200          |
| EAST RENFREWSHIRE      | Scotland  |                    65 | 10-100           |
| EDINBURGH              | Scotland  |                    12 | 10-100           |
| EILEAN SIAR            | Scotland  |                     4 | 1-10             |
| FALKIRK                | Scotland  |                    75 | 10-100           |
| FIFE                   | Scotland  |                     1 | 1-10             |
| GLASGOW                | Scotland  |                  1236 | 1000-2000        |
| HIGHLAND               | Scotland  |                    11 | 10-100           |
| INVERCLYDE             | Scotland  |                    63 | 10-100           |
| NORTH AYRSHIRE         | Scotland  |                    23 | 10-100           |
| NORTH LANARKSHIRE      | Scotland  |                   240 | 200-300          |
| NORTHAMPTONSHIRE       | England   |                     1 | 1-10             |
| ORKNEY ISLANDS         | Scotland  |                     1 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland  |                     3 | 1-10             |
| RENFREWSHIRE           | Scotland  |                   339 | 300-400          |
| SCOTTISH BORDERS       | Scotland  |                     1 | 1-10             |
| SHETLAND ISLANDS       | Scotland  |                    14 | 10-100           |
| SOUTH AYRSHIRE         | Scotland  |                     9 | 1-10             |
| SOUTH LANARKSHIRE      | Scotland  |                   106 | 100-200          |
| STIRLING               | Scotland  |                    19 | 10-100           |
| WEST DUNBARTONSHIRE    | Scotland  |                    78 | 10-100           |
| WEST LOTHIAN           | Scotland  |                     1 | 1-10             |

<div style="page-break-after: always"></div>






