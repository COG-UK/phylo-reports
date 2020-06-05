
# UK lineages summary report








This report gives summaries of UK specific lineages sequenced by PORT for week 2020-05-29. 
There are time lags due to batching, curation and analysis, the most recently sampled sequence is 2020-05-03. The analysis (eg time since last sample) is therefore undertaken from this date.
<br/>
29 sequences in the UK from the sequencing centre PORT have been included in this analysis.


A few notes: the size of a lineage may be due to a low amount of transmission of this lineage, but it is likely also that it just hasn't been sampled as frequently, especially for newer lineages.
It's also important to realise that these lineages are *estimates* of how we think the virus is spreading in the UK after being introduced from abroad, as the low evolutionary rate of the virus makes it difficult to separate lineages with certainty.



The minimum number of introductions is 6130 and the maximum is 9084


Sequences which were replicates or too error-prone were removed from this analysis.



8 are lineages which only contained five sequences or fewer, and so have been left out of visualisation in the interests of clarity


Furthermore, those sequences which haven't been sampled in the last month are not shown.



Of the 1 that remain:
1 lineage has been continuously circulating.


The following table contains information about the ten largest lineages lineages and the number of sequences the dataset. Information about other lienages is found in the appendix, along with the raw data for all of the other figures.

Each entry is the count of sequences from each lineage in each country, with the percentage of the total sequences from that lineage that this count represents.

"Activity score" is calculated by taking the average gap between sampling for each lineage, and dividing it by the number of days since the lineage was last sampled. Therefore the higher the number, the more active the lineage is.
If the score is above 1, then it has been sampled *more* recently than expected given its average gap size. We might interpret this as an increase in activity.
If the score is below 1, it has been sampled *less* recently than expect given its average gap size, so we might interpret this as a decrease in activity.



The global lineages are correct as of the data release on 2020-05-19


It is written to "summary_files" as "lineage_summary.tsv" for further use, and the full list of lineages is available in the same directory as "all_lineages.csv"



| Lineage name   | England    | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) |   Activity score |
|:---------------|:-----------|:---------------|------------------:|:-----------------|--------------------------------:|-----------------:|
| UK2464         | 6 (100.0%) | Apr-24, Apr-27 |                 6 | B.1.p11          |                               6 |              0.1 |


These data is represented in the figure one. Note that the number of sequences is likely to be due more to differing sampling efforts in different regions, rather than genuine differences in numbers of cases. 

The raw data for this bar chart are in the table above. 


![Number of sequences sampled in a lineage by country](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_stacked_bars_by_country_1.png){#stacked_bars_by_country }


Different sequencing centres have different delays in turn around from receipt of samples to submission of sequence data. 
This will affect all of the figures shown after this if lineages have geographical variation, as some regions have less up to date data.


![Lag since the most recent sequence from each sequencing centre to most current date](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_lag_fig_1.png){#lag_fig }


The relative growth and decline of the ten most sampled lineages in terms of number of counties they are present in is shown in figure three. 



![Lineages by number of adm2 regions present by epiweek](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_geog_plot_1.png){#geog_plot }







These lineages are shown on the timeline. Each line represents the length of the cluster, from oldest to most recent sampling date.
The dots are sized by the number of sequences taken on that date, and again are colour coded by country.
The raw data has been written to a summary file.




![Timeline of lineages, sized by number of sequences from each country.](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_make_timeline_1.png){#make_timeline }


The date of first sequence in the cluster is shown in figure five for every cluster with date information. 






![Lineage starts per week, split by singletons and non-singletons](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_firsts_plot_1.png){#firsts_plot }

For comparison, here is a plot of the day that every sequence was taken, coloured by country. Note that sequences without dates were not included.


![Sequences taken on each day by country](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_seqs_over_time_1.png){#seqs_over_time }


The map shows the number of sequences sampled in each admin2 region in the UK. The colour scale is the same for all four countries, but with different underlying base colours.



All sequences have been assigned clean adm2 data this week.
![Map showing the number of sequences sampled by adm2 region](UK_full_report/regional_reports/results/results_PORT/figures/report_PORT_map_1.png){#map }









Other results modules for UK lineage analysis can be added in here if required.

\pagebreak

## Appendix









Below are the raw data tables for each of the figures in the report.

**Table S1** Description of all lineages that have been circulating in the last month, and have more than 5 sequences.


| Lineage name   | England    | Date range     |   Total sequences | Global lineage   |   Time since last sample (days) |   Activity score |
|:---------------|:-----------|:---------------|------------------:|:-----------------|--------------------------------:|-----------------:|
| UK2464         | 6 (100.0%) | Apr-24, Apr-27 |                 6 | B.1.p11          |                               6 |              0.1 |

\pagebreak

**Table S2** Raw data for figure three showing the number of admin2 regions a lineage is present in over time


| Week commencing   |   UK2464 |
|:------------------|---------:|
| 2020-04-19        |        1 |
| 2020-04-26        |        1 |

\pagebreak


Table S3 is not appropriate for this report and so has been omitted.




\pagebreak

**Table S4** Raw data for figure six showing when lineages started per day, divided by singletons and non-singletons


| Day        |   Number of singleton starts |   Number of non-singleton starts |   Total |
|:-----------|-----------------------------:|---------------------------------:|--------:|
| 2020-04-24 |                            0 |                                2 |       2 |
| 2020-04-25 |                            0 |                                1 |       1 |
| 2020-04-26 |                            0 |                                1 |       1 |
| 2020-04-27 |                            1 |                                4 |       5 |

\pagebreak

**Table S5** Raw data for figure seven showing the number of sequences taken over time.


| Day        |   England |
|:-----------|----------:|
| 2020-04-24 |         2 |
| 2020-04-25 |         2 |
| 2020-04-26 |         2 |
| 2020-04-27 |        12 |
| 2020-04-28 |         7 |
| 2020-04-29 |         2 |
| 2020-05-02 |         1 |
| 2020-05-03 |         1 |

\pagebreak

**Table S6** Raw data for the map with the number of sequences assigned to each admin2 region.


| Admin2    | Country   |   Number of sequences | Sequence group   |
|:----------|:----------|----------------------:|:-----------------|
| HAMPSHIRE | England   |                    29 | 10-50            |

\pagebreak






