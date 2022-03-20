# Write an algorithm such that if an element in an M x N matrix is zero, it's entire row and column are set to 0







def zero_matrix(matrix):
  cols = len(matrix)
  rows = len(matrix[0])

  curr_col = 0
  curr_row = 0

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      pass


matrix1 = [
 [1,2,3],
 [4,0,6],
 [7,8,9]
]

print(zero_matrix(matrix1))
