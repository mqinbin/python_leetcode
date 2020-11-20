#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = "aeiouAEIOU"
        result = []
        for index ,word in enumerate (S.split()):
            new_word = ""
            if word[0] not in vowels:
                new_word = word[1:]+word[0]
            else:
                new_word = word
            new_word += 'ma' + 'a' *(index + 1)
            result.append(new_word)
        return " ".join(result)


# @lc code=end

