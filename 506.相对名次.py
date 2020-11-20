#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        first_three = [float('-inf')] * 3
        for num in nums:
            if num > first_three[0]:
                first_three = [ num, first_three[0],first_three[1] ]
                continue
            if num > first_three[1]:
                first_three = [  first_three[0],num,first_three[1] ]
                continue
            if num > first_three[2]:
                first_three = [  first_three[0],first_three[1],num ]
                continue
        dic = { t[0]:t[1] for t in zip(first_three, ["Gold Medal", "Silver Medal", "Bronze Medal"])}
        for index, val in enumerate(sorted(nums,reverse=True)):
            if index >= 3:
                dic[val] = str(index+1)

        return [ dic.get(num) for num in nums]
# @lc code=end

