class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i,n in enumerate(nums):
            if n in seen:
                return True
            else:
                seen[n] = i
        return False