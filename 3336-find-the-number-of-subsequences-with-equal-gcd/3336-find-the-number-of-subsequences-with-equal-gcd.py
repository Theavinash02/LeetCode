import math
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        memo = {} # This will store our previously calculated states
        
        def dp(index, gcd1, gcd2):
            # 1. BASE CASE: We have processed every number in the array
            if index == len(nums):
                # Check if GCDs match AND they are not empty (0)
                if gcd1 == gcd2 and gcd1 > 0:
                    return 1
                return 0
            
            # 2. MEMOIZATION: If we've seen this exact scenario before, return the saved answer
            if (index, gcd1, gcd2) in memo:
                return memo[(index, gcd1, gcd2)]
            
            # 3. THE CHOICES
            # Choice A: Skip the current number entirely
            ways = dp(index + 1, gcd1, gcd2)
            
            # Choice B: Put the current number in Sequence 1
            new_gcd1 = nums[index] if gcd1 == 0 else math.gcd(gcd1, nums[index])
            ways = (ways + dp(index + 1, new_gcd1, gcd2)) % MOD
            
            # Choice C: Put the current number in Sequence 2
            new_gcd2 = nums[index] if gcd2 == 0 else math.gcd(gcd2, nums[index])
            ways = (ways + dp(index + 1, gcd1, new_gcd2)) % MOD
            
            # 4. SAVE AND RETURN
            memo[(index, gcd1, gcd2)] = ways
            return ways
            
        # Start the process at index 0, with both sequences completely empty (GCD = 0)
        return dp(0, 0, 0)

            