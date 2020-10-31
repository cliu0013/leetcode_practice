class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        # num = str(num)
        # for i in range(len(num)):
        #     if num[i] == "6":
        #         return num[:i] + "9" + num[i+1:]
        # return num
        origin = num
        pos = -1
        i = 0
        while num != 0:
            if num % 10 == 6:
                pos = i
            i += 1
            num = num//10
        if pos == -1: return origin
        else: return origin + 10**pos * 3
    
        