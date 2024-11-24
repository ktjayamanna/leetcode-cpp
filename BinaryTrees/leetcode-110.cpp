/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <stdlib.h>
class Solution {
public:
    bool is_balanced;

    bool isBalanced(TreeNode* root) {
        is_balanced = true; // Initialize the flag to true
        height(root);
        return is_balanced;
    }

    int height(TreeNode* root) {
        if (!root)
            return -1;
        int left_height = height(root->left);
        int right_height = height(root->right);
        bool gap = abs(left_height - right_height) > 1; // Check if the difference is greater than 0
        if (gap == true)
            is_balanced = false; // Set the flag to false if gap is true
        return 1 + std::max(left_height, right_height); // Return the height of the subtree
    }
};
