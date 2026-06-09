class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,0
        best = float('inf')
        curr = 0
        for i in range(0,len(nums)):
            curr += nums[i]
            while curr >= target:
                right = i
                best= min(right - left + 1,best)
                curr -= nums[left]
                left +=1
        return 0 if best == float('inf') else best

