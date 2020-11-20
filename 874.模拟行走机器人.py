#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocks = {}
        for obstacle in obstacles:
            if obstacle[0] not in blocks:
                blocks[obstacle[0]] = set()
            blocks[obstacle[0]].add(obstacle[1])
        pos = [0,0]
        direct = (1,1) # first 1 for y  second 1 for positive
        answer = 0
        direct_map  = {
            (1,1):[(0,-1),(0,1)],
            (1,-1):[(0,1) ,(0,-1)],
            (0,1):[(1,1),(1,-1)] ,
            (0,-1):[(1,-1),(1,1)] 
            }
        for command in commands:
            if command < 0:
                direct = direct_map[direct][command]
                continue
            for step in range(command):

                pos[direct[0]] +=  direct[1]* 1

                if pos[0] in blocks and pos[1] in blocks[pos[0]]:
                    pos[direct[0]] -=  direct[1]* 1
                    break
            answer = max(answer ,pos[0] ** 2 + pos[1] ** 2)
        return answer

        
# @lc code=end

