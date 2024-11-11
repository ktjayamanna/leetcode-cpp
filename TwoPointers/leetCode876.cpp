/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if (!head) return nullptr;

        ListNode* left_ptr = head;
        ListNode* right_ptr = head;
        int distance = 0;

        // Move right_ptr to the end of the list and calculate the distance
        while (right_ptr != nullptr) {
            right_ptr = right_ptr->next;
            distance++;
        }

        // Calculate half of the distance
        distance = distance / 2;

        // Move left_ptr distance steps
        for (int i = 0; i < distance; i++) {
            left_ptr = left_ptr->next;
        }

        return left_ptr;
    }
};
