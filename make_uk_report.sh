
#!/bin/bash

CLIMBSTEM=$1
WEEK=$2
TREES=$3
WEEK2=$4



mkdir UK_full_report/results/$WEEK/report_files

if $TREES
then
mkdir UK_full_report/results/$WEEK/tree_files/
fi

echo making sure report scripts are up to date and getting ready

git pull

conda activate report

pip install .

echo copying files

#scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/analysis/5/cog_gisaid.with_all_traits.with_phylotype_traits.csv UK_full_report/results/$WEEK/report_files

if $TREES
then
scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/4/*/trees/* UK_full_report/results/$WEEK/tree_files/
fi

echo making md file
 
if $TREES
then 
generate_report --m UK_full_report/results/$WEEK/report_files/cog_gisaid.with_all_traits.with_phylotype_traits.csv  --w $WEEK --s UK_report_$WEEK --od UK_full_report/results/$WEEK/report_files/ --i UK_full_report/results/$WEEK/tree_files/
else
#generate_report --m UK_full_report/results/$WEEK/report_files/cog_gisaid.with_all_traits.with_phylotype_traits.csv --w $WEEK --s UK_report_$WEEK --od UK_full_report/results/$WEEK/report_files/ 
generate_report --m ~/VirusEvolution\ Dropbox/Group/Coronavirus_projects/UK_project/2020-05-01_rerun/cog_gisaid.with_all_traits.with_phylotype_traits.fixed_epiweeks.csv --w 2020-05-01 --s UK_report_$WEEK --od UK_full_report/results/2020-05-01/report_files/ 
fi

#echo parsing markdown file

#python3 parse_md_file.py --md $MDFILE --p md_with_figs_$WEEK.md

echo deactivating env

conda deactivate

echo converting UK_report_$WEEK.md to pdf

sh UK_full_report/call_pandoc.sh UK_report_$WEEK.md UK_full_report/utils/latex_template/latex_template.latex UK_report_$WEEK.pdf

echo copying back to climb

#scp UK_report_$WEEK.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/public/
#scp UK_report_$WEEK.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/artifacts/published/$WEEK2/phylogenetics/reports/

echo tidying

mv UK_report_$WEEK.md UK_full_report/results/$WEEK/
mv UK_report_$WEEK.pdf UK_full_report/results/$WEEK/
rm UK_full_report/results/$WEEK/report_files/cog_gisaid.with_all_traits.with_phylotype_traits.csv
rm UK_report_$WEEK.pmd

echo done!


