import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        ans = []
        if n == 0 or m == 0:
            return ans
        j = 0
        arr = [(nums1[i]+nums2[j], i, j) for i in range(n)]
        heapq.heapify(arr)
        
        for _ in range(min(k, n*m)):
            num, i, j = heapq.heappop(arr)
            ans.append((nums1[i],nums2[j]))
            if j + 1 < m:
                heapq.heappush(arr, (nums1[i]+nums2[j+1],i,j+1))
            
        return ans