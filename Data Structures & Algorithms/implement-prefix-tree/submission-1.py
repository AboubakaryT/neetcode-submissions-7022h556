class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.root
        for c in word:
            if c not in trie.children:
                trie.children[c] = TrieNode()
            trie = trie.children[c] 
        trie.end = True

    def search(self, word: str) -> bool:
        trie = self.root
        for c in word:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        
        if trie.end == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for c in prefix:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)