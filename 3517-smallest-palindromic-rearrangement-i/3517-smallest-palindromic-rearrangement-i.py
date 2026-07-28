class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)<=2:
            return s
        mid = len(s)//2
        if len(s)>2:
            if len(s)%2==0:
                return "".join(sorted(s[:mid]))+"".join(sorted(s[mid:],reverse=True))
            else:
                return "".join(sorted(s[:mid]))+s[mid]+"".join(sorted(s[mid+1:],reverse=True))
