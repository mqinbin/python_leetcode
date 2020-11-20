#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    symbols_pairs = {"}":"{","]":"[",")":"(",}
    symbols = "([{"
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.symbols:
                stack.append(c)
            elif c in self.symbols_pairs:
                if stack and stack.pop() == self.symbols_pairs[c]:
                    continue
                return False
            else :
                continue
        
        return not stack

# @lc code=end

