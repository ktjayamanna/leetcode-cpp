# Count Compounds - Dynamic Programming Problem
# Count how many words can be formed by concatenating other words

"""
PROBLEM DESCRIPTION:
================================================================================
You are a chemist and have to figure out how many ways you can make a given compound.

Write a function, count_compounds, that takes in a target compound and a list of elements. The function should return the number of ways we can make the compound with the given elements.

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
def count_compounds(compound, elements):
  return _count_compounds(compound, elements, 0, {})

def _count_compounds(compound, elements, idx, memo):
  if idx == len(compound):
    return 1

  if idx in memo:
    return memo[idx]

  count = 0
  for ele in elements:
    if compound.startswith(ele.lower(), idx):
      count += _count_compounds(compound, elements, idx + len(ele), memo)

  memo[idx] = count
  return count



