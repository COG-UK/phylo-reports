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

    locations_in_shape_file = []
    for i in all_uk["NAME_2"]:
        locations_in_shape_file.append(i.upper())

    return all_uk, locations_in_shape_file

def clean_locs(clean_locs_file, all_uk):

    straight_map = {}
    multi_loc_dict = {}
    metadata_multi_loc = []

    with open(clean_locs_file) as f:
        next(f)
        for l in f:
            toks = l.strip("\n").split(",")
            toks [:] = [x for x in toks if x]
            metadata_loc = toks[0]
            real_locs = toks[1:]   

            if metadata_loc == 'RHONDDA CYNON TAF':
                straight_map[metadata_loc] = "RHONDDA, CYNON, TAFF" 
            else:
                if len(real_locs) == 1:
                    straight_map[metadata_loc] = real_locs[0].upper()
                else:
                    for i in real_locs:
                        multi_loc_dict[i.upper()] = metadata_loc.upper()
                    

    for location in all_uk["NAME_2"]:
        if location.upper() in multi_loc_dict.keys():
            metadata_multi_loc.append(multi_loc_dict[location.upper()])
        else:
            metadata_multi_loc.append(location.upper())
        
    all_uk["Multi_loc"] = metadata_multi_loc

    merged_locs = all_uk.dissolve(by="Multi_loc")

    return merged_locs, multi_loc_dict, straight_map

def parse_metadata(metadata, merged_locs, multi_loc_dict, straight_map, sequencing_centre, not_mappable, present_in_shape_file, output_dir):

    seq_dict = defaultdict(list)
    missing_adm2 = {}
    new_unclean_locs = False

    unclean_file = open(output_dir + "unclean_locations.csv", 'w')

    missing_adm2["Country"] = ["England", "Wales", "Scotland", "Northern_Ireland"]
    missing_adm2["Colour"] = ["indianred", "darkseagreen", "steelblue", "skyblue"]

    E = 0
    W = 0
    S = 0
    NI = 0

    with open(metadata, "r") as f:
        missing_sequences = False
        reader = csv.DictReader(f)
        in_data = [r for r in reader]
        for sequence in in_data:
            if sequence['country'] == "UK":
                seq_name = sequence['sequence_name']
                adm2 = sequence['adm2']

                uk_country = sequence['adm1'].split("-")[1]
                extracted_sequencing_centre = sequence["sequencing_org_code"]

                if sequencing_centre is not None and sequencing_centre != "" and sequencing_centre != extracted_sequencing_centre:
                    continue

                if adm2 != "" and adm2 not in not_mappable:
                    if adm2 in straight_map.keys():
                        
                        new = straight_map[adm2]
                        
                        if new in multi_loc_dict.keys():
                            new = multi_loc_dict[new]

                    elif adm2 in multi_loc_dict.keys():
                        new = multi_loc_dict[adm2]

                    elif adm2 not in present_in_shape_file and adm2 not in multi_loc_dict.values():
                        new_unclean_locs = True
                        unclean_file.write(adm2 + "\n")
                        new = "NA"
                    
                    else:
                        new = adm2
                
                    seq_dict[new].append(seq_name)
                
                else:
                    
                    if uk_country == "ENG":
                        E += 1
                    elif uk_country == "WLS":
                        W +=1
                    elif uk_country == "SCT":
                        S += 1
                    elif uk_country == "NIR":
                        NI += 1
                    else:
                        print("Some sequences without adm2 not assigned to UK country")
                        
                    if E == 0 and W == 0 and S == 0 and NI == 0:
                        missing_sequences = False
                    else:
                        missing_sequences = True

                    missing_adm2["Number of missing sequences"] = [E,W,S,NI]

    unclean_file.close()

    seq_counts = {}
    df_dict = defaultdict(list)

    if len(seq_dict) != 0:

        for k,v in seq_dict.items():
            seq_counts[k] = len(v)
            
        for k,v in seq_counts.items():
            df_dict["Multi_loc"].append(k)
            df_dict["Seq_count"].append(v)

        seq_count_df = pd.DataFrame(df_dict)

        with_seq_counts = merged_locs.merge(seq_count_df, how='left', left_index=True, right_on="Multi_loc")

        missing_df = pd.DataFrame(missing_adm2)

        return with_seq_counts, missing_df, missing_sequences, new_unclean_locs
    
    else:
        no_loc_data = True
        return no_loc_data

    

def make_sequence_groups(with_seq_counts):

    seq_groups = []
    case_groups = []

    for i, row in with_seq_counts.iterrows():
        seqs = float(row["Seq_count"])
        loc = row["Multi_loc"]
        
        if not np.isnan(seqs):
            
            if seqs > 0 and seqs <10 :
                seq_group = ("1-10")
                case_group = 0
            elif seqs >=10 and seqs < 100:
                seq_group = ("10-100")
                case_group = 1
            elif seqs >=100 and seqs < 200:
                seq_group = ("100-200")
                case_group = 2
            elif seqs >=200 and seqs < 300:
                seq_group = ("200-300")
                case_group = 3
            elif seqs >=300 and seqs <400:
                seq_group = ("300-400")
                case_group = 4
            elif seqs >=400 and seqs <500:
                seq_group = ("400-500")
                case_group = 5
            elif seqs >=500 and seqs <600:
                seq_group = ("500-600")
                case_group = 6
            elif seqs >=600 and seqs <700:
                seq_group = ("600-700")
                case_group = 7
            elif seqs >=700 and seqs <1000:
                seq_group = ("700-1000")
                case_group = 8
            elif seqs >=1000 and seqs <2000:
                seq_group = ("1000-2000")
                case_group = 9
            elif seqs >= 2000:
                seq_group = (">2000")
                case_group = 10
            
                
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


def plot_whole_map(england, scotland, wales, n_i, channels, plot_dict, country):

    fig, ax = plt.subplots(1, 1, figsize=(20,15))
    england = england.to_crs("EPSG:3395")
    scotland = scotland.to_crs("EPSG:3395")
    wales = wales.to_crs("EPSG:3395")
    n_i = n_i.to_crs("EPSG:3395")
    channels = channels.to_crs("EPSG:3395")

    vmin = -1
    vmax = 12
    plotting_col = "Group"

    if country != "":
        if country == "Scotland":
            scot_legend_bool = True
            engl_legend_bool = False
            n_i_legend_bool = False
            wales_legend_bool = False
            plotting_df = scotland
        elif country == "England":
            scot_legend_bool = False
            engl_legend_bool = True
            n_i_legend_bool = False
            wales_legend_bool = False
            plotting_df = england
        elif country == "Wales":
            scot_legend_bool = False
            engl_legend_bool = False
            n_i_legend_bool = False
            wales_legend_bool = True
            plotting_df= wales
        elif country == "Northern_Ireland":
            scot_legend_bool = False
            engl_legend_bool = False
            n_i_legend_bool = True
            wales_legend_bool = False
            plotting_df = n_i
    else:
        scot_legend_bool = False
        engl_legend_bool = True
        n_i_legend_bool = False
        wales_legend_bool = False
        plotting_df = england


    if plot_dict["Scotland"]:
        scotland.plot(column=plotting_col, cmap = "Blues", ax=ax, legend=scot_legend_bool, categorical=True, vmin=vmin, vmax=vmax,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})
    
    if plot_dict["Wales"]:
        wales.plot(column=plotting_col, cmap = "Greens", ax=ax, legend=wales_legend_bool, categorical=True, vmin=vmin, vmax=vmax,
                missing_kwds={"color": "lightgrey","label": "No sequences yet"})
    
    if plot_dict["England"]:
        england.plot(column=plotting_col, cmap = "Reds", ax=ax, categorical=True,legend=engl_legend_bool,
                    vmin=vmin, vmax=vmax,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})
    if plot_dict["NI"]:
        n_i.plot(column=plotting_col, cmap = "Purples", ax=ax, legend=n_i_legend_bool, categorical=True, vmin=vmin, vmax=vmax,
                missing_kwds={"color": "lightgrey","label": "No sequences yet"})

    if plot_dict["Channels"]:
        channels.plot(column=plotting_col, cmap = "Reds", ax=ax, legend=False, vmin=vmin, vmax=vmax,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})

    label_dict = {0.0:"0-10", 1.0:"10-100", 2.0:"100-200", 3.0:"200-300", 4.0:"300-400",5.0:"400-500", 6.0:"500-600", 7.0:"600-700", 8.0:"700-1000", 9.0:"1000-2000", 10.0:">2000"}


    label_prep = set()
    new_labels = []

    for group in plotting_df["Group"]:
        if pd.notnull(group):
            label_prep.add(group)
        
    prep_sorted = sorted(list(label_prep))
    label_intermediate = []
    
    for i in prep_sorted:
        new_labels.append(label_dict[i])
        
    new_labels.append("No sequences yet")

    legend = ax.get_legend()
    legend.set_bbox_to_anchor((0.1,0.5,0.2,0.2))
    legend.set_title("Number of sequences")

    for text, label in zip(legend.get_texts(), new_labels):
        text.set_text(label)

    ax.axis("off")

def plot_individual(england, scotland, wales, n_i, country):
    
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(20, 15)
    england = england.to_crs("EPSG:3395")
    scotland = scotland.to_crs("EPSG:3395")
    wales = wales.to_crs("EPSG:3395")
    n_i = n_i.to_crs("EPSG:3395")

    plotting_col = "Group"
    
    plotting_dict = {"England": england, "Scotland":scotland, "Wales":wales, "Northern_Ireland":n_i}

    label_dict = {0.0:"0-10", 1.0:"10-100", 2.0:"100-200", 3.0:"200-300", 4.0:"300-400",5.0:"400-500", 6.0:"500-600", 7.0:"600-700", 8.0:"700-1000", 9.0:"1000-2000", 10.0:">2000"}

    colours = {"England": "Reds", "Scotland":"Blues", "Wales":"Greens", "Northern_Ireland":"Purples"}

    plotting_df = plotting_dict[country]

    new_labels = []
    label_prep = set()

    for group in plotting_df["Group"]:
        if pd.notnull(group):
            label_prep.add(group)
        
    prep_sorted = sorted(list(label_prep))
    label_intermediate = []
    
    for i in prep_sorted:
        new_labels.append(label_dict[i])
        
    new_labels.append("No sequences yet")
        
    plotting_df.plot(column=plotting_col, cmap = colours[country], ax=ax, legend=True, categorical=True,
                    missing_kwds={"color": "lightgrey","label": "No sequences yet"})


    legend = ax.get_legend()
    legend.set_bbox_to_anchor((0.1,0.5,0.2,0.2))
    legend.set_title("Number of sequences")

    for text, label in zip(legend.get_texts(), new_labels):
        text.set_text(label)

    ax.axis("off")
    #ax.set_title('COVID-19 sequences from each Admn2 region in ' + country, fontdict={'fontsize': '25', 'fontweight' : '3'})


def plot_missing_sequences(missing_df):

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(20, 15)

    plt.bar(missing_df["Country"], missing_df["Number of missing sequences"], color=missing_df["Colour"])

    plt.xlabel("Country")
    plt.ylabel("Number of sequences")

def clean_df(df, sequencing_centre, country):

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
        final = final[final["Number of sequences"] != 0] #drop ones with zeroes in if the sequencing centre is around

    final.set_index("Admin2", inplace=True)

    if sequencing_centre == "" and country != "":
        if country == "Northern_Ireland":
            final_individual = final.loc[final["Country"] == "Northern Ireland"]
        else:
            final_individual = final.loc[final["Country"] == country]
        return final_individual
    else:
        return final

def sort_missing_sequences(missing_df, missing_sequences, sequencing_centre, country):

    if missing_sequences and sequencing_centre == "":
            plot_missing_sequences(missing_df)
    elif not missing_sequences:
            print("All sequences have been assigned clean adm2 data this week.")
    elif missing_sequences and sequencing_centre != "":
        missing_number_prep = missing_df.loc[missing_df["Country"] == country]["Number of missing sequences"]
        if country == "England":
            missing_number = missing_number_prep.at[0]
        elif country == "Wales":
            missing_number = missing_number_prep.at[1]
        elif country == "Scotland":
            missing_number = missing_number_prep.at[2]
        elif country == "Northern_Ireland":
            missing_number = missing_number_prep.at[3]
        print("There are " + str(missing_number) + " sequences without enough geographical information to map from this centre.")


def make_map(input_geojsons, adm2_cleaning_file, metadata_file, overall_output_dir,week, sequencing_centre, country):

    not_mappable = ["WALES", "OTHER", "UNKNOWN", "UNKNOWN SOURCE", "NOT FOUND", "GIBRALTAR", "FALKLAND ISLANDS", "CITY CENTRE"]

    output_dir = overall_output_dir + "summary_files/"

    all_uk, locations_in_shape_file = prep_data(input_geojsons, adm2_cleaning_file)

    merged_locs, multi_loc_dict, straight_map = clean_locs(adm2_cleaning_file, all_uk)

    parsing_output = parse_metadata(metadata_file, merged_locs, multi_loc_dict, straight_map, sequencing_centre, not_mappable, locations_in_shape_file, output_dir)

    if type(parsing_output) != bool:
        with_seq_counts, missing_df, missing_sequences, new_unclean_locs = parsing_output
    
        with_seq_counts = make_sequence_groups(with_seq_counts)
        
        cleaned = clean_df(with_seq_counts, sequencing_centre, country)

        england, scotland, wales, n_i, channels, plot_dict = parse_countries(with_seq_counts)

        if sequencing_centre == "" and country != "": #so if it's an adm1 report
            plot_individual(england, scotland, wales, n_i, country)
        else:
            plot_whole_map(england, scotland, wales, n_i, channels, plot_dict, country)

        sort_missing_sequences(missing_df, missing_sequences, sequencing_centre, country)       
        
        return new_unclean_locs, cleaned

    else:
        print("There are no sequences with geographical information for this sequencing centre")
        no_seqs = True
        return no_seqs





