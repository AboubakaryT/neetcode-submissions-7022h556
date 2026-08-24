class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
            else:
                curr = curr.children[c]     
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        When we find the word we are looking for, we can back track to before we had to word and continue looking for more words from there.
        """

        ROW, COL = len(board), len(board[0])
        res, visited = set(), set()
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r == ROW or c == COL or board[r][c] not in node.children or (r,c) in visited:
                return
       
            visited.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.end:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root, "")
        return list(res)