// Stack Welcome
// Introduction to stack data structure

/*
PROBLEM DESCRIPTION:
================================================================================
Welcome to the Stack section!

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
Think of it like a stack of plates - you can only add or remove plates from the top.

Key Stack Operations:
- Push: Add an element to the top of the stack
- Pop: Remove and return the top element from the stack
- Peek/Top: View the top element without removing it
- isEmpty: Check if the stack is empty
- Size: Get the number of elements in the stack

Common Use Cases:
- Function call management (call stack)
- Undo operations in applications
- Expression evaluation and syntax parsing
- Backtracking algorithms
- Browser history navigation


EXAMPLES:
================================================================================
Basic stack operations:
std::stack<int> stack;
stack.push(1);     // push 1
stack.push(2);     // push 2
stack.push(3);     // push 3
// stack now has 3 at the top

int top = stack.top();  // returns 3
stack.pop();            // removes 3, stack now has 2 at top


CONSTRAINTS:
================================================================================
Stack Properties:
- LIFO (Last In, First Out) access pattern
- Operations are performed at one end (top)
- Efficient O(1) push and pop operations
- Can be implemented using arrays or linked lists

*/

#include <stack>
#include <vector>

// SOLUTION:
// ================================================================================
// [Add your C++ solution here]
