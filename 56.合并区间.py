#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda l: l[0])

        answer = []
        for interval in intervals:
            if not answer:
                answer.append(interval)
                continue
            last_interval = answer[-1]
            if interval[0] <= last_interval[1]:
                answer.pop()
                answer.append([last_interval[0] ,max(last_interval[1], interval[1])])
            else:
                answer.append(interval)
        return answer


# @lc code=end

