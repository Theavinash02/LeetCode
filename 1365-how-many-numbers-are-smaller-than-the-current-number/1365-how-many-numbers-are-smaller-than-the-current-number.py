class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)
        dic = {}
        lis1=[]
        for i,va in enumerate(num):
            if va not in dic:
                dic[va] = i
        for i in nums:
            lis1.append(dic[i])
        return lis1
        