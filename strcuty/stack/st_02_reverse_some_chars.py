# Reverse Some Chars
# Reverse a portion of a string using stack

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, reverse_some_chars, that takes in string and an list of characters. 
The function should return the string with the order of the given characters in reverse.


EXAMPLES:
================================================================================
reverse_some_chars("computer", ["a", "e", "i", "o", "u"]) # -> 'cemputor'



CONSTRAINTS:
================================================================================
n = length of string
m = length of chars list
Time: O(n + m)
Space: O(n + m)

"""

# SOLUTION:
# ================================================================================
def reverse_some_chars(s, chars):
  char_set = set(chars)
  stack = []
  for ch in s:
    if ch in char_set:
      stack.append(ch)

  result = []
  for ch in s:
    if ch in char_set:
      result.append(stack.pop())
    else:
      result.append(ch)

  return "".join(result)

