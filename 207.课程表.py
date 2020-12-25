#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]  
        for prere in prerequisites:
            graph[prere[0]].add(prere[1])
        
        def genEmpty(graph):
            return set([ i for i in range(len(graph)) if not graph[i] ])
            
        empty =  genEmpty(graph)
        # print(graph)
        # print(empty)
        while True:
            for dependsCouse in graph:
                dependsCouse -= empty
            empty2 = genEmpty(graph)
            if len(empty2) == numCourses:
                return True
            if empty == empty2:
                return False
            empty = empty2
            



# @lc code=end

