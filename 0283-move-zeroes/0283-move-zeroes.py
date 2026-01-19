class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        k = 0
        for x in nums:
            if x != 0:
                nums[k] = x
                k += 1
        while k < len(nums):
            nums[k] = 0
            k += 1