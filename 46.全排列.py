#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, answer):
            if not nums:
                answer.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]] ,answer )
        
        answer = []
        dfs(nums,[],answer)
        return answer
# @lc code=end

