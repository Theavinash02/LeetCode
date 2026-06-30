class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains = {}
        for i,n in enumerate(nums):
            if n in contains:
                return True
            else:
                contains[i] = n
        return False
        