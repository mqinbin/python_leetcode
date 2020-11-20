#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {v:i for i,v in enumerate(arr2)}
        not_apperence = []
        helper = {}
        for num in arr1:
            if num in dic:
                helper[num] = helper.get(num ,0) + 1
            else:
                not_apperence.append(num)
        not_apperence.sort()
        answer = []
        for n in arr2:
            answer += [n] * helper[n]
        
        return answer + not_apperence

                  
# @lc code=end

