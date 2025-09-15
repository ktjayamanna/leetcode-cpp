# Has Subarray Sum
# Check if array contains a subarray with target sum

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, has_subarray_sum, that takes in an list of numbers and a target_sum. 
The function should return a boolean indicating whether or not there exists a subarray of numbers that sums to the given target.

A subarray is a consecutive series of one or more elements of the list.

EXAMPLES:
================================================================================
has_subarray_sum([1, 3, 1, 4, 3], 8) # -> True


COMPLEXITY:
================================================================================
n = length of numbers
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def has_subarray_sum(numbers, target_sum):
  prefix_sums = [0]
  total = 0
  for num in numbers:
    total += num
    prefix_sums.append(total)

  seen = set()
  for current in prefix_sums:
    complement = current - target_sum
    if complement in seen:
      return True
    seen.add(current)
  return False

