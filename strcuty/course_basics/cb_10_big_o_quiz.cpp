// Big-O Quiz
// Test your understanding of time complexity analysis

/*
PROBLEM DESCRIPTION:
================================================================================
This quiz tests your understanding of Big-O notation and complexity analysis.

For each code snippet, determine the time complexity in Big-O notation.
Consider the worst-case scenario and focus on the dominant term.

Quiz Questions:
1. What is the time complexity of accessing an element in an array by index?
2. What is the time complexity of linear search in an unsorted array?
3. What is the time complexity of binary search in a sorted array?
4. What is the time complexity of bubble sort?
5. What is the time complexity of merge sort?


EXAMPLES:
================================================================================
Example 1:
int example1(vector<int>& arr) {
    return arr[0];
}
// Answer: O(1)

Example 2:
void example2(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << endl;
    }
}
// Answer: O(n)

Example 3:
void example3(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size(); j++) {
            cout << arr[i] << " " << arr[j] << endl;
        }
    }
}
// Answer: O(n²)


CONSTRAINTS:
================================================================================
Remember to:
- Consider worst-case scenarios
- Drop constants and lower-order terms
- Focus on how runtime grows with input size
- Identify the dominant operation

*/

#include <iostream>
#include <vector>

// SOLUTION:
// ================================================================================
// [Add your C++ solution here]
