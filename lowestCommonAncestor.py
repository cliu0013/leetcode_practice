# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(n, v):
            path = []
            v = v.val
            
            def step(node, val):
                if node.val == val:
                    path.append(node)
                    return True
                left, right = node.left, node.right
                if left and step(left, val):
                    path.append(node)
                    return True
                if right and step(right, val):
                    path.append(node)
                    return True
                return False
            
            _ = step(n, v)
            
            return path
        
        path_p, path_q = dfs(root, p)[::-1], dfs(root, q)[::-1]
        for i, node in enumerate(path_p):
            if i in range(0, len(path_q)) and node.val == path_q[i].val:
                res = node
        return res
        