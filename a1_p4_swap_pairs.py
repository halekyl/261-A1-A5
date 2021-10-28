# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: Assign 1 Problem 4 Swap Pairs
# Description: Program with a function that receives a one dimensional list of integers and
# returns a new list of the same length where pairs of elements are swapped
# (a[0] swapped with a[1], a[2] swapped with a[3] etc). Original list is not changed.

def swap_pairs(arr: []) -> []:
    """
    Returns list of swapped elements
    """
    # if empty list
    if arr == []:
        # return empty list
        return []
    # copy the list
    list_b = list(arr)
    list_length = len(list_b)
    for elem in range(0, list_length, 2):
        #if last element of list break loop, also odd numbered len lists break here
        if elem == list_length -1:
            break
        else:
            #swap the elements
            elem_temp = list_b[elem]
            list_b[elem] = list_b[elem+1]
            list_b[elem+1] = elem_temp
    return list_b


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(swap_pairs([1, 2, 3, 4, 5]))

    # example 2
    print(swap_pairs([8, 7, 6, -5, 4, 10]))

    # example 3
    print(swap_pairs([]))
