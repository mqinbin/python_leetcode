#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:

    def findDuplicate(self, nums: List[int]) -> int:
        '''快慢指针'''
        slow  = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            print(slow,fast)
            if slow == fast:
                fast = 0
                while True:
                    fast = nums[fast]
                    slow = nums[slow]
                    print('-' ,slow,fast)
                    if fast == slow:
                        return fast
    # def findDuplicate(self, nums: List[int]) -> int:
    #     '''二分法'''
    #     n = len(nums)
    #     left = 1 
    #     right = n
    #     while left < right:
    #         mid = (left + right) // 2
    #         cnt = 0
    #         for num in nums:
    #             if num <= mid:
    #                 cnt += 1
    #         if cnt <= mid:
    #             left = mid + 1
    #         else:
    #             right = mid
        
    #     return left



# @lc code=end

