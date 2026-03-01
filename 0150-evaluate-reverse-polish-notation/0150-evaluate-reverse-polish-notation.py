class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lis = []
        for i in tokens:
            if i not in ("+", "-", "*", "/"): 
                lis.append(i)
            elif i == "+":
                f= lis.pop()
                s = lis.pop()
                result = int(s) + int(f)
                lis.append(result)
            elif i == "-":
                f= lis.pop()
                s = lis.pop()
                result = int(s) - int(f)
                lis.append(result)
            elif i == "*":
                f= lis.pop()
                s = lis.pop()
                result = int(s) * int(f)
                lis.append(result)
            elif i == "/":
                f= lis.pop()
                s = lis.pop()
                result = int(s) / int(f)
                lis.append(result)
        return int(lis[0])