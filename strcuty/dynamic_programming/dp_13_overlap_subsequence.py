# Overlap Subsequence - Dynamic Programming Problem
# Find length of longest common subsequence

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, overlap_subsequence, that takes in two strings as arguments. 
The function should return the length of the longest overlapping subsequence.
A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.


EXAMPLES:
================================================================================
[Add examples here]


CONSTRAINTS:
================================================================================
[Add constraints here]

COMPLEXITY:
================================================================================

    n = length of string_1
    m = length of string_2
    Time: O(n*m)
    Space: O(n*m)

"""



# SOLUTION:
# ================================================================================

def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]
  
  if i == len(string_1) or j == len(string_2):
    return 0
  
  if string_1[i] == string_2[j]:
    memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
  else:
    memo[key] = max(
      _overlap_subsequence(string_1, string_2, i + 1, j, memo),
      _overlap_subsequence(string_1, string_2, i, j + 1, memo)
    )
  return memo[key]

