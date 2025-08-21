# Can Concat - Dynamic Programming Problem
# Determine if target string can be formed by concatenating words

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, can_concat, that takes in a string and a list of words as arguments. 
The function should return boolean indicating whether or not it is possible to concatenate words of the list together to form the string.

You may reuse words of the list as many times as needed.


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
def can_concat(s, words):
  return _can_concat(s, words, 0, {})

def _can_concat(s, words, i, memo):
  if i in memo:
    return memo[i]
  
  if i == len(s):
    return True
  
  for word in words:
    if s.startswith(word, i):
      if _can_concat(s, words, i + len(word), memo) == True:
        memo[i] = True
        return True
      
  memo[i] = False
  return False


