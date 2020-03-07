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

    while start <= end:
        mid = (start+end)//2

        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binary_search_recursive(lst, key, start=0, end=None):
    """
    Performs binary search with recursion for the given key in iterable.

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

    if not (start <= end):
        return -1

    mid = (start+end)//2

    if lst[mid] == key:
        return mid
    elif lst[mid] < key:
        return binary_search_recursive(lst, key, mid + 1, end)
    else:
        return binary_search_recursive(lst, key, start, mid-1)


if __name__ == "__main__":
    lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    key = 8
    print("index: {}".format(binary_search_iterative(lst, key)))
    print("index: {}".format(binary_search_recursive(lst, key)))
