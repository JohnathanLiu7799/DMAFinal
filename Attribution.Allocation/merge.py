import pandas as pd
import numpy as np

subdf = pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/subscribers_attribution_allocation.csv")
tierdf = pd.read_csv("C:/Users/John/Downloads/DMA Final/Attribution.Allocation/subid_tier_spend.csv")

subdf.merge(tierdf, how = "left", left_on = "subid", right_on = "subid").to_csv("sub+tier.csv")
