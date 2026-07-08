from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        k = len(digits)

        # prefix digit sums
        pref_sum = [0] * (k + 1)
        for i in range(k):
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated value
        pref_num = [0] * (k + 1)
        for i in range(k):
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD

        n = len(s)

        # first non-zero index at or after i
        next_idx = [k] * (n + 1)
        p = 0
        for i in range(n):
            while p < k and pos[p] < i:
                p += 1
            next_idx[i] = p

        # last non-zero index at or before i
        prev_idx = [-1] * n
        p = k - 1
        for i in range(n - 1, -1, -1):
            while p >= 0 and pos[p] > i:
                p -= 1
            prev_idx[i] = p

        ans = []

        for l, r in queries:
            left = next_idx[l]
            right = prev_idx[r]

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            num = (
                pref_num[right + 1]
                - pref_num[left] * pow10[length]
            ) % MOD

            digit_sum = pref_sum[right + 1] - pref_sum[left]

            ans.append((num * digit_sum) % MOD)

        return ans