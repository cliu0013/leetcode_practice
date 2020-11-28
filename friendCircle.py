class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        def step(i):
            visited.add(i)
            for j in range(len(M)):
                if M[i][j] == 1:
                    M[i][j] = 0
                    step(j)
        res = 0
        for i in range(len(M)):
            if i not in visited:
                res += 1
                step(i)
        return res