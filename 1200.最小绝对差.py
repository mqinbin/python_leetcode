#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        target_diff = float('inf')
        for i in range(1, len(arr)):
            target_diff = min(target_diff, arr[i] - arr[i-1])
        answer  = []       
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == target_diff:
                answer.append([arr[i-1] , arr[i]])
        return answer
# @lc code=end

