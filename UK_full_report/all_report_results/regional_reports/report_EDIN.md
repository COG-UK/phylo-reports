







# Lineages report for EDIN




This report gives summaries of UK specific lineages sequenced by EDIN for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-08-31. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1734 sequences in the UK from the sequencing centre EDIN have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 14 and the maximum is 645


Sequences which were replicates or too error-prone were removed from this analysis.



130 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 2 that remain:
2 lineages have gone quiet, ie haven't been seen this week.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+---------------------------+----------+
| Lineage name   | Scotland     | Date range     | Global lineage            | Total    |
+================+==============+================+===========================+==========+
| UK109          | 269 (100.0%) | Mar-21, Jun-12 | B.1, B.1.100              | 269 taxa |
+----------------+--------------+----------------+---------------------------+----------+
| UK336          | 207 (100.0%) | Mar-21, May-22 | B.1.93, B.1               | 207 taxa |
+----------------+--------------+----------------+---------------------------+----------+
| UK199          | 157 (100.0%) | Mar-20, Jun-25 | B.1.5, B.1, B.1.5.10      | 157 taxa |
+----------------+--------------+----------------+---------------------------+----------+
| UK5            | 93 (100.0%)  | Mar-11, Aug-21 | B.1.1, B.1.1.10, B.1.1.12 | 93 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1254         | 74 (100.0%)  | Mar-22, May-21 | B.1, B.1.89               | 74 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1195         | 69 (100.0%)  | Aug-01, Aug-24 | B.1.1, B.1.1.25           | 69 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK175          | 67 (100.0%)  | Mar-04, Aug-03 | B.1.5, B, B.1, B.1.71     | 67 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK2913         | 59 (100.0%)  | Mar-28, Jun-06 | B.1, B.1.11               | 59 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1964         | 42 (100.0%)  | Apr-16, Jun-02 | B.1.1.14                  | 42 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1437         | 41 (100.0%)  | Apr-08, May-14 | B.1                       | 41 taxa  |
+----------------+--------------+----------------+---------------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_EDIN_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_EDIN_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_EDIN_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by EDIN is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_EDIN_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_EDIN_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 209 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_EDIN_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+---------------------------+----------+
| Lineage name   | Scotland     | Date range     | Global lineage            | Total    |
+================+==============+================+===========================+==========+
| UK109          | 269 (100.0%) | Mar-21, Jun-12 | B.1, B.1.100              | 269 taxa |
+----------------+--------------+----------------+---------------------------+----------+
| UK336          | 207 (100.0%) | Mar-21, May-22 | B.1.93, B.1               | 207 taxa |
+----------------+--------------+----------------+---------------------------+----------+
| UK199          | 157 (100.0%) | Mar-20, Jun-25 | B.1.5, B.1, B.1.5.10      | 157 taxa |
+----------------+--------------+----------------+---------------------------+----------+
| UK5            | 93 (100.0%)  | Mar-11, Aug-21 | B.1.1, B.1.1.10, B.1.1.12 | 93 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1254         | 74 (100.0%)  | Mar-22, May-21 | B.1, B.1.89               | 74 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1195         | 69 (100.0%)  | Aug-01, Aug-24 | B.1.1, B.1.1.25           | 69 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK175          | 67 (100.0%)  | Mar-04, Aug-03 | B.1.5, B, B.1, B.1.71     | 67 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK2913         | 59 (100.0%)  | Mar-28, Jun-06 | B.1, B.1.11               | 59 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1964         | 42 (100.0%)  | Apr-16, Jun-02 | B.1.1.14                  | 42 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1437         | 41 (100.0%)  | Apr-08, May-14 | B.1                       | 41 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK2068         | 40 (100.0%)  | Apr-16, May-25 | B.1.1.4                   | 40 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK2464         | 39 (100.0%)  | Mar-20, May-22 | B.1                       | 39 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK5676         | 29 (100.0%)  | Mar-09, May-07 | B.2                       | 29 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK72           | 28 (100.0%)  | Mar-11, Apr-09 | B                         | 28 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK21           | 28 (100.0%)  | Mar-18, May-23 | B.1, B.1.40               | 28 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK4493         | 26 (100.0%)  | Apr-23, May-19 | B.1                       | 26 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1951         | 26 (100.0%)  | Mar-29, May-27 | B.1.1.1                   | 26 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1667         | 26 (100.0%)  | Mar-31, May-18 | B.1, B.1.9                | 26 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1683         | 25 (100.0%)  | Mar-18, May-13 | B.1.1, B.1.1.1            | 25 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK44           | 23 (100.0%)  | Mar-25, May-01 | B                         | 23 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK107          | 20 (100.0%)  | Mar-21, May-05 | B.2.1                     | 20 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK187          | 20 (100.0%)  | Mar-31, Jun-05 | B.1                       | 20 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK945          | 19 (100.0%)  | Mar-18, May-02 | B.1.1                     | 19 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK740          | 15 (100.0%)  | Mar-28, May-20 | B.1.1                     | 15 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK167          | 15 (100.0%)  | Mar-24, May-15 | B.1                       | 15 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK43           | 13 (100.0%)  | Mar-26, Apr-18 | A.5                       | 13 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK436          | 12 (100.0%)  | Apr-13, May-14 | B.1.5                     | 12 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK512          | 11 (100.0%)  | Apr-07, May-13 | B.1.5, B.1.5.6            | 11 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK14           | 11 (100.0%)  | Mar-21, May-21 | B                         | 11 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK1487         | 10 (100.0%)  | Apr-05, Apr-22 | B.1.5                     | 10 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK2916         | 10 (100.0%)  | Mar-04, May-18 | B.1, B.1.98               | 10 taxa  |
+----------------+--------------+----------------+---------------------------+----------+
| UK719          | 7 (100.0%)   | Mar-30, May-21 | B.1.1                     | 7 taxa   |
+----------------+--------------+----------------+---------------------------+----------+
| UK6            | 6 (100.0%)   | Mar-23, May-09 | B.1.75                    | 6 taxa   |
+----------------+--------------+----------------+---------------------------+----------+
| UK133          | 6 (100.0%)   | Mar-22, Apr-25 | B.1                       | 6 taxa   |
+----------------+--------------+----------------+---------------------------+----------+

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


| Week commencing   |   UK5 |   UK1195 |
|:------------------|------:|---------:|
| 2020-03-08        |     4 |        0 |
| 2020-03-15        |     2 |        0 |
| 2020-03-22        |     3 |        0 |
| 2020-03-29        |     4 |        0 |
| 2020-04-05        |     7 |        0 |
| 2020-04-12        |     2 |        0 |
| 2020-04-19        |     5 |        0 |
| 2020-04-26        |     3 |        0 |
| 2020-05-03        |     3 |        0 |
| 2020-05-10        |     1 |        0 |
| 2020-05-17        |     3 |        0 |
| 2020-05-24        |     1 |        0 |
| 2020-06-07        |     1 |        0 |
| 2020-06-14        |     1 |        0 |
| 2020-07-26        |     0 |        1 |
| 2020-08-02        |     0 |        3 |
| 2020-08-09        |     0 |        3 |
| 2020-08-16        |     2 |        1 |
| 2020-08-23        |     0 |        1 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-04 |                            0 |                                2 |       2 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-06 |                            1 |                                1 |       2 |
| 2020-03-07 |                            0 |                                1 |       1 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-09 |                            2 |                                2 |       4 |
| 2020-03-11 |                            3 |                                3 |       6 |
| 2020-03-12 |                            2 |                                2 |       4 |
| 2020-03-13 |                            1 |                                0 |       1 |
| 2020-03-18 |                            0 |                                3 |       3 |
| 2020-03-20 |                            2 |                                3 |       5 |
| 2020-03-21 |                            1 |                                4 |       5 |
| 2020-03-22 |                            2 |                                2 |       4 |
| 2020-03-23 |                            2 |                                4 |       6 |
| 2020-03-24 |                            4 |                                3 |       7 |
| 2020-03-25 |                            1 |                                2 |       3 |
| 2020-03-26 |                            1 |                                1 |       2 |
| 2020-03-27 |                            2 |                                0 |       2 |
| 2020-03-28 |                            1 |                                2 |       3 |
| 2020-03-29 |                            3 |                                1 |       4 |
| 2020-03-30 |                            4 |                                6 |      10 |
| 2020-03-31 |                            7 |                                2 |       9 |
| 2020-04-01 |                            3 |                                1 |       4 |
| 2020-04-02 |                            3 |                                2 |       5 |
| 2020-04-03 |                            2 |                                1 |       3 |
| 2020-04-04 |                            2 |                                1 |       3 |
| 2020-04-05 |                            0 |                                1 |       1 |
| 2020-04-06 |                            2 |                                0 |       2 |
| 2020-04-07 |                            4 |                                1 |       5 |
| 2020-04-08 |                            4 |                                1 |       5 |
| 2020-04-09 |                            1 |                                0 |       1 |
| 2020-04-10 |                            0 |                                1 |       1 |
| 2020-04-11 |                            2 |                                0 |       2 |
| 2020-04-12 |                            2 |                                1 |       3 |
| 2020-04-13 |                            1 |                                1 |       2 |
| 2020-04-14 |                            1 |                                0 |       1 |
| 2020-04-15 |                            1 |                                0 |       1 |
| 2020-04-16 |                            0 |                                3 |       3 |
| 2020-04-19 |                            1 |                                0 |       1 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-22 |                            2 |                                0 |       2 |
| 2020-04-23 |                            1 |                                1 |       2 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-25 |                            1 |                                1 |       2 |
| 2020-04-27 |                            1 |                                0 |       1 |
| 2020-04-30 |                            1 |                                0 |       1 |
| 2020-05-02 |                            0 |                                1 |       1 |
| 2020-05-05 |                            0 |                                2 |       2 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-07 |                            0 |                                1 |       1 |
| 2020-05-08 |                            1 |                                0 |       1 |
| 2020-05-11 |                            1 |                                0 |       1 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                0 |       1 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            0 |                                1 |       1 |
| 2020-05-18 |                            1 |                                0 |       1 |
| 2020-05-28 |                            1 |                                0 |       1 |
| 2020-06-13 |                            1 |                                0 |       1 |
| 2020-06-15 |                            1 |                                0 |       1 |
| 2020-08-01 |                            0 |                                1 |       1 |
| 2020-08-03 |                            1 |                                0 |       1 |
| 2020-08-04 |                            2 |                                0 |       2 |
| 2020-08-19 |                            1 |                                0 |       1 |
| 2020-08-20 |                            0 |                                1 |       1 |
| 2020-08-23 |                            1 |                                0 |       1 |
| 2020-08-26 |                            1 |                                0 |       1 |
| 2020-08-29 |                            1 |                                0 |       1 |
| 2020-08-31 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   Scotland |
|:-----------|-----------:|
| 2020-03-04 |          2 |
| 2020-03-05 |          1 |
| 2020-03-06 |          2 |
| 2020-03-07 |          2 |
| 2020-03-08 |          1 |
| 2020-03-09 |          4 |
| 2020-03-10 |          1 |
| 2020-03-11 |          9 |
| 2020-03-12 |         10 |
| 2020-03-13 |          5 |
| 2020-03-14 |          3 |
| 2020-03-15 |          3 |
| 2020-03-17 |          5 |
| 2020-03-18 |          7 |
| 2020-03-19 |          3 |
| 2020-03-20 |         11 |
| 2020-03-21 |         14 |
| 2020-03-22 |         16 |
| 2020-03-23 |         18 |
| 2020-03-24 |         13 |
| 2020-03-25 |          9 |
| 2020-03-26 |         18 |
| 2020-03-27 |         21 |
| 2020-03-28 |         17 |
| 2020-03-29 |         12 |
| 2020-03-30 |         42 |
| 2020-03-31 |         36 |
| 2020-04-01 |         28 |
| 2020-04-02 |         31 |
| 2020-04-03 |         26 |
| 2020-04-04 |         34 |
| 2020-04-05 |         21 |
| 2020-04-06 |         28 |
| 2020-04-07 |         25 |
| 2020-04-08 |         22 |
| 2020-04-09 |         11 |
| 2020-04-10 |         10 |
| 2020-04-11 |         19 |
| 2020-04-12 |         37 |
| 2020-04-13 |         31 |
| 2020-04-14 |         36 |
| 2020-04-15 |         34 |
| 2020-04-16 |         31 |
| 2020-04-17 |         15 |
| 2020-04-18 |         24 |
| 2020-04-19 |         26 |
| 2020-04-20 |         34 |
| 2020-04-21 |         29 |
| 2020-04-22 |         28 |
| 2020-04-23 |         25 |
| 2020-04-24 |         35 |
| 2020-04-25 |         32 |
| 2020-04-26 |         23 |
| 2020-04-27 |         42 |
| 2020-04-28 |         20 |
| 2020-04-29 |         23 |
| 2020-04-30 |         38 |
| 2020-05-01 |         32 |
| 2020-05-02 |          7 |
| 2020-05-03 |         15 |
| 2020-05-04 |         19 |
| 2020-05-05 |         23 |
| 2020-05-06 |         30 |
| 2020-05-07 |         17 |
| 2020-05-08 |         31 |
| 2020-05-09 |         20 |
| 2020-05-10 |         15 |
| 2020-05-11 |         19 |
| 2020-05-12 |         35 |
| 2020-05-13 |         37 |
| 2020-05-14 |         44 |
| 2020-05-15 |         21 |
| 2020-05-16 |         11 |
| 2020-05-17 |         12 |
| 2020-05-18 |         18 |
| 2020-05-19 |         22 |
| 2020-05-20 |         10 |
| 2020-05-21 |         16 |
| 2020-05-22 |         11 |
| 2020-05-23 |          4 |
| 2020-05-24 |          3 |
| 2020-05-25 |          8 |
| 2020-05-26 |          9 |
| 2020-05-27 |          3 |
| 2020-05-28 |          6 |
| 2020-05-29 |          1 |
| 2020-05-30 |          2 |
| 2020-05-31 |          1 |
| 2020-06-01 |          3 |
| 2020-06-02 |         11 |
| 2020-06-03 |          2 |
| 2020-06-04 |          7 |
| 2020-06-05 |          3 |
| 2020-06-06 |          2 |
| 2020-06-07 |          1 |
| 2020-06-08 |          1 |
| 2020-06-11 |          2 |
| 2020-06-12 |          2 |
| 2020-06-13 |          2 |
| 2020-06-15 |          2 |
| 2020-06-17 |          1 |
| 2020-06-22 |          3 |
| 2020-06-25 |          1 |
| 2020-07-16 |          1 |
| 2020-08-01 |          1 |
| 2020-08-02 |          7 |
| 2020-08-03 |         19 |
| 2020-08-04 |         19 |
| 2020-08-05 |          7 |
| 2020-08-06 |          1 |
| 2020-08-07 |          2 |
| 2020-08-08 |          1 |
| 2020-08-10 |          3 |
| 2020-08-11 |          2 |
| 2020-08-12 |          2 |
| 2020-08-13 |          2 |
| 2020-08-14 |          2 |
| 2020-08-16 |          2 |
| 2020-08-19 |          2 |
| 2020-08-20 |          2 |
| 2020-08-21 |          1 |
| 2020-08-22 |          1 |
| 2020-08-23 |          1 |
| 2020-08-24 |          2 |
| 2020-08-26 |          1 |
| 2020-08-29 |          2 |
| 2020-08-30 |          1 |
| 2020-08-31 |          2 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                 | Country   |   Number of sequences | Sequence group   |
|:-----------------------|:----------|----------------------:|:-----------------|
| ABERDEEN               | Scotland  |                    39 | 10-100           |
| ABERDEENSHIRE          | Scotland  |                    25 | 10-100           |
| ANGUS                  | Scotland  |                    47 | 10-100           |
| CLACKMANNANSHIRE       | Scotland  |                     2 | 1-10             |
| DUMFRIES AND GALLOWAY  | Scotland  |                     2 | 1-10             |
| DUNDEE                 | Scotland  |                   156 | 100-200          |
| EAST AYRSHIRE          | Scotland  |                     6 | 1-10             |
| EAST LOTHIAN           | Scotland  |                    63 | 10-100           |
| EDINBURGH              | Scotland  |                   538 | 500-600          |
| FALKIRK                | Scotland  |                     6 | 1-10             |
| FIFE                   | Scotland  |                    59 | 10-100           |
| GLASGOW                | Scotland  |                     2 | 1-10             |
| HIGHLAND               | Scotland  |                    36 | 10-100           |
| MIDLOTHIAN             | Scotland  |                   165 | 100-200          |
| MORAY                  | Scotland  |                    12 | 10-100           |
| NORTH AYRSHIRE         | Scotland  |                     1 | 1-10             |
| NORTH LANARKSHIRE      | Scotland  |                     2 | 1-10             |
| NORTHUMBERLAND         | England   |                     3 | 1-10             |
| NOTTINGHAM             | England   |                     1 | 1-10             |
| ORKNEY ISLANDS         | Scotland  |                     5 | 1-10             |
| PERTHSHIRE AND KINROSS | Scotland  |                    42 | 10-100           |
| SCOTTISH BORDERS       | Scotland  |                   154 | 100-200          |
| SOUTH AYRSHIRE         | Scotland  |                     2 | 1-10             |
| SOUTH LANARKSHIRE      | Scotland  |                     4 | 1-10             |
| STIRLING               | Scotland  |                     1 | 1-10             |
| WEST LOTHIAN           | Scotland  |                   151 | 100-200          |
| WEST YORKSHIRE         | England   |                     1 | 1-10             |

<div style="page-break-after: always"></div>






