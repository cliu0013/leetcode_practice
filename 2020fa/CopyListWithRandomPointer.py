class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = Node(head.val, None, None)
        
        self.visitedHash[head] = node 
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        
        
        return node