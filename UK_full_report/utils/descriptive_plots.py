from collections import Counter
from collections import defaultdict
from collections import OrderedDict
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


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


def make_timeline(intro_bigs):

    colour_dict = {"wales":"darkseagreen",
            "england":"indianred",
            "scotland":"steelblue",
            "northern_ireland":"skyblue"}

    fig,ax = plt.subplots(figsize=(15,35))

    count = 0
    height = []
    ytick_list = []

    for intro in intro_bigs:
        colours = []
        sizes = []
        sizes2 = []
        count += 1
        
        point_one = intro.oldest
        point_two = intro.mrd
        
        x = [point_one, point_two]
        y = [count, count]
        
        y2 = []
        x2 = list(intro.dates)
        
        for i in x2:
            sizes2.append((intro.date_counts[i])*50)
            y2.append(count)
        
        country_set = set()
        for i in intro.taxa:
            if i.date_dt != "NA":
                if i.country == "england":
                    colours.append("indianred")
                    country_set.add("england")
                elif i.country == "scotland":
                    colours.append("steelblue")
                    country_set.add("scotland")
                elif i.country == "wales":
                    colours.append("darkseagreen")
                    country_set.add("wales")
                elif i.country == "northern_ireland":
                    colours.append("skyblue")
                    country_set.add("northern_ireland")
                else:
                    print(i.country)
        
        height.append(count)
        ytick_list.append(intro.id)
        
        if point_one != point_two:
            plt.scatter(x2,y2, c=colours, zorder=2, s=sizes2)
            plt.plot(x,y, color='black', zorder=1)
            
        else:
            sizes.append(list(intro.date_counts.values())[0]*50)
            sizes.append(list(intro.date_counts.values())[0]*50)
            
            if len(country_set) > 1:
                plt.scatter(x,y, color='black',s=sizes)
            else:
                plt.scatter(x,y, color=colour_dict[list(country_set)[0]], s=sizes)
        
    plt.yticks(height, ytick_list)
    plt.xticks(rotation=45)

def plot_bars(intro_bigs):
	
    labels = []
    E = []
    S = []
    W = []
    NI = []

    for i in intro_bigs[::-1]:

        E_c=0
        S_c = 0
        W_c = 0
        NI_c = 0
        
        
        labels.append(i.id.lstrip("UK"))

        for tax in i.taxa:
            if tax.country=="england":
                E_c += 1
            elif tax.country=="scotland":
                S_c += 1
            elif tax.country=="wales":
                W_c += 1
            elif tax.country=="northern_ireland":
                NI_c += 1
        
        
        E.append(E_c)
        S.append(S_c)
        W.append(W_c)
        NI.append(NI_c)

    width = 0.8

    fig,ax = plt.subplots(figsize=(30,15))

    colours=['indianred','steelblue','darkseagreen','skyblue']

    E = np.array(E)
    S = np.array(S)
    W = np.array(W)
    NI = np.array(NI)

    ax.bar(labels, E, width, label='England', color='indianred')
    ax.bar(labels, S, width, label='Scotland', color='steelblue', bottom = E)
    ax.bar(labels, W, width, label='Wales', color='darkseagreen', bottom = E+S)
    ax.bar(labels, NI, width, label='Northern_Ireland', color='skyblue', bottom = E+S+W)

    # ax.bar(labels, E, width, label='England', color='indianred')
    # ax.bar(labels, S, width, label='Scotland', color='steelblue')
    # ax.bar(labels, W, width, label='Wales', color='darkseagreen')
    #

    plt.xticks(rotation=90, size=25, fontweight='heavy')
    plt.yticks(size=25, fontweight='heavy')

    ax.set_ylabel('Number of sequences', size=40, fontweight='bold')
    ax.set_xlabel("Introduction number", size=40, fontweight='bold')
    ax.set_title('Sequences after introduction by country', size=50, fontweight='bold')
    ax.legend(fontsize=40)

    plt.show()

def top_ten_sort(lineage):
    return len(lineage.taxa)

def plot_geog_plot(lineages_prep, normed):

    lineages_of_interest = sorted(lineages_prep, key=top_ten_sort, reverse=True)[:10]

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
            
        
        new_name = "y"+str(count)
        
        y_dict[new_name] = count_list

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
        ax.set_title("Lineages by number of adm2 regions present by epiweek normalised")
        plt.ylabel("Number of adm2 regions present in lineage normalised")
    else:
        ax.set_title("Lineages by number of adm2 regions present by epiweek")
        plt.ylabel("Number of adm2 regions present in lineage")
   
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], title = "Lineage", bbox_to_anchor=(1.2,1.05))
    plt.xticks(rotation=45)
    plt.xlabel("Week commencing")
    #plt.show()

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
    
    ax.set_title("Lineage starts per week", size=45)
    plt.xlabel("Week commencing", size=30)
    plt.ylabel("Number of earliest sequences", size=30)
    plt.legend()
    plt.show()

def plot_sequences_over_time(sequences):

    fig,ax = plt.subplots(1,1,figsize=(30,15), dpi= 80)

    sequence_dates = defaultdict(list)

    E = []
    S = []
    W = []
    NI = []
    labels = []

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
            if tax.country=="england":
                E_c += 1
            elif tax.country=="scotland":
                S_c += 1
            elif tax.country=="wales":
                W_c += 1
            elif tax.country=="northern_ireland":
                NI_c += 1

        E.append(E_c)
        S.append(S_c)
        W.append(W_c)
        NI.append(NI_c)

    #seq_counts = Counter(sequence_dates)

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
    plt.yticks(size=10, fontweight='heavy')

    ax.set_ylabel('Number of sequences', size=40, fontweight='bold')
    ax.set_xlabel("Day", size=40, fontweight='bold')
    ax.set_title('Sequences taken on each day by country', size=50, fontweight='bold')
    ax.legend(fontsize=40)

    plt.show()

    # x = list(seq_counts.keys())
    # y = list(seq_counts.values())

    # ax.bar(x,y)






                
