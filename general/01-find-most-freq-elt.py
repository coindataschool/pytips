"""
Find the most frequent element in a list
"""

# method 1. use Counter
from collections import Counter

a = [
    "George",
    "David",
    "Anna",
    "George",
    "David",
    "Anna",
    "David",
    "David",
    "Hector",
    "Jin",
    "George",
]
cnt = Counter(a)
cnt.most_common(1)  # [(element, frequency), ...]

# method 2. pass the list's count method to max()
most_freq_elt = max(set(a), key=a.count)
(most_freq_elt, a.count("David"))
