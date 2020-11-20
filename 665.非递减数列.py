#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0

        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                c +=1
            
                if i > 0 :
                    if nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i-1]
                    else :
                        nums[i+1] = nums[i]
            if c > 1:
                return False
        
        return True
                    

# @lc code=end

