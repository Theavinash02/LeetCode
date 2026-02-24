class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1=[]
        for i in range(0,n):
            nums1.append(nums[i])
            nums1.append(nums[i+n])
        return nums1
            


        