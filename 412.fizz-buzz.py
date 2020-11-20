#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:

    def n_str(self, n):
        if n % 15 == 0:
            return "FizzBuzz"
        if n % 5 == 0:
            return "Buzz"
        if n % 3 ==0:
            return "Fizz"
        return str(n)
    
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.n_str(x) for x in range(1,n+1) ]
# @lc code=end

