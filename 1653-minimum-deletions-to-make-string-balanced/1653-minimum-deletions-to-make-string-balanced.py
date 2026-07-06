class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletion = 0
        for i in s:
            if i == 'b':
                b_count +=1
            else:
                deletion= min(deletion+1,b_count)
        return deletion