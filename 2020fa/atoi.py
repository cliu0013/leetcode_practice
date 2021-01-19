class Solution:
    def myAtoi(self, str: str) -> int:
        intval=0
        try:
            intval=int(str)
        except:
            str=str.strip()
            nums=0
            coms=0
            for index,ele in enumerate(str):
                if (ele=='-' or ele=='+') and coms==0: nums+=1
                elif ele not in ('0','1','2','3','4','5','6','7','8','9') or nums>1:
                    try:
                        intval = int(str[:index])
                        break
                    except:
                        intval = 0
                        break
                else:
                    coms+=1
        if intval<=-2**31: return -2**31
        elif intval>=2**31-1: return 2**31-1
        else: return intval