#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool hasDuplicates(const std::vector<int>& array) {
        std::unordered_set<int> hash_map;  // Using std::unordered_set as a hash map

        // Iterate through each element in the array (Creation of hash map is O(n))
        for (int num : array) {
            // Check if the number already exists in the hash map
            if (hash_map.find(num) != hash_map.end()) {
                return true;  // Duplicate found
            }
            // Insert the number into the hash map
            hash_map.insert(num);
        }
        return false;  // No duplicates found
    }

    bool containsDuplicate(vector<int>& nums) {
        return hasDuplicates(nums); // No elements are equal with other elements
    }
};




int main() {
    Solution solution;
    
    vector<int> nums1 = {1, 2, 3, 4, 5};
    cout << boolalpha << solution.containsDuplicate(nums1) << endl; // Outputs: false

    vector<int> nums2 = {1, 2, 3, 4, 1};
    cout << boolalpha << solution.containsDuplicate(nums2) << endl; // Outputs: true

    return 0;
}
