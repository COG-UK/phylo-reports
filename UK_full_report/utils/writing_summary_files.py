import pandas as pd
import os

def write_summary_table(dataframe, output_dir):

    dataframe.to_csv(output_dir + "/lineage_summary.tsv", sep="\t")

def write_singletons(intro_alls, output_dir):

    fw = open(output_dir + "/singletons.csv", 'w')
    fw.write("UK_lineage,taxon\n")

    for lin in intro_alls:
        if len(lin.taxa) == 1:
            l = lin.id + "," + lin.taxa[0].id + "\n"

            fw.write(l)
    
    fw.close()

def write_splits_file(splits, output_dir):

    fw = open(output_dir + "/split_lineages.csv", 'w')
    fw.write("UK_lineage,Acctrans_designation\n")

    for lin in splits:
        new_line = lin.id + "," + ",".join([str(j) for j in lin.acctrans_designations])
        fw.write(new_line + "\n")

    fw.close()

def write_omitteds(omitted, output_dir):

    fw = open(output_dir + "/sequences_not_in_metadata.csv", 'w')

    for i in omitted:

        fw.write(i + "\n")

    fw.close()


def write_summary_files(overall_output_dir, dataframe, omitted, week, intro_alls, timeline_data):

    output_dir = os.path.join(overall_output_dir, "summary_files_" + week)

    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    write_summary_table(dataframe, output_dir)
    write_omitteds(omitted, output_dir)
    write_singletons(intro_alls, output_dir)

    timeline_data.to_csv(output_dir + "/timeline_raw_data.csv", index=False)
