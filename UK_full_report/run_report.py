from pweave import *
import sys
import subprocess
import argparse
import os

class Error (Exception): pass

scripts_directory = os.path.dirname(__file__)

def make_report(input_directory, metadata_file, name_stem, output_directory, week, scripts_directory):
    fd = os.path.join(output_directory, "figures_" + week)
    pmd_file = open(name_stem + ".pmd", 'w')
    pmd_string = name_stem + ".pmd"

    md_template = os.path.join(scripts_directory, 'UK_report_templatev2.pmd')
    with open(md_template) as f:
        for l in f:
            if "##CHANGE" in l:
                if "output_directory" in l:
                    new_l = 'output_directory = "' + str(output_directory) + '"\n'
                elif "input_directory" in l:
                    new_l = 'input_directory = "' + str(input_directory) + '"\n'
                elif "name_stem" in l:
                    new_l = 'name_stem = "' + str(name_stem) + '"\n'
                elif "week" in l:
                    new_l = 'week = "' + str(week) + '"\n'
                elif "metadata_file" in l:
                    new_l = 'metadata_file = "' + str(metadata_file) + '"\n'
                elif "scripts_directory" in l:
                    new_l = 'scripts_directory = "' + str(scripts_directory) + '"\n'

            else:
                new_l = l

            pmd_file.write(new_l)


    pmd_file.close()


    weave(pmd_string, doctype = "pandoc", figdir=fd)

def syscall(command, allow_fail=False):
    completed_process = subprocess.run(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True)
    if (not allow_fail) and completed_process.returncode != 0:
        print('Error running this command:', command, file=sys.stderr)
        print('Return code:', completed_process.returncode, file=sys.stderr)
        print('\nOutput from stdout:', completed_process.stdout, sep='\n', file=sys.stderr)
        print('\nOutput from stderr:', completed_process.stderr, sep='\n', file=sys.stderr)
        raise Error('Error in system call. Cannot continue')
    print(completed_process.stdout)
    return completed_process

def convert_report_to_pdf(name_stem, scripts_directory):
    call_pandoc = os.path.join(scripts_directory, 'call_pandoc.sh')
    md_file = name_stem + ".md"
    latex_template = os.path.join(scripts_directory, 'utils/latex_template/latex_template.latex')
    pdf_file = name_stem + ".pdf"
    command = " ".join(["sh", call_pandoc, md_file, latex_template, pdf_file])
    syscall(command)

def main():
    parser = argparse.ArgumentParser(description="Report generator script")
    parser.add_argument("--i", required=False, default="", help="path to tree and annotations inputs as a string")
    parser.add_argument("--m", required=True, help="path to metadata file")
    parser.add_argument("--w", required=True, help="most recent date included as a string")
    parser.add_argument("--s", default="UK_report", help="output name stem as a string")
    parser.add_argument("--od", default="./", help="output directory, default is working directory")
    parser.add_argument("--pdf", action="store_true", help="tries to run pandoc conversion to pdf")

    args = parser.parse_args()

    make_report(args.i, args.m, args.s, args.od, args.w, scripts_directory)
    if args.pdf:
        convert_report_to_pdf(args.s, scripts_directory)

if __name__ == "__main__":
    main()
