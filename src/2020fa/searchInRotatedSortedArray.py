class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binSearch(i, j):
            n = j - i + 1
            if n == 1:
                return -1 if nums[i] != target else i
            mid = i + n//2
            
            if nums[j] >= nums[i]:
                if target < nums[i] or target > nums[j]:
                    return -1
                if nums[mid] > target:
                    return binSearch(i, mid - 1)
                else:
                    return binSearch(mid, j)
            else:
                return max(binSearch(i, mid - 1), binSearch(mid, j))
        
        return binSearch(0, len(nums) - 1)