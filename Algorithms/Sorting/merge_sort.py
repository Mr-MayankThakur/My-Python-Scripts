def merge_sort(lst, reversed = False):
    """
    Sorts the given list using recursive merge sort algorithm.

    Parameters
    ----------
    lst (iterable)- python which you want to search
    reversed (bool): sorts the list in ascending order if False

    Returns
    -------
    sorted_list

    """
    if len(lst) == 1:
        return lst
    mid = (0+len(lst))//2
    if reversed:
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))[::-1]
    else:
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


def merge(lst1, lst2):
    output = []
    i = j = 0
    while i<len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            output.append(lst1[i])
            i+=1
        else:
            output.append(lst2[j])
            j+=1

    # checking if elements left in lst1
    if i<len(lst1):
        output += lst1[i:]

    # checking if elements left in lst2
    if j < len(lst2):
        output += lst2[j:]

    return output

if __name__ == "__main__":
    l1 = [1,2, 4,6]
    l2 = [2, 3, 5]
    l3 = [99,22,33,44,88,55,77,66,11]
    print(merge_sort(l3, True))