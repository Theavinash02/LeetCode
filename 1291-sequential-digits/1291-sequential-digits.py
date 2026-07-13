# Breath first search method
from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque(range(1,10))
        res = []

        while queue:
            num = queue.popleft()
            if low<= num <=high:
                res.append(num)
            if num>high:
                continue
            last_digit = num%10
            if last_digit<9:
                next_num = (num*10) + last_digit + 1
                queue.append(next_num)
        return res