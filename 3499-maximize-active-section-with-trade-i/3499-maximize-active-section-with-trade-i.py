class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = 0
        max_trade_gain = 0
        prev_zero_len = float('-inf')
        i = 0
        n = len(s)
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            
            length = j - i
            
            if s[i] == '1':
                total_ones += length
            else:  # s[i] == '0'
                max_trade_gain = max(max_trade_gain, prev_zero_len + length)
                prev_zero_len = length
            
            i = j
            
        return total_ones + max_trade_gain