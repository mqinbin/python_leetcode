#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(1, len(flowerbed) -1 ):
            if flowerbed[i-1] == 0 and flowerbed[i+1] ==0 and flowerbed[i] ==0 :
                print(i)
                flowerbed[i] = 1
                n -=1
        


        return n <= 0
# @lc code=end

