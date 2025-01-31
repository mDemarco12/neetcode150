import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.count: int = 0
        self.tweetMap = defaultdict(list)  # map each userId to list of [count, tweetId]
        self.followMap = defaultdict(set)  # map userId to set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # decrement for minHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        res: List = []
        minHeap: List = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # get the last val in the list
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        # pop at most 10 values
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            #
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # add to the hashSet
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove from hashSet
        self.followMap[followerId].discard(followeeId)


    def testCase(self) -> None:
        twitter = Twitter()

        twitter.postTweet(1, 10)
        twitter.postTweet(2, 20)
        print(twitter.getNewsFeed(1))
        print(twitter.getNewsFeed(2))

        twitter.follow(1, 2)
        print(twitter.getNewsFeed(1))
        print(twitter.getNewsFeed(2))

        twitter.unfollow(1, 2)
        print(twitter.getNewsFeed(1))


if __name__ == '__main__':
    twitter = Twitter()
    twitter.testCase()
