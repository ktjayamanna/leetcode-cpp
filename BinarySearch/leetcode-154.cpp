#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If the array is already sorted, return the smallest element
            if (nums[left] <= nums[right]) {
                return nums[left];
            }

            // Check if mid is the pivotal point
            if (mid + 1 < nums.size() && nums[mid] > nums[mid + 1]) {
                return nums[mid + 1];
            }
            if (mid - 1 >= 0 && nums[mid - 1] > nums[mid]) {
                return nums[mid];
            }

            // Check if the current subarray is sorted; stop immediately
            if (nums[mid] >= nums[left] && nums[mid] <= nums[right]) {
                return nums[left];
            }

            // Decide which half to search next
            if (nums[mid] >= nums[left]) {
                left = mid + 1; // Pivot is in the right half
            } else {
                right = mid - 1; // Pivot is in the left half
            }
        }

        // This point is never reached if the input satisfies the problem constraints
        return nums[0];
    }
};
