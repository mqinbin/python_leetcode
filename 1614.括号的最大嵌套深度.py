#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        depth =0
        for char in s:
            if char == "(":
                depth += 1
                answer = max(depth,answer)
            elif char == ")":
                depth -= 1
        return answer
# @lc code=end

