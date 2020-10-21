class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tor = nums[0]
        rab = nums[0]
        while True:
            tor = nums[tor]
            rab = nums[nums[rab]]
            if tor == rab:
                break
        
        tor = nums[0]
        while tor != rab:
            tor = nums[tor]
            rab = nums[rab]
        return tor
            
            
            
        
        
        # n = len(nums)
        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return nums[i]
                