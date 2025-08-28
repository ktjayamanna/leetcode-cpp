# Paired Parentheses
# Check if parentheses are properly paired

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function pairedParentheses that takes in a string as an argument.
The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only parentheses, no other characters.


EXAMPLES:
================================================================================
pairedParentheses("(david)((abby))") # -> True
pairedParentheses("()rose(jeff") # -> False
pairedParentheses(")(") # -> False
pairedParentheses("()") # -> True
pairedParentheses("(((pokemon)))") # -> True
pairedParentheses("(())(water)()") # -> True
pairedParentheses("((()") # -> False


CONSTRAINTS:
================================================================================
- String contains only '(' and ')' characters
- 0 <= len(string) <= 10^5

Time: O(n) where n is the length of the string
Space: O(n) in worst case for the stack

"""

# SOLUTION:
# ================================================================================
# [Add your Python solution here]
