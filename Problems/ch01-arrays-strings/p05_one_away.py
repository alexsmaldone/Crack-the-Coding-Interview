# There are 3 types of edits that can be perfromed on a string -- insert a character, remove a character, or replace a character.
# Given two strings, write function to check if they are one edit or zero edits away


# pale, ple TRUE
# pales, pale TRUE
# pale, bale TRUE
# pale, bae FALSE

def oneEdit(s1, s2):
  if s1 == s2:
    return True

  return False


print(oneEdit("pale","ple"))
print(oneEdit("pales","pale"))
print(oneEdit("pale","bale"))
print(oneEdit("pale","bae"))
