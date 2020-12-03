#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start



class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        class Node():
            def __init__(self):
                self.nexts = []
        
        dic = {}
        for path in paths:
            for site in path:
                if site not in dic:
                    dic[site] = Node()
            dic[path[0]].nexts.append(path[1])
        
        for city in dic:
            if not dic[city].nexts:
                return city
        return None
# @lc code=end

