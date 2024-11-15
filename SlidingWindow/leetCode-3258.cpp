#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
    int left = 0;              // Left pointer
    int countZeros = 0;        // Count of zeros in the current window
    int countOnes = 0;         // Count of ones in the current window
    int numOfSubstrings = 0;   // Total number of valid substrings

    // Iterate over the string with the right pointer
    for (int right = 0; right < s.size(); ++right) {
        // Update the counts based on the current character
        if (s[right] == '0') {
            countZeros++;
        } else {
            countOnes++;
        }

        // Shrink the window if it doesn't satisfy the k-constraint
        while (countZeros > k && countOnes > k) {
            if (s[left] == '0') {
                countZeros--;
            } else {
                countOnes--;
            }
            left++;
        }

        // Add the number of valid substrings ending at the current position
        numOfSubstrings += (right - left + 1);
    }

    return numOfSubstrings;
    }
};


