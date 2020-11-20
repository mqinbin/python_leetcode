#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        head_index = 0
        tear_index = 1
        while head_index < tear_index and tear_index < len(nums):
            if nums[tear_index] - nums[head_index] == k:
                result +=1
                head_index = self.next_diff_index(nums, head_index)
                tear_index = self.next_diff_index(nums, tear_index)
                
            elif nums[tear_index] - nums[head_index] < k:
                tear_index = self.next_diff_index(nums, tear_index)
            elif nums[tear_index] - nums[head_index] > k:
                head_index = self.next_diff_index(nums, head_index)
            if tear_index == head_index:
                    tear_index = head_index +1
                    
        return result

    def next_diff_index(self, nums,cur):
        n = len(nums)
        while cur < n-1:
            if nums[cur] != nums[cur+1]:
                break
            cur  +=1
        return cur +1
# @lc code=end

