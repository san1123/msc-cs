def MaxSubArray(MyList):
  max_sum = 0
  current_sum = 0
  for i in MyList:
    current_sum = current_sum + i
    if current_sum < 0:
      current_sum = 0
    if max_sum < current_sum:
      max_sum = current_sum
  return max_sum


MyList = [-66,-3,64,-12,-37,19,26,60,6,-33,-64,-68,56,-14,21,27,-21,43,87,1]
print(f"Input array: {MyList}")
print("Maximum SubArray is:",MaxSubArray(MyList))
