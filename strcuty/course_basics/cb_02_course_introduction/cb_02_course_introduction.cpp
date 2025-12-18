// Course Introduction
// Overview of the Structy course

/*
PROBLEM DESCRIPTION:
================================================================================
Welcome to the Structy Data Structures and Algorithms Course!

Course Structure:
- Introduction and Fundamentals
- Array and String Manipulation
- Linked Lists
- Stacks and Queues
- Binary Trees
- Graphs
- Dynamic Programming
- Advanced Topics

What You'll Learn:
- Core data structures and their operations
- Algorithm design patterns
- Time and space complexity analysis
- Problem-solving strategies
- Interview preparation techniques


EXAMPLES:
================================================================================
Topics covered:
- Arrays and Strings
- Linked Lists
- Stacks and Queues
- Binary Trees
- Graphs
- Dynamic Programming
- Recursion
- Sorting and Searching


CONSTRAINTS:
================================================================================
Prerequisites:
- Basic programming knowledge
- Understanding of variables, functions, loops
- Familiarity with at least one programming language

*/

#include <iostream>
#include <vector>
#include <string>

// SOLUTION:
// ================================================================================
std::vector<std::string> courseOverview() {
    /*
    This course covers essential data structures and algorithms
    needed for technical interviews and software development.
    */
    std::vector<std::string> topics = {
        "Arrays and Strings",
        "Linked Lists", 
        "Stacks and Queues",
        "Binary Trees",
        "Graphs",
        "Dynamic Programming",
        "Recursion",
        "Sorting and Searching"
    };
    
    return topics;
}

int main() {
    std::cout << "Course Introduction" << std::endl;
    auto topics = courseOverview();
    std::cout << "Topics covered:" << std::endl;
    for (const auto& topic : topics) {
        std::cout << "- " << topic << std::endl;
    }
    return 0;
}
