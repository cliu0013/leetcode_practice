# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None
        res = TreeNode(val = preorder[0])
        def recur(cur_node, pre, ino):
            pos = ino.index(cur_node.val)
            l = pos
            r = len(pre) - l - 1
            if pos:
                cur_node.left = TreeNode(pre[1])
                recur(cur_node.left, pre[1: l + 1], ino[: l])
            if pos != len(pre) - 1:
                cur_node.right = TreeNode(pre[l + 1])
                recur(cur_node.right, pre[l + 1:], ino[l + 1: ])
        recur(res, preorder, inorder)
        return res