from math import log
from math import exp
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=exp(n*log(abs(x)))
        if(x<0 and n&1==1):
            return -ans
        else:
            return ans