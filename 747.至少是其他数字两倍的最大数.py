#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return 0
        # large=max(nums)
        # if large>=2*sorted(nums)[-2]:
        #     return nums.index(large)
        # return -1
        cur_max = float('-inf')
        sec_max = float('-inf')
        twice = False
        index = -1
        for i, num in enumerate(nums):
            
            if num > cur_max:
                twice = num >=  cur_max* 2
                index = i 
                sec_max = cur_max
                cur_max = num
            elif num > sec_max:
                twice = cur_max >= num*2
                sec_max = num
        if twice:
            return index
        else:
            return  -1
        
# @lc code=end

