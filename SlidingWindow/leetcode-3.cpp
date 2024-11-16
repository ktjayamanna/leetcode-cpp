

#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
     int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet; // To track unique characters
        int left = 0;               // Left pointer of the window
        int maxLength = 0;          // To store the maximum length

        for (int right = 0; right < s.size(); ++right) {
            // If duplicate character found, move the left pointer
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]); // Remove the leftmost character
                ++left;                // Move the left pointer
            }
            charSet.insert(s[right]);  // Add the current character to the set
            maxLength = max(maxLength, right - left + 1); // Update maxLength
        }

        return maxLength;
    }
};
