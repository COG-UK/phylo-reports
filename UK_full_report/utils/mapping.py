import json
import geopandas
from geopandas import GeoSeries,GeoDataFrame
import pandas as pd
from collections import defaultdict
from collections import Counter
from shapely.geometry import Point, Polygon
from shapely.ops import cascaded_union
import matplotlib.pyplot as plt
import numpy as np
import warnings
import csv

warnings.filterwarnings("ignore")


def prep_data(input_geojsons, adm2_cleaning_file):

    uk_input = input_geojsons[0]
    channel_input = input_geojsons[1]
    ni_input = input_geojsons[2]

    uk = geopandas.read_file(uk_input)
    channels = geopandas.read_file(channel_input)
    NI = geopandas.read_file(ni_input)


    ni_name = []
    for i in range(len(NI["CountyName"])):
        ni_name.append("Northern Ireland C")
    
    NI["NAME_2"] = NI["CountyName"]
    NI["NAME_1"] = ni_name  

    all_uk = uk.append(channels).append(NI)

    return all_uk

def clean_locs(cleaning_file, all_uk):

    mapping_dictionary = defaultdict(list)

    with open(cleaning_file) as f:
        next(f)
        for l in f:
            toks = l.strip("\n").split(",")
            toks [:] = [x for x in toks if x] #to get rid of empty strings in the csv
            mapping_dictionary[toks[0]] = toks[1:]


    multi_loc_dict = {}

    for key, value in mapping_dictionary.items():
        if len(value) > 1:
            for i in value:
                multi_loc_dict[i] = key


    metadata_multi_loc = []

    for location in all_uk["NAME_2"]:
        if location in multi_loc_dict.keys():
            metadata_multi_loc.append(multi_loc_dict[location])
        else:
            metadata_multi_loc.append(location.upper())
        
    all_uk["Multi_loc"] = metadata_multi_loc

    merged_locs = all_uk.dissolve(by="Multi_loc")

    return merged_locs, mapping_dictionary, multi_loc_dict

def parse_metadata(metadata, mapping_dictionary, merged_locs, multi_loc_dict, sequencing_centre):

    seq_dict = defaultdict(list)
    missing_adm2 = {}

    wales = []
    scotland = []
    england = []
    ni = []

    totals = {}

    missing_adm2["Country"] = ["England", "Wales", "Scotland", "Northern_Ireland"]
    missing_adm2["Colour"] = ["indianred", "darkseagreen", "steelblue", "skyblue"]

    E = 0
    W = 0
    S = 0
    NI = 0

    with open(metadata, "r") as f:
        reader = csv.DictReader(f)
        in_data = [r for r in reader]
        for sequence in in_data:
            if sequence['country'] == "UK":
                seq_name = sequence['sequence_name']
                adm2 = sequence['adm2']
                
                #uk_country = sequence['adm1'].split("-")[1]
                uk_country = seq_name.split("/")[0]
                
                extracted_sequencing_centre = seq_name.split("/")[1].split("-")[0]
                if sequencing_centre is not None and sequencing_centre != "" and sequencing_centre != extracted_sequencing_centre:
                    continue

                if adm2 != "OTHER" and adm2 != "NOT FOUND" and adm2 != "UNKNOWN SOURCE" and adm2 != "" and adm2 != "WALES":
                    if adm2 in mapping_dictionary.keys():
                        if len(mapping_dictionary[adm2]) == 1:  #if it's a 1:1 and it's just mislabelled
                            new = mapping_dictionary[adm2][0].upper()
                        else: #if it's a larger one that's merging several small ones
                            new = adm2

                    elif adm2 in multi_loc_dict.keys():
                        new = multi_loc_dict[adm2]

                    else:
                        new = adm2


                    seq_dict[new].append(seq_name)

                    #if uk_country == "WLS":
                    if uk_country == "Wales":
                        wales.append(seq_name)
                    #elif uk_country == "SCT":
                    elif uk_country == "Scotland":
                        scotland.append(seq_name)
                    #elif uk_country == "ENG":
                    elif uk_country == "England":
                        england.append(seq_name)
                    #elif uk_country == "NIR":
                    elif uk_country == "Northern_Ireland":
                        ni.append(seq_name)
                    else:
                        print("Some sequences with adm2 not assigned to UK country")

                else:
                    
                    #if uk_country == "ENG":
                    if uk_country == "England":
                        E += 1
                    #elif uk_country == "WLS":
                    elif uk_country == "Wales":
                        W +=1
                    elif uk_country == "Scotland":
                    # elif uk_country == "SCT":
                        S += 1
                    elif uk_country == "Northern_Ireland":
                    # elif uk_country == "NIR":
                        NI += 1
                    else:
                        print("Some sequences without adm2 not assigned to UK country")
                        
                    if E == 0 and W == 0 and S == 0 and NI == 0:
                        missing_sequences = False
                    else:
                        missing_sequences = True

                    missing_adm2["Number of missing sequences"] = [E,W,S,NI]

    seq_counts = {}
    df_dict = defaultdict(list)

    for k,v in seq_dict.items():
        seq_counts[k] = len(v)
        
    for k,v in seq_counts.items():
        df_dict["Multi_loc"].append(k)
        df_dict["Seq_count"].append(v)

    seq_count_df = pd.DataFrame(df_dict)

    with_seq_counts = merged_locs.merge(seq_count_df, how='left', left_index=True, right_on="Multi_loc")

    missing_df = pd.DataFrame(missing_adm2)

    return with_seq_counts, missing_df, missing_sequences

def make_sequence_groups(with_seq_counts):

    seq_groups = []
    case_groups = []

    for i, row in with_seq_counts.iterrows():
        seqs = float(row["Seq_count"])
        loc = row["Multi_loc"]
        
        if not np.isnan(seqs):
            
            if seqs <10 and seqs > 0:
                seq_group = ("1-10")
                case_group = 0
            elif seqs < 50 and seqs >= 10:
                seq_group = ("10-50")
                case_group = 1
            elif seqs >=50 and seqs < 100:
                seq_group = ("50-100")
                case_group = 2
            elif seqs >=100 and seqs < 150:
                seq_group = ("100-150")
                case_group = 3
            elif seqs >=150 and seqs <200:
                seq_group = ("150-200")
                case_group = 4
            elif seqs >=200 and seqs <250:
                seq_group = ("200-250")
                case_group = 5
            elif seqs >=250 and seqs <300:
                seq_group = ("250-300")
                case_group = 6
            elif seqs >=300 and seqs <400:
                seq_group = ("300-400")
                case_group = 7
            elif seqs >=400 and seqs <500:
                seq_group = ("400-500")
                case_group = 8
            elif seqs >=500:
                seq_group = (">500")
                case_group = 9
            
                
        else:
            seq_group=seqs
            case_group=seqs
            
        seq_groups.append(seq_group)
        case_groups.append(case_group)

    with_seq_counts["Seq_group"] = seq_groups
    with_seq_counts["Group"] = case_groups

    return with_seq_counts

def parse_countries(with_seq_counts):

    england = with_seq_counts.loc[with_seq_counts["NAME_1"] == "England"]
    scotland = with_seq_counts.loc[with_seq_counts["NAME_1"] == "Scotland"]
    wales = with_seq_counts.loc[with_seq_counts["NAME_1"] == "Wales"]
    n_i = with_seq_counts.loc[with_seq_counts["NAME_1"] == "Northern Ireland C"]
    channels = with_seq_counts.loc[with_seq_counts["NAME_1"] == "Channel_islands"]

    df_list = {"England":england, "Scotland":scotland, "Wales":wales, "NI":n_i, "Channels":channels}    

    plot_dict = {}

    for i,v in df_list.items():
        if v["Seq_count"].isnull().all():
            england = england.append(v) #for missing data
            plot_dict[i] = False
        else:
            plot_dict[i] = True


    return england, scotland, wales, n_i, channels, plot_dict


def plot_map(england, scotland, wales, n_i, channels, plot_dict):

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(20, 15)
    england = england.to_crs("EPSG:3395")
    scotland = scotland.to_crs("EPSG:3395")
    wales = wales.to_crs("EPSG:3395")
    n_i = n_i.to_crs("EPSG:3395")
    channels = channels.to_crs("EPSG:3395")

    vmin = -1
    vmax = 12
    plotting_col = "Group"

    if plot_dict["Scotland"]:
        scotland.plot(column=plotting_col, cmap = "Blues", ax=ax, legend=True, categorical=True, vmin=vmin, vmax=vmax,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})
    if plot_dict["Wales"]:
        wales.plot(column=plotting_col, cmap = "Greens", ax=ax, legend=True, categorical=True, vmin=vmin, vmax=vmax,
                missing_kwds={"color": "lightgrey","label": "No sequences yet"})
    if plot_dict["England"]:
        england.plot(column=plotting_col, cmap = "Reds", ax=ax, categorical=True,legend=True,
                    vmin=vmin, vmax=vmax,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})
    if plot_dict["NI"]:
        n_i.plot(column=plotting_col, cmap = "Purples", ax=ax, legend=False, categorical=False, vmin=vmin, vmax=vmax,
                missing_kwds={"color": "lightgrey","label": "No sequences yet"})

    if plot_dict["Channels"]:
        channels.plot(column=plotting_col, cmap = "Reds", ax=ax, legend=False, vmin=vmin, vmax=vmax,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})

    legend = ax.get_legend()
    new_labels = ["0-10", "10-50", "50-100", "100-150", "150-200","200-250", "250-300", "300-400", "400-500", ">500",
                "No sequences yet"]
    legend.set_bbox_to_anchor((0.1,0.5,0.2,0.2))
    legend.set_title("Number of sequences")

    for text, label in zip(legend.get_texts(), new_labels):
        text.set_text(label)

    ax.axis("off")
    ax.set_title('COVID-19 sequences from each Admn2 region UK', fontdict={'fontsize': '25', 'fontweight' : '3'})

def plot_missing_sequences(missing_df):

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(20, 15)

    plt.bar(missing_df["Country"], missing_df["Number of missing sequences"], color=missing_df["Colour"])

    plt.xlabel("Country")
    plt.ylabel("Number of sequences")
    plt.title("Unplotted sequences")


def find_new_locs_cleaning(metadata, mapping_dictionary, all_uk, output_dir, sequencing_centre):

    present_locs = []

    new_unclean_locs = False
    fw = open(output_dir + "unclean_locations.csv", 'w')

    for i in all_uk["NAME_2"]:
        present_locs.append(i.upper())

    with open(metadata, "r") as f:
        reader = csv.DictReader(f)
        in_data = [r for r in reader]
        for sequence in in_data:
            if sequence['country'] == "UK":
                adm2 = sequence['adm2']
                #country = sequence['adm1'].split("-")[1]
                country = sequence["sequence_name"].split("/")[0]
                extracted_sequencing_centre = sequence["sequence_name"].split("/")[1].split("-")[0]
                # extracted_sequencing_centre = sequence['sequencing_org_code']
                if sequencing_centre is not None and sequencing_centre != "" and sequencing_centre != extracted_sequencing_centre:
                    continue

                if adm2 not in present_locs and adm2 not in mapping_dictionary.keys() and adm2 != "WALES" and adm2 != "" and adm2 != "OTHER" and adm2 != "UNKNOWN" and adm2 != "GIBRALTAR" and adm2 != "UNKNOWN SOURCE":
                    new_unclean_locs = True
                    fw.write(adm2 + "\n")

    fw.close()

    return new_unclean_locs

                    
def clean_df(df, sequencing_centre):

    first_step = df[["Multi_loc", "NAME_1","Seq_count", "Seq_group"]]
    second_step = first_step.reset_index(drop=True)

    drop_labels = []

    for index,row in second_step.iterrows():
        if row["NAME_1"] == "Northern Ireland":
            drop_labels.append(index)      

    third_step = second_step.drop([second_step.index[i] for i in drop_labels])
    new_names = []

    for i in third_step["NAME_1"]:
        if i == "Northern Ireland C":
            new_names.append("Northern Ireland")
        else:
            new_names.append(i)
            
    third_step["Country"] = new_names

    fourth_step = third_step.drop(["NAME_1"], axis=1)

    headers = ["Admin2", "Number of sequences", "Sequence group", "Country"]
    fourth_step.columns = headers
    fourth_step = fourth_step[["Admin2","Country", "Number of sequences", "Sequence group"]]

    final = fourth_step.fillna(0)

    if sequencing_centre != "":
        final.loc[(final!=0).any(1)] #drop ones with zeroes in if the sequencing centre is around

    final.set_index("Admin2", inplace=True)

    return final

def make_map(input_geojsons, adm2_cleaning_file, metadata_file, overall_output_dir,week, sequencing_centre, country):

    output_dir = overall_output_dir + "summary_files_" + week + "/"

    all_uk = prep_data(input_geojsons, adm2_cleaning_file)

    merged_locs, mapping_dictionary, multi_loc_dict = clean_locs(adm2_cleaning_file, all_uk)

    with_seq_counts, missing_df, missing_sequences = parse_metadata(metadata_file, mapping_dictionary, merged_locs, multi_loc_dict, sequencing_centre)

    with_seq_counts = make_sequence_groups(with_seq_counts)
    cleaned = clean_df(with_seq_counts, sequencing_centre)

    england, scotland, wales, n_i, channels, plot_dict = parse_countries(with_seq_counts)

    plot_map(england, scotland, wales, n_i, channels, plot_dict)

    if missing_sequences and sequencing_centre == "":
        plot_missing_sequences(missing_df)
    elif not missing_sequences:
        print("All sequences have been assigned clean adm2 data this week.")
    elif missing_sequences and sequencing_centre != "":
        missing_number = missing_df.loc[missing_df["Country"] == country]["Number of missing sequences"]
        print("There are " + str(missing_number) + " sequences without enough geographical information to map from this centre.")
                             
    
    new_unclean_locs = find_new_locs_cleaning(metadata_file, mapping_dictionary, all_uk, output_dir, sequencing_centre)

    return new_unclean_locs, cleaned





