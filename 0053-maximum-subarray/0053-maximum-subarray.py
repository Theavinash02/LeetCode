class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        ma = float(-inf)
        for i in range(0,len(nums)):
            cur = max(cur+nums[i],nums[i])
            ma = max(cur,ma)

        return ma

            
            