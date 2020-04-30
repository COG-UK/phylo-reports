## Generate detailed UK report

Generates UK report for weekly COG-UK data

Inputs required:

- metadata csv

- In individual folders for each global lineage (if you want tree rendering):
    - subtrees cut up into newick files


Caveats:
- The lineage subfolders must all be in one directory with nothing else in it
- The date format in the metadata must be yyyy-mm-dd if there are months/days


Tree visualisations are undertaken using baltic (https://github.com/evogytis/baltic)

Shape files for mapping for England, Wales and Scotland were taken from the Global Administrative Database (https://gadm.org/)

Shape files for mapping Northern Ireland were taken from Open Data NI (https://www.opendatani.gov.uk/dataset?tags=Counties)

Shape files for mapping the channel islands were taken from https://gist.github.com/markmarkoh
