class Solution:
    def isValid(self, s: str) -> bool:
        lis=[]
        for i in s:
            if i == "(" or i == "{" or i == "[":
                lis.append(i)
            else:
                if lis == [] :
                    return False
                elif (i ==")" and lis[-1]=="(") or (i =="]" and lis[-1]=="[") or (i =="}" and lis[-1]=="{") :
                    lis.pop(-1)
                else: 
                    return False
        return lis ==[]