class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i)-1
            if nums[index] <0:
                duplicate = abs(i)
            else:
                nums[index] = -nums[index]
        for i in range (0,len(nums)):
            if nums[i]>0:
                missing = i + 1
        return [duplicate,missing]