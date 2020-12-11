import pandas as pd
import numpy as np

subdf = pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/subscribers_attribution_allocation.csv")
tierdf = pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/subid_tier_spend.csv")
convertdf = pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/sub_convert.csv")

subdf = subdf.merge(tierdf, how = "left", left_on = "subid", right_on = "subid")
subdf = subdf.merge(convertdf, how = "left", left_on = "subid", right_on = "subid")

subdf = subdf.dropna()
subdf.to_csv("sub+tier.csv")


