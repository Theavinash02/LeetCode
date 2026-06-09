class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro,pro1 = 0,0
        left = 0
        for right in range(left+1,len(prices)):
            if prices[left] < prices[right]:
                pro1 = prices[right] - prices[left]
            else:
                pro1 = 0
                left = right
            pro = max(pro1,pro)
        return pro
            
            
            