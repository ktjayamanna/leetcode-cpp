# Subsets
# Generating all subsets of a collection

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, subsets, that takes in a list as an argument. 

The function should return a 2D list where each sublist represents one of the possible subsets of the list.

The elements within the subsets and the subsets themselves may be returned in any order.

You may assume that the input list contains unique elements.

EXAMPLES:
================================================================================
subsets(['a', 'b', 'c']) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]


COMPLEXITY:
================================================================================
n = length of elements array
Time: ~O(2^n)
Space: ~O(2^n)

"""

# SOLUTION:
# ================================================================================
def subsets(elements):
  if not elements:
    return [[]]

  first = elements[0]
  remaining_elements = elements[1:]
  subsets_without_first = subsets(remaining_elements)

  subsets_with_first = []
  for sub in subsets_without_first:
    subsets_with_first.append([ first, *sub ])

  return subsets_without_first + subsets_with_first


