# Subarray Sum Count
# Count number of subarrays with target sum

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, subarray_sum_count, that takes in an list of numbers and a targetSum. The function should return the number of subarrays that sum to the given target.

A subarray is a consecutive series of one or more elements of the list.

EXAMPLES:
================================================================================
subarray_sum_count([-2, 1, 1, 1, -1, 1, 1, 1, 1], 3) # -> 8
subarray_sum_count([1, 3, 1, 4, -2, 3], 5) # -> 3

COMPLEXITY:
================================================================================
n = length of numbers
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
from collections import Counter

def subarray_sum_count(numbers, target_sum):
  prefix_sums = [0]
  total = 0
  for num in numbers:
    total += num
    prefix_sums.append(total)

  seen = Counter()
  count = 0
  for current in prefix_sums:
    complement = current - target_sum
    count += seen[complement]
    seen[current] += 1
  return count

