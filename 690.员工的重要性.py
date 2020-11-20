#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        e_imp = {}
        e_subs = {}

        for employee in employees:
            e_imp[employee.id] = employee.importance
            e_subs[employee.id] = employee.subordinates
        
        answer = 0
        stack = [id]
        while stack:
            cur_id = stack.pop()
            answer += e_imp[cur_id]
            if e_subs[cur_id]:
                stack.extend(e_subs[cur_id])
        
        return answer
# @lc code=end

