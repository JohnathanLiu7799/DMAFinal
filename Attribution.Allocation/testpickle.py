import pandas as pd
import numpy as np

pd.DataFrame()

df = pd.read_csv('subtier.csv')
df.to_pickle("pickled_sub_tier.pkl")
channel_spend = pd.read_csv('channel_spend_undergraduate.csv')
channel_spend.to_pickle("channel_spend_undergraduate.pkl")

channel_spend['total'] = dict()