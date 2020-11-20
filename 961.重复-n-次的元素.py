#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()

        for num in A:
            if num in s:
                return num
            else:
                s.add(num)

    
