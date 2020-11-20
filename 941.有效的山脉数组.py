#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        l , r =  0, len(arr) -1
        while l < r and arr[l+1] > arr[l]:
            l += 1
        while r > l and arr[r-1] > arr[r]:
            r -= 1
        print(l,r)
        return l == r and l != 0 and r != len(arr) -1
# @lc code=end

