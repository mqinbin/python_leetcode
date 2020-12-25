#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return "".join(sorted(map(str,nums),key=lambda s: (-ord(s[0]),len(s), int(s) )  )) 

# @lc code=end

