class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) runtime, O(n) space
        n = len(intervals)
        if n == 0:
            return []
        start_time = [0]* n
        finish_time = {}
        for i in range(0, n):
            start_time[i]= intervals[i][0]
            if start_time[i] in finish_time.keys():
                finish_time[start_time[i]] = max(finish_time[start_time[i]], intervals[i][1])
            else:
                finish_time[start_time[i]]= intervals[i][1]
                
        start_time.sort()
        res = []
        cur_interval = start_time[0]
        for i in range(1, n):
            if finish_time[cur_interval] >= start_time[i]:
                finish_time[cur_interval] = max(finish_time[cur_interval], finish_time[start_time[i]])
            else:
                res.append([cur_interval, finish_time[cur_interval]])
                cur_interval = start_time[i]
        res.append([cur_interval, finish_time[cur_interval]])
        return res