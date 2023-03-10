class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = ['']
        for ch in s:
            if int(ans[-1]+ch) <= k:
                ans[-1] += ch  
            elif int(ch) > k:
                return -1
            else:
                ans.append(ch)
        return len(ans)