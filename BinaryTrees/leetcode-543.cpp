struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


#include <bits/algorithmfwd.h>

class Solution {
public:
    int diameter = 0;
    
    // Height is defined as the number of edges from the node to its deepest leaf
    int height(TreeNode* node) {
        if (node == nullptr) {
            return 0; // Base case: no edges in an empty tree
        }
        
        // Recursively find the height of left and right subtrees
        int left_height = height(node->left);
        int right_height = height(node->right);
        
        // Update the diameter if the path through this node is longer
        diameter = std::max(diameter, left_height + right_height);
        
        // Height of the current node is 1 more than the maximum of its children's heights
        return 1 + std::max(left_height, right_height);
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return diameter; // Diameter is the maximum number of edges found
    }
};
