# find the most frequent element in a list

# method 1: pass frequency count method to max's key arg
a = [1,2,3,1,2,3,2,2,4,5,1]
max(set(a), key=a.count)
# a.count(2)

# method 2: use Counter
from collections import Counter
cnt = Counter(a)
cnt.most_common(1) # [(element, frequency), ...]
