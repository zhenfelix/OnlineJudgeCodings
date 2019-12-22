# class Twitter:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.id2user = {}
#         self.sz = 10
#         self.time = 0

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         """
#         Compose a new tweet.
#         """
#         if userId not in self.id2user:
#             self.id2user[userId] = User()
#         u = self.id2user[userId]
#         u.activity.append((self.time,tweetId))
#         self.time += 1
#         return
        

#     def getNewsFeed(self, userId: int) -> List[int]:
#         """
#         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
#         """
#         if userId not in self.id2user:
#             self.id2user[userId] = User()
#         u = self.id2user[userId]
#         q = []
#         for f in u.following:
#             # print(f,f.activity,f.following)
#             idx = len(f.activity)-1
#             # print(idx)
#             if idx < 0:
#                 continue
#             time, tweetId = f.activity[-1]
#             q.append((-time, tweetId, f, idx))
#         # print(q)
#         heapq.heapify(q)
#         feeds = []
#         while q and len(feeds) < self.sz:
            
#             _, tweetId, f, idx = heapq.heappop(q)
#             feeds.append(tweetId)
#             if idx == 0:
#                 continue
#             idx -= 1
#             heapq.heappush(q,(-f.activity[idx][0],f.activity[idx][1],f,idx))
#         return feeds
        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         """
#         Follower follows a followee. If the operation is invalid, it should be a no-op.
#         """
#         if followerId not in self.id2user:
#             self.id2user[followerId] = User()
#         if followeeId not in self.id2user:
#             self.id2user[followeeId] = User()
#         follower, followee = self.id2user[followerId], self.id2user[followeeId]
#         follower.following.add(followee)
#         return
        

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         """
#         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
#         """
#         if followerId not in self.id2user:
#             self.id2user[followerId] = User()
#         if followeeId not in self.id2user:
#             self.id2user[followeeId] = User()
#         if followerId == followeeId:
#             return
#         follower, followee = self.id2user[followerId], self.id2user[followeeId]
#         if followee in follower.following:
#             follower.following.remove(followee)
#         return
        
# class User:
#     def __init__(self):
#         self.activity = []
#         self.following = set([self])


# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)


class Twitter(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)