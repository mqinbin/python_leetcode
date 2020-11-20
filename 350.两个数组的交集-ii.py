/#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        p1 = p2 = 0
        while True:
            try:
                if nums1[p1] < nums2[p2]:
                    p1+=1
                elif nums1[p1] > nums2[p2]:
                    p2+=1
                else:
                    result.append(nums1[p1])
                    p1+=1
                    p2+=1
            except IndexError:
                break
        
        return result

# @lc code=end

