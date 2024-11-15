#include <iostream>
#include <string>
#include <unordered_set>

class Solution {
public:
    std::string longestNiceSubstring(const std::string& s) {
        int n = s.size();
        std::string longestNiceSubstring = "";
        int left = 0;

        while (left < n) {
            std::unordered_set<char> charSet;
            std::string currentSubstring = "";

            for (int right = left; right < n; ++right) {
                charSet.insert(s[right]);
                currentSubstring += s[right];
                bool isNice = true;

                // Check if the substring is nice
                for (char c : charSet) {
                    if (islower(c) && charSet.find(toupper(c)) == charSet.end()) {
                        isNice = false;
                        break;
                    }
                    if (isupper(c) && charSet.find(tolower(c)) == charSet.end()) {
                        isNice = false;
                        break;
                    }
                }

                if (isNice && currentSubstring.length() > longestNiceSubstring.length()) {
                    longestNiceSubstring = currentSubstring;
                }
            }

            // Advance the left pointer
            ++left;
        }

        return longestNiceSubstring;
    }
};

int main() {
    Solution solution;
    std::string s = "YazaAay";
    std::cout << "Longest nice substring: " << solution.longestNiceSubstring(s) << std::endl;
    return 0;
}
