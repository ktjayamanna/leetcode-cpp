def dfs(root):
    if not root:
        []
    left = dfs(root.left)
    right = dfs(root.right)
    return [root.val] + left + right



from collections import deque

def bfs(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            result.append(current.left)
        if current.right:
            result.append(current.right)
    return result

    