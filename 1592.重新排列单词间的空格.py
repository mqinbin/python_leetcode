#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.strip().split()
        space_count = len(text) - sum(map(len,words))
        if len(words)==1:
            return words[0] + " " * space_count
        split_space_count =  (space_count // (len(words) -1))
        return (" " * split_space_count).join(words) + (" " * (space_count %   (len(words) -1)))
# @lc code=end

