CLIMBSTEM=$1
WEEK=$2

countries=(England Scotland Wales Northern_Ireland)

metadata=report_metadata.csv

pip install .

scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/COG/$metadata UK_full_report/results/

for country in ${countries[*]}; do
echo generating $country report
generate_report --m UK_full_report/results/$metadata --w $WEEK --s $country --od UK_full_report/adm1_reports/$country/ --adm $country
done

conda deactivate

echo converting report

for country in ${countries[*]}; do
echo converting $country to pdf
sh UK_full_report/call_pandoc.sh $country.md UK_full_report/utils/latex_template/latex_template.latex $country.pdf
done

rm UK_full_report/results/$metadata


for country in ${country[*]}; do
scp $country.pdf climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/adm1_reports/$country
scp $country.md climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$CLIMBSTEM/publish/phylogenetics/reports/adm1_reports/$country
done


for country in ${countries[*]}; do
mv $country.md UK_full_report/adm1_reports/$country
mv $country.pdf UK_full_report/regional_reports/$country
rm $country.pmd
done
