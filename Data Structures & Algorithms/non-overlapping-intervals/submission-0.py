class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0

        # sort by earliest end time
        intervals.sort(key=lambda entry:entry[1])

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < prev_end:
                removed += 1
            else:
                prev_end = end

        return removed
