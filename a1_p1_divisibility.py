# CS261 - Data Structures
# Kylee Bonds
# Description: Program with a function that receives 4 integers ( m, n, a, b )
# and for each number in the range [ m, n ] (inclusive) determines whether it is divisible by
# a , or it is divisible by b , or both a and b or by neither a nor b and returns the result
# as a list of strings, each string as separate list element.


def length(s: str) -> int:
    """
    Calculates the length of string, but not used.
    """
    len = 0
    for elem in s:
        len += 1
    return 0


def is_divisible(m: int, n: int, a: int, b: int) -> []:
    """
    Returns the result as list of strings.
    """
    # if any of these true then return incorrect input
    if (m > n or a == b or a < 0 or b < 0 or m < 0 or n < 0):
        return "Incorrect input"
    else:
        list_nums = []
        list_nums.append("Num\tDiv by "+str(a)+" and/or "+str(b)+"?")
        list_nums.append("---\t-------------------")
        # string format = number and divisible by separated by tab
        for num in range(n, m - 1, -1):
            if (num % a == 0 and num % b == 0):
                list_nums.append(str(num) + "\t" + "both")
            elif (num % a == 0):
                list_nums.append(str(num) + "\t" + "div by " + str(a))
            elif (num % b == 0):
                list_nums.append(str(num) + "\t" + "div by " + str(b))
            else:
                list_nums.append(str(num) + "\t" + "None")
        return list_nums


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(*is_divisible(2, 7, 2, 3), sep="\n")

    # example 2
    print(is_divisible(1, 20, -1, 3))
    print(is_divisible(20, 0, 100, 200))
    print(is_divisible(10, 8, 7, 2))
    print(is_divisible(3, 30, 7, 7))
