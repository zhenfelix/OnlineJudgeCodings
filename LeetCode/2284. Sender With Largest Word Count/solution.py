class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cc = Counter()
        for i, (m, s) in enumerate(zip(messages,senders)):
            cc[s] += len(m.split())
        arr = sorted([(v,k) for k, v in cc.items()])
        return arr[-1][-1]