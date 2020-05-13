# Generate detailed UK report

Generates UK report for weekly COG-UK data

Inputs required:

- metadata csv

- In individual folders for each global lineage (if you want tree rendering):
    - subtrees cut up into newick files


Caveats:
- The lineage subfolders must all be in one directory with nothing else in it
- The date format in the metadata must be yyyy-mm-dd if there are months/days

## Adding figures and text

Scripts for data management and figure generation are in ```/utils```.

The report is made using ```UK_report_templatev2.pmd```. This is where the calls to these scripts are made, and text added. Therefore if you want to add a new figure or text, you must put a callable python script in ```/utils``` and add the function call to the template.

### Report generation

This template is then parsed to make the pmd file with inputs, and weaved to create an md file using Pweave (http://mpastell.com/pweave/). This MD file is then converted to a PDF using pandoc. 


To generate the report:

    - Clone this repo
    - ```cd Reports```
    - ```pip install .```
    - If you haven't run it before, make the environment by running ```conda env create -f UK_full_report/environment.yml``` 
    - Activate the environment by running ```conda activate report```
    - Run the command: ```generate_report --m path/to/metadata --w relevant_week --s file_name_stem --od path/to/output```
    
This will produce a MD file, a PDF and the figures as PNGs. Depending on your output file path, the markdown may not contain the figures, but the PDF will. 


## Acknowledgements

Tree visualisations are undertaken using baltic (https://github.com/evogytis/baltic)

Shape files for mapping for England, Wales and Scotland were taken from the Global Administrative Database (https://gadm.org/)

Shape files for mapping Northern Ireland were taken from Open Data NI (https://www.opendatani.gov.uk/dataset?tags=Counties)

Shape files for mapping the channel islands were taken from https://gist.github.com/markmarkoh


