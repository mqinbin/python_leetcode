#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # answer = 0
        # for num1 in arr1:

        #     for num2 in arr2:
        #         if abs(num1-num2) <= d:
        #             break
        #     else:
        #         answer += 1
        # return answer
        arr2.sort()
        answer = 0
        len2 = len(arr2)
        import bisect
        for num in arr1:
            mid = bisect.bisect(arr2,num)
            if (0<=mid< len2  and abs(arr2[mid] - num) <= d) or (0<= (mid-1)< len2  and abs(arr2[mid-1] - num) <= d):
                continue
            else:
                answer += 1
        return answer


# @lc code=end

