# comment change

# O(n)T and O(1)S
def isValidSubsequence(array, sequence):
  length = len(sequence)
  counter = 0
  seq_index = 0

  i = 0
  while i < len(array):
    if seq_index >= length:
      break
    if array[i] == sequence[seq_index]:
      counter += 1
      seq_index += 1
    i += 1

  return counter == length

arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]


print(isValidSubsequence(arr, seq))
