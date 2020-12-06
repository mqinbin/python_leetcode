#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#

# @lc code=start
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        def matchPattern(arr, pattern, k):
            m = len(pattern)
            if k == 0:
                return True
            if len(pattern) > len(arr):
                return False

            return arr[0:m] == pattern and matchPattern(arr[m:], pattern, k - 1)

        for start in range(0, len(arr) - m * k + 1):
            if matchPattern(arr[start:], arr[start:start + m], k):
                return True

        return False


# @lc code=end

