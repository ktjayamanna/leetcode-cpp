# Permutations
# Generating all permutations of a collection

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, permutations, that takes in a list an argument. 

The function should return a 2D list where each sublist represents one of the possible permutations of the list.

The sublists may be returned in any order.

You may assume that the input list contains unique items.

EXAMPLES:
================================================================================

permutations(['a', 'b', 'c']) # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 


COMPLEXITY:
================================================================================
n = length of elements array
Time: ~O(n!)
Space: ~O(n!)

"""

# SOLUTION:
# ================================================================================
def permutations(items):
  if not items:
    return [[]]
  
  first = items[0]
  remaining = items[1:]
  perms = permutations(remaining)
  result = []
  for perm in perms:
    for i in range(len(perm) + 1):
      result.append([*perm[:i], first, *perm[i:]])
    
  return result


