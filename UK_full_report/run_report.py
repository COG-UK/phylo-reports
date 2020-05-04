from pweave import *
import sys
import argparse
import os

parser = argparse.ArgumentParser(description="Report generator script")
parser.add_argument("--i", required=False, help="path to tree and annotations inputs as a string")
parser.add_argument("--m", required=True, help="path to metadata file")
parser.add_argument("--w", required=True, help="most recent date included as a string")
parser.add_argument("--s", default="UK_report", help="output name stem as a string")
parser.add_argument("--od", default="./", help="output directory, default is working directory")
parser.add_argument("--sd", default="./", help="directory in which latex utils are located")

args=parser.parse_args()

#will both need to be full path

input_directory =  str(args.i)
metadata_file = str(args.m)
name_stem = str(args.s)
output_directory = str(args.od)
week = str(args.w)

fd = output_directory + "figures_" + week


pmd_file = open(name_stem + ".pmd", 'w')
pmd_string = name_stem + ".pmd"

script_dir = os.path.dirname(sys.argv[0])
with open("%s/UK_report_templatev2.pmd" %script_dir) as f:
    for l in f:
        if "##CHANGE" in l:
            if "output_directory" in l:
                new_l = 'output_directory = "' + output_directory + '"\n'
            elif "input_directory" in l:
                new_l = 'input_directory = "' + input_directory + '"\n'
            elif "name_stem" in l:
                new_l = 'name_stem = "' + name_stem + '"\n'
            elif "week" in l:
                new_l = 'week = "' + week + '"\n'
            elif "metadata_file" in l:
                new_l = 'metadata_file = "' + metadata_file + '"\n' 
            
        else:
            new_l = l
        
        pmd_file.write(new_l)
    
    
pmd_file.close()


weave(pmd_string, doctype = "pandoc", figdir=fd)
