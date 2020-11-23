#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_heap = []
        cur_max = -1
        for i in range(len(arr) - 1 , -1 , -1):
            max_heap.append(cur_max)
            if arr[i] > cur_max:
                cur_max = arr[i]
        # print(max_heap[::-1])

        return max_heap[::-1]
                
# @lc code=end

