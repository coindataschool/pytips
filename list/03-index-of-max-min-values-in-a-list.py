# find the index of the max and min value in a list
lst = [40, 10, 20, 30]

# which index makes lst.__getitem__(index) the biggest
max(range(len(lst)), key=lst.__getitem__)

# which index makes lst.__getitem__(index) the smallest
min(range(len(lst)), key=lst.__getitem__)
