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
tech = dict()
for comp in df_true['attribution_technical'].unique():
    tech[comp] = [[] for i in range(df_true['tier'].nunique())]

for comp in df_true['attribution_technical'].unique():
    tech[comp] = [[] for i in range(df_true['tier'].nunique())]

survey = dict()
for comp in df_true['attribution_survey'].unique():
    survey[comp] = [[] for i in range(df_true['tier'].nunique())]

for comp in df_true['attribution_survey'].unique():
    survey[comp] = [[] for i in range(df_true['tier'].nunique())]

"""
survey = {comp: [[] for i in range(df_true['tier'].nunique())] for comp in df['attribution_technical'].unique()}
survey.pop('display')
survey.pop('bing')
"""

tier = df_true['tier'].unique()
tier.sort()

###Fills in Values
for i in tier:
    temp = df_true.loc[df['tier']==i,:]
    for j in range(len(temp['attribution_technical'].value_counts())):
        tech[temp['attribution_technical'].unique()[j]][i-1] = temp['attribution_technical'].value_counts()[j]
        
for i in tier:
    temp = df_true.loc[(df['tier']==i)&(df_true['attribution_survey'].isin(survey.keys())),:]
    for j in range(len(temp['attribution_survey'].value_counts())):
        survey[temp['attribution_survey'].unique()[j]][i-1] = temp['attribution_survey'].value_counts()[j]


###Gives values to people by attribution
df_tech=pd.DataFrame(columns=tech.keys(),index=tier)
for k in tech:
    df_tech[k]=tech[k]


df_survey=pd.DataFrame(columns=survey.keys(),index=tier)
for j in survey:
    df_survey[j]=survey[j]

###Imports channel data
channel_spend=pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/channel_spend_undergraduate.csv")

###Creates and loads tiers of spending into channel_spend
channel_spend_dict={}
for i in range(8):
  channel_spend_dict[i+1]= json.loads(channel_spend['spend'][i].replace("'",'"'))
#assign the value of chan_spand_dict to channel_spend
channel_spend=channel_spend_dict

df_spend=pd.DataFrame(columns=tech.keys(),index=tier)
for c in df_spend.columns:
    l = []
    for i in tier:
        l.append(channel_spend[i][c])

    df_spend[c] = l

###Calculates AVG CAC for each spending and tier
df_tech_avg_CAC=pd.DataFrame(columns=tech.keys(),index=tier)

for v in df_spend.columns:
    for i in tier:
        df_tech_avg_CAC[v][i] = df_spend[v][i] / df_tech[v][i]
        

df_survey_avg_CAC=pd.DataFrame(columns=survey.keys(),index=tier)

for k in [k for k in df_spend.columns if k in survey.keys()]:
    for i in tier:
        df_survey_avg_CAC[k][i] = df_spend[k][i] / df_survey[k][i]

###Calculates Marginal CAC
df_tech_marg_CAC=pd.DataFrame(columns=tech.keys(),index=tier)

for z in df_spend.columns:
    for i in tier:
        if i == 1:
            df_tech_marg_CAC[z][i] = df_spend[z][i] / df_tech[z][i]
        else:
            df_tech_marg_CAC[z][i] = (df_spend[z][i] - df_spend[z][i-1]) / df_tech[z][i]
    
df_survey_marg_CAC=pd.DataFrame(columns=survey.keys(),index=tier)

for z in [z for z in df_spend.columns if z in survey.keys()]:
    for i in tier:
        if i == 1:
            df_survey_marg_CAC[z][i] = df_spend[z][i] / df_survey[z][i]
        else:
            df_survey_marg_CAC[z][i] = (df_spend[z][i] - df_spend[z][i-1]) / df_survey[z][i]

print(df_tech_marg_CAC)
print(df_survey_marg_CAC)
print(df_tech_avg_CAC)
print(df_survey_avg_CAC)