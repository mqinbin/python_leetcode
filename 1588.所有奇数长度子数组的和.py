#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # answer = 0
        # for i in range(len(arr)):
        #     for l in range(1,len(arr)+1,2):
        #         if i+l <=len(arr):
        #             answer += sum(arr[i:i+l])
        # return answer

        answer = 0
        length = len(arr)
        for i in range(length):
            left = i + 1
            right = length-i

            left_even = (left + 1) // 2
            left_odd = left - left_even
            right_even = (right + 1) // 2
            right_odd = right - right_even

            answer  += arr[i] * ( left_even*right_even   +left_odd*right_odd   )

        return answer 


# @lc code=end

