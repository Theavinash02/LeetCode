class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        co = {}
        if len(s) != len(t):
            return False
        for i in s:
            co[i] = co.get(i,0) + 1
        for j in t:
            if j not in co:
                return False
            co[j] -=1

            if co[j] < 0:
                return False
        return True