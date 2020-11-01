# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # BST is a tree, all left substree's nodes smaller than the root, and all right subtree's nodes larger than the root
        # O(h), O(1)
        res, cur = None, root
        while cur:
            if cur.val > p.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res