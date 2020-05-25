
#!/bin/bash

CLIMBSTEM=$1
WEEK=$2
TREES=$3


centres=(LIVE PHWC CAMB NORW GLAS EDIN SHEF EXET NOTT PORT OXON NORT NIRE LOND)

metadata=report_metadata.csv

echo making sure report scripts are up to date and getting ready

git pull

conda activate report

pip install .

echo copying files

scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/COG/$metadata UK_full_report/results/

if $TREES
then
scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/4/*/trees/* UK_full_report/results/$WEEK/tree_files/
fi

echo making md file
 
if $TREES
then 
generate_report --m UK_full_report/results/$metadata --w $WEEK --s UK_report --od UK_full_report/results/--i UK_full_report/results/tree_files/
else
generate_report --m UK_full_report/results/$metadata --w $WEEK --s UK_report --od UK_full_report/results/

echo generating centre specific reports

#for centre in ${centres[*]}; do
#generate_report --m UK_full_report/results/$metadata --w $WEEK --s report_$centre --od UK_full_report/regional_reports/results/results_$centre/
#done
#generate_report --m ~/VirusEvolution\ Dropbox/Group/Coronavirus_projects/UK_project/2020-05-01_rerun2/cog_gisaid.with_all_traits.with_phylotype_traits.fixed_epiweeks.csv --w 2020-05-01 --s UK_report_$WEEK --od UK_full_report/results/2020-05-01/report_files/ 

fi

#echo parsing markdown file

#python3 parse_md_file.py --md $MDFILE --p md_with_figs_$WEEK.md

echo deactivating env

conda deactivate

echo converting to pdf

sh UK_full_report/call_pandoc.sh UK_report.md UK_full_report/utils/latex_template/latex_template.latex UK_report.pdf

#for centre in ${centres[*]}; do
#sh UK_full_report/call_pandoc.sh report_$centre.md UK_full_report/utils/latex_template/latex_template.latex report_$centre.pdf
#done

echo copying back to climb

rm UK_full_report/results/$metadata

#scp UK_report.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/
#scp UK_report.md  climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/
#scp -r UK_full_report/results/figures climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/
#scp -r UK_full_report/results/summary_files climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/

#scp -r UK_full_report/regional_reports climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/

#for centre in ${centres[*]}; do
#scp report_$centre.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/results_$centre/
#scp report_$centre.md  climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/results_$centre/
#done


echo tidying

mv UK_report.md UK_full_report/results/
mv UK_report.pdf UK_full_report/results/
rm UK_report.pmd


#for centre in ${centres[*]}; do
#mv report_$centre.md UK_full_report/regional_reports/results_$centre
#mv report_$centre.pdf UK_full_report/regional_reports/results_$centre
#rm report_$centre.pmd
#done


echo done!


