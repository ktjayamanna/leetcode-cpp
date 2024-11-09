#include <vector>
#include <algorithm>
#include <limits.h>

class Solution {
public:
    int maxProfit(std::vector<int>& arr) {
        if (arr.size() < 2) {
                return 0; // Not enough elements for a valid comparison
            }
            
            int left = 0;            // Left pointer at the start
            int right = 1;           // Right pointer at the second element
            int maxDiff = INT_MIN;   // Initialize maxDiff to the minimum integer value

            while (right < arr.size()) {
                if (arr[left] > arr[right]) {
                    left = right;    // Move the left pointer to right's position if left > right
                } else {
                    int currentDiff = arr[right] - arr[left];
                    maxDiff = std::max(maxDiff, currentDiff); // Update maxDiff if currentDiff is larger
                }
                right++; // Move right pointer to the next element
            }

                return maxDiff == INT_MIN ? 0 : maxDiff; // Return maxDiff (0 if no valid difference found)
            }
        };

