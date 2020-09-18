class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n):
            cnt = 0
            j = i + m
            while j < n and arr[j] == arr[j-m]:
                j += 1
            # print(i,j)
            cnt += (j-i)//m 
            if cnt >= k:
                return True
        return False


class Solution:
    def containsPattern(self, arr, m, k):
        cnt = 0
        for i, a in enumerate(arr):
            if i < m: continue
            if arr[i] != arr[i-m]:
                cnt = 0
                continue
            cnt += 1
            if cnt == m*(k-1):
                return True
        return False