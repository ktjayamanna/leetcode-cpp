#include <vector>
using namespace std;

class Solution {
public:

int findMin(vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;

    // Edge case: the array is not rotated.
    if (nums[left] <= nums[right]) {
        return nums[left];
    }

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Check if mid is the pivot point
        if (mid < right && nums[mid] > nums[mid + 1]) {
            return nums[mid + 1];
        }
        if (mid > left && nums[mid - 1] > nums[mid]) {
            return nums[mid];
        }

        // Decide which side to go
        if (nums[mid] > nums[right]) {
            // Minimum is in the right half
            left = mid + 1;
        } else {
            // Minimum is in the left half
            right = mid - 1;
        }
    }

    // After exiting the loop, left should point to the minimum element
    return nums[left];
}

};
