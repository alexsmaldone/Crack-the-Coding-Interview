
# initial solution that is O(n logn)T and O(n)S
def sortedSquaredArray(array):
  # Write your code here.
  squaredArray = [num**2 for num in array]
  squaredArray.sort()
  return squaredArray

arr1 = [-20, 1, 2, 3, 5, 6, 8, 9]
arr2 = [1]

print(sortedSquaredArray(arr1))
print(sortedSquaredArray(arr2))


# 2nd solution that is O(n)T and O(n)S
def sortedSquaredArray2(array):
  smIdx = 0
  lgIdx = len(array) - 1
  result = [0 for _ in array]

  for idx in reversed(range(len(array))):
    smallerValue = array[smIdx]
    largerValue = array[lgIdx]

    if abs(smallerValue) > abs(largerValue):
      result[idx] = smallerValue**2
      smIdx += 1
    else:
      result[idx] = largerValue**2
      lgIdx -= 1

  return result


# comment


print(sortedSquaredArray2(arr1))
print(sortedSquaredArray2(arr2))
