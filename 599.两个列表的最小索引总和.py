#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # result = {}
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        #         if list1[i] == list2[j]:
        #             val = result.get(i+j,[])
        #             val.append(list1[i])
        #             result[i+j] =  val
        
        # return result[ min(result.keys())]
        d1 = {n:i for i, n in enumerate(list1)}
        d2 = {n:i for i, n in enumerate(list2)}

        index_sum = float('inf')
        result = []
        for n in d1:
            if n in d2:
                if (d1[n] + d2[n]) <index_sum:
                    result = [n]
                    index_sum = d1[n] + d2[n]
                elif (d1[n] + d2[n] )== index_sum:
                    result.append(n)
        return result
                
# @lc code=end

