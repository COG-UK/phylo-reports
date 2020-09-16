







# Lineages report for NORT




This report gives summaries of UK specific lineages sequenced by NORT for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-07-16. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
847 sequences in the UK from the sequencing centre NORT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 11 and the maximum is 483


Sequences which were replicates or too error-prone were removed from this analysis.



124 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 7 that remain:
5 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
1 lineage has been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+------------+----------------+--------------------------+----------+
| Lineage name   | England      | Scotland   | Date range     | Global lineage           | Total    |
+================+==============+============+================+==========================+==========+
| UK5            | 228 (100.0%) | 0 (0%)     | Mar-16, Jun-29 | B.1.1.10, B.1.1.1, B.1.1 | 228 taxa |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1951         | 106 (99.07%) | 1 (0.93%)  | Mar-08, Jul-16 | B.1.1.1, B.1.1           | 107 taxa |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK267          | 52 (100.0%)  | 0 (0%)     | Mar-04, May-08 | B.2                      | 52 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1684         | 26 (100.0%)  | 0 (0%)     | Mar-16, May-28 | B.1.1.1                  | 26 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK669          | 22 (100.0%)  | 0 (0%)     | Mar-07, May-12 | B.1.1                    | 22 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK315          | 20 (100.0%)  | 0 (0%)     | Mar-02, May-04 | B.2.2                    | 20 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK199          | 19 (100.0%)  | 0 (0%)     | Mar-21, Jun-25 | B.1.5, B.1, B.1.5.10     | 19 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1060         | 17 (100.0%)  | 0 (0%)     | Mar-05, May-24 | B.1.1                    | 17 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK175          | 16 (100.0%)  | 0 (0%)     | Mar-12, Jun-22 | B.1                      | 16 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK2916         | 13 (100.0%)  | 0 (0%)     | Mar-23, May-10 | B.1                      | 13 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_NORT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_NORT_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_NORT_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by NORT is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_NORT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_NORT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 117 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_NORT_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+------------+----------------+--------------------------+----------+
| Lineage name   | England      | Scotland   | Date range     | Global lineage           | Total    |
+================+==============+============+================+==========================+==========+
| UK5            | 228 (100.0%) | 0 (0%)     | Mar-16, Jun-29 | B.1.1.10, B.1.1.1, B.1.1 | 228 taxa |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1951         | 106 (99.07%) | 1 (0.93%)  | Mar-08, Jul-16 | B.1.1.1, B.1.1           | 107 taxa |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK267          | 52 (100.0%)  | 0 (0%)     | Mar-04, May-08 | B.2                      | 52 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1684         | 26 (100.0%)  | 0 (0%)     | Mar-16, May-28 | B.1.1.1                  | 26 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK669          | 22 (100.0%)  | 0 (0%)     | Mar-07, May-12 | B.1.1                    | 22 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK315          | 20 (100.0%)  | 0 (0%)     | Mar-02, May-04 | B.2.2                    | 20 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK199          | 19 (100.0%)  | 0 (0%)     | Mar-21, Jun-25 | B.1.5, B.1, B.1.5.10     | 19 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1060         | 17 (100.0%)  | 0 (0%)     | Mar-05, May-24 | B.1.1                    | 17 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK175          | 16 (100.0%)  | 0 (0%)     | Mar-12, Jun-22 | B.1                      | 16 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK2916         | 13 (100.0%)  | 0 (0%)     | Mar-23, May-10 | B.1                      | 13 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK994          | 13 (100.0%)  | 0 (0%)     | Apr-05, May-18 | B.1.5, B.1               | 13 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK109          | 13 (100.0%)  | 0 (0%)     | Mar-22, May-05 | B.1, B.1.99              | 13 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK5676         | 12 (100.0%)  | 0 (0%)     | Mar-24, May-08 | B.2, B.2.9               | 12 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK107          | 12 (100.0%)  | 0 (0%)     | Mar-23, Apr-25 | B.2.1                    | 12 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK167          | 10 (100.0%)  | 0 (0%)     | Mar-26, May-07 | B.1                      | 10 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK667          | 10 (100.0%)  | 0 (0%)     | Mar-26, May-07 | B.1.77, B.1              | 10 taxa  |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1076         | 9 (100.0%)   | 0 (0%)     | Apr-17, Jun-22 | B.1.1                    | 9 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1603         | 9 (100.0%)   | 0 (0%)     | May-04, Jun-02 | B.1.1                    | 9 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1223         | 8 (100.0%)   | 0 (0%)     | Apr-04, May-08 | B.1.1.1                  | 8 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1683         | 7 (100.0%)   | 0 (0%)     | Mar-23, Jul-03 | B.1.1.1, B.1.1           | 7 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1205         | 7 (100.0%)   | 0 (0%)     | Mar-15, Jun-23 | B.1.1.1, B.1.1           | 7 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK31           | 6 (100.0%)   | 0 (0%)     | Mar-24, Apr-13 | B.2, B.3                 | 6 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+
| UK1369         | 6 (100.0%)   | 0 (0%)     | Mar-18, May-06 | B.1.1                    | 6 taxa   |
+----------------+--------------+------------+----------------+--------------------------+----------+

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


| Week commencing   |   UK5 |   UK1951 |   UK199 |   UK175 |   UK1076 |   UK1205 |   UK1683 |
|:------------------|------:|---------:|--------:|--------:|---------:|---------:|---------:|
| 2020-03-08        |     0 |        3 |       0 |       1 |        0 |        0 |        0 |
| 2020-03-15        |     1 |        1 |       1 |       0 |        0 |        1 |        0 |
| 2020-03-22        |     5 |        2 |       1 |       1 |        0 |        1 |        1 |
| 2020-03-29        |     6 |        1 |       1 |       1 |        0 |        1 |        1 |
| 2020-04-05        |     1 |        1 |       0 |       1 |        0 |        0 |        0 |
| 2020-04-12        |     1 |        0 |       0 |       1 |        1 |        0 |        0 |
| 2020-04-19        |     3 |        2 |       3 |       1 |        1 |        0 |        1 |
| 2020-04-26        |     5 |        1 |       2 |       1 |        0 |        1 |        1 |
| 2020-05-03        |     6 |        1 |       2 |       2 |        1 |        0 |        0 |
| 2020-05-10        |     6 |        1 |       1 |       1 |        1 |        1 |        0 |
| 2020-05-17        |     3 |        2 |       0 |       0 |        0 |        0 |        0 |
| 2020-05-24        |     1 |        1 |       0 |       0 |        0 |        0 |        0 |
| 2020-05-31        |     3 |        2 |       0 |       0 |        1 |        0 |        0 |
| 2020-06-07        |     2 |        2 |       0 |       0 |        0 |        0 |        0 |
| 2020-06-14        |     2 |        1 |       0 |       0 |        0 |        0 |        0 |
| 2020-06-21        |     2 |        2 |       1 |       1 |        1 |        1 |        0 |
| 2020-06-28        |     1 |        3 |       0 |       0 |        0 |        0 |        1 |
| 2020-07-05        |     0 |        3 |       0 |       0 |        0 |        0 |        0 |
| 2020-07-12        |     0 |        1 |       0 |       0 |        0 |        0 |        0 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-02 |                            0 |                                2 |       2 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-05 |                            0 |                                1 |       1 |
| 2020-03-07 |                            0 |                                1 |       1 |
| 2020-03-08 |                            0 |                                1 |       1 |
| 2020-03-10 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                2 |       2 |
| 2020-03-13 |                            0 |                                1 |       1 |
| 2020-03-14 |                            1 |                                0 |       1 |
| 2020-03-15 |                            2 |                                1 |       3 |
| 2020-03-16 |                            0 |                                2 |       2 |
| 2020-03-18 |                            1 |                                1 |       2 |
| 2020-03-19 |                            2 |                                0 |       2 |
| 2020-03-20 |                            1 |                                2 |       3 |
| 2020-03-21 |                            3 |                                3 |       6 |
| 2020-03-22 |                            3 |                                1 |       4 |
| 2020-03-23 |                            2 |                                7 |       9 |
| 2020-03-24 |                            2 |                                5 |       7 |
| 2020-03-25 |                            4 |                                3 |       7 |
| 2020-03-26 |                            2 |                                3 |       5 |
| 2020-03-27 |                            1 |                                4 |       5 |
| 2020-03-28 |                            3 |                                3 |       6 |
| 2020-03-29 |                            2 |                                1 |       3 |
| 2020-03-30 |                            1 |                                1 |       2 |
| 2020-03-31 |                            2 |                                3 |       5 |
| 2020-04-01 |                            0 |                                1 |       1 |
| 2020-04-02 |                            4 |                                3 |       7 |
| 2020-04-03 |                            5 |                                0 |       5 |
| 2020-04-04 |                            0 |                                1 |       1 |
| 2020-04-05 |                            1 |                                1 |       2 |
| 2020-04-07 |                            2 |                                0 |       2 |
| 2020-04-09 |                            1 |                                0 |       1 |
| 2020-04-10 |                            2 |                                0 |       2 |
| 2020-04-12 |                            1 |                                0 |       1 |
| 2020-04-14 |                            0 |                                1 |       1 |
| 2020-04-16 |                            0 |                                1 |       1 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            1 |                                0 |       1 |
| 2020-04-19 |                            2 |                                0 |       2 |
| 2020-04-20 |                            2 |                                0 |       2 |
| 2020-04-21 |                            1 |                                0 |       1 |
| 2020-04-22 |                            1 |                                0 |       1 |
| 2020-04-23 |                            1 |                                0 |       1 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-27 |                            1 |                                1 |       2 |
| 2020-04-28 |                            1 |                                1 |       2 |
| 2020-04-29 |                            2 |                                0 |       2 |
| 2020-04-30 |                            2 |                                2 |       4 |
| 2020-05-01 |                            1 |                                0 |       1 |
| 2020-05-02 |                            1 |                                0 |       1 |
| 2020-05-04 |                            1 |                                2 |       3 |
| 2020-05-06 |                            0 |                                2 |       2 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-11 |                            1 |                                1 |       2 |
| 2020-05-14 |                            1 |                                0 |       1 |
| 2020-05-15 |                            1 |                                0 |       1 |
| 2020-05-17 |                            0 |                                1 |       1 |
| 2020-06-02 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-21 |                            1 |                                0 |       1 |
| 2020-06-24 |                            3 |                                0 |       3 |
| 2020-06-26 |                            1 |                                0 |       1 |
| 2020-07-03 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Scotland |
|:-----------|----------:|-----------:|
| 2020-03-02 |         2 |          0 |
| 2020-03-04 |         1 |          0 |
| 2020-03-05 |         2 |          0 |
| 2020-03-07 |         1 |          0 |
| 2020-03-08 |         1 |          0 |
| 2020-03-09 |         1 |          0 |
| 2020-03-10 |         4 |          0 |
| 2020-03-12 |         2 |          0 |
| 2020-03-13 |         1 |          0 |
| 2020-03-14 |         1 |          0 |
| 2020-03-15 |         3 |          0 |
| 2020-03-16 |         3 |          0 |
| 2020-03-17 |         2 |          0 |
| 2020-03-18 |         3 |          0 |
| 2020-03-19 |         8 |          0 |
| 2020-03-20 |         9 |          0 |
| 2020-03-21 |         7 |          0 |
| 2020-03-22 |        10 |          0 |
| 2020-03-23 |        23 |          0 |
| 2020-03-24 |        21 |          0 |
| 2020-03-25 |        26 |          0 |
| 2020-03-26 |        22 |          0 |
| 2020-03-27 |        31 |          0 |
| 2020-03-28 |        27 |          0 |
| 2020-03-29 |        31 |          0 |
| 2020-03-30 |        20 |          0 |
| 2020-03-31 |        32 |          0 |
| 2020-04-01 |         9 |          0 |
| 2020-04-02 |        18 |          0 |
| 2020-04-03 |        28 |          0 |
| 2020-04-04 |        13 |          0 |
| 2020-04-05 |        10 |          0 |
| 2020-04-06 |         3 |          0 |
| 2020-04-07 |         3 |          0 |
| 2020-04-08 |         3 |          0 |
| 2020-04-09 |         3 |          0 |
| 2020-04-10 |         3 |          0 |
| 2020-04-11 |         3 |          0 |
| 2020-04-12 |         3 |          0 |
| 2020-04-13 |         1 |          0 |
| 2020-04-14 |         1 |          0 |
| 2020-04-15 |         1 |          0 |
| 2020-04-16 |         4 |          0 |
| 2020-04-17 |         2 |          0 |
| 2020-04-18 |         3 |          0 |
| 2020-04-19 |         6 |          0 |
| 2020-04-20 |         5 |          0 |
| 2020-04-21 |         8 |          0 |
| 2020-04-22 |        14 |          0 |
| 2020-04-23 |         9 |          0 |
| 2020-04-24 |         3 |          0 |
| 2020-04-25 |         2 |          0 |
| 2020-04-26 |         3 |          0 |
| 2020-04-27 |        12 |          0 |
| 2020-04-28 |        10 |          0 |
| 2020-04-29 |        13 |          0 |
| 2020-04-30 |        21 |          0 |
| 2020-05-01 |        19 |          0 |
| 2020-05-02 |        11 |          0 |
| 2020-05-03 |        11 |          0 |
| 2020-05-04 |        14 |          0 |
| 2020-05-05 |        12 |          0 |
| 2020-05-06 |        17 |          0 |
| 2020-05-07 |        15 |          0 |
| 2020-05-08 |        13 |          0 |
| 2020-05-09 |         4 |          0 |
| 2020-05-10 |        13 |          0 |
| 2020-05-11 |        18 |          0 |
| 2020-05-12 |        17 |          0 |
| 2020-05-13 |         8 |          0 |
| 2020-05-14 |         5 |          0 |
| 2020-05-15 |         5 |          0 |
| 2020-05-16 |         6 |          0 |
| 2020-05-17 |         7 |          0 |
| 2020-05-18 |         3 |          0 |
| 2020-05-19 |         4 |          0 |
| 2020-05-20 |         2 |          0 |
| 2020-05-21 |         1 |          0 |
| 2020-05-22 |         4 |          0 |
| 2020-05-23 |         1 |          0 |
| 2020-05-24 |         1 |          0 |
| 2020-05-25 |         1 |          0 |
| 2020-05-26 |         4 |          0 |
| 2020-05-27 |         2 |          0 |
| 2020-05-28 |         1 |          0 |
| 2020-05-30 |         2 |          0 |
| 2020-05-31 |         3 |          0 |
| 2020-06-01 |         3 |          0 |
| 2020-06-02 |         9 |          0 |
| 2020-06-03 |         1 |          0 |
| 2020-06-04 |         2 |          0 |
| 2020-06-05 |         2 |          0 |
| 2020-06-06 |         1 |          0 |
| 2020-06-07 |         1 |          0 |
| 2020-06-08 |         3 |          0 |
| 2020-06-09 |         1 |          0 |
| 2020-06-10 |         1 |          0 |
| 2020-06-15 |         2 |          0 |
| 2020-06-16 |         1 |          0 |
| 2020-06-17 |         1 |          0 |
| 2020-06-18 |         2 |          0 |
| 2020-06-19 |         2 |          0 |
| 2020-06-20 |         3 |          0 |
| 2020-06-21 |         2 |          0 |
| 2020-06-22 |         9 |          0 |
| 2020-06-23 |         3 |          0 |
| 2020-06-24 |         8 |          0 |
| 2020-06-25 |         3 |          0 |
| 2020-06-26 |         5 |          0 |
| 2020-06-27 |         4 |          0 |
| 2020-06-28 |         1 |          0 |
| 2020-06-29 |         3 |          0 |
| 2020-06-30 |         4 |          0 |
| 2020-07-01 |         1 |          0 |
| 2020-07-02 |         4 |          0 |
| 2020-07-03 |         3 |          0 |
| 2020-07-06 |        10 |          1 |
| 2020-07-09 |         2 |          0 |
| 2020-07-11 |         1 |          0 |
| 2020-07-13 |         7 |          0 |
| 2020-07-14 |         4 |          0 |
| 2020-07-15 |         1 |          0 |
| 2020-07-16 |         1 |          0 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2                | Country   |   Number of sequences | Sequence group   |
|:----------------------|:----------|----------------------:|:-----------------|
| CUMBRIA               | England   |                   106 | 100-200          |
| DUMFRIES AND GALLOWAY | Scotland  |                     1 | 1-10             |
| DURHAM                | England   |                   113 | 100-200          |
| NORTH YORKSHIRE       | England   |                   142 | 100-200          |
| NORTHUMBERLAND        | England   |                    62 | 10-100           |
| TYNE AND WEAR         | England   |                   304 | 300-400          |
| WEST YORKSHIRE        | England   |                     1 | 1-10             |

<div style="page-break-after: always"></div>






