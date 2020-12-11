import pandas as pd
import numpy as np

from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
import matplotlib.pylab as plt

import os

pd.set_option('display.max_columns', 25)

def run_kmeans(n_clusters_f, init_f, df_f):
    ##### Complete this function
    # This function should at least take a dataframe as an argument. I have suggested additional arguments you may
    # want to provide, but these can be changed as you need to fit your solution.
    # The output of this function should be the input data frame will the model object KMeans and a data summary. The
    # function will need to add an additional column to the input dataframe called 'predict_cluster_kmeans'
    # that contains the cluster labels assigned by the algorithm.

    k_means_model_f = KMeans(n_clusters_f, init_f)
    
    df_f['predict_cluster_kmeans'] = k_means_model_f.fit_predict(df_f)

    # summarize cluster attributes
    #k_means_model_f_summary = df_f.groupby('predict_cluster_kmeans').agg(attribute_summary_method_dict)
    return k_means_model_f #k_means_model_f_summary

attribute_summary_method_dict = {'intended_use': sum, 'male_TF': sum, 'attribution_technical': sum, 'current_sub_TF': sum, 'trial_completed': sum}    

# ------ Import data ------
#df_transactions = pd.read_pickle('transactions_n100000')
# fp = os.path.join("C:","Users",   "John","Documents","Github","Fall2020_CustomerSegmentation")
# fp = "C:\\Users\\John\\Documents\\Github\\Fall2020_CustomerSegmentation"
fp = "~John\\Downloads\\DMA Final\\Segmentation"
df_subscribers = pd.read_csv(os.path.join(fp, "subscribers_processed.csv"), sep = ",")

df = df_subscribers

# --- convert categorical store variables to dummies
encoded_data = OneHotEncoder(sparse = False)   ##### use sklearn.preprocessing.OneHotEncoder() to create a class object called encoded_data (see documentation for OneHotEncoder online)
categories = ['intended_use','male_TF','attribution_technical','current_sub_TF','trial_completed']

for cat in categories:
    encoded_data.fit_transform(np.array(df[cat]).reshape(-1,1)) 
    ##### call the method used to fit data for a OneHotEncorder object. Note: you will have to reshape data from a column of the data frame. useful functions may be DataFrame methods .to_list(), .reshape(), and .shape()
    col_map_store_binary = dict(zip(list(encoded_data.get_feature_names()), [ x.split('x0_')[1] for x in encoded_data.get_feature_names()]))

    df_store_binary = pd.DataFrame(encoded_data.transform(X=np.array(df[cat].tolist()).reshape(df.shape[0], 1)))
    df_store_binary.columns = encoded_data.get_feature_names()
    df_store_binary.rename(columns=col_map_store_binary, inplace=True)

    df = pd.concat([df, df_store_binary], axis=1)

# ------ RUN CLUSTERING -----
# --- set parameters
n_clusters = 5
init_point_selection_method = 'k-means++'

df_s_b = df_store_binary.columns[:]

#cols_for_clustering = df.columns[1:5].union(df.columns[7:8]).union(df_s_b)
cols_for_clustering = df.columns[2:4].union(df.columns[7:8]).union(df.columns[9:])
df_cluster = df.loc[:, cols_for_clustering]

# --- split to test and train
df_cluster_train, df_cluster_test, _, _, = train_test_split(df_cluster, [1]*df_cluster.shape[0], test_size=0.33)   # ignoring y values for unsupervised

# training data
train_model = run_kmeans(n_clusters, init_point_selection_method, df_cluster_train.reindex())
# testing data
test_model = run_kmeans(n_clusters, init_point_selection_method, df_cluster_test.reindex())
# all data
model= run_kmeans(n_clusters, init_point_selection_method, df_cluster)

# --- run for various number of clusters
##### add the code to run the clustering algorithm for various numbers of clusters
"""
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = run_kmeans(k, init_point_selection_method, df_cluster)
    distortions.append(kmeanModel.inertia_)
# --- draw elbow plot
##### create an elbow plot for your numbers of clusters in previous step

plt.figure(figsize=(16,8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title("Elbow Plot With Optimal K")
plt.show()
"""

# --- output tagged data for examination ----
#store_col_names = ['store_1', 'store_2', 'store_3', 'store_4', 'store_5', 'store_6', 'store_7', 'store_8', 'store_9']
#cols_for_clustering = df.columns[2:4].union(df.columns[7:8]).union(df.columns[9:])
#store_col_names = ['access to exclusive content','education','expand international access','expand regional access','other','replace OTT','supplement OTT']
store_col_names = cols_for_clustering.tolist()
df_cluster['intended_usage'] = None
for t_col in store_col_names:
    df_cluster.loc[df_cluster[t_col] == 1, 'intended_use'] = t_col

attribute_names = cols_for_clustering[2:34]
current_names = cols_for_clustering[34:36]
intended_names = cols_for_clustering[36:43]
gender_names = cols_for_clustering[43:45]
trial_names = cols_for_clustering[47:49]

df_cluster['attribute'] = None
for t_col in attribute_names:
    df_cluster.loc[df_cluster[t_col] == 1, 'attribute'] = t_col.split('_')[1]

df_cluster['currentSub'] = None
for t_col in current_names:
    df_cluster.loc[df_cluster[t_col] == 1, 'currentSub'] = t_col.split('_')[1]

df_cluster['intended'] = None
for t_col in intended_names:
    df_cluster.loc[df_cluster[t_col] == 1, 'intended'] = t_col.split('_')[1]

df_cluster['gender'] = None
for t_col in gender_names:
    df_cluster.loc[df_cluster[t_col] == 1, 'gender'] = t_col.split('_')[1]

df_cluster['trial'] = None
for t_col in trial_names:
    df_cluster.loc[df_cluster[t_col] == 1, 'trial'] = t_col.split('_')[1]

df_cluster.to_csv('clustering_output.csv')