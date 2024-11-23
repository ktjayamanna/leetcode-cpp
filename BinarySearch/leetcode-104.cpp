class Solution {
public: 
    int maxDepth(TreeNode* root) {
        // Base case: If the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursive calls for left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return 1 + max(leftDepth, rightDepth)
        return 1 + std::max(leftDepth, rightDepth);
    }
};
