from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        freq = sorted(collections.Counter(word).values(), reverse = True)\

        for i,c in enumerate(freq):
            ans+= c*(i//8 +1 )
        return ans