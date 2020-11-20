#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)


        max_sum = 0
        target = None
        for k in sorted(c.keys()):
            if k+1 in c:
                if c[k] + c[k+1] > max_sum:
                    max_sum = c[k] + c[k+1]
                    target = k
            print(k, max_sum,target)

        return max_sum
        # if target is None:
        #     return 0

        # result = 0
        # for x in nums :
        #     if x in (target,target+1):
        #         result +=1
        # return result

# @lc code=end

