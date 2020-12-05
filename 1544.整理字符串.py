#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        def isPair(charA,charB):
            return abs(ord(charA) - ord(charB)) == abs(ord('a')- ord('A'))

        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if isPair(char, stack[-1]):
                stack.pop()
                continue
            else:
                stack.append(char)
        return "".join(stack)

# @lc code=end

