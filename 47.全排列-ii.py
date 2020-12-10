#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, answer):
            if not nums:
                answer.append(path)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:],path+[nums[i]] ,answer )
        nums.sort()
        answer = []
        dfs(nums,[],answer)
        return answer
# @lc code=end

