class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lis = []
        for i in tokens:
            if i not in ("+", "-", "*", "/"): 
                lis.append(int(i))
            elif i == "+":
                f= lis.pop()
                s = lis.pop()
                result = s + f
                lis.append(result)
            elif i == "-":
                f= lis.pop()
                s = lis.pop()
                result = s - f
                lis.append(result)
            elif i == "*":
                f= lis.pop()
                s = lis.pop()
                result = s * f
                lis.append(result)
            elif i == "/":
                f= lis.pop()
                s = lis.pop()
                result = int(s / f)
                lis.append(result)
        return lis[0]