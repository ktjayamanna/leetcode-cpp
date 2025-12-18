// Pairs
// Find pairs that sum to a target

/*
PROBLEM DESCRIPTION:
================================================================================
Write a function, isPrime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.


EXAMPLES:
================================================================================


Complexity:
================================================================================
n = input number
Time: O(square_root(n))
Space: O(1)

*/


// SOLUTION:
// ================================================================================
#include <math.h>

bool isPrime(int n) {
  if (n < 2) {
    return false;
  }
  
  for (int i = 2; i <= sqrt(n); i += 1) {
    if (n % i == 0) {
      return false;
    }
  }
  
  return true;
}
