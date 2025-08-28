# Decompress Braces
# Expand compressed string with braces

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function decompressBraces that takes in a compressed string as an argument.
The function should return the decompressed version of the string.

The compression format is: number followed by braces containing the string to repeat.
For example, "3{abc}" should become "abcabcabc".

You can assume that the input only contains lowercase alphabetic characters and numeric digits.


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

"""

# SOLUTION:
# ================================================================================
# [Add your Python solution here]
