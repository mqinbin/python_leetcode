#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) >= ord(letters[-1]):
            return letters[0]
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        
# @lc code=end

