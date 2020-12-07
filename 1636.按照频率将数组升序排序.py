#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)

        answer = []
        for kv in sorted(counter.items() ,key = lambda kv: (kv[1],-kv[0])) :
            answer.extend([kv[0]] * kv[1])
        return answer
# @lc code=end

