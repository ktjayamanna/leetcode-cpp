// Hey Programmer!
// Welcome message for new programmers

/*
PROBLEM DESCRIPTION:
================================================================================
A warm welcome to all programmers starting their DSA journey!

This is your starting point for mastering data structures and algorithms.
Whether you're preparing for interviews, improving your problem-solving skills,
or just curious about how computers work efficiently, you're in the right place.

Programming Mindset:
- Think before you code
- Break problems into smaller pieces
- Test your assumptions
- Learn from failures
- Keep practicing regularly


EXAMPLES:
================================================================================
Success Tips:
1. Start with simple problems
2. Understand before optimizing
3. Practice coding by hand
4. Explain your solutions aloud
5. Learn from others' code
6. Don't give up on difficult problems
7. Build projects to apply knowledge


CONSTRAINTS:
================================================================================
Remember:
- Every expert was once a beginner
- Consistency is key to improvement
- Don't be afraid to make mistakes
- Ask questions and seek help when needed
- Celebrate small victories along the way

*/

#include <iostream>
#include <vector>
#include <string>

// SOLUTION:
// ================================================================================
std::string welcomeMessage() {
    /*
    Welcome message for new programmers
    */
    std::string message = R"(
    Hey Programmer! 👋
    
    Welcome to your data structures and algorithms journey!
    
    You're about to learn some of the most fundamental concepts
    in computer science. These skills will make you a better
    programmer and problem solver.
    
    Remember: every line of code you write is progress!
    )";
    return message;
}

std::vector<std::string> programmerTips() {
    /*
    Essential tips for programming success
    */
    std::vector<std::string> tips = {
        "Start with simple problems",
        "Understand before optimizing", 
        "Practice coding by hand",
        "Explain your solutions aloud",
        "Learn from others' code",
        "Don't give up on difficult problems",
        "Build projects to apply knowledge"
    };
    return tips;
}

int main() {
    std::cout << welcomeMessage() << std::endl;
    
    std::cout << "\nTips for success:" << std::endl;
    auto tips = programmerTips();
    for (size_t i = 0; i < tips.size(); ++i) {
        std::cout << (i + 1) << ". " << tips[i] << std::endl;
    }
    
    return 0;
}
