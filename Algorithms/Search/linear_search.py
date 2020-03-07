def linear_search_iterative(lst, key):
    for index, value in enumerate(lst):
        if key == value:
            return index
    return -1


def linear_search_recursive(lst, key, start=0):
    if len(lst[start:]) == 0:
        return -1
    elif lst[start] == key:
        return start
    else:
        return linear_search_recursive(lst, key, start+1)


if __name__ == "__main__":
    lst = input("Please enter a space separated list: ").split(" ")
    key = input("Please enter key you want to find: ")
    method = input("Enter\n1 for iterative linear search(Default).\n2 for recursive linear search.\n>> ")
    if method == "2":
        print("Using Recursive Linear Search")
        result = linear_search_recursive(lst, key)
    else:
        print("Using Iterative Linear Search")
        result = linear_search_iterative(lst, key)

    if result == -1:
        print("Element not Found")
    else:
        print("Element found at index: {}".format(result))
