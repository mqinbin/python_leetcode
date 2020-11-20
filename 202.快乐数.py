#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        
        while n!=1:
            n = sum([ int(i) ** 2 for i in str(n)])
            if n in cache:
                return False
            else:
                cache.add(n)
        else:
            return True
# @lc code=end

