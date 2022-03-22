
# O(n^2)T, O(1)S
def twoNumberSum(array, targetSum):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i] + array[j] == targetSum:
        return [array[i], array[j]]
  return []


arr = [3, 5, -4, 8, 11, 1, -1, 6, 4]
target = 10

print(twoNumberSum(arr, target))


# O(n)T | O(n)S
def twoNumberSum2(array, targetSum):
  nums = {}
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  return []

print(twoNumberSum2(arr, target))
