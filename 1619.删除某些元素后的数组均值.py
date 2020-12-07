#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        from bisect import bisect
        drops = len(arr) // 20
        min_drops = [float("inf")] * drops
        max_drops = [float("-inf")] * drops

        all_sum = 0
        for num in arr:
            all_sum += num
            if num < min_drops[-1]:
                p = bisect(min_drops ,num)
                min_drops.insert(p,num)
                min_drops.pop()
            if num > max_drops[0]:
                p = bisect(max_drops ,num)
                max_drops.insert(p,num)
                max_drops.pop(0)
        
        print(min_drops,max_drops)
        return (all_sum - sum(min_drops) - sum(max_drops)) /  (len(arr) - 2 * drops)
        # arr.sort()
        # drops = len(arr) // 20
        # return sum(arr[drops:-drops]) / (len(arr) - 2 * drops)
# @lc code=end

