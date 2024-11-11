#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> intersection(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::unordered_map<int, bool> hashMap;
        std::vector<int> result;

        // Insert elements of arr1 into the hash map
        for (int num : arr1) {
            hashMap[num] = true;
        }

        // Iterate over arr2 and check if each element is in the hash map
        for (int num : arr2) {
            if (hashMap.find(num) != hashMap.end()) {
                result.push_back(num);
                hashMap.erase(num); // Remove element from the hash map after adding to result
            }
        }

        return result;
    }
};
