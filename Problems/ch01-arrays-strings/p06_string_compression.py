# Implement method to perform basic string compression using the counts of repeated characters
# for example, 'aabccccaaa' would become 'a2b1c4a3'
# If the compressed string would not become smaller than the original string, reuturn the original string
#  Can assume that string has only uuppercase and lowercase letters

#O(n) time complexity and linear O(n) space complexity
def compressString(string):
  compressed = []
  counter = 0
  for i in range(len(string)):
    if i != 0 and string[i] != string[i-1]:
      compressed.append(string[i-1] + str(counter))
      counter = 0
    counter += 1

  if counter:
    compressed.append(string[-1] + str(counter))

  return min(string, "".join(compressed), key=len)


print(compressString("aabcccccaaa"))
print(compressString("abcdef"))
print(compressString("aabb"))
print(compressString("aaa"))
print(compressString("aa"))
print(compressString("a"))
print(compressString(""))

#  ("aabcccccaaa", "a2b1c5a3"),
#         ("abcdef", "abcdef"),
#         ("aabb", "aabb"),
#         ("aaa", "a3"),
#         ("a", "a"),
#         ("", ""),
