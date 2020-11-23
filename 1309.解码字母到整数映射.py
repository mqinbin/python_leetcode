#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        # s = list(s)

        # answer = []
        # while s:
        #     char = s.pop()
        #     if char == "#":
        #         second = s.pop()
        #         first = s.pop()
        #         char = first + second
                
        #     answer.append(char)
        # ord_0 = ord('0')
        # ord_a = ord('a')
        # answer = [ chr(int(n) + ord_a -1) for n in answer]
        # return "".join(answer[::-1])
        import re
        ord_a = ord('a')
        s = re.sub(r'(\d\d)#' , lambda m: chr(int(m.group(1)) +  ord_a - 1),s  )
        s = re.sub(r'(\d)' , lambda m: chr(int(m.group(1)) +  ord_a - 1),s  )

        return s

# @lc code=end

