#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashTable;  // value -> index

        for (int i = 0; i < nums.size(); i++) {
            int num2 = nums[i];
            int num1 = target - num2;

            // Check if num1 exists in the hash table
            if (hashTable.find(num1) != hashTable.end()) {
                // Return the indices of num1 and num2
                return {hashTable[num1], i};
            }

            // Store num2 in the hash table with its index
            hashTable[num2] = i;
        }

        // If no solution exists, return an empty vector
        return {};
    }
};
