#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {}
        for index , chars in enumerate(["qwertyuiop","asdfghjkjl","zxcvbnm"]):
            for char in chars:
                dic[char] = index
        
        result = []
        for word in words:
            word_l = word.lower()
            for i in range(1,len(word)):
                if dic[word_l[i]] != dic[word_l[0]]:
                    break
            else:
                result.append(word)
        
        return result
# @lc code=end

