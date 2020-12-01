#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import date
        d1 = date(*map(int, date1.split("-")))
        d2 = date(*map(int, date2.split("-")))
        return abs((d2-d1).days)
# @lc code=end

