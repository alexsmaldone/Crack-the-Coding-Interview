"""
Write a method to replace all spaces in a string with `%20`. You may assume that the string has sufficient
space at the end to hold the additional characters.
and that you are given the true length of the string.
"""

str1 = "Mr John Smith    " #answer: "Mr%20John%20Smith"
listStr = list(str1)
print(str1[:13])

def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")


print(urlify_algo(str1, 13))
print(urlify_pythonic(str1, 13))
