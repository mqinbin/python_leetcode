#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # from itertools import combinations
        # answer = 0
        # for comb in combinations(time,2):
        #     answer += (sum(comb) % 60 == 0)
        # return answer
        from collections import Counter
        answer = 0
        c = Counter([t % 60 for t in time])
        for k in c:
            if k == 0 or k ==30:
                answer += c[k] * (c[k] - 1) // 2
            elif k < 30 and 60 - k in c:
                answer += c[k] * c[60-k]
        return answer

# @lc code=end

