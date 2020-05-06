
#!/bin/bash

WEEK=$1
TREES=$2


mkdir UK_full_report/results/$WEEK/report_files
mkdir UK_full_report/results/$WEEK/report_files/tree_files/

echo making sure report scripts are up to date

git pull
pip install .

echo copying files

scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$WEEK/analysis/5/cog_gisaid.with_all_traits.with_phylotype_traits.csv $WEEK/report_files

scp climb-covid19-hillv@bham.covid19.climb.ac.uk:/cephfs/covid/bham/raccoon-dog/$WEEK/4/*/trees/* $WEEK/report_files/tree_files/

echo making md file
 
if [$TREES==True]
then 
generate_report --m $WEEK/report_files/cog_gisaid.with_traits.with_updated_lineages.csv  --w $WEEK --s UK_report_$WEEK --od UK_full_report/results/$WEEK/report_files/ --i $WEEK/report_files/tree_files/
else
generate_report --m $WEEK/report_files/cog_gisaid.with_traits.with_updated_lineages.csv  --w $WEEK --s UK_report_$WEEK --od UK_full_report/results/$WEEK/report_files/ 
fi

#echo parsing markdown file

#python3 parse_md_file.py --md $MDFILE --p md_with_figs_$WEEK.md

echo converting to pdf

sh ./UK_full_report/call_pandoc.sh $NAMESTEM.md UK_report_$WEEK.pdf





