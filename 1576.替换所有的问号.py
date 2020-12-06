#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) <= 1:
            if s == "?":
                return "a"
            else:
                return s
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                for char in "abc":
                    if i == 0 and s[i+1] != char :
                        s[i] = char
                        break
                    if i == len(s) -1 and s[i-1] != char:
                        s[i] = char
                        break
                    if i > 0 and i < len(s) -1 and s[i-1]!=char and s[i+1] !=char:
                        s[i] =char
                        break
        return "".join(s)



# @lc code=end

