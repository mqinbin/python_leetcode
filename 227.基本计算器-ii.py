#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        ops = '+-*/'
        nums = '1234567890'
        s_nums = []
        s_ops = []
        temp_num = 0


        for char in s+'+0':
            if char in ops:
                s_nums.append(temp_num)
                if s_ops and s_ops[-1] in "*/":
                    arg2 = s_nums.pop()
                    arg1 = s_nums.pop()
                    s_nums.append(self.cal(arg1,arg2 , s_ops.pop()))

                # if s_ops and s_ops[-1] == '-':
                #     s_nums[-1] = - s_nums[-1]

                s_ops.append(char)
                temp_num= 0

            elif char in nums:
                temp_num = temp_num * 10 + (ord(char) - ord('0'))

        for i in range(len(s_ops)):
            if s_ops[i] == '-':
                s_ops[i] = '+'
                s_nums[i+1] = -s_nums[i+1]

        # print(s)
        # print(s_nums)    
        # print(s_ops)    
        
        return sum(s_nums)

    def cal(self,arg1,arg2,op):
        if '*' == op: return arg1 * arg2
        if '/' == op: return arg1 // arg2
        if '+' == op: return arg1 + arg2
        if '-' == op: return arg1 - arg2

# @lc code=end

