#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, right = 0, maxLen = 0;
        unordered_map<char, int> freqMap;
        int maxFreq = 0;

        // Iterate over the string with the right pointer
        while (right < s.size()) {
            // Increment the frequency of the character at the right pointer
            freqMap[s[right]]++;
            
            // Update the maximum frequency of any character in the current window
            maxFreq = max(maxFreq, freqMap[s[right]]);

            // Check if the window is valid
            // (length of window - maxFreq) > k means we need more swaps than allowed
            while ((right - left + 1) - maxFreq > k) {
                freqMap[s[left]]--; // Decrease frequency of the left character
                left++; // Shrink the window from the left
            }

            // Update the maximum length
            maxLen = max(maxLen, right - left + 1);

            // Move the right pointer to expand the window
            right++;
        }

        return maxLen;
    }
};
