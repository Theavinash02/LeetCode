class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        out = []
        for i in range(0,len(nums)):
            summ = summ + nums[i]
            out.append(summ)
        return out
