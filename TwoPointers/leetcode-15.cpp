class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int n = nums.size();

        // Step 1: Sort the array in increasing order
        sort(nums.begin(), nums.end());

        // Initialize a set to store unique triplets as strings
        unordered_set<string> tripletSet;

        // Middle pointer starts from index 1 to n - 2
        for (int middle = 1; middle < n - 1; ++middle) {
            int left = 0;
            int right = n - 1;

            while (left < middle && right > middle) {
                // Negate the values at left and right pointers
                int negLeft = -nums[left];
                int negRight = -nums[right];
                int sumNegLR = negLeft + negRight;

                // Compare the sum to the value at the middle pointer
                if (sumNegLR == nums[middle]) {
                    // Create a unique key for the triplet
                    string key = to_string(nums[left]) + "," + to_string(nums[middle]) + "," + to_string(nums[right]);
                    if (tripletSet.find(key) == tripletSet.end()) {
                        tripletSet.insert(key);
                        result.push_back({nums[left], nums[middle], nums[right]});
                    }
                    // Move the middle pointer to the next index
                    break; // As per your description, we move to the next middle
                } else if (sumNegLR < nums[middle]) {
                    // If sum is smaller, move the right pointer to the left
                    --right;
                } else {
                    // If sum is larger, move the left pointer to the right
                    ++left;
                }
            }
        }

        return result;
    }
};
