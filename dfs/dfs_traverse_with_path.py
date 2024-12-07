def all_tree_paths(root):
    def dfs(node, path):
        if not node:
            return []
        path.append(node.val)
        if not node.left and not node.right:
            result = [path[:]]
        else:
            result = dfs(node.left, path) + dfs(node.right, path)
        path.pop()
        return result
    return dfs(root, [])
