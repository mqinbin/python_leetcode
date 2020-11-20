#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        c = Counter(deck)
        min_v = min(c.values())
        if min_v >=2:
            for factor in self.get_factors(min_v):
                found = True
                for v in c.values():
                    if v % factor != 0:
                        found =False
                        break
                if found:
                    return True
        else:
            return False
        return False
    
    def get_factors(self,n):
        result = set()
        for i in range(2, int(n ** 0.5 ) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n//i)
        result.add(n)
        return sorted(list(result))
# @lc code=end

