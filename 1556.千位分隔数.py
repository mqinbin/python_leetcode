#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        n_len = len(n_str)
        dot_count = (n_len - 1)  // 3 
        start = 0
        end = n_len-dot_count*3
        answer = []
        # 1234    4   1    0 1
        while end <= n_len:
            answer.append(n_str[start:end])
            start = end
            end +=3
        return ".".join(answer)
# @lc code=end

