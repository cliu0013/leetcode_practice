# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # O(N), O(N)
        if not root: return []
        stack = []
        stack.append([root, 0])
        tree = collections.defaultdict(list)
        tree[0] = [root.val]
        while stack:
            cur = stack.pop(0)
            node = cur[0]
            depth = cur[1]
            left, right = node.left, node.right
            if left: 
                stack.append([left, depth + 1])
                tree[depth + 1].append(left.val)
            if right: 
                stack.append([right, depth + 1])
                tree[depth + 1].append(right.val)
        res = [[] for _ in range(depth + 1)]
        for i in range(depth + 1):
            res[i] = tree[i]
            if i % 2 == 1:
                res[i] = res[i][::-1]
        
        return res
        
        