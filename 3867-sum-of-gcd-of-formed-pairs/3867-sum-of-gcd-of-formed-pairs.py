from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        current_max = 0
        pre = []
        for i in nums:
            current_max = max(current_max,i)
            pre.append(gcd(current_max,i))
        pre.sort()
        total_sum = 0
        low = 0
        high = len(pre) - 1
        while low < high:
            total_sum += gcd(pre[low], pre[high])
            low += 1
            high -= 1
            
        return total_sum
