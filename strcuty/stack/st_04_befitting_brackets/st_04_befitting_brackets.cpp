// Befitting Brackets
// Check if brackets are properly matched

/*
PROBLEM DESCRIPTION:
================================================================================
Write a function befittingBrackets that takes in a string as an argument.
The function should return a boolean indicating whether or not the string contains properly matched brackets.

You may assume the string contains only brackets and no other characters.
The types of brackets are: ( ) [ ] { }


EXAMPLES:
================================================================================
befittingBrackets("(){}[](())") // -> true
befittingBrackets("({[]})") // -> true
befittingBrackets("[][}") // -> false
befittingBrackets("{[}]") // -> false
befittingBrackets("((()") // -> false


CONSTRAINTS:
================================================================================
- String contains only bracket characters: ( ) [ ] { }
- 0 <= len(string) <= 10^5

Time: O(n) where n is the length of the string
Space: O(n) in worst case for the stack

*/

#include <string>
#include <stack>

// SOLUTION:
// ================================================================================
// [Add your C++ solution here]
