# Running Sum
# Calculate running sum of array elements

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, running_sum, that takes in a list of numbers. 
The function should return a new list of the same length where each element contains the running sum up to that index of the original list.
For example, the i-th result should be the sum of all elements 0 to i:

result[i] = numbers[0] + numbers[1] + numbers[2] + ... + numbers[i]

EXAMPLES:
================================================================================


COMPLEXITY:
================================================================================
n = length of list
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def running_sum(numbers):
  total = 0
  result = []
  for num in numbers:
    total += num
    result.append(total)
  return result

