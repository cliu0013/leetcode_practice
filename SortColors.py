class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if n == 1:
            return nums

        right_zero = 0
        left_two = -1
        cur = 0
        
        while cur <= n + left_two:
            if nums[cur] == 0:
                temp = nums[right_zero]
                nums[right_zero] = 0
                nums[cur] = temp
                cur += 1
                right_zero += 1
            elif nums[cur] == 1:
                cur += 1
            elif nums[cur] == 2:
                temp = nums[left_two]
                nums[left_two] = 2
                nums[cur] = temp
                left_two -= 1
            