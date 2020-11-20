#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_num = nums[0]
        vote = 0
        for num in nums:
            if cur_num == num:
                vote +=1
            else:
                vote -=1
            if vote == 0:
                cur_num = num
                vote = 1
            print(cur_num,vote)
        return cur_num

# @lc code=end

