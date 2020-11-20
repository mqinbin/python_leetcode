#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
class Solution:
    month_dict = {
        "Jan":1, "Feb":2, "Mar":3,
         "Apr":4, "May":5, "Jun":6, 
         "Jul":7, "Aug":8, "Sep":9,
          "Oct":10, "Nov":11, "Dec":12
    }
    def reformatDate(self, date: str) -> str:
        d , m ,y = date.split()
        try:
            d = int(d[:2])
        except :
             d = int(d[:1])
        # return y+"-"+ ("%02d" % self.month_dict[m])   + ("%02d" % d) 
        return "%s-%02d-%02d" %( y, self.month_dict[m],d)
# @lc code=end

