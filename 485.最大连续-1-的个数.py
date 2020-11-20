#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cur = 0
        is_one =False
        for num in nums:
            if num == 1:
                if is_one:
                    cur +=1
                else:
                    cur = 1
                is_one = True
            else:
                is_one = False
            
            result = max(result,cur) 
        return result

# @lc code=end

