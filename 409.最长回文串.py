#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        result  = 0
        odd = False
        for v in c.values():
            d,m = divmod(v,2)
            result +=d
            if m:
                odd=True

        return result * 2  + odd                
# @lc code=end

