#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ai = 0
        used_pieces = set()

        while ai < len(arr):
            for pi, nums in enumerate(pieces):
                if pi not in used_pieces and nums[0] == arr[ai]:
                    if nums == arr[ai:ai+len(nums)]:
                        ai += len(nums) 
                        used_pieces.add(pi)
                        break
                    else:
                        return False
            else:
                return False
        return True


                    

        

# @lc code=end

