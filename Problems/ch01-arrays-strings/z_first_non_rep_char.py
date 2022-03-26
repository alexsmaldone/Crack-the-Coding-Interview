# return index of first non repeating character, -1 if no non-repeating characters

def firstNonRepChar(string):
  char_freq = {}

  for character in string:
    char_freq[character] = char_freq.get(character, 0) + 1

  for i in range(len(string)):
    character = string[i]
    if char_freq[character] == 1:
      return i

  return -1

test = "abcdcaf"

print(firstNonRepChar(test))
