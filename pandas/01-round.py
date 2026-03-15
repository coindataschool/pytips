import numpy as np
import pandas as pd

np.random.seed(444)

ser = pd.Series(np.random.randn(4))
print(ser)
print(ser.round(2))

df = pd.DataFrame(np.random.randn(3, 3), columns=["A", "B", "C"])
df
df.round(3)

# round col A to 1 decimal place, B to 2 decimals, and C to 3 decimals
df.round({"A": 1, "B": 2, "C": 3})

# alternatively, we can construct a series to hold the decimal places
decimals = pd.Series([1, 2, 3], index=["A", "B", "C"])
df.round(decimals)

# we can apply numpy's rounding functions to pandas' dataframes
np.floor(df)
np.ceil(df)
np.rint(df)  # round to the nearest integer
