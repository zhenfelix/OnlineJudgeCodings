class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [1000000]*(n+1)
        dp[0] = 0
        dp[1] = books[0][1]
        for i in range(2,n+1):
            h = books[i-1][1]
            w = books[i-1][0]
            idx = i-1
            while idx >=0 and w <= shelf_width:
                dp[i] =min(dp[i], h+dp[idx])
                w += books[idx-1][0]
                h = max(h,books[idx-1][1])
                
                idx -= 1
        
        return dp[-1]