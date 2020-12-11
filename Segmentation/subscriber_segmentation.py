import pandas as pd
import numpy as np

from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
import matplotlib.pylab as plt

import os
from sklearn.preprocessing import LabelEncoder

import math

pd.set_option('display.max_columns', 25)

# ------ Define functions ------
def run_kmeans(n_clusters_f, init_f, df_f):
    ##### Complete this function
    # This function should at least take a dataframe as an argument. I have suggested additional arguments you may
    # want to provide, but these can be changed as you need to fit your solution.
    # The output of this function should be the input data frame will the model object KMeans and a data summary. The
    # function will need to add an additional column to the input dataframe called 'predict_cluster_kmeans'
    # that contains the cluster labels assigned by the algorithm.

    k_means_model_f = KMeans(n_clusters_f, init_f)
    
    df_f['predict_cluster_kmeans'] = k_means_model_f.fit_predict(df_f)

    return k_means_model_f

# ------ Import data ------
#df_transactions = pd.read_pickle('transactions_n100000')
# fp = os.path.join("C:","Users",   "John","Documents","Github","Fall2020_CustomerSegmentation")
# fp = "C:\\Users\\John\\Documents\\Github\\Fall2020_CustomerSegmentation"
fp = "~John\\Downloads\\DMA Final\\Segmentation"
df_subscribers = pd.read_csv(os.path.join(fp, "subscribers_processed.csv"), sep = ",")

df = df_subscribers

# --- convert categorical store variables to dummies
encoded_data = OneHotEncoder(sparse = False)   ##### use sklearn.preprocessing.OneHotEncoder() to create a class object called encoded_data (see documentation for OneHotEncoder online)

categorical_headers = ['intended_use','male_TF','attribution_technical','current_sub_TF','trial_completed']
categorical_labelled_dfs = []
for i in categorical_headers:
    le = LabelEncoder()
    tent_curr_types = list(set(df[i]))
    curr_types = []
    for j in tent_curr_types:
        if not pd.isnull(j):
            curr_types.append(j)
    curr_df = pd.DataFrame(curr_types, columns=[i])
    print(curr_types, curr_df)
    curr_df[f'{i}_cat'] = le.fit_transform(curr_df[i])
    categorical_labelled_dfs.append(curr_df)

for i in categorical_labelled_dfs:
    print(i)

fit_targets = ['intended_use_cat','male_TF_cat','attribution_technical_cat','current_sub_TF_cat','trial_completed_cat']
j = 0
print(categorical_labelled_dfs[1]['male_TF_cat'])
for i in categorical_headers:
    print(f'{i}_cat')
    print(categorical_labelled_dfs[j][f"{i}_cat"])
    encoded_data.fit(np.array(categorical_labelled_dfs[j][i]).reshape(-1,1))

    j+=1

# ------ RUN CLUSTERING -----
# --- set parameters
n_clusters = 3
init_point_selection_method = 'k-means++'

"""
# --- convert categorical store variables to dummies
encoded_data = OneHotEncoder(sparse = False)   ##### use sklearn.preprocessing.OneHotEncoder() to create a class object called encoded_data (see documentation for OneHotEncoder online)
encoded_data.fit(np.array(df['location']).reshape(-1,1)) 
"""

model = run_kmeans(n_clusters, init_point_selection_method, df)