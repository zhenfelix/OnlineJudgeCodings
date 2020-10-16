class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.res = 0
        arr = sorted(A)
        def check(x):
            tmp = int(x**0.5)
            return tmp*tmp == x

        def dfs(i, arr):
            n = len(arr)
            if i == n:
                self.res += 1
                print(arr)
                return
            for k in range(i,n):
                if k != i and arr[i] == arr[k]: continue
                arr[i], arr[k] = arr[k], arr[i]
                if i == 0 or check(arr[i-1]+arr[i]):
                    dfs(i+1, arr.copy())  
                # arr[i], arr[k] = arr[k], arr[i]
            return   
        dfs(0,arr.copy())
        return self.res