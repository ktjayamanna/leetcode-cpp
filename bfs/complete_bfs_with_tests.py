from collections import deque

class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    values = []
    if not root:
        return values
    queue = deque([root])
    while queue:
        current = queue.popleft()
        values.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return values

   


# Test cases
def test_bfs():
    # Test case 1: Empty tree
    assert bfs(None) == [], "Test case 1 failed"

    # Test case 2: Single node tree
    root = TreeNode(1)
    assert bfs(root) == [1], "Test case 2 failed"

    # Test case 3: Tree with multiple levels
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert bfs(root) == [1, 2, 3, 4, 5, 6, 7], "Test case 3 failed"

    # Test case 4: Left-skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert bfs(root) == [1, 2, 3, 4], "Test case 4 failed"

    # Test case 5: Right-skewed tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert bfs(root) == [1, 2, 3, 4], "Test case 5 failed"

    print("All test cases passed!")

# Run the tests
test_bfs()
