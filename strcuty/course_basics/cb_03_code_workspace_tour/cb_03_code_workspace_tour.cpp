// Code Workspace Tour
// Development environment setup and best practices

/*
PROBLEM DESCRIPTION:
================================================================================
This lesson introduces the coding environment and best practices for
working through data structures and algorithms problems.

Workspace Setup:
- Choose a comfortable code editor (VS Code, PyCharm, etc.)
- Set up proper syntax highlighting
- Configure debugging tools
- Install useful extensions/plugins

Coding Best Practices:
- Use meaningful variable names
- Write clean, readable code
- Add comments for complex logic
- Test your solutions thoroughly
- Use proper indentation and formatting


EXAMPLES:
================================================================================
File Organization:
- Group related problems together
- Use descriptive file names
- Include problem descriptions
- Add time/space complexity notes
- Keep test cases with solutions

Debugging Strategies:
- Use print statements for tracing
- Step through code with debugger
- Test with edge cases
- Verify assumptions with assertions


CONSTRAINTS:
================================================================================
Setup Requirements:
- Code editor with syntax highlighting
- Debugging capabilities
- Version control (Git)
- Testing framework

*/

#include <iostream>
#include <vector>
#include <string>
#include <map>

// SOLUTION:
// ================================================================================
std::vector<std::string> setupWorkspace() {
    /*
    Guidelines for setting up an effective coding workspace
    */
    std::vector<std::string> setupSteps = {
        "Choose a code editor",
        "Install language extensions",
        "Configure debugging",
        "Set up version control",
        "Create project structure",
        "Write first test program"
    };
    return setupSteps;
}

std::map<std::string, std::string> codingStandards() {
    /*
    Best practices for writing clean code
    */
    std::map<std::string, std::string> standards = {
        {"naming", "Use descriptive variable names"},
        {"comments", "Explain complex logic"},
        {"formatting", "Consistent indentation"},
        {"testing", "Include test cases"},
        {"complexity", "Note time/space complexity"}
    };
    return standards;
}

int main() {
    std::cout << "Code Workspace Tour" << std::endl;
    
    auto steps = setupWorkspace();
    std::cout << "Setup steps:" << std::endl;
    for (const auto& step : steps) {
        std::cout << "- " << step << std::endl;
    }
    
    return 0;
}
