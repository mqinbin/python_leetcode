#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1 , len(arr)):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    answer += 1
        return answer
# @lc code=end 

