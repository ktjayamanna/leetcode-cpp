#include <unordered_map>
#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        // Step 1: Check if lengths are different
        if (s.length() != t.length()) {
            return false;
        }

        // Step 2: Create a hashmap to count characters in s
        std::unordered_map<char, int> charCount;
        for (char ch : s) {
            charCount[ch]++;
        }

        // Step 3: Iterate through t and adjust the frequency counts
        for (char ch : t) {
            if (charCount.find(ch) == charCount.end() || charCount[ch] == 0) {
                return false;  // Character not found or too many occurrences in t
            }
            charCount[ch]--;
        }

        // Step 4: Check if all counts are zero (optional, since t length matches s)
        for (const auto& pair : charCount) {
            if (pair.second != 0) {
                return false;
            }
        }

        return true;
    }
};
