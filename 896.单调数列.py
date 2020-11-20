#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        help = new_help = 0
        for i in range(1, len(A)):
            new_help += A[i]-A[i-1]
            if abs(new_help) < abs(help) or new_help * help < 0:
                return False
            help = new_help
        return True
# @lc code=end

