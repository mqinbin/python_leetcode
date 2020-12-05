#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        miss_count = 0
        for num in range(1, 2**31):
            if i < len(arr) and num == arr[i]:
                i += 1
            else:
                miss_count += 1
            if miss_count == k:
                return num
            
# @lc code=end

