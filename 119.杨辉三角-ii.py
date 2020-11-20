#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start


class Solution:
    cache = {0:[1]}

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex not in self.cache:
            result = []
            last_result = self.getRow(rowIndex -1)
            result.append(1)
            for i in range(1, rowIndex):
                result.append(last_result[i-1]+last_result[i])
            result.append(1)
            self.cache[rowIndex] = result
        return self.cache[rowIndex]
# @lc code=end

