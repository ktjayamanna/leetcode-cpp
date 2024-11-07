#include <string>
#include <cctype> // for isalnum and tolower
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // Move left pointer to the next alphanumeric character
            while (left < right && !isalnum(s[left])) {
                left++;
            }
            // Move right pointer to the previous alphanumeric character
            while (left < right && !isalnum(s[right])) {
                right--;
            }

            // Convert both characters to lowercase for case-insensitive comparison
            if (tolower(s[left]) != tolower(s[right])) {
                return false; // Characters do not match
            }

            left++;
            right--;
        }
        return true; // All characters match
    }
};
