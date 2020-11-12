class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def product(arr):
            if len(arr) == 0: return -float('inf')
            if len(arr) == 1: return arr[0]
            rt = 1
            for ele in arr:
                rt *= ele
            return rt
        
        def noNegative(arr, noNeg = False):
            if len(arr) == 0: return -float('inf')
            if len(arr) == 1: return arr[0]
            if not noNeg:
                count = 0
                first = last = -1
                for i, ele in enumerate(arr):
                    if ele < 0:
                        count += 1
                        if first == -1:
                            first = i
                        last = i
                if count % 2 == 0:
                    return product(arr)
                else:
                    return max(noNegative(arr[0: last], True), noNegative(arr[first + 1:], True))    
            else:
                return product(arr)


        res = -float('inf')
        arrays = []
        pointer = 0
        for i, ele in enumerate(nums):
            if ele == 0:
                res = 0
                arrays.append(nums[pointer: i])
                pointer = i + 1
        if pointer != len(nums):
            arrays.append(nums[pointer:])

        
        return max([noNegative(arr, noNeg = False) for arr in arrays] + [res])