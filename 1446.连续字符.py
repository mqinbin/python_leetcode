#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        power = 1
        last_char = None
        cur_count = 1
        for char in s:
            if char == last_char:
                cur_count += 1
                power = max(power,cur_count)
            else:
                last_char = char
                cur_count = 1
        return power
# @lc code=end

