def list_powerset(iterable):
    """
    Find all subsets (in the form of list not set) of an interable.

    Parameters
    ----------
    iterable : an iterable object
        A list, string, tuple, set, or an iterator.

    Returns
    -------
    list
        A list containing all subsets of elements from the given iterable.
    """
    result = [[]]
    for x in iterable:
        # 1) .extend() modifies the list in-place, while + creates a new list.
        #   So for large lists, .extend() is much faster while + wastes memory
        #   and time by copying everything.
        # 2) we cannot use .extend() for the inner list expansion: `subset + [x]`.
        #   Doing so throws AttributeError: 'NoneType' object has no attribute 'extend'.
        result.extend([subset + [x] for subset in result])
    return result


if __name__ == "__main__":
    print(list_powerset(range(3)))
    print(list_powerset("BTC"))
    print(list_powerset(["BTC", "ETH"]))
    print(list_powerset({"ETH", "BTC", "GMX"}))
    print(list_powerset(("ETH", "BTC", "GMX")))
