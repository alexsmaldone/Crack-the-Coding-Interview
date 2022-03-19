# Given two strings, write a method to decide if one is a permutation of the other
from collections import Counter
# counter returns dictionary with count of characters in key value pairs

string1 = "cat 1"
string10 = "1 cat"

string2 = "a  aaabc"
string20 = "cb aaaa"

string3 = ""
string30 = ""


# O(N logN + M logM) time complexity for the sort functions, O(n) space complexity for the variables created
def is_permutation_sort(s1, s2):
  if len(s1) != len(s2):
    return False
  s1, s2 = sorted(s1), sorted(s2)
  return s1 == s2


# O(n+m time complexity, same for space complexity?)
def is_permutation_pythonic(s1, s2):
  if len(s2) != len(s2):
    return False
  return Counter(s1) == Counter(s2)


print(is_permutation_sort(string1, string10))
print(is_permutation_sort(string2, string20))
print(is_permutation_sort(string3, string30))

print(is_permutation_pythonic(string2, string20))
