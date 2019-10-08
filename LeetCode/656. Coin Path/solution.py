class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
      n = len(A)
      if n == 1:
        return [1]
      cost = [float('inf')]*n
      if A[-1] != -1:
        cost[-1] = A[-1]
      path = [-1]*n
      for i in range(n-1,-1,-1):
        if cost[i] == float('inf'):
          continue
        for j in range(max(0,i-B),i):
          if A[j] != -1 and cost[i] + A[j] <= cost[j]:
            path[j] = i
            cost[j] = cost[i] + A[j]
      # print(path)
      # print(cost)
      ans = []
      if path[0] == -1:
        return ans
      p = 0
      ans.append(p)
      while p != n-1:
        p = path[p]
        ans.append(p)
      return [a+1 for a in ans]