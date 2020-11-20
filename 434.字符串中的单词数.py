#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        is_blank = True
        for char in s:
            if char == " ":
                is_blank = True
            else:
                if is_blank == True:
                    result+=1
                    is_blank = False
        return result
# @lc code=end

