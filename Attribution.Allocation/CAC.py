import pandas as pd
import numpy as np
import json

###Imports Data###
#-note: Something with my installations is messing with relative paths, hence why I use all absolute paths.
#-note: Relatves paths will be commented under anywhere a file is imported
df = pd.read_csv('C:/Users/John/Downloads/DMA Final/Attribution.Allocation/sub+tier.csv')
#df = pd.read_csv('sub+tier.csv')

df_true=df[(df.convert_TF==True)]
df_true

###Creates dictionary of People By Attribution & Tier
tech_people = dict()
for comp in df_true['attribution_technical'].unique():
    tech_people[comp] = [[] for i in range(df_true['tier'].nunique())]

for comp in df_true['attribution_technical'].unique():
    tech_people[comp] = [[] for i in range(df_true['tier'].nunique())]

survey_people = {comp: [[] for i in range(df_true['tier'].nunique())] for comp in df['attribution_technical'].unique()}
survey_people.pop('display')
survey_people.pop('bing')

tier = df_true['tier'].unique()
tier.sort()

###Fills in Values
for i in tier:
    temp = df_true.loc[df['tier']==i,:]
    for j in range(len(temp['attribution_technical'].value_counts())):
        tech_people[temp['attribution_technical'].unique()[j]][i-1] = temp['attribution_technical'].value_counts()[j]
        
for i in tier:
    temp = df_true.loc[(df['tier']==i)&(df_true['attribution_survey'].isin(survey_people.keys())),:]
    for j in range(len(temp['attribution_survey'].value_counts())):
        survey_people[temp['attribution_survey'].unique()[j]][i-1] = temp['attribution_survey'].value_counts()[j]


###Gives values to people by attribution
df_tech_people=pd.DataFrame(columns=tech_people.keys(),index=tier)
for k in tech_people:
    df_tech_people[k]=tech_people[k]


df_survey_people=pd.DataFrame(columns=survey_people.keys(),index=tier)
for j in survey_people:
    df_survey_people[j]=survey_people[j]

###Imports channel data
channel_spend=pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/channel_spend_undergraduate.csv")

###Creates and loads tiers of spending into channel_spend
chan_spend_dict={}
for i in range(8):
  chan_spend_dict[i+1]= json.loads(channel_spend['spend'][i].replace("'",'"'))
#assign the value of chan_spand_dict to channel_spend
channel_spend=chan_spend_dict

df_spend=pd.DataFrame(columns=tech_people.keys(),index=tier)
for c in df_spend.columns:
    l = []
    for i in tier:
        l.append(channel_spend[i][c])

    df_spend[c] = l

###Calculates AVG CAC for each spending and tier
df_avg_CAC_tech=pd.DataFrame(columns=tech_people.keys(),index=tier)

for v in df_spend.columns:
    for i in tier:
        df_avg_CAC_tech[v][i] = df_spend[v][i] / df_tech_people[v][i]
        

df_avg_CAC_survey=pd.DataFrame(columns=survey_people.keys(),index=tier)

for k in [k for k in df_spend.columns if k in survey_people.keys()]:
    for i in tier:
        df_avg_CAC_survey[k][i] = df_spend[k][i] / df_survey_people[k][i]

###Calculates Marginal CAC
df_Marg_CAC_tech=pd.DataFrame(columns=tech_people.keys(),index=tier)

for z in df_spend.columns:
    for i in tier:
        if i == 1:
            df_Marg_CAC_tech[z][i] = df_spend[z][i] / df_tech_people[z][i]
        else:
            df_Marg_CAC_tech[z][i] = (df_spend[z][i] - df_spend[z][i-1]) / df_tech_people[z][i]
    
df_Marg_CAC_survey=pd.DataFrame(columns=survey_people.keys(),index=tier)

for z in [z for z in df_spend.columns if z in survey_people.keys()]:
    for i in tier:
        if i == 1:
            df_Marg_CAC_survey[z][i] = df_spend[z][i] / df_survey_people[z][i]
        else:
            df_Marg_CAC_survey[z][i] = (df_spend[z][i] - df_spend[z][i-1]) / df_survey_people[z][i]
        
print(df_avg_CAC_survey)
print(df_avg_CAC_tech)
print(df_avg_CAC_survey)
print(df_avg_CAC_tech)
