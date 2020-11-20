#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        for k in range(n-2):
            if k > 0:
                if nums[k] == nums[k-1]:
                    continue

            i = k+1
            j = n-1
            a = nums[k]
            if a > 0:
                break
            while i < j:
                b = nums[i]
                c = nums[j]
                if b + c + a == 0:
                    result.append((a, b, c))
                    while i < j:
                        i += 1
                        if nums[i] != b:
                            break
                    while i < j:
                        j -= 1
                        if nums[j] != c:
                            break
                    continue
                elif b + c + a < 0:
                    while i < j:
                        i += 1
                        if nums[i] !=b:
                            break
                else:
                    while i < j:
                        j -= 1
                        if nums[j] != c:
                            break

        return result
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = set()
#         n = len(nums)
#         for ai in range(n-2) :
#             a = nums[ai]
#             for bi in range(ai+1,n-1):
#                 b = nums[bi]
#                 for ci in range(bi+1,n):
#                     c = nums[ci]
#                     if a + b + c == 0:
#                         result.add(tuple(sorted([a,b,c])))

#         return [list(e) for e in result]
# @lc code=end
