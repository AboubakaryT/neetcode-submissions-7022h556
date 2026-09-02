class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #if not true then we know that the word is in the list and we can proceed from there.
        res = 0 
        adjList = collections.defaultdict(list)
        """
        cat: *at -> c*t -> ca*
        """
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        queue = collections.deque()
        queue.append(beginWord)
        res = 1

        while queue: 
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjList[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)

            res+=1

            
        return 0 



            

        