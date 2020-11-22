#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        from operator import add ,mul
        return reduce(mul, map(int,str(n))) - reduce(add, map(int,str(n))) 
# @lc code=end

