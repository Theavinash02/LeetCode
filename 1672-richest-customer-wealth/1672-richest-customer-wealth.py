class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        cur_sum=0
        lis=[]
        for i in accounts:
            for j in i:
                cur_sum += j
                lis.append(cur_sum)
            cur_sum = 0
        return max(lis)