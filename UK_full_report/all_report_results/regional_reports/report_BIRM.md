







# Lineages report for BIRM




This report gives summaries of UK specific lineages sequenced by BIRM for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-09-02. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
732 sequences in the UK from the sequencing centre BIRM have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 17 and the maximum is 279


Sequences which were replicates or too error-prone were removed from this analysis.



105 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 8 that remain:
4 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
1 has reactivated.
2 lineages have been continuously circulating.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+----------------------+----------+
| Lineage name   | England      | Date range     | Global lineage       | Total    |
+================+==============+================+======================+==========+
| UK1951         | 152 (100.0%) | Mar-23, Aug-09 | B.1.1, B.1.1.1       | 152 taxa |
+----------------+--------------+----------------+----------------------+----------+
| UK5            | 89 (100.0%)  | Mar-23, Sep-02 | B.1.1, B.1.1.10      | 89 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1134         | 59 (100.0%)  | Apr-28, Aug-06 | B.1.1                | 59 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1312         | 36 (100.0%)  | Jul-11, Jul-14 | B.1.1                | 36 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1153         | 34 (100.0%)  | Jun-18, Aug-21 | B.1.1                | 34 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK2022         | 33 (100.0%)  | May-21, Aug-29 | B.1.1                | 33 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1683         | 19 (100.0%)  | Apr-30, Jul-30 | B.1.1, B.1.1.1       | 19 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1205         | 16 (100.0%)  | May-03, Jul-24 | B.1.1, B.1.1.1       | 16 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1060         | 14 (100.0%)  | Mar-23, May-10 | B.1.1                | 14 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK352          | 14 (100.0%)  | Aug-07, Sep-02 | B.1.113, B.1, B.1.36 | 14 taxa  |
+----------------+--------------+----------------+----------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_BIRM_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_BIRM_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_BIRM_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by BIRM is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_BIRM_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_BIRM_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 150 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_BIRM_map_1.png){#map }







There are some sequences with locations that are not matched to real Admin2 regions, some manual curation required.





Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+----------------------+----------+
| Lineage name   | England      | Date range     | Global lineage       | Total    |
+================+==============+================+======================+==========+
| UK1951         | 152 (100.0%) | Mar-23, Aug-09 | B.1.1, B.1.1.1       | 152 taxa |
+----------------+--------------+----------------+----------------------+----------+
| UK5            | 89 (100.0%)  | Mar-23, Sep-02 | B.1.1, B.1.1.10      | 89 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1134         | 59 (100.0%)  | Apr-28, Aug-06 | B.1.1                | 59 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1312         | 36 (100.0%)  | Jul-11, Jul-14 | B.1.1                | 36 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1153         | 34 (100.0%)  | Jun-18, Aug-21 | B.1.1                | 34 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK2022         | 33 (100.0%)  | May-21, Aug-29 | B.1.1                | 33 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1683         | 19 (100.0%)  | Apr-30, Jul-30 | B.1.1, B.1.1.1       | 19 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1205         | 16 (100.0%)  | May-03, Jul-24 | B.1.1, B.1.1.1       | 16 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK1060         | 14 (100.0%)  | Mar-23, May-10 | B.1.1                | 14 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK352          | 14 (100.0%)  | Aug-07, Sep-02 | B.1.113, B.1, B.1.36 | 14 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK72           | 11 (100.0%)  | Mar-22, May-12 | B, B.2               | 11 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK167          | 10 (100.0%)  | Mar-23, May-25 | B.1                  | 10 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK49           | 10 (100.0%)  | Mar-23, Aug-06 | B.9                  | 10 taxa  |
+----------------+--------------+----------------+----------------------+----------+
| UK2087         | 8 (100.0%)   | Apr-16, May-18 | B.1.1                | 8 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK973          | 8 (100.0%)   | Jul-14, Jul-24 | B.1, B.1.36          | 8 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK698          | 7 (100.0%)   | Jul-14, Jul-26 | B.1.1                | 7 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK1641         | 7 (100.0%)   | May-25, Jun-05 | B.1.1                | 7 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK1037         | 6 (100.0%)   | Mar-24, Jun-02 | B.1.1                | 6 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK1082         | 6 (100.0%)   | May-02, Jun-10 | B.1                  | 6 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK1881         | 6 (100.0%)   | Apr-23, Apr-30 | B.1.1                | 6 taxa   |
+----------------+--------------+----------------+----------------------+----------+
| UK331          | 6 (100.0%)   | Jul-06, Aug-14 | B.1, B.1.36          | 6 taxa   |
+----------------+--------------+----------------+----------------------+----------+

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


| Week commencing   |   UK1951 |   UK5 |   UK1134 |   UK1153 |   UK2022 |   UK352 |   UK49 |   UK331 |
|:------------------|---------:|------:|---------:|---------:|---------:|--------:|-------:|--------:|
| 2020-03-22        |        2 |     2 |        0 |        0 |        0 |       0 |      1 |       0 |
| 2020-04-12        |        1 |     1 |        0 |        0 |        0 |       0 |      0 |       0 |
| 2020-04-19        |        2 |     4 |        0 |        0 |        0 |       0 |      0 |       0 |
| 2020-04-26        |        7 |     9 |        1 |        0 |        0 |       0 |      0 |       0 |
| 2020-05-03        |        3 |    11 |        0 |        0 |        0 |       0 |      0 |       0 |
| 2020-05-10        |       12 |    14 |        3 |        0 |        0 |       0 |      0 |       0 |
| 2020-05-17        |       13 |     2 |        1 |        0 |        1 |       0 |      0 |       0 |
| 2020-05-24        |        8 |     1 |        4 |        0 |        2 |       0 |      0 |       0 |
| 2020-05-31        |        4 |     4 |        5 |        0 |        0 |       0 |      0 |       0 |
| 2020-06-07        |        3 |     3 |        1 |        0 |        3 |       0 |      0 |       0 |
| 2020-06-14        |        2 |     1 |        1 |        1 |        0 |       0 |      0 |       0 |
| 2020-06-21        |        2 |     0 |        0 |        0 |        0 |       0 |      0 |       0 |
| 2020-06-28        |        1 |     1 |        0 |        0 |        0 |       0 |      0 |       0 |
| 2020-07-05        |        0 |     1 |        0 |        0 |        0 |       0 |      0 |       1 |
| 2020-07-12        |        1 |     2 |        0 |        0 |        2 |       0 |      0 |       1 |
| 2020-07-19        |        0 |     1 |        1 |        0 |        2 |       0 |      0 |       1 |
| 2020-07-26        |        0 |     1 |        2 |        0 |        1 |       0 |      0 |       0 |
| 2020-08-02        |        0 |     1 |        1 |        0 |        1 |       1 |      1 |       0 |
| 2020-08-09        |        1 |     1 |        0 |        0 |        2 |       1 |      0 |       1 |
| 2020-08-16        |        0 |     1 |        0 |        2 |        0 |       2 |      0 |       0 |
| 2020-08-23        |        0 |     0 |        0 |        0 |        1 |       5 |      0 |       0 |
| 2020-08-30        |        0 |     2 |        0 |        0 |        0 |       3 |      0 |       0 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-22 |                            0 |                                1 |       1 |
| 2020-03-23 |                            7 |                                5 |      12 |
| 2020-03-24 |                            7 |                                5 |      12 |
| 2020-03-25 |                            3 |                                7 |      10 |
| 2020-03-26 |                            4 |                                2 |       6 |
| 2020-03-27 |                            2 |                                0 |       2 |
| 2020-04-15 |                            0 |                                1 |       1 |
| 2020-04-16 |                            2 |                                1 |       3 |
| 2020-04-23 |                            0 |                                3 |       3 |
| 2020-04-24 |                            1 |                                0 |       1 |
| 2020-04-26 |                            2 |                                0 |       2 |
| 2020-04-27 |                            1 |                                0 |       1 |
| 2020-04-28 |                            1 |                                5 |       6 |
| 2020-04-29 |                            2 |                                2 |       4 |
| 2020-04-30 |                            2 |                                1 |       3 |
| 2020-05-01 |                            1 |                                1 |       2 |
| 2020-05-02 |                            1 |                                2 |       3 |
| 2020-05-03 |                            1 |                                2 |       3 |
| 2020-05-04 |                            2 |                                0 |       2 |
| 2020-05-05 |                            3 |                                0 |       3 |
| 2020-05-06 |                            1 |                                0 |       1 |
| 2020-05-09 |                            1 |                                0 |       1 |
| 2020-05-10 |                            1 |                                1 |       2 |
| 2020-05-11 |                            1 |                                0 |       1 |
| 2020-05-12 |                            1 |                                0 |       1 |
| 2020-05-13 |                            1 |                                0 |       1 |
| 2020-05-15 |                            4 |                                0 |       4 |
| 2020-05-19 |                            1 |                                1 |       2 |
| 2020-05-20 |                            1 |                                0 |       1 |
| 2020-05-21 |                            0 |                                1 |       1 |
| 2020-05-22 |                            1 |                                0 |       1 |
| 2020-05-25 |                            0 |                                1 |       1 |
| 2020-05-27 |                            0 |                                1 |       1 |
| 2020-05-28 |                            1 |                                0 |       1 |
| 2020-06-02 |                            2 |                                0 |       2 |
| 2020-06-05 |                            1 |                                0 |       1 |
| 2020-06-08 |                            1 |                                0 |       1 |
| 2020-06-11 |                            0 |                                1 |       1 |
| 2020-06-18 |                            0 |                                2 |       2 |
| 2020-06-25 |                            1 |                                0 |       1 |
| 2020-07-03 |                            0 |                                1 |       1 |
| 2020-07-06 |                            0 |                                1 |       1 |
| 2020-07-11 |                            0 |                                1 |       1 |
| 2020-07-14 |                            2 |                                2 |       4 |
| 2020-07-23 |                            0 |                                1 |       1 |
| 2020-08-02 |                            0 |                                1 |       1 |
| 2020-08-04 |                            1 |                                0 |       1 |
| 2020-08-07 |                            0 |                                1 |       1 |
| 2020-08-13 |                            0 |                                1 |       1 |
| 2020-08-15 |                            1 |                                2 |       3 |
| 2020-08-16 |                            0 |                                1 |       1 |
| 2020-08-24 |                            1 |                                0 |       1 |
| 2020-08-28 |                            1 |                                0 |       1 |
| 2020-09-02 |                            0 |                                1 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-22 |         1 |
| 2020-03-23 |        20 |
| 2020-03-24 |        26 |
| 2020-03-25 |        23 |
| 2020-03-26 |        25 |
| 2020-03-27 |        11 |
| 2020-04-13 |         2 |
| 2020-04-14 |         3 |
| 2020-04-15 |         6 |
| 2020-04-16 |         7 |
| 2020-04-23 |        11 |
| 2020-04-24 |         1 |
| 2020-04-25 |         1 |
| 2020-04-26 |         9 |
| 2020-04-27 |         5 |
| 2020-04-28 |        19 |
| 2020-04-29 |        15 |
| 2020-04-30 |        12 |
| 2020-05-01 |         3 |
| 2020-05-02 |        11 |
| 2020-05-03 |         7 |
| 2020-05-04 |         5 |
| 2020-05-05 |        13 |
| 2020-05-06 |         5 |
| 2020-05-07 |         4 |
| 2020-05-08 |         2 |
| 2020-05-09 |         5 |
| 2020-05-10 |        11 |
| 2020-05-11 |        11 |
| 2020-05-12 |         8 |
| 2020-05-13 |         7 |
| 2020-05-14 |         6 |
| 2020-05-15 |         8 |
| 2020-05-16 |         9 |
| 2020-05-17 |         2 |
| 2020-05-18 |         2 |
| 2020-05-19 |        12 |
| 2020-05-20 |         7 |
| 2020-05-21 |         7 |
| 2020-05-22 |        12 |
| 2020-05-23 |         5 |
| 2020-05-24 |        13 |
| 2020-05-25 |         9 |
| 2020-05-26 |        11 |
| 2020-05-27 |        13 |
| 2020-05-28 |        11 |
| 2020-05-29 |        10 |
| 2020-05-30 |         1 |
| 2020-05-31 |         1 |
| 2020-06-01 |         3 |
| 2020-06-02 |        10 |
| 2020-06-03 |         3 |
| 2020-06-04 |         3 |
| 2020-06-05 |         9 |
| 2020-06-06 |         6 |
| 2020-06-07 |         5 |
| 2020-06-08 |         7 |
| 2020-06-09 |         9 |
| 2020-06-10 |         3 |
| 2020-06-11 |         3 |
| 2020-06-12 |         3 |
| 2020-06-13 |         3 |
| 2020-06-14 |         2 |
| 2020-06-15 |         2 |
| 2020-06-16 |         2 |
| 2020-06-18 |         3 |
| 2020-06-19 |         2 |
| 2020-06-20 |         1 |
| 2020-06-22 |         1 |
| 2020-06-25 |         2 |
| 2020-06-30 |         1 |
| 2020-07-03 |         2 |
| 2020-07-06 |         1 |
| 2020-07-08 |         1 |
| 2020-07-10 |         1 |
| 2020-07-11 |         8 |
| 2020-07-12 |         2 |
| 2020-07-13 |        29 |
| 2020-07-14 |        26 |
| 2020-07-15 |         1 |
| 2020-07-16 |         9 |
| 2020-07-17 |        14 |
| 2020-07-18 |         2 |
| 2020-07-19 |         1 |
| 2020-07-20 |         5 |
| 2020-07-21 |         5 |
| 2020-07-22 |         8 |
| 2020-07-23 |         8 |
| 2020-07-24 |         2 |
| 2020-07-25 |         1 |
| 2020-07-26 |         1 |
| 2020-07-27 |         1 |
| 2020-07-29 |         1 |
| 2020-07-30 |         2 |
| 2020-08-01 |         1 |
| 2020-08-02 |         3 |
| 2020-08-03 |         1 |
| 2020-08-04 |         3 |
| 2020-08-05 |         1 |
| 2020-08-06 |         2 |
| 2020-08-07 |         2 |
| 2020-08-08 |         4 |
| 2020-08-09 |         1 |
| 2020-08-10 |         1 |
| 2020-08-11 |         1 |
| 2020-08-13 |         3 |
| 2020-08-14 |         1 |
| 2020-08-15 |         6 |
| 2020-08-16 |         4 |
| 2020-08-19 |        15 |
| 2020-08-20 |        16 |
| 2020-08-21 |         8 |
| 2020-08-23 |         2 |
| 2020-08-24 |         2 |
| 2020-08-25 |         1 |
| 2020-08-27 |         1 |
| 2020-08-28 |         3 |
| 2020-08-29 |         1 |
| 2020-09-01 |         3 |
| 2020-09-02 |         4 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2          | Country   |   Number of sequences | Sequence group   |
|:----------------|:----------|----------------------:|:-----------------|
| DERBYSHIRE      | England   |                     1 | 1-10             |
| EDINBURGH       | Scotland  |                    15 | 10-100           |
| ESSEX           | England   |                     1 | 1-10             |
| HEREFORDSHIRE   | England   |                    32 | 10-100           |
| HERTFORDSHIRE   | England   |                     3 | 1-10             |
| SHROPSHIRE      | England   |                     2 | 1-10             |
| SOUTH YORKSHIRE | England   |                     1 | 1-10             |
| STAFFORDSHIRE   | England   |                    39 | 10-100           |
| STOKE-ON-TRENT  | England   |                     1 | 1-10             |
| WARWICKSHIRE    | England   |                     4 | 1-10             |
| WEST MIDLANDS   | England   |                   426 | 400-500          |
| WORCESTERSHIRE  | England   |                    12 | 10-100           |

<div style="page-break-after: always"></div>






