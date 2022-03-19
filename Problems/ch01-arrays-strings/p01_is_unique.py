# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# QUESTIONS TO ASK
  # Are we dealing with ASCII or Unicode strings?
  # ASCII -- 7bit 128 characters. First 32 are control codes, until 128 are upper and lowercase letters and numbers, along w/ special symbols
  # extended ASCII -- 8bit 256chars, different symbols like fractions, intl currency, accented letters, etc.
  # Unicode --  as of  May 2019, unicode contains over 137k characters including different scripts of languages and emojis, represetned by unicode pointsl ike U+0061, U+1F590, etc

test1 = "abcdefg"
test2 = "aabcdefg"
test3 = ""

# This solution is O(n) time complexity as it loops through entire string
# Add to dict and check dict are average case O(1) worst case O(n). space complexity could be O(1) since we're never making anything bigger than 128 keys (in ASCII case)
def isUnique(string):
  if len(string) <= 1:
    return True

  if len(string) > 128: # in the case that we're dealing with regular ASCII character set.
    return False

  newDict = {}

  for char in string:
    if char in newDict:
      return False
    else:
      newDict[char] = 1

  return True

# O(n) time complexity, O(1) space complexity?
def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)

print(isUnique(test1))
print(isUnique(test2))
print(isUnique(test3))

print(is_unique_chars_pythonic(test1))
print(is_unique_chars_pythonic(test2))
print(is_unique_chars_pythonic(test3))
