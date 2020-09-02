from pweave import *
import sys
import subprocess
import argparse
import os
from pathlib import Path

class Error (Exception): pass

scripts_directory = os.path.dirname(__file__)

def make_report(input_directory, metadata_file, name_stem, output_directory, week, sequencing_centre, adm1, pillar2, scripts_directory):
    
    fd = os.path.join(output_directory, "figures")
    sd = os.path.join(output_directory, "summary_files")

    Path(fd).mkdir(parents=True, exist_ok=True)
    Path(sd).mkdir(parents=True, exist_ok=True)


    pmd_string = os.path.join(output_directory, name_stem + ".pmd")
    pmd_file = open(pmd_string, 'w')

    md_template = os.path.join(scripts_directory, 'UK_report_templatev2.pmd')

    change_line_dict = {"summary_output": f'summary_output = "{sd}"\n',
                        "figdir": f'figdir = "{fd}"\n',
                        "input_directory": f'input_directory = "{input_directory}"\n',
                        "name_stem": f'name_stem = "{name_stem}"\n',
                        "metadata_file": f'metadata_file = "{metadata_file}"\n',
                        "week": f'week = "{week}"\n',
                        "scripts_directory": f'scripts_directory = "{scripts_directory}"\n',
                        "sequencing_centre": f'sequencing_centre = "{sequencing_centre}"\n',
                        "adm1": f'adm1 = "{adm1}"\n',
                        "pillar2": f'pillar2 = "{pillar2}"\n'}

    with open(md_template) as f:
            for l in f:
                if "##CHANGE" in l:
                    for key in change_line_dict:
                        if key in l:
                            new_l = change_line_dict[key]
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
    parser.add_argument("--sc", default="", type=str, help="Optional filter by sequencing centre, e.g. CAMB/NORW/PHWC, default all centres")
    parser.add_argument("--adm", default="", type=str, help="Optional filter by adm1 region")
    parser.add_argument("--p2", required=False, default=False, help="Optional filter by pillar2 sequences")

    parser.add_argument("--pdf", action="store_true", help="tries to run pandoc conversion to pdf")

    args = parser.parse_args()

    make_report(args.i, args.m, args.s, args.od, args.w, args.sc, args.adm, args.p2, scripts_directory)
    if args.pdf:
        convert_report_to_pdf(args.s, scripts_directory)

if __name__ == "__main__":
    main()
