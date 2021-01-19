class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        visited = set(beginWord)
        wordSet = set(wordList)

        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in string.ascii_lowercase:
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordSet:
                        queue.append((tmp, dist+1))
                        visited.add(tmp)
        return 0
                    
        
        
        
        

        
        
                    
            
        