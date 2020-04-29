pandoc "$1" \
    -V linkcolor:blue \
    -V geometry:a4paper \
    -V geometry:margin=2cm \
    -V mainfont="Helvetica Neue" \
    -V monofont="Helvetica Neue" \
    -V fontsize=12pt \
    --latex-engine=xelatex \
    --template=utils/latex_template.latex \
    -o "$2"