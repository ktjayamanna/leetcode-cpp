class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def dfs(root):
    if not root:
        return []
    
    left = dfs(root.left)
    right = dfs(root.right)
    return [root.value] + left + right
    
# Test cases
def test_dfs():
    # Test case 1: Empty tree
    assert dfs(None) == [], "Test case 1 failed"

    # Test case 2: Single node tree
    root = TreeNode(1)
    assert dfs(root) == [1], "Test case 2 failed"

    # Test case 3: Tree with multiple levels
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert dfs(root) == [1, 2, 4, 5, 3, 6, 7], "Test case 3 failed"

    # Test case 4: Left-skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert dfs(root) == [1, 2, 3, 4], "Test case 4 failed"

    # Test case 5: Right-skewed tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert dfs(root) == [1, 2, 3, 4], "Test case 5 failed"

    print("All test cases passed!")


# Run the tests
test_dfs()
