#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c1 =Counter(s)
        c2 =Counter(t)
        return c1==c2
# @lc code=end

