        if sum(nums) == 0:
            return "0"
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x,y:int(y+x) - int(x+y))
        return "".join(nums)