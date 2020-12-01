#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if num % 2 == 0:
                if (num // 2 )in s or (num * 2) in s:
                    return True
            else:
                if (num * 2) in s  :
                    return True
            s.add(num)
        return False
# @lc code=end

