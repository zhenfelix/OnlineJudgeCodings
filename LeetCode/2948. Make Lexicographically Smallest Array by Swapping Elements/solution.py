class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = [(nums[i],i) for i in range(n)]
        arr.sort()
        # parent = list(range(n))
        # def find(cur):
        #     if parent[cur] != cur:
        #         parent[cur] = find(parent[cur])
        #     return parent[cur]
        # def connect(u,v):
        #     ru, rv = find(u), find(v)
        #     parent[ru] = rv  
        candidates = [arr[0][1]]
        for j in range(1,n):
            if arr[j][0]-arr[j-1][0] <= limit:
                candidates.append(arr[j][1])
            else:
                m = len(candidates)
                candidates.sort()
                for i in range(m):
                    nums[candidates[i]] = arr[j-m+i][0]
                candidates = [arr[j][1]]
        # print(candidates)
        if candidates:
            m = len(candidates)
            candidates.sort()
            for i in range(m):
                nums[candidates[i]] = arr[n-m+i][0]

        return nums