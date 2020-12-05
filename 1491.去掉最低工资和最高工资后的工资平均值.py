#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        count = 0
        total = 0
        min = float('inf')
        max = float('-inf')
        for s in salary:
            total += s
            if s > max:
                max = s
            if s < min:
                min =s
            count += 1
        return (total - min - max) / (count -2)

# @lc code=end

