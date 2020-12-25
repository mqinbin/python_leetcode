#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        answer = []
        if numerator * denominator < 0 :
            answer.append("-")
            numerator = abs(numerator)
            denominator = abs(denominator)

        temp , numerator = divmod( numerator , denominator )
        answer.append(str(temp))
        if numerator:
            answer.append('.')
            numerator *= 10

        cache = {}
        # digitCount = 0
        recycle = []
        while numerator:
            # digitCount += 1
            if numerator in cache:
                recycle = [cache[numerator] , len(answer)]
                break
            if numerator < denominator:
                numerator *= 10
                answer.append("0")
            else:
                cache[numerator] = len(answer)
                temp , numerator = divmod( numerator , denominator ) 
                answer.append(str(temp))
                numerator *= 10



        if recycle:
            answer.insert(recycle[1],")")
            answer.insert(recycle[0],"(")
        return "".join(answer)
# @lc code=end

