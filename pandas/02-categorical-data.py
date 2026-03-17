# use when
#   - data has only a few (<10 or 20 ideally) unique values
#   - not limited to strings
# benefits:
#   - use less memory than strings
#   - improved performance
#   - can have an ordering
#   - can perform operations on categories
#   - enforce membership on values

import pandas as pd

sizes = ["M", "L", "XS", "S", "XL"]
s1 = pd.Series(sizes, dtype="category")
s1

s2 = pd.Series(sizes)
s2 = s2.astype("category")
s2

# check if the categories are ordered
s2.cat.ordered
# order the categories
size_type = pd.api.types.CategoricalDtype(categories=["S", "M", "L"], ordered=True)
s3 = s2.astype(size_type)
s3  # categories omitted from the ordering are converted to NaN
s3 > "S"  # can compare the ordered categories
s3.str.upper()  # can still use the 'str' attribute

# alternatively
s2.cat.reorder_categories(["XS", "S", "M", "L", "XL"], ordered=True)
