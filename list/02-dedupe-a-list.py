from collections import OrderedDict

items = ["zoo", "foo", "bar", "bar", "foo", "baz", "zoo"]

# remove duplicates from a list without preserving the original order
list(set(items))

# remove duplicates from a list and keep the original order
list(OrderedDict.fromkeys(items).keys())
