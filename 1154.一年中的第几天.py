#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
cache = [0,31,28,31,30,31,30,31,31,30,31,30]
for i in range(1,12):
    cache[i] += cache[i-1]

def is_leap_year(year):
    return  (year% 400 == 0)  or (year %4 == 0 and year % 100 != 0)
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int,date.split('-'))
        return cache[month-1] + day + (month > 2 and is_leap_year(year))
# @lc code=end

