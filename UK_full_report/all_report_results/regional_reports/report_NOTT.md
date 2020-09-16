







# Lineages report for NOTT




This report gives summaries of UK specific lineages sequenced by NOTT for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-09-10. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
1451 sequences in the UK from the sequencing centre NOTT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 20 and the maximum is 566


Sequences which were replicates or too error-prone were removed from this analysis.



138 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 3 that remain:
3 are pending extinction, ie last seen three weeks ago.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+---------+----------------+------------------+----------+
| Lineage name   | England      | Wales   | Date range     | Global lineage   | Total    |
+================+==============+=========+================+==================+==========+
| UK5            | 308 (100.0%) | 0 (0%)  | Mar-12, Aug-27 | B.1.1            | 308 taxa |
+----------------+--------------+---------+----------------+------------------+----------+
| UK1205         | 124 (100.0%) | 0 (0%)  | Mar-30, Aug-09 | B.1.1.1, B.1.1   | 124 taxa |
+----------------+--------------+---------+----------------+------------------+----------+
| UK2464         | 81 (100.0%)  | 0 (0%)  | Mar-18, Jun-18 | B.1, B.1.11      | 81 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK1951         | 73 (100.0%)  | 0 (0%)  | Mar-22, Aug-09 | B.1.1.1, B.1.1   | 73 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK1323         | 58 (100.0%)  | 0 (0%)  | Mar-22, Jul-02 | B.1.1            | 58 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK709          | 49 (100.0%)  | 0 (0%)  | Apr-23, Jun-29 | B.1.1            | 49 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK175          | 45 (100.0%)  | 0 (0%)  | Mar-17, Jun-02 | B.1, B.1.5       | 45 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK4            | 42 (100.0%)  | 0 (0%)  | Mar-04, Apr-29 | B                | 42 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK607          | 38 (100.0%)  | 0 (0%)  | Mar-02, May-18 | B, B.2           | 38 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+
| UK315          | 33 (100.0%)  | 0 (0%)  | Mar-11, Apr-24 | B.2.2            | 33 taxa  |
+----------------+--------------+---------+----------------+------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_NOTT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_NOTT_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_NOTT_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by NOTT is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_NOTT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_NOTT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 158 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_NOTT_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+---------+----------------+----------------------+----------+
| Lineage name   | England      | Wales   | Date range     | Global lineage       | Total    |
+================+==============+=========+================+======================+==========+
| UK5            | 308 (100.0%) | 0 (0%)  | Mar-12, Aug-27 | B.1.1                | 308 taxa |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1205         | 124 (100.0%) | 0 (0%)  | Mar-30, Aug-09 | B.1.1.1, B.1.1       | 124 taxa |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK2464         | 81 (100.0%)  | 0 (0%)  | Mar-18, Jun-18 | B.1, B.1.11          | 81 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1951         | 73 (100.0%)  | 0 (0%)  | Mar-22, Aug-09 | B.1.1.1, B.1.1       | 73 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1323         | 58 (100.0%)  | 0 (0%)  | Mar-22, Jul-02 | B.1.1                | 58 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK709          | 49 (100.0%)  | 0 (0%)  | Apr-23, Jun-29 | B.1.1                | 49 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK175          | 45 (100.0%)  | 0 (0%)  | Mar-17, Jun-02 | B.1, B.1.5           | 45 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK4            | 42 (100.0%)  | 0 (0%)  | Mar-04, Apr-29 | B                    | 42 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK607          | 38 (100.0%)  | 0 (0%)  | Mar-02, May-18 | B, B.2               | 38 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK315          | 33 (100.0%)  | 0 (0%)  | Mar-11, Apr-24 | B.2.2                | 33 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK600          | 31 (100.0%)  | 0 (0%)  | Mar-28, May-04 | B.1.1                | 31 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1307         | 29 (100.0%)  | 0 (0%)  | Mar-17, May-01 | B.1, B.1.34, B.1.5   | 29 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK107          | 28 (100.0%)  | 0 (0%)  | Mar-16, Jun-02 | B.2.1                | 28 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1060         | 26 (100.0%)  | 0 (0%)  | Mar-22, Apr-30 | B.1.1                | 26 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK899          | 24 (100.0%)  | 0 (0%)  | Mar-16, Apr-20 | B.1.11, B.1.5        | 24 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1271         | 21 (100.0%)  | 0 (0%)  | May-30, Aug-13 | B.1.1                | 21 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1683         | 20 (100.0%)  | 0 (0%)  | Apr-29, Aug-18 | B.1.1.1, B.1.1       | 20 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK31           | 18 (100.0%)  | 0 (0%)  | Mar-21, Jul-23 | B.3                  | 18 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK39           | 17 (100.0%)  | 0 (0%)  | Apr-13, May-03 | A.2                  | 17 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK2022         | 17 (100.0%)  | 0 (0%)  | Apr-02, Aug-09 | B.1.1                | 17 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK199          | 15 (100.0%)  | 0 (0%)  | Mar-23, Aug-09 | B.1, B.1.5           | 15 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK5676         | 15 (100.0%)  | 0 (0%)  | Mar-18, May-06 | B.2                  | 15 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK2916         | 14 (100.0%)  | 0 (0%)  | Mar-25, Jun-29 | B.1                  | 14 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK352          | 12 (100.0%)  | 0 (0%)  | Aug-05, Aug-09 | B.1.113, B.1, B.1.36 | 12 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK266          | 11 (100.0%)  | 0 (0%)  | Apr-06, Apr-30 | B.1                  | 11 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK72           | 10 (100.0%)  | 0 (0%)  | Mar-18, May-05 | B                    | 10 taxa  |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK945          | 8 (100.0%)   | 0 (0%)  | Mar-28, Jun-10 | B.1.1                | 8 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK336          | 8 (100.0%)   | 0 (0%)  | Apr-05, Apr-24 | B.1                  | 8 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK267          | 8 (100.0%)   | 0 (0%)  | Mar-24, Apr-11 | B.2                  | 8 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK384          | 7 (100.0%)   | 0 (0%)  | Mar-14, Apr-18 | B.2.1                | 7 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1097         | 7 (100.0%)   | 0 (0%)  | Aug-06, Aug-10 | B.1                  | 7 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK1535         | 7 (100.0%)   | 0 (0%)  | Apr-04, Aug-14 | B.1.1                | 7 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK331          | 7 (100.0%)   | 0 (0%)  | Jul-04, Aug-09 | B.1.36               | 7 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK719          | 7 (100.0%)   | 0 (0%)  | Mar-31, Jun-10 | B.1.1                | 7 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK2913         | 7 (100.0%)   | 0 (0%)  | Mar-30, Jun-29 | B.1, B.1.11          | 7 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK387          | 6 (100.0%)   | 0 (0%)  | Mar-24, Jun-22 | B.1                  | 6 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+
| UK478          | 6 (100.0%)   | 0 (0%)  | Apr-10, Jul-01 | B.1, B.1.5           | 6 taxa   |
+----------------+--------------+---------+----------------+----------------------+----------+

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


| Week commencing   |   UK5 |   UK1683 |   UK1535 |
|:------------------|------:|---------:|---------:|
| 2020-03-08        |     1 |        0 |        0 |
| 2020-03-15        |     1 |        0 |        0 |
| 2020-03-22        |     2 |        0 |        0 |
| 2020-03-29        |     2 |        0 |        1 |
| 2020-04-05        |     2 |        0 |        0 |
| 2020-04-12        |     2 |        0 |        0 |
| 2020-04-19        |     2 |        0 |        0 |
| 2020-04-26        |     3 |        1 |        0 |
| 2020-05-03        |     2 |        0 |        0 |
| 2020-05-10        |     1 |        0 |        0 |
| 2020-05-17        |     1 |        0 |        0 |
| 2020-05-24        |     2 |        0 |        0 |
| 2020-05-31        |     5 |        0 |        0 |
| 2020-06-07        |     4 |        0 |        0 |
| 2020-06-14        |     3 |        0 |        0 |
| 2020-06-21        |     2 |        0 |        0 |
| 2020-06-28        |     2 |        0 |        0 |
| 2020-07-05        |     1 |        0 |        0 |
| 2020-07-12        |     2 |        0 |        0 |
| 2020-07-19        |     2 |        1 |        0 |
| 2020-07-26        |     2 |        1 |        1 |
| 2020-08-02        |     1 |        1 |        1 |
| 2020-08-09        |     2 |        1 |        1 |
| 2020-08-16        |     0 |        1 |        0 |
| 2020-08-23        |     1 |        0 |        0 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-02 |                            0 |                                1 |       1 |
| 2020-03-04 |                            0 |                                1 |       1 |
| 2020-03-11 |                            0 |                                1 |       1 |
| 2020-03-12 |                            0 |                                2 |       2 |
| 2020-03-14 |                            1 |                                1 |       2 |
| 2020-03-16 |                            0 |                                4 |       4 |
| 2020-03-17 |                            2 |                                2 |       4 |
| 2020-03-18 |                            0 |                                3 |       3 |
| 2020-03-19 |                            1 |                                0 |       1 |
| 2020-03-20 |                            0 |                                2 |       2 |
| 2020-03-21 |                            0 |                                1 |       1 |
| 2020-03-22 |                            1 |                                4 |       5 |
| 2020-03-23 |                            0 |                                2 |       2 |
| 2020-03-24 |                            2 |                                3 |       5 |
| 2020-03-25 |                            2 |                                2 |       4 |
| 2020-03-27 |                            0 |                                1 |       1 |
| 2020-03-28 |                            4 |                                2 |       6 |
| 2020-03-29 |                            4 |                                2 |       6 |
| 2020-03-30 |                            6 |                                3 |       9 |
| 2020-03-31 |                            0 |                                1 |       1 |
| 2020-04-01 |                            2 |                                0 |       2 |
| 2020-04-02 |                            3 |                                2 |       5 |
| 2020-04-03 |                            3 |                                2 |       5 |
| 2020-04-04 |                            3 |                                4 |       7 |
| 2020-04-05 |                            3 |                                3 |       6 |
| 2020-04-06 |                            0 |                                1 |       1 |
| 2020-04-07 |                            2 |                                1 |       3 |
| 2020-04-08 |                            2 |                                1 |       3 |
| 2020-04-09 |                            5 |                                1 |       6 |
| 2020-04-10 |                            0 |                                2 |       2 |
| 2020-04-11 |                            1 |                                0 |       1 |
| 2020-04-13 |                            0 |                                1 |       1 |
| 2020-04-14 |                            0 |                                2 |       2 |
| 2020-04-16 |                            2 |                                0 |       2 |
| 2020-04-17 |                            0 |                                1 |       1 |
| 2020-04-18 |                            1 |                                0 |       1 |
| 2020-04-19 |                            1 |                                1 |       2 |
| 2020-04-20 |                            4 |                                0 |       4 |
| 2020-04-21 |                            1 |                                0 |       1 |
| 2020-04-22 |                            2 |                                0 |       2 |
| 2020-04-23 |                            3 |                                2 |       5 |
| 2020-04-24 |                            2 |                                0 |       2 |
| 2020-04-27 |                            2 |                                1 |       3 |
| 2020-04-29 |                            1 |                                3 |       4 |
| 2020-04-30 |                            3 |                                0 |       3 |
| 2020-05-01 |                            1 |                                0 |       1 |
| 2020-05-02 |                            2 |                                0 |       2 |
| 2020-05-04 |                            0 |                                1 |       1 |
| 2020-05-07 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                0 |       1 |
| 2020-05-18 |                            1 |                                0 |       1 |
| 2020-05-30 |                            1 |                                1 |       2 |
| 2020-06-03 |                            1 |                                0 |       1 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-06 |                            1 |                                1 |       2 |
| 2020-06-09 |                            0 |                                1 |       1 |
| 2020-06-17 |                            1 |                                0 |       1 |
| 2020-06-18 |                            1 |                                0 |       1 |
| 2020-06-23 |                            1 |                                0 |       1 |
| 2020-06-24 |                            1 |                                0 |       1 |
| 2020-06-29 |                            1 |                                0 |       1 |
| 2020-06-30 |                            1 |                                0 |       1 |
| 2020-07-02 |                            0 |                                1 |       1 |
| 2020-07-04 |                            0 |                                1 |       1 |
| 2020-07-10 |                            0 |                                1 |       1 |
| 2020-07-21 |                            0 |                                1 |       1 |
| 2020-07-29 |                            1 |                                0 |       1 |
| 2020-07-30 |                            1 |                                0 |       1 |
| 2020-07-31 |                            0 |                                1 |       1 |
| 2020-08-05 |                            1 |                                1 |       2 |
| 2020-08-06 |                            1 |                                1 |       2 |
| 2020-08-09 |                            2 |                                1 |       3 |
| 2020-08-10 |                            1 |                                0 |       1 |
| 2020-08-19 |                            0 |                                1 |       1 |
| 2020-08-27 |                            1 |                                0 |       1 |
| 2020-09-02 |                            1 |                                0 |       1 |
| 2020-09-07 |                            1 |                                0 |       1 |
| 2020-09-09 |                            0 |                                1 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |   Wales |
|:-----------|----------:|--------:|
| 2020-03-02 |         1 |       0 |
| 2020-03-04 |         1 |       0 |
| 2020-03-07 |         2 |       0 |
| 2020-03-11 |         2 |       0 |
| 2020-03-12 |         4 |       0 |
| 2020-03-13 |         1 |       0 |
| 2020-03-14 |         6 |       0 |
| 2020-03-15 |         2 |       0 |
| 2020-03-16 |         4 |       0 |
| 2020-03-17 |         8 |       0 |
| 2020-03-18 |         9 |       0 |
| 2020-03-19 |         9 |       0 |
| 2020-03-20 |        12 |       0 |
| 2020-03-21 |        12 |       0 |
| 2020-03-22 |        17 |       0 |
| 2020-03-23 |        16 |       0 |
| 2020-03-24 |        21 |       0 |
| 2020-03-25 |        19 |       0 |
| 2020-03-26 |         3 |       0 |
| 2020-03-27 |         9 |       0 |
| 2020-03-28 |        33 |       0 |
| 2020-03-29 |        29 |       0 |
| 2020-03-30 |        38 |       0 |
| 2020-03-31 |        12 |       0 |
| 2020-04-01 |        23 |       0 |
| 2020-04-02 |        27 |       0 |
| 2020-04-03 |        33 |       0 |
| 2020-04-04 |        27 |       0 |
| 2020-04-05 |        23 |       0 |
| 2020-04-06 |         8 |       0 |
| 2020-04-07 |        28 |       0 |
| 2020-04-08 |        18 |       0 |
| 2020-04-09 |        28 |       0 |
| 2020-04-10 |        18 |       0 |
| 2020-04-11 |        23 |       0 |
| 2020-04-12 |        10 |       0 |
| 2020-04-13 |         7 |       0 |
| 2020-04-14 |        15 |       0 |
| 2020-04-15 |         6 |       0 |
| 2020-04-16 |        11 |       0 |
| 2020-04-17 |        19 |       0 |
| 2020-04-18 |         9 |       0 |
| 2020-04-19 |        10 |       0 |
| 2020-04-20 |        23 |       0 |
| 2020-04-21 |         8 |       0 |
| 2020-04-22 |        21 |       0 |
| 2020-04-23 |        30 |       0 |
| 2020-04-24 |        15 |       0 |
| 2020-04-25 |         9 |       0 |
| 2020-04-26 |        10 |       0 |
| 2020-04-27 |         9 |       0 |
| 2020-04-28 |        13 |       0 |
| 2020-04-29 |        43 |       0 |
| 2020-04-30 |        29 |       0 |
| 2020-05-01 |        29 |       0 |
| 2020-05-02 |        15 |       0 |
| 2020-05-03 |        13 |       0 |
| 2020-05-04 |        12 |       0 |
| 2020-05-05 |        10 |       0 |
| 2020-05-06 |         3 |       0 |
| 2020-05-07 |         4 |       0 |
| 2020-05-09 |         4 |       0 |
| 2020-05-11 |         3 |       0 |
| 2020-05-12 |         3 |       0 |
| 2020-05-13 |         4 |       0 |
| 2020-05-14 |         3 |       0 |
| 2020-05-15 |         5 |       0 |
| 2020-05-16 |         3 |       0 |
| 2020-05-17 |         5 |       0 |
| 2020-05-18 |         9 |       0 |
| 2020-05-19 |        11 |       0 |
| 2020-05-20 |         6 |       0 |
| 2020-05-21 |        11 |       0 |
| 2020-05-22 |         8 |       0 |
| 2020-05-24 |         2 |       0 |
| 2020-05-26 |         7 |       0 |
| 2020-05-27 |         3 |       0 |
| 2020-05-28 |         9 |       0 |
| 2020-05-29 |         5 |       0 |
| 2020-05-30 |        22 |       0 |
| 2020-05-31 |        16 |       0 |
| 2020-06-01 |         7 |       0 |
| 2020-06-02 |        15 |       0 |
| 2020-06-03 |        11 |       0 |
| 2020-06-04 |         6 |       0 |
| 2020-06-05 |        15 |       0 |
| 2020-06-06 |         7 |       0 |
| 2020-06-07 |         7 |       0 |
| 2020-06-08 |        12 |       0 |
| 2020-06-09 |        14 |       0 |
| 2020-06-10 |        15 |       0 |
| 2020-06-11 |        16 |       0 |
| 2020-06-12 |         6 |       0 |
| 2020-06-13 |         3 |       0 |
| 2020-06-14 |         4 |       0 |
| 2020-06-15 |        10 |       0 |
| 2020-06-16 |         8 |       0 |
| 2020-06-17 |         7 |       0 |
| 2020-06-18 |         4 |       0 |
| 2020-06-19 |         2 |       0 |
| 2020-06-20 |         3 |       0 |
| 2020-06-21 |         1 |       0 |
| 2020-06-22 |         6 |       0 |
| 2020-06-23 |         4 |       0 |
| 2020-06-24 |         5 |       0 |
| 2020-06-25 |         4 |       0 |
| 2020-06-26 |         2 |       0 |
| 2020-06-27 |         1 |       0 |
| 2020-06-29 |         8 |       0 |
| 2020-06-30 |         3 |       0 |
| 2020-07-01 |         5 |       0 |
| 2020-07-02 |         5 |       0 |
| 2020-07-04 |         1 |       0 |
| 2020-07-05 |         1 |       0 |
| 2020-07-07 |         1 |       0 |
| 2020-07-08 |         1 |       0 |
| 2020-07-09 |         3 |       0 |
| 2020-07-10 |         2 |       0 |
| 2020-07-11 |         2 |       0 |
| 2020-07-13 |         1 |       0 |
| 2020-07-14 |         2 |       0 |
| 2020-07-15 |         2 |       0 |
| 2020-07-16 |         1 |       0 |
| 2020-07-17 |         1 |       0 |
| 2020-07-20 |         6 |       0 |
| 2020-07-21 |         4 |       0 |
| 2020-07-22 |         1 |       0 |
| 2020-07-23 |         2 |       0 |
| 2020-07-24 |        12 |       0 |
| 2020-07-25 |         4 |       0 |
| 2020-07-27 |         4 |       0 |
| 2020-07-29 |         3 |       0 |
| 2020-07-30 |        25 |       0 |
| 2020-07-31 |         7 |       0 |
| 2020-08-01 |         2 |       0 |
| 2020-08-02 |         2 |       0 |
| 2020-08-04 |         3 |       0 |
| 2020-08-05 |         8 |       0 |
| 2020-08-06 |        20 |       0 |
| 2020-08-07 |         1 |       0 |
| 2020-08-08 |         8 |       0 |
| 2020-08-09 |        35 |       0 |
| 2020-08-10 |         4 |       0 |
| 2020-08-11 |         1 |       0 |
| 2020-08-12 |         1 |       0 |
| 2020-08-13 |         1 |       0 |
| 2020-08-14 |         1 |       0 |
| 2020-08-17 |         1 |       0 |
| 2020-08-18 |         1 |       0 |
| 2020-08-19 |         1 |       0 |
| 2020-08-27 |         1 |       1 |
| 2020-09-02 |         2 |       0 |
| 2020-09-07 |         2 |       0 |
| 2020-09-09 |         1 |       0 |
| 2020-09-10 |         4 |       0 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2           | Country          |   Number of sequences | Sequence group   |
|:-----------------|:-----------------|----------------------:|:-----------------|
| ANTRIM           | Northern Ireland |                     1 | 1-10             |
| DERBYSHIRE       | England          |                     2 | 1-10             |
| DEVON            | England          |                     1 | 1-10             |
| LEICESTERSHIRE   | England          |                   150 | 100-200          |
| LINCOLNSHIRE     | England          |                   149 | 100-200          |
| NORTHAMPTONSHIRE | England          |                     3 | 1-10             |
| NOTTINGHAM       | England          |                   926 | 700-1000         |
| NOTTINGHAMSHIRE  | England          |                    56 | 10-100           |
| STAFFORDSHIRE    | England          |                     2 | 1-10             |
| WARWICKSHIRE     | England          |                     2 | 1-10             |

<div style="page-break-after: always"></div>






