""" 
PROBLEM DESCRIPTION:
================================================================================
Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth X + Y points where X, Y are substrings of well-formed brackets
[S] is worth S * 2 points where S is a substring of well-formed brackets
For example:

[[][][]] is equivalent to (1 + 1 + 1) * 2 = 6

You may assume that the input only contains well-formed square brackets. 


COMPLEXITY:
================================================================================
n = length of string
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def nesting_score(string):
  stack = [0]
  
  for char in string:
    if char == '[':
      stack.append(0)
    else:
      popped = stack.pop()
      if popped == 0:
        stack[-1] += 1
      else:
        stack[-1] += 2 * popped
  
  return stack[0]
