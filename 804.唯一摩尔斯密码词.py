#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#


# @lc code=start


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = { chr(t[0]):t[1] for t in zip( range(ord('a'),ord('z') + 1) , [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}

        s = set()
        for word in words:
            s.add(''.join([dic[char] for char in word]))

        return len(s)

# @lc code=end

