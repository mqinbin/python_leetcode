#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        from itertools import chain
        total = len(grid) * len(grid[0])
        k = k % total
        def skip(iter, n):
            for _ in range(n):
                next(iter)
            return iter

        def take(iter, n):
            for _ in range(n):
                yield next(iter)
            return

        answer = []
        temp = []
        for num in chain(skip(chain(*grid),total-k),take(chain(*grid),total-k)):
            temp.append(num)
            if len(temp) == len(grid[0]):
                answer.append(temp)
                temp = []
        return answer


# @lc code=end

