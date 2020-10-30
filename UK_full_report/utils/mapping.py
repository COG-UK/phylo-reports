import json
import geopandas
from geopandas import GeoSeries,GeoDataFrame
import pandas as pd
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from shapely.geometry import Point, Polygon
from shapely.ops import cascaded_union
import matplotlib.pyplot as plt
import numpy as np
import warnings
import csv
import os

warnings.filterwarnings("ignore")


def prep_data(input_geojsons):

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

    # locations_in_shape_file = []
    # for i in all_uk["NAME_2"]:
    #     locations_in_shape_file.append(i.upper().replace(" ","_"))

    return all_uk


def parse_metadata(metadata,sequencing_centre, not_mappable, pillar_2):

    pillar_2s = ["ALDP", "QEUH", "MILK", "CAMC"]

    seq_dict = defaultdict(list)
    missing_adm2 = {}
    adm2s = set()

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
                if pillar_2:
                    this_seq = False
                    for place in pillar_2s:
                        if place in seq_name:
                            this_seq = True
                    if not this_seq:
                        continue

                if adm2 != "" and adm2 not in not_mappable:
                    if "|" in adm2:
                        new_adm2 = "|".join(sorted(adm2.split("|")))
                    else:
                        new_adm2 = adm2
                    
                    seq_dict[new_adm2].append(seq_name)
                    adm2s.add(new_adm2)
                
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

    missing_df = pd.DataFrame(missing_adm2)

    return seq_dict, adm2s, missing_df, missing_sequences

def find_ambiguities(adm2s):

    ambiguous = []
    ambiguous_dict = defaultdict(set)
    clusters = []

    for adm2 in adm2s:
        if "|" in adm2:
            ambiguous.append(set(adm2.split("|")))

    for group in ambiguous:
        for group2 in ambiguous:
            if group & group2:
                group |= group2

        clusters.append(group)

    for cluster in clusters:
        for place in cluster:
            ambiguous_dict[place] = "|".join(sorted(cluster))


    return ambiguous_dict



def match_to_dataframe(all_uk, seq_dict, adm2s, ambiguous_dict):

    count = 0
    
    metadata_multi_loc = []

    for location in all_uk["NAME_2"]:
        location = location.upper().replace(" ","_")
        if location in ambiguous_dict:
            metadata_multi_loc.append(ambiguous_dict[location])
        else:
            metadata_multi_loc.append(location)
        
    all_uk["Multi_loc"] = metadata_multi_loc

    merged_locs = all_uk.dissolve(by="Multi_loc")

    seq_counts = {}
    df_dict = defaultdict(list)

    if len(seq_dict) != 0:

        for k,v in seq_dict.items():
            if k in ambiguous_dict:
                testing = ambiguous_dict[k]
                if testing in seq_counts.keys():
                    seq_counts[testing] += len(v)
                else:
                    seq_counts[testing] = len(v)
            
            elif "|" in k:
                for location in ambiguous_dict.values():
                    if any([i for i in k.split("|") if i in location.split("|")]):
                        if location in seq_counts.keys():
                            seq_counts[location] += len(v)
                        else:
                            seq_counts[location] = len(v)
                        break
            
            else:
                seq_counts[k] = len(v)
            
        for k,v in seq_counts.items():
            df_dict["Multi_loc"].append(k)
            df_dict["Seq_count"].append(v)

        seq_count_df = pd.DataFrame(df_dict)

        with_seq_counts = merged_locs.merge(seq_count_df, how='left', left_index=True, right_on="Multi_loc")
        
        return with_seq_counts
    
    else:
        no_loc_data = True

    

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

    try:
        legend = ax.get_legend()
        legend.set_bbox_to_anchor((0.1,0.5,0.2,0.2))
        legend.set_title("Number of sequences")
    
        for text, label in zip(legend.get_texts(), new_labels):
            text.set_text(label)

    except AttributeError:
        pass

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


def plot_missing_sequences(missing_df):

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(20, 15)

    plt.bar(missing_df["Country"], missing_df["Number of missing sequences"], color=missing_df["Colour"])

    plt.xlabel("Country")
    plt.ylabel("Number of sequences")

def sort_nice_names(df):

    nice_names = commonly_used_names()

    aka_list = []
    new_names = []
    for i in df["Multi_loc"]:
        new_name = i.replace("|","/")
        new_names.append(new_name)
        if i in nice_names:
            aka_list.append(nice_names[i])
        else:
            for key, value in nice_names.items():
                if all(item in value for item in i.split("|")):
                    name = key
                    for ele in i.split("|"):
                        if ele not in value.split("|"):
                            name += f'and {ele}'

                else:
                    name = ""
            aka_list.append(name)

    return aka_list, new_names

def clean_df(df, sequencing_centre, country):

    first_step = df[["Multi_loc", "NAME_1","Seq_count", "Seq_group"]]

    aka_list, new_names = sort_nice_names(first_step)

    first_step["Also known as"] = aka_list
    first_step["Multi_loc"] = new_names

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

    headers = ["Admin2", "Number of sequences", "Sequence group", "Also known as", "Country"]

    fourth_step.columns = headers
    fourth_step = fourth_step[["Admin2","Also known as", "Country", "Number of sequences", "Sequence group"]]

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


def make_map(input_geojsons, metadata_file, sequencing_centre, country, pillar2):

    not_mappable = ["WALES", "OTHER", "UNKNOWN", "UNKNOWN_SOURCE", "NOT_FOUND", "GIBRALTAR", "FALKLAND_ISLANDS", "CITY_CENTRE"]

    all_uk = prep_data(input_geojsons)

    seq_dict, adm2s, missing_df, missing_sequences = parse_metadata(metadata_file,sequencing_centre, not_mappable, pillar2)
    ambiguous_dict = find_ambiguities(adm2s)

    parsing_output = match_to_dataframe(all_uk,seq_dict,adm2s,ambiguous_dict)

    if type(parsing_output) != bool:
        with_seq_counts = parsing_output
    
        with_seq_counts = make_sequence_groups(with_seq_counts)
        
        cleaned = clean_df(with_seq_counts, sequencing_centre, country)

        england, scotland, wales, n_i, channels, plot_dict = parse_countries(with_seq_counts)

        if sequencing_centre == "" and country != "": #so if it's an adm1 report
            plot_individual(england, scotland, wales, n_i, country)
        else:
            plot_whole_map(england, scotland, wales, n_i, channels, plot_dict, country)

        sort_missing_sequences(missing_df, missing_sequences, sequencing_centre, country)       
        
        return cleaned

    else:
        print("There are no sequences with geographical information for this sequencing centre")
        no_seqs = True
        return no_seqs




def commonly_used_names():

    nice_names = {
        "BIRMINGHAM|COVENTRY|DUDLEY|SANDWELL|SOLIHULL|WALSALL|WOLVERHAMPTON":"West Midlands",
        "DERBY|DERBYSHIRE|LEICESTER|LEICESTERSHIRE|LINCOLNSHIRE|NORTHAMPTONSHIRE|NOTTINGHAM|NOTTINGHAMSHIRE|RUTLAND":"East Midlands",
        "BOLTON|BURY|MANCHESTER|OLDHAM|ROCHDALE|SALFORD|STOCKPORT|TAMESIDE|TRAFFORD|WIGAN":"Greater Manchester",
        "EAST_SUSSEX|WEST_SUSSEX":"Sussex",
        "BRADFORD|CALDERDALE|KIRKLEES|LEEDS|WAKEFIELD":"West Yorkshire",
        "GATESHEAD|NEWCASTLE_UPON_TYNE|NORTH_TYNESIDE|SOUTH_TYNESIDE|SUNDERLAND": "Tyne & Wear",
        "BARNSLEY|DONCASTER|ROTHERHAM|SHEFFIELD": "South Yorkshire",
        "BRACKNELL_FOREST|READING|SLOUGH|WEST_BERKSHIRE|WINDSOR_AND_MAIDENHEAD|WOKINGHAM":"Berkshire",
        "BRACKNELL_FOREST|BUCKINGHAMSHIRE|READING|SLOUGH|WEST_BERKSHIRE|WINDSOR_AND_MAIDENHEAD|WOKINGHAM":"Berkshire and Buckinghamshire",
        'KNOWSLEY|SAINT_HELENS|SEFTON|WIRRAL':"Merseyside",
        "CHESHIRE_EAST|CHESHIRE_WEST_AND_CHESTER":"Cheshire"
    }

    return nice_names