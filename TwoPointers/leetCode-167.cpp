#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                // Return one-based indices
                return {left + 1, right + 1};
            } else if (sum > target) {
                // Move the right pointer left
                right--;
            } else {
                // Move the left pointer right
                left++;
            }
        }
        
        // If no solution is found
        return {-1, -1};
    }
};
