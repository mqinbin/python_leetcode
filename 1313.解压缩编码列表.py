#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0,len(nums),2):
            for _ in range(nums[i]):
                answer.append(nums[i+1])

        return answer
# @lc code=end

