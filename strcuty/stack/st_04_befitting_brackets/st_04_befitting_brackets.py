# Befitting Brackets
# Check if brackets are properly matched

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, befitting_brackets, that takes in a string as an argument. 
The function should return a boolean indicating whether or not the string contains correctly matched brackets.
You may assume the string contains only characters: ( ) [ ] { }


EXAMPLES:
================================================================================
print(befitting_brackets('(){}[](())'))   # True
print(befitting_brackets('({[]})'))       # True
print(befitting_brackets('[]{}('))        # False
print(befitting_brackets('{[]}({}'))      # False
print(befitting_brackets('{}[]{}[]'))     # False
print(befitting_brackets('{}[](){}[]'))   # True
print(befitting_brackets('{}]()'))        # False
print(befitting_brackets(''))             # True
print(befitting_brackets('{[]()}'))       # False


CONSTRAINTS:
================================================================================
n = length of string
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================

def befitting_brackets(string):
  stack = []
  
  brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  
  for char in string:
    if char in brackets:
      stack.append(brackets[char])
    else:
      if stack and stack[-1] == char:
        stack.pop()
      else:
        return False
      
  return len(stack) == 0

