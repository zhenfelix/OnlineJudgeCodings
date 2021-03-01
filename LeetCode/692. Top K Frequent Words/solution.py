class Node(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], K: int) -> List[str]:
        cnt = Counter()
        for word in words:
            cnt[word] += 1
        pq = []
        for k, v in cnt.items():
            heapq.heappush(pq,Node(k,v))
            if len(pq) > K:
                heapq.heappop(pq)
        res = []
        while pq:
            word = heapq.heappop(pq).word
            res.append(word)
        return res[::-1]