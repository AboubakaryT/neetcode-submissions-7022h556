class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if len(word) == i:
                return root.end
            if word[i] == ".":
                for letter in root.children.values():
                    if dfs(i+1, letter):
                        return True
                return False
            elif word[i] not in root.children:
                return False

            return dfs(i+1, root.children[word[i]])

        return dfs(0, self.root)

