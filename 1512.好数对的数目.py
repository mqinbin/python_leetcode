#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        answer = 0
        for v in counter.values():
            answer +=  v * (v-1) // 2
        return answer
# @lc code=end

