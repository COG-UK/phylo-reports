
#!/bin/bash

CLIMBSTEM=$1
WEEK=$2
TREES=$3


centres=(BIRM SANG PHEC LIVE PHWC CAMB NORW GLAS EDIN SHEF EXET NOTT PORT OXON NORT NIRE LOND)
countries=(England Scotland Wales Northern_Ireland)

metadata=report_metadata.csv

echo making sure report scripts are up to date and getting ready

#git pull

conda activate report

pip install .

echo copying files

scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/COG/$metadata UK_full_report/results/


# if $TREES
# then
# scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/4/*/trees/* UK_full_report/results/$WEEK/tree_files/
# fi

echo making md file
 
# if $TREES
# then 
# generate_report --m UK_full_report/results/$metadata --w $WEEK --s UK_report --od UK_full_report/results/ --i UK_full_report/results/tree_files/
# else
# generate_report --m UK_full_report/results/$metadata --w $WEEK --s UK_report --od UK_full_report/results/

# echo generating centre specific reports

# for centre in ${centres[*]}; do
# echo generating $centre report
# generate_report --m UK_full_report/results/$metadata --w $WEEK --s report_$centre --od UK_full_report/regional_reports/results/results_$centre/ --sc $centre
# done

for country in ${countries[*]}; do
echo generating $country report
generate_report --m UK_full_report/results/$metadata --w $WEEK --s $country --od UK_full_report/results/ --adm $country
done

fi


echo deactivating env

conda deactivate

echo converting to pdf

# sh UK_full_report/call_pandoc.sh UK_report.md UK_full_report/utils/latex_template/latex_template.latex UK_report.pdf

# for centre in ${centres[*]}; do
# echo converting $centre to pdf
# sh UK_full_report/call_pandoc.sh report_$centre.md UK_full_report/utils/latex_template/latex_template.latex report_$centre.pdf
# done

for country in ${countries[*]}; do
echo converting $centre to pdf
sh UK_full_report/call_pandoc.sh $country.md UK_full_report/utils/latex_template/latex_template.latex $country.pdf
done

# echo copying back to climb

rm UK_full_report/results/$metadata

# scp UK_report.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/
# scp UK_report.md  climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/
# scp -r UK_full_report/results/figures climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/
# scp -r UK_full_report/results/summary_files climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/

# scp -r UK_full_report/regional_reports climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/

# scp -r UK_full_report/adm1_reports climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/

# for centre in ${centres[*]}; do
# scp report_$centre.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/regional_reports/
# scp report_$centre.md  climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/regional_reports/
# done

# for country in ${countries[*]}; do
# scp $country.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/adm1_reports/$country
# scp $country.md climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/adm1_reports/$country
# done


echo tidying

mv UK_report.md UK_full_report/results/
mv UK_report.pdf UK_full_report/results/
rm UK_report.pmd


for centre in ${centres[*]}; do
mv report_$centre.md UK_full_report/regional_reports/
mv report_$centre.pdf UK_full_report/regional_reports/
rm report_$centre.pmd
done

for country in ${countries[*]}; do
mv $country.md UK_full_report/adm1_reports/$country
mv $country.pdf UK_full_report/adm1_reports/$country
rm $country.pmd
done


echo done!


