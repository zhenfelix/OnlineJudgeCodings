# import bisect

# class TweetCounts:

#     def __init__(self):
#         self.times = defaultdict(set)
#         self.mp = {'minute':60, 'hour':3600, 'day':3600*24}

#     def recordTweet(self, tweetName: str, time: int) -> None:
#         self.times[tweetName].add(time)
        

#     def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
#         delta = self.mp[freq]
#         arr = self.times[tweetName]
#         res = []
#         for t in range(startTime,endTime+1):
#             idx = (t-startTime)//delta
#             while idx >= len(res):
#                 res.append(0)
#             if t in arr:
#                 res[-1] += 1

#         return res

class TweetCounts:

    def __init__(self):
        self.a = defaultdict(list)

    def recordTweet(self, tn: str, time: int) -> None:
        bisect.insort(self.a[tn], time)
       
    def getTweetCountsPerFrequency(self, freq: str, tn: str, startTime: int, endTime: int) -> List[int]:
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        i = startTime
        res = []
        while i <= endTime:
            j = min(i + delta, endTime+1)
            res.append(bisect_left(self.a[tn], j) - bisect_left(self.a[tn], i))
            i += delta
        return res
            
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)