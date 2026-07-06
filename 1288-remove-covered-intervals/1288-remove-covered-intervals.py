class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        max_end = 0
        count = 0
        for s,e in intervals:
            if e>max_end:
                count+=1
                max_end = e
        return count
                