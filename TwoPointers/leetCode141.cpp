/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <cstddef>
using namespace std;

class Solution {
private:
    ListNode* nextNode; // Global tracker
public:
    bool hasCycle(ListNode* head) {
        if (!head || !head->next) {
            // If the list is empty or has only one node, end the algorithm
            return false;
        }

        // Initialize left and right pointers
        ListNode* left = head;
        ListNode* right = head->next;

        // Initialize the global tracker to the initial position of the right pointer
        nextNode = right;

        while (left != NULL) { // Algorithm ends when left pointer is pointing to a NULL node
            while (right != NULL) { // Keep moving right pointer by hitting next
                if (right == left) {
                    // If the location of right pointer is the same as left pointer, return true
                    return true;
                }
                right = right->next; // Move right pointer to the next node

                if (right == NULL) {
                    // If the next position of the current node is NULL, it's the end of the linked list
                    break;
                }
            }

            // Move the right pointer back to the global tracker's location
            right = nextNode;

            if (right != NULL) {
                // Move the right pointer one more node
                right = right->next;
                // Update the global tracker position
                nextNode = right;
            }

            // Move the left pointer to the next node
            left = left->next;
        }

        // If no matching location is found, return false
        return false;
    }
};

// Optimal solution requires specialized knowledge so I will not implement it. My code works but not upto the time limit that Leetcode wants it to be. But I did hit O(1) space complexity tho.

