#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        new_color = newColor
        totalr = len(image)
        totalc = len(image[0])

        self.dfs(sr,sc,image, totalr,totalc,old_color,new_color)
        return image


    def dfs(self, r, c , image, totalr,totalc, old_color, new_color ):
        if r < 0 or r > totalr-1 or c <0 or c > totalc-1:
            return 
        

        if image[r][c] == new_color or image[r][c] != old_color:
            return 
        
        
        image[r][c] = new_color
        self.dfs( r-1, c , image, totalr,totalc, old_color, new_color )
        self.dfs( r+1, c , image, totalr,totalc, old_color, new_color )
        self.dfs( r, c-1 , image, totalr,totalc, old_color, new_color )
        self.dfs( r, c+1 , image, totalr,totalc, old_color, new_color )

# @lc code=end
