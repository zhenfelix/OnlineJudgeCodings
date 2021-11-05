class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cc = Counter(arr)
        cnt = 0
        for s in arr:
            if cc[s] == 1:
                cnt += 1
            if cnt == k:
                return s  
        return ""