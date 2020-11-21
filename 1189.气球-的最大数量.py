#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        c_count = Counter("balloon")
        t_count = Counter(text)

        return min([t_count[k] // c_count[k]  for k in c_count])

            
        
# @lc code=end

