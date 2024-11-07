#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Map to store groups of strings based on their length
        unordered_map<int, vector<string>> lengthGroups;
        
        // Step 1: Group strings by their length
        for (const string& str : strs) {
            // Group strings by pushing them into the corresponding length key
            lengthGroups[str.size()].push_back(str);
        }

        // Result vector to store the final groups of anagrams
        vector<vector<string>> result;
        
        // Step 2: Process each length group separately
        for (const auto& group : lengthGroups) {
            // Map to store anagrams by their sorted character pattern
            unordered_map<string, vector<string>> anagramMap;
            
            // Step 2a: Iterate over each string in the current length group
            for (const string& str : group.second) {
                // Sort the string to find its "signature" for anagram grouping
                string sortedStr = str;
                sort(sortedStr.begin(), sortedStr.end());
                
                // Use sorted string as a key to group anagrams in the map
                anagramMap[sortedStr].push_back(str);
            }
            
            // Step 3: Collect all groups of anagrams from anagramMap into the result
            for (const auto& anagramGroup : anagramMap) {
                result.push_back(anagramGroup.second);
            }
        }
        
        // Return all the groups of anagrams
        return result;
    }
};

int main() {
    Solution solution;
    // Sample input: array of strings with potential anagrams
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    
    // Call the groupAnagrams function and store the result
    vector<vector<string>> groupedAnagrams = solution.groupAnagrams(strs);

    // Output the result in groups
    for (const auto& group : groupedAnagrams) {
        for (const string& str : group) {
            cout << str << " ";
        }
        cout << endl;
    }

    return 0;
}
