class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        ma = float(-inf)
        for i in nums:
            cur = max(cur+i,i)
            ma = max(cur,ma)

        return ma

            
            