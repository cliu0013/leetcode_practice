"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        def inner_connect(node, neighbor = None):
            node.next = neighbor
            if node.left:
                inner_connect(node.left, node.right)
                right_neighbor = None
                if neighbor:
                    right_neighbor = neighbor.left
                inner_connect(node.right, right_neighbor)
            else:
                return
        inner_connect(root)
        return root