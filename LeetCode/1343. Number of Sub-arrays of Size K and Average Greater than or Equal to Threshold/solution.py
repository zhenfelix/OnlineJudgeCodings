class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0 
        arr = [0]+arr
        n = len(arr)
        sums = sum(arr[:k])
        for i in range(k,n):
            sums += arr[i]-arr[i-k]
            if sums >= threshold*k:
                cnt += 1
        return cnt
        