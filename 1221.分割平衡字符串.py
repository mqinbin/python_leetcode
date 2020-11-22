#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        answer = 0
        for char in s:
            if not(stack):
                stack.append(char)
            elif stack[-1] == char:
                stack.append(char)
            else:
                stack.pop()
                if not stack:
                    answer += 1
        return answer

# @lc code=end

