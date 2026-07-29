class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Frequency count using fixed-size array
        freq = [0] * 26
        for char in s:
            freq[ord(char) - 97] += 1
            
        half = [0] * 26
        half_len = 0
        mid_char = ""
        
        for i in range(26):
            half[i] = freq[i] // 2
            half_len += half[i]
            if freq[i] % 2 == 1:
                mid_char = chr(97 + i)

        LIMIT = 10**6 + 1  # Cap values to fit within required k limit

        def get_total_ways(cnt: list[int], total: int) -> int:
            """Calculates distinct permutations capped at LIMIT."""
            res = 1
            rem = total
            for c in cnt:
                if c > 0:
                    # Compute combinations incrementally
                    for j in range(1, c + 1):
                        res = res * (rem - c + j) // j
                        if res >= LIMIT:
                            return LIMIT
                    rem -= c
            return res

        # Check total possible palindromes
        total_ways = get_total_ways(half, half_len)
        if total_ways < k:
            return ""

        left_half = []
        rem_len = half_len

        # Step 2: Build the left half position by position
        for _ in range(half_len):
            for ch in range(26):
                if half[ch] == 0:
                    continue
                
                # If total ways is capped at LIMIT, recompute ways for this branch directly
                if total_ways >= LIMIT:
                    half[ch] -= 1
                    ways = get_total_ways(half, rem_len - 1)
                    half[ch] += 1
                else:
                    # O(1) transition formula: ways = total_ways * count / rem_len
                    ways = (total_ways * half[ch]) // rem_len

                if ways >= k:
                    left_half.append(chr(97 + ch))
                    half[ch] -= 1
                    total_ways = ways
                    rem_len -= 1
                    break
                else:
                    k -= ways

        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]