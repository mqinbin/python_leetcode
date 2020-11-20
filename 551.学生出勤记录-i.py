#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        last_char = None
        a_count = 0
        for i in range(len(s)):
            char = s[i]
            if char == "A":
                if a_count == 1:
                    return False
                a_count +=1
            elif char == "L":
                if i >= 2 and s[i-2:i] == "LL":
                    return False
                
            last_char = char
        return True
# @lc code=end

