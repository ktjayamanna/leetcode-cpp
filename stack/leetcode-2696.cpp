#include <stack>
#include <string>

class Solution {
public:
    int minLength(string s) {
        std::stack<char> stack;
        std::string result = "";
        
        // Push all characters to stack
        for (char c : s) {
            stack.push(c);
        }

        // Pointer to the current result string
        int pointer = -1;

        while (!stack.empty()) {
            char poppedChar = stack.top();
            stack.pop();

            if (pointer == -1) {
                // First character, append to the result
                result.push_back(poppedChar);
                pointer = 0;
            } else {
                // Add the character to the result but check for BA or CD
                result.push_back(poppedChar);

                // Check the last two characters
                int len = result.length();
                if (len >= 2 && 
                   ((result[len - 2] == 'B' && result[len - 1] == 'A') ||
                    (result[len - 2] == 'D' && result[len - 1] == 'C'))) {
                    // Remove the last two characters
                    result.pop_back();
                    result.pop_back();

                    // Update the pointer
                    pointer = result.empty() ? -1 : result.length() - 1;
                } else {
                    // Update the pointer to the last character
                    pointer = result.length() - 1;
                }
            }
        }

        // Return the final length of the result string
        return result.length();
    }
};
