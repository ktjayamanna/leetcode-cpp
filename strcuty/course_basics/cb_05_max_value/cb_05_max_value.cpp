// Max Value
// Find the maximum value in an array

/*
PROBLEM DESCRIPTION:
================================================================================
Write a function, maxValue, that takes in a vector of numbers as an argument. The function should return the largest number in the vector.

Solve this without using any built-in methods.

You can assume that the vector is non-empty.


EXAMPLES:
================================================================================
max_value([4, 7, 2, 8, 10, 9]) // -> 10
max_value([-5, -2, -10, -4]) // -> -2
max_value([42]) // -> 42


CONSTRAINTS:
================================================================================
n = # numbers
Time: O(n)
Space: O(1)

*/

// SOLUTION:
// ================================================================================
#include <vector>
#include <limits>

float maxValue(std::vector<float> numbers) {
  float max = -std::numeric_limits<float>::infinity();
  for (float num : numbers) {
    if (num > max) {
      max = num;
    }
  }
  return max;
}
