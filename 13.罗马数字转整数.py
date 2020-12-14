#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        helper = [("CM",900),("CD",400),("XC",90),("XL",40),("IV",4),
        ("IX",9),("M",1000),("D",500),("C",100),("L",50),
        ("X",10),("V",5),("I",1)]
        offset = 0
        while offset < len(s):
            for p in helper:
                if s[offset:].startswith(p[0]):
                    answer += p[1]
                    offset += len(p[0])
                    break
        return answer
# @lc code=end

