class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        non_zero_digits = [c for c in s if c != '0']
        
        if not non_zero_digits:
            return 0
            
        x = int("".join(non_zero_digits))
        digit_sum = sum(int(c) for c in non_zero_digits)
        
        return x * digit_sum