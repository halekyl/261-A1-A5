# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: Assignment 1 Problem 3 Matrix Addition
# Description: Program with a function that receives two two-dimensional matrices and returns the result
# of their addition. If matrices have different dimensions, the function returns None.


def matrix_add(a: [[]], b: [[]]) -> [[]]:
    """
    Returns result of matrices addition.
    """
    #create zero filled matrix
    matrix = [[0] * len(a[_]) for _ in range(len(a))]

    # check if matrices have same number of rows
    # true if lengthof matrices is equal otherwise is false
    if len(a) == len(b):
        result = [True if len(row_m2) == len(row_m1) else False for row_m2 in b for row_m1 in a]
    # if all are True in output
        if all(result):
        #iterate over m1 rows
            for elem in range(0, len(a)):
            #iterate over columns
                for val in range(0, len(a[elem])):
                #add elements in matrix m1 and m2
                    matrix[elem][val] = a[elem][val] + b[elem][val]
            # return the matrix
            return matrix
        else:
            return None
    # if different number of rows return False
    else:
        return None

# BASIC TESTING
if __name__ == "__main__":
    # example 1
    m1 = [[1, 2, 3], [2, 3, 4]]
    m2 = [[5, 6, 7], [8, 9, 10]]
    m3 = [[1, 2], [3, 4], [5, 6]]

    print(matrix_add(m1, m2))
    print(matrix_add(m1, m3))
    print(matrix_add(m1, m1))
    print(matrix_add([[]], [[]]))
    print(matrix_add([[]], m1))

