class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hashtable increases space complexity but lower the runtime complexity O(n), O(n)
        tb = {}
        for i in range(0, len(nums)):
                tb[nums[i]]=i
                
        for i in range(0, len(nums)):
            a = nums[i]
            b = target - a
            if b in tb and tb[b]!=i:
                return([i,tb[b]])
            
        
        return None

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute force O(n^2)
        for i in range(0, len(nums)):
            a = nums[i]
            b = target - a
            for j in range(i+1, len(nums)):
                if nums[j] == b:
                    return[i,j]
        
        return None

class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # One pass! O(n), O(n)
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

        