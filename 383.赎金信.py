#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)

        return not ( r_counter - m_counter)
# @lc code=end

