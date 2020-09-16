







# Lineages report for LOND




This report gives summaries of UK specific lineages sequenced by LOND for week 2020-09-13. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-14. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
715 sequences in the UK from the sequencing centre LOND have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 9 and the maximum is 541


Sequences which were replicates or too error-prone were removed from this analysis.



165 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 20 that remain:
18 are pending extinction, ie last seen three weeks ago.
1 has gone quiet, ie hasn't been seen this week.
1 has reactivated.



The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lineages is found in the appendix, along with the raw data for all of the other figures.


Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expected given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-07-20


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



+----------------+--------------+----------------+---------------------+----------+
| Lineage name   | England      | Date range     | Global lineage      | Total    |
+================+==============+================+=====================+==========+
| UK5            | 133 (100.0%) | Mar-27, May-14 | B.1.1.10, B.1.1     | 133 taxa |
+----------------+--------------+----------------+---------------------+----------+
| UK175          | 59 (100.0%)  | Mar-31, Apr-20 | B.1.88, B.1, B.1.76 | 59 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK5741         | 41 (100.0%)  | Mar-30, Apr-19 | B.1                 | 41 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK2906         | 37 (100.0%)  | Mar-27, May-04 | B.1                 | 37 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK719          | 25 (100.0%)  | Mar-31, Apr-19 | B.1.1               | 25 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK902          | 23 (100.0%)  | Apr-04, Apr-18 | B.1.1               | 23 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK917          | 19 (100.0%)  | Apr-02, Apr-18 | B.1.1               | 19 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK107          | 17 (100.0%)  | Mar-27, Apr-20 | B.2.1               | 17 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK2916         | 15 (100.0%)  | Mar-27, Apr-19 | B.1                 | 15 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK678          | 11 (100.0%)  | Apr-02, Apr-17 | B.1.1               | 11 taxa  |
+----------------+--------------+----------------+---------------------+----------+


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above.


![Number of sequences sampled in a lineage by country](figures/report_LOND_stacked_bars_by_country_1.png){#stacked_bars_by_country }


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



![Lineages by number of adm2 regions present by epiweek](figures/report_LOND_geog_plot_1.png){#geog_plot }









These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.



![Timeline of lineages, sized by number of sequences from each country.](figures/report_LOND_make_timeline_1.png){#make_timeline }




The date of first sequence in the cluster sampled by LOND is shown in figure five for every cluster with date information.



![Lineage starts per week, split by singletons and non-singletons](figures/report_LOND_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](figures/report_LOND_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.





```
There are 526 sequences without enough geographical information to map
from this centre.
```

![Map showing the number of sequences sampled by adm2 region](figures/report_LOND_map_1.png){#map }












Other results modules for UK lineage analysis can be added in here if required.

<div style="page-break-after: always"></div>

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


+----------------+--------------+----------------+---------------------+----------+
| Lineage name   | England      | Date range     | Global lineage      | Total    |
+================+==============+================+=====================+==========+
| UK5            | 133 (100.0%) | Mar-27, May-14 | B.1.1.10, B.1.1     | 133 taxa |
+----------------+--------------+----------------+---------------------+----------+
| UK175          | 59 (100.0%)  | Mar-31, Apr-20 | B.1.88, B.1, B.1.76 | 59 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK5741         | 41 (100.0%)  | Mar-30, Apr-19 | B.1                 | 41 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK2906         | 37 (100.0%)  | Mar-27, May-04 | B.1                 | 37 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK719          | 25 (100.0%)  | Mar-31, Apr-19 | B.1.1               | 25 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK902          | 23 (100.0%)  | Apr-04, Apr-18 | B.1.1               | 23 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK917          | 19 (100.0%)  | Apr-02, Apr-18 | B.1.1               | 19 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK107          | 17 (100.0%)  | Mar-27, Apr-20 | B.2.1               | 17 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK2916         | 15 (100.0%)  | Mar-27, Apr-19 | B.1                 | 15 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK678          | 11 (100.0%)  | Apr-02, Apr-17 | B.1.1               | 11 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK9            | 11 (100.0%)  | Mar-31, Apr-20 | B.1.13, B.1         | 11 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK2913         | 11 (100.0%)  | Mar-27, Apr-18 | B.1.11, B.1         | 11 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK1205         | 10 (100.0%)  | Mar-31, Apr-17 | B.1.1.1, B.1.1      | 10 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK1060         | 10 (100.0%)  | Mar-31, Apr-19 | B.1.1               | 10 taxa  |
+----------------+--------------+----------------+---------------------+----------+
| UK387          | 9 (100.0%)   | Mar-31, Apr-17 | B.1                 | 9 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK37           | 9 (100.0%)   | Apr-02, Apr-19 | B.1.30, B.1         | 9 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK894          | 9 (100.0%)   | Apr-04, Apr-17 | B.1.1               | 9 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK945          | 8 (100.0%)   | Apr-06, Apr-19 | B.1.1               | 8 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK2464         | 7 (100.0%)   | Mar-30, Apr-19 | B.1.11, B.1         | 7 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK2062         | 7 (100.0%)   | Mar-31, Apr-11 | B.1.1               | 7 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK515          | 7 (100.0%)   | Apr-04, Apr-20 | B.1                 | 7 taxa   |
+----------------+--------------+----------------+---------------------+----------+
| UK1153         | 6 (100.0%)   | Apr-03, Apr-11 | B.1.1               | 6 taxa   |
+----------------+--------------+----------------+---------------------+----------+

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


| Week commencing   |   UK5 |   UK175 |   UK5741 |   UK2906 |   UK719 |   UK902 |   UK917 |   UK107 |   UK2916 |   UK678 |
|:------------------|------:|--------:|---------:|---------:|--------:|--------:|--------:|--------:|---------:|--------:|
| 2020-03-22        |     3 |       0 |        0 |        1 |       0 |       0 |       0 |       1 |        1 |       0 |
| 2020-03-29        |     4 |       4 |        2 |        6 |       2 |       1 |       3 |       2 |        1 |       1 |
| 2020-04-05        |     4 |       4 |        2 |        5 |       1 |       2 |       0 |       1 |        2 |       2 |
| 2020-04-12        |     3 |       2 |        1 |        2 |       1 |       1 |       2 |       1 |        1 |       1 |
| 2020-04-19        |     1 |       1 |        1 |        0 |       1 |       0 |       0 |       1 |        1 |       0 |
| 2020-04-26        |     0 |       0 |        0 |        1 |       0 |       0 |       0 |       0 |        0 |       0 |
| 2020-05-03        |     0 |       0 |        0 |        1 |       0 |       0 |       0 |       0 |        0 |       0 |
| 2020-05-10        |     1 |       0 |        0 |        0 |       0 |       0 |       0 |       0 |        0 |       0 |

<div style="page-break-after: always"></div>



Table S4 is not appropriate for this report and so has been omitted.





<div style="page-break-after: always"></div>

**Table S5** Raw data for figure five showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-03-19 |                            0 |                                1 |       1 |
| 2020-03-27 |                            2 |                                7 |       9 |
| 2020-03-30 |                            0 |                                2 |       2 |
| 2020-03-31 |                            4 |                                7 |      11 |
| 2020-04-01 |                            4 |                                0 |       4 |
| 2020-04-02 |                            7 |                                9 |      16 |
| 2020-04-03 |                            8 |                                8 |      16 |
| 2020-04-04 |                           14 |                                9 |      23 |
| 2020-04-06 |                           10 |                                5 |      15 |
| 2020-04-08 |                           11 |                                3 |      14 |
| 2020-04-09 |                            1 |                                0 |       1 |
| 2020-04-10 |                            5 |                                0 |       5 |
| 2020-04-11 |                            3 |                                2 |       5 |
| 2020-04-12 |                            1 |                                0 |       1 |
| 2020-04-13 |                            4 |                                2 |       6 |
| 2020-04-14 |                            8 |                                6 |      14 |
| 2020-04-15 |                           13 |                                0 |      13 |
| 2020-04-16 |                            4 |                                0 |       4 |
| 2020-04-17 |                            5 |                                0 |       5 |
| 2020-04-18 |                            6 |                                1 |       7 |
| 2020-04-19 |                            6 |                                0 |       6 |
| 2020-04-20 |                            4 |                                0 |       4 |
| 2020-04-22 |                            1 |                                0 |       1 |
| 2020-04-23 |                            1 |                                0 |       1 |
| 2020-04-25 |                            1 |                                0 |       1 |
| 2020-05-11 |                            1 |                                0 |       1 |
| 2020-05-14 |                            1 |                                0 |       1 |

<div style="page-break-after: always"></div>

**Table S6** Raw data for figure six showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-03-19 |         1 |
| 2020-03-27 |        12 |
| 2020-03-30 |         3 |
| 2020-03-31 |        32 |
| 2020-04-01 |        10 |
| 2020-04-02 |        39 |
| 2020-04-03 |        41 |
| 2020-04-04 |        69 |
| 2020-04-06 |        57 |
| 2020-04-08 |        53 |
| 2020-04-09 |         8 |
| 2020-04-10 |        21 |
| 2020-04-11 |        36 |
| 2020-04-12 |         3 |
| 2020-04-13 |        17 |
| 2020-04-14 |        61 |
| 2020-04-15 |        66 |
| 2020-04-16 |        40 |
| 2020-04-17 |        55 |
| 2020-04-18 |        34 |
| 2020-04-19 |        27 |
| 2020-04-20 |        14 |
| 2020-04-22 |         2 |
| 2020-04-23 |         5 |
| 2020-04-25 |         1 |
| 2020-04-29 |         1 |
| 2020-05-04 |         1 |
| 2020-05-11 |         1 |
| 2020-05-14 |         5 |

<div style="page-break-after: always"></div>

**Table S7** Raw data for the figure seven with the number of sequences assigned to each admin2 region.


| Admin2          | Country   |   Number of sequences | Sequence group   |
|:----------------|:----------|----------------------:|:-----------------|
| ABERDEEN        | Scotland  |                     1 | 1-10             |
| BEDFORDSHIRE    | England   |                     1 | 1-10             |
| BERKSHIRE       | England   |                     1 | 1-10             |
| BUCKINGHAMSHIRE | England   |                     1 | 1-10             |
| ESSEX           | England   |                     4 | 1-10             |
| GREATER LONDON  | England   |                   132 | 100-200          |
| HERTFORDSHIRE   | England   |                    41 | 10-100           |
| KENT            | England   |                     3 | 1-10             |
| MERSEYSIDE      | England   |                     1 | 1-10             |
| SURREY          | England   |                     4 | 1-10             |

<div style="page-break-after: always"></div>






