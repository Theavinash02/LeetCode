class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num= {}
        for i,n in enumerate(nums):
            fake = target - n

            if fake in num:
                return(num[fake],i)
            
            num[n] = i
        


        