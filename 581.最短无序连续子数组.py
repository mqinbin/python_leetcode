#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        i = 0 
        j = len(nums) -1

        while i<=j:
            if nums[i] == nums2[i]:
                i+=1
                continue
            if nums[j] == nums2[j]:
                j-=1  
                continue
            break


        return j-i + 1

# @lc code=end

