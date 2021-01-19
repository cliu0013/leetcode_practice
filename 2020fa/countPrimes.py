class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        sieve = [0, 0] + [-1] * (n - 2)
        k = int(math.sqrt(n)) + 1
        for i in range(2, n):
            if sieve[i] != -1:
                continue
            sieve[i] = 1     
            if i < k:
                j = i
                while (j * i < n):
                    sieve[j * i] = 0
                    j += 1
        return sum(sieve)
    
        # if n <= 1:
        #     return 0
        # isPrime = [0, 0] + [-1] * (n - 2)
        # # k = int(math.sqrt(n))+1
        # for i in range(2, n):
        #     if isPrime[i] != -1:
        #         continue
        #     isPrime[i] = 1
        #     j = i
        #     while j * i < n:
        #         isPrime[j * i] = 0
        #         j += 1      
        # return sum(isPrime)