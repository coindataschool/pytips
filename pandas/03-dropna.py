# drop rows where all cell values are missing
# if a row has at least 1 non-missing cells, it won't be dropped
df.dropna(how="all")

# drop columns where all cell values are missing
# if a col has at least 1 non-missing cells, it won't be dropped
df.dropna(how="all", axis=1)
