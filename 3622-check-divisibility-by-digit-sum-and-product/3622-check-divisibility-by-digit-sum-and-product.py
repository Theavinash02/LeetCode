class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n1 = str(n)
        tp,ts =1,0
        for i in n1:
            ts += int(i)
            tp *= int(i)
        s = ts+tp
        if n%s == 0:
            return True
        else :
            return False