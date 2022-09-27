class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        def check(arr):
            n = len(arr)
            flag = [0]*n 
            dp = [1]*n 
            for i in range(1,n):
                if dp[i-1] >= k:
                    flag[i] = 1
                if arr[i-1] >= arr[i]:
                    dp[i] += dp[i-1]
            return flag
        left, right = check(nums), check(nums[::-1])
        right = right[::-1]
        # print(left,right)
        n = len(nums)
        ans = []
        for i in range(k,n-k):
            if left[i] and right[i]:
                ans.append(i)
        return ans






class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        def check(arr):
            n = len(arr)
            q = deque()
            flag = [0]*n 
            for i in range(n):
                while q and i - q[0] > k:
                    q.popleft()
                if len(q) == k:
                    flag[i] = 1
                # print(i,q)
                while q and arr[q[-1]] < arr[i]:
                    q.pop()
                q.append(i)
            return flag
        left, right = check(nums), check(nums[::-1])
        right = right[::-1]
        print(left,right)
        n = len(nums)
        ans = []
        for i in range(k,n-k):
            if left[i] and right[i]:
                ans.append(i)
        return ans

