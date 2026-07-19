class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {c:i for i,c in enumerate(s)}
        visted = set()
        stack = []

        for i,c in enumerate(s):
            if c in visted:
                continue
            while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                rem = stack.pop()
                visted.remove(rem)
            
            stack.append(c)
            visted.add(c)
        return "".join(stack)