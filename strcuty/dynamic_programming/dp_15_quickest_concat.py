# Quickest Concat - Dynamic Programming Problem
# Find minimum number of words to form target string

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, quickest_concat, that takes in a string and a list of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the list. If it is not possible to build the string, then return -1.

You may use words of the list as many times as needed.


EXAMPLES:
================================================================================
[Add examples here]


CONSTRAINTS:
================================================================================
[Add constraints here]

COMPLEXITY:
================================================================================

s = length of string
w = # of words
Time: ~O(sw)
Space: O(s)

"""

# SOLUTION:
# ================================================================================
def quickest_concat(s, words):
  result = _quickest_concat(s, words, 0, {})
  if result == float('inf'):
    return -1
  else:
    return result

def _quickest_concat(s, words, i, memo):
  if i in memo:
    return memo[i]
  
  if i == len(s):
    return 0
  
  min_words = float('inf')
  for word in words:
    if s.startswith(word, i):
      attempt = 1 + _quickest_concat(s, words, i + len(word), memo)
      min_words = min(attempt, min_words)
  
  memo[i] = min_words
  return min_words


