def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    return None if (len(lst) == 0) else lst[-1]

    if len(lst) == 0:
        return None
    return lst[-1]