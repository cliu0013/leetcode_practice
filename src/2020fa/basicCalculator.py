class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0
        s += "+"
        
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c in "-+*/":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    pop = stack.pop()
                    stack.append(pop*num)
                elif sign == "/":
                    pop = stack.pop()
                    stack.append(math.trunc(pop/num))
                sign = c
                num = 0
        return sum(stack)