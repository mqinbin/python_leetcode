#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        helper = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),
                    (90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),
                    (5,"V"),(4,"IV"),(1,"I")
                    ]
        while num:
            for t in helper:
                if num >= t[0]:
                    answer+=t[1]
                    num -= t[0]
                    break
        return answer

# @lc code=end

