# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: Assignment 1 Problem 2 Min-Max
# Description: Program with a function that receives a one dimensional list of integers
# and returns a tuple with two values - minimum and maximum values in the input list.
# If the input list is empty, the function returns a tuple (None, None)

def min_max(arr: []) -> ():
    """
    Returns the minimum and maximum values of the input list.
    """
    min = 1
    max = -1
    counter = 0
    for num in arr:
        if num < min:     # if true update min
            min = num
        if num > max:     # if true update max
            max = num
        counter +=1       # increment the counter
    if counter != 0:
        return min, max
    return None, None


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(min_max([1, 2, 3, 4, 5]))

    # example 2
    print(min_max([8, 7, 6, -5, 4]))

    # example 3
    print(min_max([]))