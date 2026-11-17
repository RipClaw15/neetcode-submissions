class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        overlapping = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = overlapping[-1][1]

            if start <= lastEnd:
                overlapping[-1][1] = max(lastEnd,end)
            else:
                overlapping.append([start,end])
        return overlapping