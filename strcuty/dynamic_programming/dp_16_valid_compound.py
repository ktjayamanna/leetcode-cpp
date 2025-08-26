# Valid Compound - Dynamic Programming Problem
# Check if a word can be formed by concatenating other words

"""
PROBLEM DESCRIPTION:
================================================================================
You are a chemist and have to figure out if you can make a compound from some given elements!

Write a function, valid_compound, that takes in a target compound and a list of elements. The function should return a boolean indicating whether or not the compound can be created from the given elements.

A compound is made by concatenating one or more elements together.

You may reuse elements of the list as many times as needed to make a compound.


EXAMPLES:
================================================================================
[Add examples here]


CONSTRAINTS:
================================================================================
[Add constraints here]

COMPLEXITY:
================================================================================

c = length of compound
e = # of elements
Time: O(cw)
Space: O(c)

"""

# SOLUTION:
# ================================================================================
def valid_compound(compound, elements):
  return _valid_compound(compound, elements, 0, {})

def _valid_compound(compound, elements, i, memo):
  if i == len(compound):
    return True

  if i in memo:
    return memo[i]

  for ele in elements:
    if compound.startswith(ele.lower(), i):
      if _valid_compound(compound, elements, i + len(ele), memo):
        memo[i] = True
        return True

  memo[i] = False
  return False

