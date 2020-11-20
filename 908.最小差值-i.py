#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        _min = min(A)
        _max = max(A)

        return max(0, _max - _min - 2 * K)
        
# @lc code=end

