#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_two = [0,0]
        for num in nums:
            if num > max_two[0]:
                max_two = [num,max_two[0]]
            elif num > max_two[1]:
                max_two[1] = num
        
        return (max_two[0] - 1 )*(max_two[1] - 1 ) 
# @lc code=end

