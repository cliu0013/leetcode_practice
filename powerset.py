class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def recur(arr):
            if len(arr) == 0: return
            if len(self.res) == 0:
                self.res += [[], [arr[0]]]
            else:
                incre = []
                for s in self.res:
                    incre.append(s + [arr[0]])
                self.res += incre
            arr = arr[1:]
            recur(arr)
        recur(nums)
        return self.res
        