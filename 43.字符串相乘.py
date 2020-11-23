#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        answer  = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1 ,-1):
            carry = 0
            for j in range(len(num2)-1, -1 ,-1):
                temp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + carry
                carry ,answer[i+j+1]   = divmod(answer[i+j+1] + temp, 10)

            answer[i] += carry
            # print(answer)

        answer = ''.join(map(str,answer))
        answer = answer.lstrip('0')
        return "0" if not answer else answer
# @lc code=end

