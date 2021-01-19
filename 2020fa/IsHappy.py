class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = {}
        while True:
            res = 0
            length = len(str(n))
            for i in range(0, length):
                digit, n = n % 10, int(n/10)
                res += digit * digit
            if res == 1:
                return True
            elif res in hashmap.keys():
                return False
            else:
                hashmap[res] = True
                n = res

    # def isHappy(self, n: int) -> bool:
    #     def get_next(number):
    #         total_sum = 0
    #         while number > 0:
    #             number, digit = divmod(number, 10)
    #             total_sum += digit ** 2
    #         return total_sum
        
    #     slow_runner = n
    #     fast_runner = get_next(n)
    #     while fast_runner != 1 and fast_runner != slow_runner:
    #         slow_runner = get_next(slow_runner)
    #         fast_runner = get_next(get_next(fast_runner))
    #     return fast_runner == 1
            
            