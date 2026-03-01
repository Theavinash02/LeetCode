class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        lis = []
        target_index=0
        for i in range(1,n+1):
            if target_index<len(target) and i ==target[target_index] :
                lis.append("Push")
                target_index+=1
            else:
                lis.append("Push")
                lis.append("Pop")
            if target_index == len(target):
                break
        return lis