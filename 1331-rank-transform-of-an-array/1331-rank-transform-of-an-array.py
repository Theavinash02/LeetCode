class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        ans=[]
        rank1= 0
        for i in sorted(arr):
            if i not in rank:
                rank1+=1
                rank[i] = rank1
        for i in arr:
            ans.append(rank[i])
        return ans
        

        