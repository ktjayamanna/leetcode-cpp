#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void _preorderTraversal(struct TreeNode *root, int *result, int *current_idx)
{
    if (!root)
    {
        return;
    }
    result[*current_idx] = root->val;
    *current_idx = (*current_idx) + 1;
    _preorderTraversal(root->left, result, current_idx);
    _preorderTraversal(root->right, result, current_idx);
}

int *preorderTraversal(struct TreeNode *root, int *returnSize)
{
    *returnSize = 100;
    int *result = malloc((*returnSize) * sizeof(int));
    int current_idx = 0;

    _preorderTraversal(root, result, &current_idx);
    *returnSize = current_idx;
    result = (int *)realloc(result, *returnSize * sizeof(int));
    return result;
}
