def is_iterable(obj):
    """
    Check if an object is iterable or not.

    Parameters
    ----------
    obj : object
        Any python object.

    Returns
    -------
    bool
        True if an iterator can be obtained from the object; False otherwise.
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False


if __name__ == "__main__":
    print(is_iterable(range(5)))  # True
    print(is_iterable("klsdf"))  # True
    print(is_iterable(34))  # False
