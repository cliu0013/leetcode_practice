class Solution(object):
    def maxChunksToSorted(self, arr):
        res = chunk_max = 0
        for i, x in enumerate(arr):
            chunk_max = max(chunk_max, x)
            if chunk_max == i: res += 1
        return res