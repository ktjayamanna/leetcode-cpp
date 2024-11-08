#include <vector>
#include <climits>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& arr) {
        int n = arr.size();
        if (n < 2) return 0;  // If array has less than 2 elements, return 0 as there can be no difference.

        int left = 0;
        int right = 1;
        int maxDiff = INT_MIN;

        while (right < n) {
            // Check if the minimum is at the right and maximum is at the left
            if (arr[left] > arr[right]) {
                // Move left pointer to the right to ensure minimum is to the left
                left++;
                continue; // Skip to the next iteration
            }

            // Find min and max within the range defined by the left and right pointers
            int currentMin = INT_MAX;
            int currentMax = INT_MIN;
            
            for (int i = left; i <= right; ++i) {
                currentMin = std::min(currentMin, arr[i]);
                currentMax = std::max(currentMax, arr[i]);
            }
            
            // Calculate current difference
            int currentDiff = currentMax - currentMin;
            
            // Update maxDiff if the current difference is larger
            if (currentDiff > maxDiff) {
                maxDiff = currentDiff;
            }
            
            // Move the right pointer to the right
            right++;
        }

        return maxDiff;
    }
};
