# Parsing the input
def getWord(st):
    """
    Get input and its length
    @params String st: input of a word
    @return String word, int length_word: word is the input String, length_word is the length of the word
    """
    # O(1) as we know the input st is not infinitely long
    word = st
    length_word = len(word)
    return word, length_word

x, m = getWord(input())
y, n = getWord(input())

A = [[0] * (n + 1) for _ in range(m + 1)]
P = [[""] * (n + 1) for _ in range(m + 1)]

def penalty():
    for i in range(m + 1): A[i][0] = i
    for j in range(n + 1): A[0][j] = j
    
    def alpha(i, j):
        if x[i - 1] == y[j - 1]: return 0
        else: return 1    
        
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            match = alpha(i, j) + A[i - 1][j - 1]
            gap_x = 1 + A[i][j - 1]
            gap_y = 1 + A[i - 1][j]
            
            A[i][j] = min(match, gap_x, gap_y)
            if A[i][j] == gap_x:
                P[i][j] = "x"
            elif A[i][j] == gap_y:
                P[i][j] = "y"
            elif A[i][j] == match:
                P[i][j] = "m"
    
    return A[m][n]

line1 = penalty()



def alignment():
    i, j = m, n
    res_x = res_y = ""
    while i != 0 and j != 0:
        if P[i][j] == "m":
            res_x = x[i - 1] + res_x
            res_y = y[j - 1] + res_y
            i -= 1
            j -= 1
        elif P[i][j] == "x":
            res_x = " " + res_x
            res_y = y[j - 1] + res_y
            j -= 1
        else:
            res_x = x[i - 1] + res_x
            res_y = " " + res_y
            i -= 1
    if i == 0 and j == 0:
        return res_x, res_y
    elif i == 0:
        return " " * j + res_x, y[0:j] + res_y
    else:
        return x[0:i] + res_x, " " * i + res_y    
    

res_x, res_y = alignment()
print(line1)
print(res_x)
print(res_y)