class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        lis1 = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            lis1.append(count)
            count = 0
        return lis1