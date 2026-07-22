class Twitter:
    from collections import defaultdict
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        #Decrement to be able to use in Python min heap
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap =[]
        self.followMap[userId].add(userId)
        for followeId in self.followMap[userId]:
            if followeId in self.tweetMap:
                index = len(self.tweetMap[followeId]) - 1
                count, tweetId = self.tweetMap[followeId][index]
                minHeap.append([count,tweetId, followeId, index- 1])
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

