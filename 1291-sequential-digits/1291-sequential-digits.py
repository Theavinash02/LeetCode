class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        ans =[]

        lows = len(str(low))
        highs = len(str(high))

        for length in range(lows,highs+1):
            for start in range(9+1-length):
                arr = int(sample[start:start+length])
                if low <= arr <= high:
                    ans.append(arr)
        return ans