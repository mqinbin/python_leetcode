#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        letter_stack = [x for x in s if x.isalpha()]
        num_stack = [x for x in s if x.isdigit()]
        letters = len(letter_stack)
        nums = len(num_stack)
        if abs(letters -nums) > 1:
            return ""
        help = []
        if letters > nums:
            help.append(letter_stack)
            help.append(num_stack)
        else:
            help.append(num_stack)
            help.append(letter_stack)

        answer = []
        for i in range(len(s)):
            answer.append(help[i%2][i//2])
        return "".join(answer)
# @lc code=end

