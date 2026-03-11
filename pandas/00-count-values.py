"""
Get the frequency count of each unique level in a categorical column.
"""

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "coin": ["BTC", "ETH", "SOL", "HYPE", "LIT", "ENA", "ZRO", "AAVE", "UNI"],
        "category": [
            "MAJORs",
            "MAJORs",
            "MAJORs",
            "ALTs",
            "ALTs",
            "ALTs",
            "ALTs",
            "ALTs",
            "ALTs",
        ],
    }
)

# 1. use .value_counts() method in pandas
df["category"].value_counts()

# 2. use .unique() method in numpy
counts = np.unique(df["category"].values, return_counts=True)
# it returns a tuple of arrays
print(type(counts))
print(counts[0])
print(counts[1])
# more flexible for plotting with matplotlib
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.bar(counts[0], counts[1], align="center", width=0.6, alpha=0.5)
