class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        # Greedy Algorithm O(N), O(1), very smart
        last = {char: idx for idx, char in enumerate(S)}
        anchor = ptr2 = 0
        res = []
        
        for i, char in enumerate(S):
            ptr2 = max(last[char], ptr2)
            if i == ptr2:
                res.append(ptr2 - anchor + 1)
                anchor = i + 1
        return res
        
        
        # Brute Force O(N^2), O(logN)
        # n = len(S)
        # if n == 1: return [1]
        # ptr1, ptr2, mark = 0, 1, 1
        # while ptr2 != n:
        #     if  S[ptr1] == S[ptr2]:
        #         ptr1 += 1
        #         mark = ptr2 + 1
        #     ptr2 += 1
        #     if ptr2 == n and ptr1 < mark - 1:
        #         ptr1 += 1
        #         ptr2 = mark 
        # if n - mark:
        #     return self.partitionLabels(S[0: mark]) + self.partitionLabels(S[mark:])
        # else:
        #     return [n]
        