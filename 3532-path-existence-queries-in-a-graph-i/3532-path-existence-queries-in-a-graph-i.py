class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans = [0]*n
        id=0

        for i in range(1,n):
            if abs(nums[i]-nums[i-1]) > maxDiff:
                id+=1
            ans[i] = id
        answer = []
        for i,j in queries:
            answer.append(ans[i]==ans[j])
        return answer