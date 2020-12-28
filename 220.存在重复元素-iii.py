#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        length = len(nums) 
        for i in range(0,length-1):
            for offset in range(1,k+1):
                if i+offset < length and abs(nums[i] - nums[i+offset] ) <= t :
                    return True

        return False
# @lc code=end

