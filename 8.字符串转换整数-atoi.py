#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        sign = 1
        sign_found =False
        number_found =False
        for char in s:
            if char == " ":
                if number_found or sign_found:
                    break
                continue
            if char in "-+":
                if number_found or sign_found:
                    break
                if char == "+":
                    sign_found = True
                    sign *= 1
                    continue
                if char == "-":
                    sign_found = True
                    sign *= -1
                    continue
            if char in "0123456789":
                number_found = True
                answer = answer*10 + ord(char)-ord('0')
            else:
                break
        answer =  sign * answer
        if answer > 2**31-1:
            return  2**31-1
        if answer < -2**31:
            return -2**31
        return answer
# @lc code=end

