#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        
        pos_1 = m - 1
        pos_2 = n-1
        total = m + n
        moved = 0
        # if m == 0:
        #     nums1[0:total] = nums2

        while pos_1 >=0 and  pos_2 >=0: 
            if nums1[pos_1] > nums2[pos_2]:
                nums1[total - moved - 1] = nums1[pos_1]
                pos_1 -=1
            else :
                nums1[total - moved - 1] = nums2[pos_2]
                pos_2 -=1

            moved +=1

        if pos_1 == -1:
            nums1[0:total-moved] = nums2[0:pos_2+1]    





# @lc code=end

