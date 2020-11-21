#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        c1 = Counter(arr)
        c2 = {v:k for k,v in c1.items()}
        return len(c1) == len(c2)
# @lc code=end

