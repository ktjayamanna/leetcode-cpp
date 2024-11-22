#include <vector>
class Solution {
public:
    int binarySearch(vector<int>& nums, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;
    }

    int findPivot(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        if (nums[left] <= nums[right])
            return 0; // Array is not rotated
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int next = (mid + 1) % nums.size();
            int prev = (mid - 1 + nums.size()) % nums.size();
            if (nums[mid] <= nums[next] && nums[mid] <= nums[prev])
                return mid; // Pivot found (Pivot is the smallest element in this implementation)
            else if (nums[mid] <= nums[right])
                right = mid - 1;
            else if (nums[mid] >= nums[left])
                left = mid + 1;
        }
        return 0;
    }

    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0)
            return -1;
        int pivot = findPivot(nums);
        if (nums[pivot] == target)
            return pivot;
        int result = -1;
        if (pivot == 0) {
            // The array is not rotated
            result = binarySearch(nums, 0, n - 1, target);
        } else if (target >= nums[0]) {
            // Target is in the left subarray
            result = binarySearch(nums, 0, pivot - 1, target);
        } else {
            // Target is in the right subarray
            result = binarySearch(nums, pivot, n - 1, target);
        }
        return result;
    }
};
