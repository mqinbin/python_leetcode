#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        netGas = [gas[i] - cost[i] for i in range(len(gas))] * 2

        targetIndex = 0 
        reducegas = 0
        for i in range(len(netGas)):
            if reducegas< 0:
                targetIndex = i
                reducegas = 0
            reducegas += netGas[i]
        
        return targetIndex if targetIndex < len(gas) else -1



# @lc code=end

