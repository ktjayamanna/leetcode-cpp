#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
      vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0); // Initialize the result array with zeros
        stack<int> s; // Stack to store indices

        for (int i = 0; i < n; ++i) {
            // While the stack is not empty and the current element is greater than the top element of the stack
            while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
                int idx = s.top(); // Get the index at the top of the stack
                s.pop(); // Remove it from the stack
                result[idx] = i - idx; // Calculate the difference and store it in the result array
            }
            s.push(i); // Push the current index onto the stack
        }

        return result;
    }
};
