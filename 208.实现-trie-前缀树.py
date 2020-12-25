#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.children = {}
        self.isLeaf = False


    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isLeaf = True
            return 
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])


    def search(self, word: str) -> bool:
        if len(word) == 0 :
            return self.isLeaf
        if word[0] not in self.children:
            return  False
        else:
            return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0 :
            return True
        if prefix[0] not in self.children:
            return  False
        else:
            return self.children[prefix[0]].startsWith(prefix[1:])



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

