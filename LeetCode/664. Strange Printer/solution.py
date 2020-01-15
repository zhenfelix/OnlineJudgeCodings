There is a key proof missing in most of the popular posts, which is we can always print from left to right in a optimal solution. More specifically, assuming we have `S(i,j)` ,  whose optimal solution includes that we print from `i` to `k` at step `t`, and the key obeservation is that there will be no printing overlaping with interval `(i,k)` prior to step `t` since it will be covered eventally. Therefore, we can always move the step `t` to the first step and extend the interval `(i,k)` to the full length `(i,j)` without changing the optimal results. With such an important observation, we can easily have many different approaches to the problem

```python
from functools import lru_cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i+1,j)
            return min(dfs(i,k)+dfs(k+1,j) for k in range(i,j))
        
        s = re.sub(r'(.)\1*', r'\1', s)
        # print(s)
        return dfs(0,len(s)-1)
```


```python
from functools import lru_cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 0
            res = dfs(i,j-1) + 1
            for k in range(i,j):
                if s[j] == s[k]:
                    res = min(res, dfs(i,k)+dfs(k+1,j)-1)
            return res
        
        s = re.sub(r'(.)\1*', r'\1', s)
        print(s)
        return dfs(0,len(s)-1)
```

```python
from functools import lru_cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 0
            res = dfs(i+1,j) + 1
            for k in range(i+1,j+1):
                if s[i] == s[k]:
                    # res = min(res, dfs(i,k-1)+dfs(k+1,j))
                    res = min(res, dfs(i+1,k)+dfs(k+1,j))
            return res
        
        s = re.sub(r'(.)\1*', r'\1', s)
        print(s)
        return dfs(0,len(s)-1)
```

```python
from functools import lru_cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 0
            if i == j:
                return 1
            res = dfs(i+1,j) + 1
            for k in range(i+1,j+1):
                if s[i] == s[k]:
                    res = min(res, dfs(i+1,k-1)+dfs(k,j))
            return res
        
        s = re.sub(r'(.)\1*', r'\1', s)
        print(s)
        return dfs(0,len(s)-1)
```