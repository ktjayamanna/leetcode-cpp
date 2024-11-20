#include <stack>
#include <string>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> st;

        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            // If the character is a closing bracket, check for a match
            else {
                // If the stack is empty, no matching opening bracket exists
                if (st.empty()) return false;

                char top = st.top();
                st.pop();

                // Check if the current character matches the top of the stack
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }

        // If the stack is empty at the end, all brackets are matched
        return st.empty();
    }
};
