#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        counter = Counter(arr)
        for k in sorted(counter.keys(),reverse=True):
            if counter[k] == k:
                return k
        return -1
        
# @lc code=end

