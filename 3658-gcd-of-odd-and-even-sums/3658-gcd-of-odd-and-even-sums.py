from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd =0
        sumeven =0
        for i in range(0,2*n,2):
                sumeven+=i
        for i in range(1,2*n,2):
                sumodd+=i
        return gcd(sumodd,sumeven)