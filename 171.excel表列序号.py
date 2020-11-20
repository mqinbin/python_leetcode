#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        a_ord = ord("A")
        result = 0
        n = len(s)
        for i in range(len(s)):
            result += (ord(s[i]) - a_ord  + 1) * 26 ** (n - i -1) 
        return result
# @lc code=end

