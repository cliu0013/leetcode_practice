# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left, right = root.left, root.right
        
        cur = left
        while cur:
            if cur.val >= root.val:
                return False
            cur = cur.right
        
        cur = right
        while cur:
            if cur.val <= root.val:
                return False
            cur = cur.left
        
        return self.isValidBST(left) and self.isValidBST(right)