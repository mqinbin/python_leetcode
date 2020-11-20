#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) -1
        answer = []
        while left <right:
            while left<right and left & 1 == A[left] & 1:
                left +=1
            while left<right and right & 1 == A[right] & 1:
                right -=1
            if left< right:
                answer.append(left)
                answer.append(right)
            left +=1
            right -=1
        print(answer)
        while answer:
            anyone = answer.pop()
            for i in answer:
                if i & 1 != anyone & 1:
                    A[anyone] , A[i] =  A[i] ,A[anyone] 
                    answer.remove(i)
                    break

        return A
# @lc code=end

