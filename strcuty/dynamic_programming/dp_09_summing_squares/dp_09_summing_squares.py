# Summing Squares - Dynamic Programming Problem
# Find minimum number of perfect squares that sum to target

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, summing_squares, that takes a target number as an argument. The function should return the minimum number of perfect squares that sum to the target. A perfect square is a number of the form (i*i) where i >= 1.

For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.


EXAMPLES:
================================================================================
Given 12:

summing_squares(12) -> 3

The minimum squares required for 12 is three, by doing 4 + 4 + 4.

Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.



Complexity:
================================================================================

    n = length of nums
    Time: O(n * sqrt(n))
    Space: O(n)


"""

# SOLUTION:
# ================================================================================
def summing_squares(n, memo = None):
  if memo is None:
    memo = dict()
  if n in memo:
    return memo[n]
  if n == 0:
    return 0
  if n < 0:
    return float('inf')
  min_sq = float('inf')
  for base in range(1, n + 1):
    sq = base ** 2
    if sq <= n:
      min_sq = min(
        summing_squares(n - sq, memo),
        min_sq
      )
    else:
      break
  memo[n] = 1 + min_sq
  assert min_sq != float('inf'), f"no update happened for n={n}"

  return 1 + min_sq


import math

def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n) + 1)):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(min_squares, num_squares)
  
  memo[n] = min_squares
  return min_squares

    
  


