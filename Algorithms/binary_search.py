def binary_search_iterative(lst, key, start=0, end=None):
    """
    Performs binary search for the given key in iterable.

    Parameters
    ----------
    lst : python iterable in which you want to search key
    key : value you want to search
    start : starting index
    end : ending index

    Returns
    -------
    index (int): key's index if found else -1

    """

    if not end:
        end = len(lst)

    while start<end:
        mid = (start+end)//2

        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return -1

