class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        MAX_XOR = 2048
        pair_xors = [False] * MAX_XOR
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                pair_xors[nums[i] ^ nums[j]] = True
        triplet_xors = [False] * MAX_XOR
        for v in range(MAX_XOR):
            if pair_xors[v]:
                for num in nums:
                    triplet_xors[v ^ num] = True

        return sum(triplet_xors)