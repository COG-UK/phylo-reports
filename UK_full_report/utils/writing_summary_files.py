import pandas as pd
import os

def write_summary_table(dataframe, output_dir):

    dataframe.to_csv(output_dir + "lineage_summary.tsv", sep="\t")

def write_microreact_csv(taxa, output_dir):

    fw = open(output_dir + "microreact.csv", 'w')
    fw.write("taxon,uk_lineage\n")

    for tax in taxa:
        lineage = tax.introduction
    
        fw.write(tax.id + "," + lineage + "\n")

    fw.close()


def write_merges_file(merged_dict, lineage_dict, output_dir):

    UK_merged = {}

    fw = open(output_dir + "merged_lineages.csv", 'w')
    fw.write("UK_lineage_designation,Acctrans_designation\n")

    count = 0

    for uk, value in merged_dict.items():
        if value:
            acctrans = list(lineage_dict[uk].acctrans_designations)[0]

            count += 1

            fw.write(uk + "," + acctrans + "\n")

    fw.close()

def write_splits_file(splits, output_dir):

    fw = open(output_dir + "split_lineages.csv", 'w')
    fw.write("UK_lineage,Acctrans_designation\n")

    for lin in splits:
        new_line = lin.id + "," + ",".join([str(j) for j in lin.acctrans_designations])
        fw.write(new_line + "\n")

    fw.close()

def write_omitteds(omitted, output_dir):

    fw = open(output_dir + "sequences_not_in_metadata.csv", 'w')

    for i in omitted:

        fw.write(i + "\n")

    fw.close()

def write_unclears(taxa, output_dir):
    fw = open(output_dir + "unclear_taxon_assignment.csv", 'w')
    fw.write("taxon,acctrans_assignation\n")

    for tax in taxa:
        if tax.unclear:
            fw.write(tax.id + "," + tax.acctrans + "\n")

    fw.close()

def write_new_lins(new_lineages, output_dir):

    fw = open(output_dir + "new_lineages.csv", 'w')

    for i,v in new_lineages.items():
        fw.write(i + "," + v + "\n")
    
    fw.close()

def write_summary_files(overall_output_dir, dataframe, merged_dict, obj_dict, lineage_objects, omitted, taxa, new_lineages, week):

    output_dir = overall_output_dir + "summary_files_" + week + "/"

    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    write_summary_table(dataframe, output_dir)
    write_merges_file(merged_dict, obj_dict,output_dir)
    #write_splits_file(splits, output_dir)
    write_omitteds(omitted, output_dir)
    write_unclears(taxa, output_dir)
    write_new_lins(new_lineages, output_dir)
    write_microreact_csv(taxa, output_dir)
