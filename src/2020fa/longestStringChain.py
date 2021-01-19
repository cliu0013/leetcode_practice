class Solution(object):
    def longestStrChain(self, words: List[str]) -> int:
        levels = collections.defaultdict(list)
        for word in words:
            levels[len(word)].append(word)
            
        res = {w:1 for w in words}
        for size in range(2, 17):
            for w1 in levels[size]:
                for i in range(len(w1)):
                    w0 = w1[:i] + w1[i+1:]
                    if w0 in res:
                        res[w1] = max(res[w1], res[w0] + 1)
            
        return max(res.values())