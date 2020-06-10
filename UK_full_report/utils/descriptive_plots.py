from collections import Counter
from collections import defaultdict
from collections import OrderedDict
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os
import pandas as pd
import joypy


def make_plotting_dfs(intro_country_counts, intro_object_dict):

    acctrans_counts = defaultdict(dict)
    df_counts = pd.DataFrame(intro_country_counts)
    df_counts.fillna(0,inplace=True)	

    df_thinned = df_counts.drop([col for col, val in df_counts.sum().iteritems() if val <= 5], axis=1, inplace=False)

    for intro, country_counts in intro_country_counts.items(): #check here we're only doing those with one designation
        new_key = list(intro_object_dict[intro].acctrans_designations)[0]
        acctrans_counts[new_key] = country_counts

    df_acctrans_counts = pd.DataFrame(acctrans_counts)
    df_acctrans_counts.fillna(0, inplace=True)

    return df_counts, df_thinned, df_acctrans_counts


def make_timeline(intro_bigs, sequencing_centre, filter_country):

    if sequencing_centre == "" and filter_country != "":
        if filter_country == "England":
            colour_dict = {"Wales":"lightgrey",
            "England":"indianred",
            "Scotland":"lightgrey",
            "Northern_Ireland":"lightgrey"}
        elif filter_country == "Wales":
            colour_dict = {"Wales":"darkseagreen",
            "England":"lightgrey",
            "Scotland":"lightgrey",
            "Northern_Ireland":"lightgrey"}
        elif filter_country == "Scotland":
            colour_dict = {"Wales":"lightgrey",
            "England":"lightgrey",
            "Scotland":"steelblue",
            "Northern_Ireland":"lightgrey"}
        elif filter_country == "Northern_Ireland":
            colour_dict = {"Wales":"lightgrey",
            "England":"lightgrey",
            "Scotland":"lightgrey",
            "Northern_Ireland":"skyblue"}
    else:
        colour_dict = {"Wales":"darkseagreen",
                "England":"indianred",
                "Scotland":"steelblue",
                "Northern_Ireland":"skyblue"}
    
    fig,ax = plt.subplots(figsize=(15,40))

    count = 0
    height = []
    ytick_list = []

    for intro in intro_bigs:
        
        if sequencing_centre == "" and filter_country != "" and filter_country not in intro.adm1:
            continue
        
        colours = []
        sizes = []
        sizes2 = []
        count += 2
        
        point_one = intro.oldest
        point_two = intro.mrd
        
        x = [point_one, point_two]
        y = [count, count]
        
        y2 = []
        x2 = []
        
        country_set = set()

        for i in intro.taxa:
            if i.date_dt != "NA":
                if sequencing_centre == "" and filter_country != "":
                    if i.country != filter_country:
                        x2.insert(0,i.date_dt)
                        colours.insert(0,colour_dict[i.country])
                    else:
                        x2.append(i.date_dt)
                        colours.append(colour_dict[i.country])
                    country_set.add(i.country)
                else:
                    x2.append(i.date_dt)
                    colours.append(colour_dict[i.country])
                    country_set.add(i.country)

        for i in x2:
            sizes2.append((intro.date_counts[i])*40)
            y2.append(count)
                 
        height.append(count)
        ytick_list.append(intro.id)
        
        if point_one != point_two:
            #for x_point, y_point, colour, order, size in zip(x2, y2, colours, orders, sizes2):
            plt.scatter(x2,y2, c=colours, zorder=2, s=sizes2)
            plt.plot(x,y, color='black', zorder=1)
            
        else:
            sizes.append(list(intro.date_counts.values())[0]*50)
            sizes.append(list(intro.date_counts.values())[0]*50)
            
            if len(country_set) > 1:
                plt.scatter(x,y, color='black',s=sizes)
            else:
                plt.scatter(x,y, color=colour_dict[list(country_set)[0]], s=sizes)
    

    text_size = 1/len(intro_bigs)*1500
    
    plt.yticks(height, ytick_list, size=text_size)
    plt.ylim(1, count+1)
    plt.xticks(rotation=45)

def raw_data_timeline(intros):

    raw_dict = defaultdict(list)

    for intro in intros:

        self_list = []

        for i in range(len(intro.dates)):
            self_list.append(intro.id)

        raw_dict["Lineage"].extend(self_list)
        
        sorted_intros = sorted(list(intro.dates))

        raw_dict["Days"].extend(sorted_intros)

        for date in sorted_intros:
            E = 0
            S = 0
            W = 0
            NI = 0
            for i in intro.taxa:
                if i.date_dt != "NA" and i.date_dt == date:
                    if i.country == "England":
                        E += 1
                    elif i.country == "Scotland":
                        S += 1
                    elif i.country == "Wales":
                        W += 1
                    elif i.country == "Northern_Ireland":
                        NI += 1
            
            raw_dict["England"].append(E)
            raw_dict["Scotland"].append(S)
            raw_dict["Wales"].append(W)
            raw_dict["Northern Ireland"].append(NI)

    raw_df = pd.DataFrame(raw_dict)
    
    return raw_df

def plot_bars(intro_bigs, filter_country, sequencing_centre): #NB the raw data for this is in the plot, already displayed
	
    labels = []
    E = []
    S = []
    W = []
    NI = []

    seq_count_list = []
    labels_for_country_specific = []

    for i in intro_bigs[::-1]:

        if filter_country != "" and sequencing_centre == "":
            if len(i.country_specific_taxa) > 5:
                labels_for_country_specific.append(i.id.lstrip("UK"))
                seq_count = len(i.country_specific_taxa)
  

                seq_count_list.append(seq_count)
                
        else:
            labels.append(i.id.lstrip("UK"))
            
            E_c = 0
            S_c = 0
            W_c = 0
            NI_c = 0

            for tax in i.taxa:
                if tax.country=="England":
                    E_c += 1
                elif tax.country=="Scotland":
                    S_c += 1
                elif tax.country=="Wales":
                    W_c += 1
                elif tax.country=="Northern_ireland":
                    NI_c += 1
        
        
            E.append(E_c)
            S.append(S_c)
            W.append(W_c)
            NI.append(NI_c)

    width = 0.8

    fig,ax = plt.subplots(figsize=(30,15))

    colour_dict = {"England":'indianred',"Scotland":'steelblue',"Wales":'darkseagreen',"Northern_Ireland":'skyblue'}

    if filter_country != "" and sequencing_centre == "":
        ax.bar(labels_for_country_specific, seq_count_list, color=colour_dict[filter_country])
    else:
        E = np.array(E)
        S = np.array(S)
        W = np.array(W)
        NI = np.array(NI)

        ax.bar(labels, E, width, label='England', color='indianred')
        ax.bar(labels, S, width, label='Scotland', color='steelblue', bottom = E)
        ax.bar(labels, W, width, label='Wales', color='darkseagreen', bottom = E+S)
        ax.bar(labels, NI, width, label='Northern_Ireland', color='skyblue', bottom = E+S+W)

    plt.xticks(rotation=90, size=25, fontweight='heavy')
    plt.yticks(size=25, fontweight='heavy')

    ax.set_ylabel('Number of sequences', size=40, fontweight='bold')
    ax.set_xlabel("Lineage number", size=40, fontweight='bold')


    if sequencing_centre == "":
        #ax.set_title('Sequences after introduction by country', size=50, fontweight='bold')
        ax.legend(fontsize=40)
   
def top_ten_sort(lineage):
    return len(lineage.taxa)

def prep_geog_data(lineages_prep, filter_country, sequencing_centre):

    if filter_country != "" and sequencing_centre == "": #Should select the top ten from the relevant country
        relevant_counts = {}
        for lin in lineages_prep:
            country_count = lin.adm1.count(filter_country)
            relevant_counts[lin] = country_count
        
        d = Counter(relevant_counts)

        lineages_of_interest = []
        for i in d.most_common(10):
            lineages_of_interest.append(i[0])

    else:
        lineages_of_interest = sorted(lineages_prep, key=top_ten_sort, reverse=True)[:10]

    
    #the week_to_adm2 is already filtered
    overall_weeks = set()
    for lin in lineages_of_interest:
        for week in lin.week_to_adm2.keys():
            overall_weeks.add(week)
        
        
    first_week = min(overall_weeks)
    final_week = max(overall_weeks)

    for lin in lineages_of_interest:
        for k in overall_weeks:
            if k not in lin.week_to_adm2.keys():
                lin.week_to_adm2[k] = set()

    y_dict = defaultdict(list)
    count = 0
    labels = []
    for lin in lineages_of_interest:
        #if len(lin.taxa) > 10:
        count += 1
        count_list = []
        
        labels.append(lin.id)
        
        lin.week_to_adm2 = OrderedDict((k,v) for k,v in sorted(lin.week_to_adm2.items(), key=lambda x:x[0]))
        
        for k,v in lin.week_to_adm2.items():
            count_list.append(len(v))
        
        #new_name = "y"+str(count)
        
        y_dict[lin.id] = count_list

    totals = {}

    for j in range(len(overall_weeks)):
        totals[str(j)] = 0
        
    for y, count_list in y_dict.items():
        for index, number in enumerate(count_list):
            totals[str(index)] += number

    x = []
    for i in sorted(overall_weeks):
        new = i.startdate()
        x.append(new)

    return y_dict, x

def stacked_geog_plot(y_dict, x,normed, totals, labels):

    if normed:
        y_norm = defaultdict(list)

        for key, value in y_dict.items():
            for index, count in enumerate(value):
                normed = (count/(totals[str(index)])*100)
                y_norm[key].append(normed)

        y = np.vstack(list(y_norm.values()))
        
    else: 
        y = np.vstack(list(y_dict.values()))
        
    fig, ax = plt.subplots(1,1,figsize=(16, 9), dpi= 80)

    ax = plt.gca()

    colors = plt.cm.magma(np.linspace(0,1,10))

    ax.stackplot(x,y,labels=labels, colors=colors, alpha=0.8)

    if normed:
        #ax.set_title("Lineages by number of adm2 regions present by epiweek normalised")
        plt.ylabel("Number of adm2 regions present in lineage normalised")
    else:
        #ax.set_title("Lineages by number of adm2 regions present by epiweek")
        plt.ylabel("Number of adm2 regions present in lineage")
   
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], title = "Lineage", bbox_to_anchor=(1.2,1.05))
    plt.xticks(rotation=45)
    plt.xlabel("Week commencing")
    #plt.show()

def plot_ridge_plot(weeks, count_dict):
    
    new_weeks = []

    ridge_dict = defaultdict(list)

    for key, value in count_dict.items():
        ridge_dict["Week_commencing"].extend(weeks)
        ridge_dict["Number_adm2_regions"].extend(value)
        for i in range(len(value)):
            ridge_dict["Lineage"].append(key)

        
    ridge_df = pd.DataFrame(ridge_dict)

    fig, axes = joypy.joyplot(ridge_df, by="Lineage", column="Number_adm2_regions", figsize=(20,20), kind="values", ylim='own', x_range=(0,len(weeks)), colormap=plt.cm.GnBu)

    axes[-1].set_xticks(range(len(weeks)))
    axes[-1].set_xticklabels(weeks, rotation=90)



def make_raw_data_geog_plot(y_dict, weeks):
    
    raw_data = defaultdict(list)

    raw_data["Week commencing"] = weeks

    for key, value in y_dict.items():

        raw_data[key] = value

    raw_df = pd.DataFrame(raw_data)
    raw_df.set_index("Week commencing", inplace=True)
    # raw_df.index.name = "Week commencing"

    return raw_df


def plot_starts(lineages_of_interest):

    single_dates = []
    dates = []
    for lin in lineages_of_interest:
        try:
            if len(lin.taxa) > 1:
                dates.append(lin.oldest)
            else:
                single_dates.append(lin.oldest)
        except AttributeError:
            pass

        
    date_counts = Counter(dates)
    singles_date_counts = Counter(single_dates)

    for date in singles_date_counts.keys():
        if date not in date_counts.keys():
            date_counts[date] = 0

    for date in date_counts.keys():
        if date not in singles_date_counts.keys():
            singles_date_counts[date] = 0

    ordered_dates = OrderedDict((k,v) for k,v in sorted(date_counts.items(), key=lambda x:x[0]))
    single_ordered = OrderedDict((k,v) for k,v in sorted(singles_date_counts.items(), key=lambda x:x[0]))


    x = list(ordered_dates.keys())
    y = np.array(list(ordered_dates.values()))
    x2 = list(single_ordered.keys())
    y2 = np.array(list(single_ordered.values()))

    fig,ax = plt.subplots(1,1,figsize=(30,15), dpi= 80)

    # ax.bar(x,y)
    
    ax.bar(x, y, label='non-singletons', color='midnightblue')
    ax.bar(x2, y2, label='singletons', color='goldenrod', bottom = y)

    plt.xticks(rotation=45, size=25, fontweight='heavy')
    plt.yticks(size=25, fontweight='heavy')
    
    #ax.set_title("Lineage starts per week", size=45)
    plt.xlabel("Week commencing", size=30)
    plt.ylabel("Number of earliest sequences", size=30)
    plt.legend()

    return ordered_dates, single_ordered

def raw_data_starts(singles, non_singles):

    raw_dict = defaultdict(list)

    for day, count in singles.items():
        raw_dict["Day"].append(day)
        raw_dict["Number of singleton starts"].append(count)
    
    for count2 in non_singles.values():
        raw_dict["Number of non-singleton starts"].append(count2)

    for i,j in zip(raw_dict["Number of singleton starts"], raw_dict["Number of non-singleton starts"]):
        raw_dict["Total"].append(i+j)

    raw_df = pd.DataFrame(raw_dict)

    raw_df.set_index("Day", inplace=True)
    #raw_df.index.name = "Day"

    return raw_df


def plot_sequences_over_time(sequences, country, sequencing_centre):

    fig,ax = plt.subplots(1,1,figsize=(30,15), dpi= 80)

    sequence_dates = defaultdict(list)

    E = []
    S = []
    W = []
    NI = []
    labels = []

    date_counts = defaultdict(list)

    for i in sequences:
        if i.date_dt != "NA":
            sequence_dates[i.date_dt].append(i)

    for date,tax_list in sequence_dates.items():
        
        labels.append(date)

        E_c = 0
        S_c = 0
        W_c = 0
        NI_c = 0

        for tax in tax_list:
            if tax.country=="England":
                E_c += 1
            elif tax.country=="Scotland":
                S_c += 1
            elif tax.country=="Wales":
                W_c += 1
            elif tax.country=="Northern_Ireland":
                NI_c += 1

        E.append(E_c)
        S.append(S_c)
        W.append(W_c)
        NI.append(NI_c)

        date_counts[date] = [E_c, S_c, W_c, NI_c]

    E = np.array(E)
    S = np.array(S)
    W = np.array(W)
    NI = np.array(NI)

    width = 0.8

    ax.bar(labels, E, width, label='England', color='indianred')
    ax.bar(labels, S, width, label='Scotland', color='steelblue', bottom = E)
    ax.bar(labels, W, width, label='Wales', color='darkseagreen', bottom = E+S)
    ax.bar(labels, NI, width, label='Northern_Ireland', color='skyblue', bottom = E+S+W)

    plt.xticks(rotation=55, size=25, fontweight='heavy')
    plt.yticks(size=25, fontweight='heavy')

    ax.set_ylabel('Number of sequences', size=40, fontweight='bold')
    ax.set_xlabel("Day", size=40, fontweight='bold')

    
    if country == "":
        #ax.set_title('Sequences taken on each day by country', size=50, fontweight='bold')
        ax.legend(fontsize=40)


    return date_counts   

def raw_data_seqs_over_time(date_counts):

    raw_dict = defaultdict(list)

    for key, value in date_counts.items():

        raw_dict["Day"].append(key)
        raw_dict["England"].append(value[0])
        raw_dict["Scotland"].append(value[1])
        raw_dict["Wales"].append(value[2])
        raw_dict["Northern Ireland"].append(value[3])

    raw_df = pd.DataFrame(raw_dict)
    raw_df.sort_values('Day',ascending=True, inplace=True)
    raw_df.set_index("Day", inplace=True)

    raw_df = raw_df.loc[:, (raw_df != 0).any(axis=0)] #Should remove columns of all 0s 

    return raw_df

def sdi(data):
    """ Given a hash { 'species': count } , returns the SDI
    
    >>> sdi({'a': 10, 'b': 20, 'c': 30,})
    1.0114042647073518"""
    
    from math import log as ln
    
    def p(n, N):
        """ Relative abundance """
        if n is  0:
            return 0
        else:
            return (float(n)/N) * ln(float(n)/N)
            
    N = sum(data.values())
    
    return -sum(p(n, N) for n in data.values() if n is not 0)

def make_diversity_plot(intro_alls, taxa_list):
    
    England_div = defaultdict(dict)
    Wales_div = defaultdict(dict)
    Scotland_div = defaultdict(dict)
    NI_div = defaultdict(dict)

    total_epiweeks = set()
    for lin in intro_alls:
        for j in lin.epiweeks:
            total_epiweeks.add(j)
            
    total_epiweeks = sorted(total_epiweeks)
    week_labels = []

    for i in total_epiweeks:
        week_labels.append(i.startdate())

    countries = ["England","Scotland", "Wales", "Northern_Ireland"]

    for country in countries:
        if country == "England":
            outer_dict = England_div
        elif country == "Wales":
            outer_dict = Wales_div
        elif country == "Scotland":
            outer_dict = Scotland_div
        elif country == "Northern_Ireland":
            outer_dict = NI_div
    
        for week in total_epiweeks:
            inner_dict = {}
            for tax in taxa_list:
                if tax.epiweek == week and tax.country == country:

                    outer_key = week
                    inner_key = tax.introduction

                    if inner_key in inner_dict.keys():
                        inner_dict[inner_key] += 1
                    else:
                        inner_dict[inner_key] = 0
                        inner_dict[inner_key] += 1


                    outer_dict[outer_key] = inner_dict

    england_sorted = OrderedDict(sorted(England_div.items()))
    wales_sorted = OrderedDict(sorted(Wales_div.items()))
    scotland_sorted = OrderedDict(sorted(Scotland_div.items()))
    ni_sorted = OrderedDict(sorted(NI_div.items()))

    df_dict = defaultdict(list)

    England_sdi = {}
    for date, inner_dict in england_sorted.items():
        new_date = date.startdate()
        div = sdi(inner_dict)
        England_sdi[new_date] = div
        df_dict["Adm1"].append("England")
        df_dict["Dates"].append(new_date)
        df_dict["Shannon_diversity"].append(div)
        
    Scotland_sdi = {}
    for date, inner_dict in scotland_sorted.items():
        new_date = date.startdate()
        div = sdi(inner_dict)
        Scotland_sdi[new_date] = div
        df_dict["Adm1"].append("Scotland")
        df_dict["Dates"].append(new_date)
        df_dict["Shannon_diversity"].append(div)
        
    Wales_sdi = {}
    for date, inner_dict in wales_sorted.items():
        new_date = date.startdate()
        div = sdi(inner_dict)
        Wales_sdi[new_date] = div
        df_dict["Adm1"].append("Wales")
        df_dict["Dates"].append(new_date)
        df_dict["Shannon_diversity"].append(div)

    NI_sdi = {}
    for date, inner_dict in ni_sorted.items():
        new_date = date.startdate()
        div = sdi(inner_dict)
        NI_sdi[new_date] = div
        df_dict["Adm1"].append("Northern_Ireland")
        df_dict["Dates"].append(new_date)
        df_dict["Shannon_diversity"].append(div)

    df = pd.DataFrame(df_dict)

    cmap = cm.get_cmap('GnBu')

    fig, axes = joypy.joyplot(df, by="Adm1", column="Shannon_diversity", figsize=(10,15), kind="values",
                         ylim='own', x_range=(0,len(week_labels)), colormap=cmap)

    axes[-1].set_xticks(range(len(week_labels)))
    axes[-1].set_xticklabels(week_labels, rotation=90)

    return df

def tidy_div_df(div_df):

    england_dict = defaultdict(list)
    w_dict = defaultdict(list)
    s_dict = defaultdict(list)
    ni_dict = defaultdict(list)

    for index,row in div_df.iterrows():
        if row["Adm1"] == "England":
            england_dict["Week"].append(row["Dates"])
            england_dict["England"].append(row["Shannon_diversity"])
            
        if row["Adm1"] == "Wales":
            w_dict["Wales"].append(row["Shannon_diversity"])
            w_dict["Week"].append(row["Dates"])
            
        if row["Adm1"] == "Scotland":
            s_dict["Scotland"].append(row["Shannon_diversity"])
            s_dict["Week"].append(row["Dates"])
            
        if row["Adm1"] == "Northern_Ireland":
            ni_dict["Northern Ireland"].append(row["Shannon_diversity"])
            ni_dict["Week"].append(row["Dates"])
            
            
    england_df = pd.DataFrame(england_dict)
    w_df = pd.DataFrame(w_dict)
    s_df = pd.DataFrame(s_dict)
    ni_df = pd.DataFrame(ni_dict)

    new = england_df.merge(w_df, on="Week", how="outer")
    new2 = new.merge(s_df, on="Week", how="outer")
    new3 = new2.merge(ni_df, on="Week", how="outer")

    new3.sort_values(by="Week", inplace=True)
    new3.fillna(0, inplace=True)
    new3.set_index("Week", inplace=True)

    return new3


def sequencing_centre_lags(taxa_list, sc_dict, submission_date, country):

    colour_dict = {"England":'indianred', "Wales":'darkseagreen', "Northern_Ireland":"skyblue", "Scotland": "steelblue"}

    centre_dates = defaultdict(set)
    lag_dict = defaultdict(list)

    if country == "":
        centres = sc_dict.keys()
    else:
        centres = []
        for k,v in sc_dict.items():
            if v == country:
                centres.append(k)


    for tax in taxa_list:
        centre_dates[tax.sequencing_centre].add(tax.date_dt)

    mrt = {}

    for centre, dates in centre_dates.items():
        most_recent_date = (sorted(dates, reverse=True))[0]
        mrt[centre] = most_recent_date

    lags = {}
    for centre, date in mrt.items():
        lags[centre] = (submission_date - date).days

    ordered_lags = {k:v for k,v in sorted(lags.items(), key=lambda item:item[1])}

    x = ordered_lags.keys()
    y = ordered_lags.values()

    colours = []

    for sc in x:
        colours.append(colour_dict[sc_dict[sc]])

    plt.xticks(rotation=45, size=15)
    plt.ylabel("Days since most recent sequence", size=15)
    plt.xlabel("Sequencing centre", size=15)

    plt.bar(x, y, color = colours)

    for k,v in ordered_lags.items():
        lag_dict["Centre"].append(k)
        lag_dict["Lag in days"].append(v)

    return lag_dict

        

    

    







                
