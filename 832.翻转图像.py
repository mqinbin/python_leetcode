#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        revese = [1,0]
        return [list(map( lambda v: revese[v]  ,reversed(l))  )   for l in A]
# @lc code=end

