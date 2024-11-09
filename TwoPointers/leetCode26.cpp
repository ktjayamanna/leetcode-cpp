#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Check for empty input
        if (nums.empty()) return 0;
        
        // Initialize two pointers
        int left = 0;
        int right = 1;
        
        // Traverse the array using the pointers
        while (right < nums.size()) {
            // If values at left and right pointers are different, move left to the next unique position
            if (nums[left] != nums[right]) {
                left++;
                nums[left] = nums[right];
            }
            // Move the right pointer
            right++;
        }
        
        // The length of the array with unique adjacent values is left + 1
        return left + 1;
    }
};
