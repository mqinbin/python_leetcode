#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for e in arr:
            if e%2:
                odd_count +=1
                if odd_count ==3:
                    return True
            else:
                odd_count =0
        
        return False
            
# @lc code=end

