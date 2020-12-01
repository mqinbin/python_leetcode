#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        sorted_key = list(sorted(c.keys()))

        answer = []
        char_counts = len(s)
        while char_counts:
            for i in range(len(sorted_key)):
                if c[sorted_key[i]] > 0:
                    answer.append(sorted_key[i])
                    c[sorted_key[i]] -= 1
                    char_counts -= 1
            for i in range(len(sorted_key)-1,-1,-1):
                if c[sorted_key[i]] > 0:
                    answer.append(sorted_key[i])
                    c[sorted_key[i]] -= 1
                    char_counts -= 1

        return "".join(answer)
# @lc code=end

