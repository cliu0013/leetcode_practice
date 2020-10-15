class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # very slow DP, but very little space
        if len(s) == 0:
            return 0
        all_length = set()
        all_length.add(1)
        st = s
        while st != "" and len(st) != 1:
            substr = {}
            length = 0
            for i in range(0, len(st)):
                if st[i] not in substr.keys():
                    substr[st[i]] = i
                    length += 1
                else:
                    pos = substr[st[i]]
                    st = st[pos+1:]
                    break
                if i == len(st) -1:
                    st = ""
                
            all_length.add(length)
        return max(all_length)
            