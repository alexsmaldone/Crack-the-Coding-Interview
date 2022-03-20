# given an image represented by an N x N matrix, where each pixel in the image is represented by an integer,
# write a method to rotate this matrix by 90degrees
#  Can you do this in place?

# [[1,2,3],
#  [4,5,6],
#  [7,8,9]
# ]

# BECOMES

# [[7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]



def rotate_matrix(matrix):
  """ Rotates a matrix 90deg clockwise """

  n = len(matrix)
  for layer in range(n//2):
    first, last = layer, n - layer - 1
    for i in range(first, last):
      # save top
      top = matrix[layer][i]

      # left -> top
      matrix[layer][i] = matrix[-i - 1][layer]

      # bottom -> left
      matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

      # right -> bottom
      matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

      # top -> right
      matrix[i][-layer - 1] = top
  return matrix

# everything in first mx needs to be last element

mx = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(rotate_matrix(mx))
