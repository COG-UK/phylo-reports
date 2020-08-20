pandoc "$1" \
    -V linkcolor:blue \
    -V geometry:a4paper \
    -V geometry:margin=2cm \
    -V mainfont="Helvetica Neue" \
    -V monofont="Helvetica Neue" \
    -V fontsize=10pt \
    --template="$2" \
    --latex-engine=pdflatex \
    -o "$3"
