# Given a string, write a function to check if it's a permutation of a palindrome.
# A palindrome is a word or phrase that is the same backwards as it is forward.
# Not limited to just dictionary words
# Can ignore casing and non-letter characters
from collections import Counter
import string



def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]


test1 = "racecar" #true
test2 = "apple" # false
test3 = "Tact Coa" #true
test4 = "aaaassasdfs" #true
test5 = "" #true

def is_palindrome(string):
  strippedString = string.replace(" ", "")
  lowerString = strippedString.lower()
  length = len(lowerString)

  if length <= 1:
    return True

  charDict = {}
  for char in lowerString:
    if char in charDict:
      charDict[char] += 1
    else:
      charDict[char] = 1

  if length % 2 == 0:
    for val in charDict.values():
      if val % 2 != 0:
        return False
    return True

  if length % 2 != 0:
    counter = 0
    for val in charDict.values():
      if val % 2 != 0:
        counter += 1
    if counter > 1:
      return False
    else:
      return True

def is_palindrome_permutation_pythonic(phrase):
  counter = Counter(clean_phrase(phrase))
  print(counter)
  print(sum(val % 2 for val in counter.values()))
  return sum(val % 2 for val in counter.values()) <= 1



# print(is_palindrome(test1))
# print(is_palindrome(test2))
# print(is_palindrome(test3))
# print(is_palindrome(test4))
# print(is_palindrome(test5))

print(is_palindrome_permutation_pythonic(test1))
print(is_palindrome_permutation_pythonic(test2))
print(is_palindrome_permutation_pythonic(test3))
print(is_palindrome_permutation_pythonic(test4))
print(is_palindrome_permutation_pythonic(test5))
