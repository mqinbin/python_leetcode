#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        target_sum = total // 3
        found = 0
        part_sum = 0
        for j in range(len(A)):
            part_sum += A[j]
            if part_sum == target_sum:
                part_sum = 0
                found += 1
        return part_sum == 0 and found > 2
# @lc code=end

