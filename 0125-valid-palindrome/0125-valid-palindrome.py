class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(i.lower() for i in s if i.isalnum())
        print(res)
        l,r= 0,len(res)-1
        while l<r:
            if res[l] == res[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            
        
        