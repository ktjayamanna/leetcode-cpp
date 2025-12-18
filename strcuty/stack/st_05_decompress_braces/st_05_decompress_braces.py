# Decompress Braces
# Expand compressed string with braces

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.


EXAMPLES:
================================================================================
decompressBraces("2{q}3{tu}v") # -> "qqtututuv"
decompressBraces("ch3{ao}") # -> "chaoaoao"
decompressBraces("2{y3{o}}s") # -> "yoooyooos"
decompressBraces("z") # -> "z"
decompressBraces("2{3{r}4{e}5{w}}") # -> "rrreeeeewwwwwrrreeeeewwwww"


CONSTRAINTS:
================================================================================
- String contains only lowercase letters, digits, and braces
- Numbers are always followed by braces
- Braces can be nested
- 1 <= len(string) <= 10^5

Time: O(m) where m is the length of the decompressed string
Space: O(m) for the result and stack space

COMPLEXITY:
================================================================================
s = length of string
m = count of brace pairs
Time: O((9^m) * s)
Space: O((9^m) * s)

"""

# SOLUTION:
# ================================================================================
def decompress_braces(string):
  numbers = '123456789'
  stack = []
  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      if char == '}':
        segment = ''
        while isinstance(stack[-1], str):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segment * num)
      elif char != '{':
        stack.append(char)
  return ''.join(stack)

