#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        helper = path.split('/')
        stack = []
        for part in helper:
            if part == '.' or part == '' :
                pass
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        # print(stack)
        return '/' + '/'.join(stack)
# @lc code=end

