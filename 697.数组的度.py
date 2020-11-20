#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # from collections import Counter
        # c = Counter(nums)

        # max_repeat = max(c.values())
        # result = len(nums)
        # for k in c:
        #     if c[k] == max_repeat:
        #         l ,r = 0 , len(nums) -1
        #         while nums[l] != k:
        #             l += 1
        #         while nums[r] != k:
        #             r -=1
        #         result = min(result, r-l+1)
        # return result
        dic = {}
        for index , num in enumerate(nums):
            if num in dic:
                dic[num].append(index)
            else:
                dic[num] = [index]

        dimension = max([len(x) for x in dic.values()])

        result = min( [ idx[-1] - idx[0]  for idx in dic.values() if len(idx) == dimension ]  )  + 1
        return result
# @lc code=end

