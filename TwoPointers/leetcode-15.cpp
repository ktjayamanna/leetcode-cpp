#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        unordered_set<string> uniqueTriplets;

        // Step 1: Sort the array
        sort(nums.begin(), nums.end());

        int left = 0;
        int right = nums.size() - 1;

        while (left < right - 1) {  // Ensure at least one index remains for 'middle'
            int mid = left + 1;  // Start the middle pointer at index left + 1

            while (mid < right) {
                // Negate the values of left and right pointers and compare their sum to mid's value
                int sum = -nums[left] - nums[right];

                if (sum == nums[mid]) {
                    // Create a unique key and check if this triplet is already added
                    string key = to_string(nums[left]) + "," + to_string(nums[mid]) + "," + to_string(nums[right]);
                    if (uniqueTriplets.find(key) == uniqueTriplets.end()) {
                        // Add the triplet to the result
                        result.push_back({nums[left], nums[mid], nums[right]});
                        uniqueTriplets.insert(key);
                    }
                    mid++;  // Move the middle pointer to the next position
                } else if (sum < nums[mid]) {
                    right--;  // Move the right pointer to the left
                } else {
                    left++;   // Move the left pointer to the right
                }
            }

            // Reset pointers after middle pointer reaches the end of the array
            right = nums.size() - 1;
            left++;
        }

        return result;
    }
};