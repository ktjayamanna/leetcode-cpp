# Paired Parentheses
# Check if parentheses are properly paired

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.

Complexity:
================================================================================
n = length of string
Time: O(n)
Space: O(1)

"""

# SOLUTION:
# ================================================================================
def paired_parentheses(string):
  count = 0
  
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1
      
  return count == 0



# TESTS:
# ================================================================================
def test_paired_parentheses():
    """Test cases for paired parentheses function"""

    # Test case 1: Nested parentheses with names
    assert paired_parentheses("(david)((abby))") == True

    # Test case 2: Unmatched opening parenthesis
    assert paired_parentheses("()rose(jeff") == False

    # Test case 3: Closing before opening
    assert paired_parentheses(")(") == False

    # Test case 4: Simple balanced pair
    assert paired_parentheses("()") == True

    # Test case 5: Multiple nested parentheses
    assert paired_parentheses("(((pokemon)))") == True

    # Test case 6: Multiple balanced groups
    assert paired_parentheses("(())(water)()") == True

    # Test case 7: Unmatched opening parentheses
    assert paired_parentheses("((()") == False

    print("All tests passed!")


if __name__ == "__main__":
    # Run tests when file is executed directly
    test_paired_parentheses()
