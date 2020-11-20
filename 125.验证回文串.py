#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not str:
            return True
        import re
        s = re.sub(r'[\W_]',"",s)
        s = s.lower()
        return s == s[::-1]
# @lc code=end

