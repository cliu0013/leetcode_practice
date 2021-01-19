class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # expand from center
        n = len(s)
        max_len = 0
        max_str = ""
        for i in range(0, 2*n-1):
            # two pointers, one for the center, the other for the increment
            
            stop = False
            if i % 2 == 0:
                k = 1
                c = i//2
                print("c is: " + str(c))
                while (c-k >= 0 and c+k <= n-1) and not stop:
                    print(s[c-k] )
                    print(s[c+k] )
                    if s[c-k] == s[c+k]:
                        k += 1
                    else: 
                        stop = True
                        
                st =s[c-k:c+k+1]      
                k = 2*k -1
                print(len(st) == k)
            else:
                k = 0
                c = (i-1)//2
                while (c- k >= 0 and c+1+k <= n-1) and not stop:
                    if s[c+1+k] == s[c-k]:
                        k += 1
                    else: 
                        stop = True
                st =s[c-k:c+k+2]  
                k = 2*k
            if k > max_len:
                max_len = k
                max_str = st

        return max_str
            
        
        
        
        
        
#         # DP solution
#         n = len(s)
#         table = {}
#         for i in range(1, n+1):
#             for j in range(0, n-i+1):
#                 table[s[j:j+i]] = self.isPalindrome(s[j:j+i], table) 
                
#         longest = ""
#         for key in table.keys():
#             if table[key] == True and len(key) >len(longest):
#                 longest = key
        
#         return longest
        
    
#     def isPalindrome(self, st, table):
#         if len(st) == 1:
#             return True
#         elif len(st) == 2 or table[st[1:-1]] == True:
#             return st[0] == st[-1]
#         else: 
#             return False

    
            