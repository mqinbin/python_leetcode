#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        charges = {n:0 for n in (5,10,20)}
        for bill in bills:
            success =  self.update_charges(bill,charges)
            print(bill, charges)
            if not success:
                return False
        return True

    def update_charges(self,bill,charges):
        if bill ==5:
            charges[5]+=1
            return True
        if bill ==10:
            if charges[5]:
                charges[5]-=1
                charges[10]+=1
                return True
            return False
        if bill == 20:
            if charges[10] and charges[5]:
                charges[10]-=1
                charges[5]-=1
                return True
            if charges[5]>=3:
                charges[5]-=3
                return True

            return False

# @lc code=end

