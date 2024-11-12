class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Step 1: Sort the array in increasing order.
        sort(nums.begin(), nums.end());
        int n = nums.size();
        
        // Step 2: Initialize a set to store unique triplets.
        set<vector<int>> unique_triplets;
        
        // Step 3: Iterate through the array with the middle pointer.
        for (int middle = 0; middle < n; ++middle) {
            int left = 0;
            int right = n - 1;
            
            // Step 4: Use two pointers to find matching triplets.
            while (left < right) {
                // Skip if pointers overlap with the middle pointer.
                if (left == middle) { ++left; continue; }
                if (right == middle) { --right; continue; }
                
                // Negate the values at the left and right pointers and sum them.
                int sum_negated = -nums[left] - nums[right];
                
                // Compare the sum with the value at the middle pointer.
                if (sum_negated == nums[middle]) {
                    // Define an array to hold the sorted triplet.
                    vector<int> triplet(3);
                    
                    // Since nums[left] <= nums[right], we compare nums[middle] with them.
                    if (nums[middle] <= nums[left]) {
                        // Middle is smallest.
                        triplet[0] = nums[middle];
                        triplet[1] = nums[left];
                        triplet[2] = nums[right];
                    } else if (nums[middle] >= nums[right]) {
                        // Middle is largest.
                        triplet[0] = nums[left];
                        triplet[1] = nums[right];
                        triplet[2] = nums[middle];
                    } else {
                        // Middle is between left and right.
                        triplet[0] = nums[left];
                        triplet[1] = nums[middle];
                        triplet[2] = nums[right];
                    }
                    
                    unique_triplets.insert(triplet);
                    
                    // Move the pointers inward since we found a valid triplet.
                    ++left;
                    --right;
                } else if (sum_negated < nums[middle]) {
                    // If sum is smaller, move the right pointer to the left.
                    --right;
                } else {
                    // If sum is larger, move the left pointer to the right.
                    ++left;
                }
            }
        }
        
        // Step 5: Convert the set to a vector of vectors and return.
        return vector<vector<int>>(unique_triplets.begin(), unique_triplets.end());
    }
};
