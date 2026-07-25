class Solution:
    def maxProduct(self, n: int) -> int:
        nu = [int(i) for i in str(n)]
        ma1=0
        for i in range(len(nu)-1):
            j=i+1
            while j<len(nu):
                ma1= max(ma1,nu[i]*nu[j])
                j+=1 
        return ma1

