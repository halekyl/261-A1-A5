# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: Assignment 1 Problem 5 - Camel Case
# Description: Three functions that work together to convert a given input string to a “camel case” string.
# Input string will consist of any printable ASCII characters (english letters,
# digits, spaces, underscores, some special characters).

def length(input_string: str) -> int:
    """
    Returns the length of a string.
    """
    length = 0
    for elem in input_string:
        length += 1
    return length

def is_a_letter(character: str) -> bool:
    """
    Returns True is given character is a letter, otherwise False.
    """
    # if not a single letter
    if length(character) > 1:
        return False
    # return True if it a lowercase or uppercase letter
    lowercase = ord("a") <= ord(character) <= ord("z")
    uppercase = ord("A") <= ord(character) <= ord("Z")
    return lowercase or uppercase

def make_lower(character: str) -> str:
    """
    Returns character in lower case.
    """
    # if not a letter
    if not is_a_letter(character):
        return character
    # if uppercase convert to lowercase
    if ord("A") <= ord(character) <= ord("Z"):
        character = chr(ord("a") +  ord(character) - ord("A"))
    return character

def make_upper(character: str) -> str:
    """Returns character in upper case."""
    # if not a letter
    if not is_a_letter(character):
        return character

    # if lowercase convert to uppercase
    if ord("a") <= ord(character) <= ord("z"):
        character = chr(ord("A") + ord(character) - ord("a"))
    return character

def input_cleanup(input_string: str) -> str:
    """
    This function receives the original input string from the user and
    returns a ‘clean’ version of it.
    """

    # indicates start of string
    begin = True
    # if char before was '_' then True
    underscore = False
    # var for string that has been cleaned
    clean_string = ""

    # string cleaning process
    for char in input_string:
        #if it is a letter convert to lowercase and add to clean_string
        if is_a_letter(char):
            clean_string += make_lower(char)
            begin = False
            underscore = False
        # if it not a letter, add "_"
        else:
            if not begin and not underscore:
                clean_string += "_"
                underscore = True
    # remove trailing underscores
    end_char = length(clean_string) - 1
    while end_char >= 0 and not is_a_letter(clean_string[end_char]):
        end_char -= 1
    clean_string = clean_string[:end_char+1]

    return clean_string

def is_clean_string(input_string: str) -> bool:
    """
    This function verifies whether input string is ‘clean’
    and is ready for a ‘camel case’ conversion according to the rules below:
    """
    # if empty string return True
    if length(input_string) == 0:
        return  True
    # if previous character was "_" = True
    underscore = False
    for char in input_string:
        # if char is a letter confirm check that its lowercase
        if is_a_letter(char):
            underscore = False
            if ord("A") <= ord(char) <= ord('Z'):
                return False
            # if the char is not a letter check that its an underscore
        else:
            if char != "_":
                return False
            if underscore:
                return False
            underscore = True
    # check for leading and trailing underscore
    if input_string[0] == '_' or input_string[length(input_string) - 1] == '_':
        return False

    return True


def camel_case(input_string: str, func_is_clean, func_cleanup):
    """
    This function accepts the original input string from the user, as well as functions
    is_clean_string() and input_clean(). It then ‘cleans up’ the
    original user string by calling ​ func_cleanup()​ on it and verifies that
    the resulting string is in fact ‘clean’ by calling ​ func_is_clean()​ function on it.
    returns None or the camelCase version of the given string
    """

    # sanitize input string
    clean_input = func_cleanup(input_string)     # DO NOT DELETE / CHANGE
    # check if input string is ready for camelCase conversion
    if not func_is_clean(clean_input):           # DO NOT DELETE / CHANGE
        return None                              # DO NOT DELETE / CHANGE

    # check that input string has at least two words in it
    # return None if it does not
    underscore_here = False
    for character in clean_input:
        if character == "_":
            underscore_here = True
            break
    # its a single word if no underscore
    if not underscore_here:
        return None

    camel_case_string = ""
    # If previous char was a "_" = True
    underscore = False
    for character in clean_input:
        # if char if a letter convert to uppercase and if the previous char was "_"
        # else lowercase letter
        if is_a_letter(character):
            if underscore:
                camel_case_string += make_upper(character)
                underscore = False
            else:
                camel_case_string += character
        else:
            underscore = True
    # convert clean input string to camel case
    return camel_case_string


# BASIC TESTING
if __name__ == "__main__":
    if __name__ == "__main__":
        test_set = ("_random_ _word_provided",
                    "@$ptr*4con_", " ran  dom  word",
                    "example    word   ", "ANOTHER_Word",
                    "__", "_ _ _", "    ", "435%7_$$", "random")

        # example 1
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(length(result), result)
        print()

        # example 2
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(is_clean_string(test_string), is_clean_string(result))
        print()

        # example 3
        for test_string in test_set:
            result = camel_case(test_string, is_clean_string, input_cleanup)
            print("'" + test_string + "'", "-->", result)