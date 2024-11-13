#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:


int maxArea(std::vector<int>& heights) {
    int left = 0;
    int right = heights.size() - 1;
    int maxArea = 0;

    while (left < right) {
        // Calculate the xLen as the distance between the two pointers
        int xLen = right - left;
        
        // Calculate yLen as the minimum value of the two pointers
        int yLen = std::min(heights[left], heights[right]);
        
        // Calculate the area
        int area = xLen * yLen;
        
        // Update maxArea if the current area is larger
        if (area > maxArea) {
            maxArea = area;
        }
        
        // Move the pointer that points to the smaller value
        if (heights[left] < heights[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}
};