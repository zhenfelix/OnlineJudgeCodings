class VideoSharingPlatform:

    def __init__(self):
        self.videos = []
        self.candidates = []
        self.likes = []
        self.dislikes = []
        self.views = []

    def valid(self, videoId):
        return videoId < len(self.videos) and self.videos[videoId] != ""

    def upload(self, video: str) -> int:
        if self.candidates:
            idx = heapq.heappop(self.candidates)
            self.videos[idx] = video
        else:
            idx = len(self.videos)
            self.videos.append(video)
            self.likes.append(0)
            self.dislikes.append(0)
            self.views.append(0)
        return idx 


    def remove(self, videoId: int) -> None:
        if not self.valid(videoId):
            return
        heapq.heappush(self.candidates, videoId)
        self.videos[videoId] = ""
        self.likes[videoId] = 0
        self.dislikes[videoId] = 0
        self.views[videoId] = 0


    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if not self.valid(videoId):
            return "-1"
        s = self.videos[videoId]
        self.views[videoId] += 1
        endMinute = min(endMinute,len(s)-1)
        return s[startMinute:endMinute+1]


    def like(self, videoId: int) -> None:
        if not self.valid(videoId):
            return
        self.likes[videoId] += 1


    def dislike(self, videoId: int) -> None:
        if not self.valid(videoId):
            return
        self.dislikes[videoId] += 1


    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if not self.valid(videoId):
            return [-1]
        return [self.likes[videoId],self.dislikes[videoId]]


    def getViews(self, videoId: int) -> int:
        if not self.valid(videoId):
            return -1
        return self.views[videoId]



# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)