#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()

        while len(A)>=3:
            if A[-1] >= A[-2]+A[-3]:
                A.pop()
            else:
                return A[-1]+A[-2]+A[-3]
        return 0
# @lc code=end

