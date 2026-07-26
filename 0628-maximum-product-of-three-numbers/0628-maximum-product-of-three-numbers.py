class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ma1=float('-inf')
        '''
        brute force approach n**3
        for i in range(len(nums)-2):
            j=i+1
            k = j+1
            while j<=len(nums)-2:
                ml1=nums[i]*nums[j]
                while k<=len(nums)-1:
                    ml2= ml1*nums[k]
                    ma1= max(ml2,ma1)
                    k+=1
                j+=1
                k=j+1
        return ma1
        '''
        num = sorted(nums)
        for i in range(len(num)-2):
            ml1 = num[i]*num[i+1]*num[-1]
            ml2 = num[i]*num[i+1]*num[i+2]
            ma1=max(ma1,ml1,ml2)
        return ma1
                                


        