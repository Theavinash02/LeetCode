class Solution:
    def maxScore(self, s: str) -> int:
        m_s = 0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            sum = left.count('0')+ right.count('1')
            m_s = max(m_s,sum)
        return m_s