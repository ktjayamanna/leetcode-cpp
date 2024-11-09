#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size();
        int m = needle.size();

        // Edge case: if the needle is empty, return 0
        if (m == 0) return 0;

        // Iterate through the haystack
        for (int i = 0; i <= n - m; ++i) {
            int j = 0;

            // Check for match starting at index i
            while (j < m && haystack[i + j] == needle[j]) {
                ++j;
            }

            // If we reached the end of the needle, match found
            if (j == m) {
                return i;
            }
        }

        // No match found
        return -1;
    }
};
