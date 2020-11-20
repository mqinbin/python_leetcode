#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
from typing import List
# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]

        statck = []
        statck.append(-1)
        answer = 0
        for i in range(n):
            while heights[i] < heights[statck[-1]]:
                j = statck.pop()
                answer = max(answer, heights[j]* (i-statck[-1]-1))
            statck.append(i)

        # while len(statck) >2:
        #     j = statck.pop()
        #     answer = max(answer, heights[j] * (i-statck[-1]-1))
        return answer

    # 暴力 宽
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     if not heights:
    #         return 0

    #     n = len(heights)
    #     max_area = heights[0]
    #     width = 1
    #     while width < n+1:
    #         min_height_in_window = min(heights[0:width])
    #         max_min_height_in_window = min_height_in_window
    #         offset = 1
    #         while offset <= n-width:
    #             if heights[offset+width-1] < min_height_in_window:
    #                 offset = offset + width
    #                 if offset+width <= n:
    #                     min_height_in_window = min(heights[offset:offset+width])
    #                     if min_height_in_window > max_min_height_in_window:
    #                         max_min_height_in_window = min_height_in_window
    #                 continue
    #             if heights[offset-1] <= min_height_in_window:

    #                 min_height_in_window = min(heights[offset:offset+width])
    #                 if min_height_in_window > max_min_height_in_window:
    #                     max_min_height_in_window = min_height_in_window
    #             offset += 1
    #         max_area = max(max_area, max_min_height_in_window * width)

    #         width+=1
    #     return max_area

    # 暴力 高
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     if not heights:
    #         return 0

    #     n = len(heights)

    #     max_area = heights[0]
    #     cur_height = 0
    #     for i in range(n):
    #         if cur_height ==heights[i]:
    #             continue
    #         else:
    #             cur_height = heights[i]
    #         l = i
    #         for l in  range(i-1, -1 , -1):
    #             if heights[l] < cur_height:
    #                 l +=1
    #                 break
    #         r = i
    #         for r in  range(i+1,n ,):
    #             if heights[r] < cur_height:
    #                 r -=1
    #                 break
    #         max_area = max(max_area,cur_height  * (r-l+1))

    #     return max_area


if __name__ == "__main__":

    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
# @lc code=end
