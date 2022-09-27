# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         n = len(s)
#         start = 0
#         Next = [0]*(n+1)
#         Next[0] = -1
#         cur = 0
#         while cur < n:
#             print(Next)
#             i = cur-start
#             j = Next[i]
#             print(i,j)
#             print(s[start:cur+1])
#             print("")
#             if j == -1 or s[start+i] == s[start+j]:
#                 Next[i+1] = j+1
#                 cur += 1
#             elif s[start+i] > s[start+j]:
#                 start = cur - j
#             else:
#                 Next[i] = Next[j]
        
#         return s[start:]


# https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation
# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         count=collections.defaultdict(list)
#         for i in range(len(s)):
#             count[s[i]].append(i)
#         largeC=max(count.keys())
#         starts={}
#         for pos in count[largeC]:
#             starts[pos]=pos+1
#       # Initialize all candidates and their pointers
        
#         while len(starts)>1:
#       # Eliminate till we have only one
#             toDel=set()
#             nextC=collections.defaultdict(list)
#             for start,end in starts.items():
#                 if end==len(s):
#               # Remove if reaching the end
#                     toDel.add(start)
#                     continue
                    
#                 nextC[s[end]].append(start)
#               # Filter by current letter
                
#                 if end in starts:
#                     toDel.add(end)
#               # "Swallow" the latter candidate
            
#             nextStarts={}
#             largeC=max(nextC.keys())
#             for start in nextC[largeC]:
#                 if start not in toDel:
#                     nextStarts[start]=starts[start]+1
#                   # Select what we keep for the next step
#             starts=nextStarts.copy()
#         for start,end in starts.items():
#             return s[start:]

# from collections import deque

# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         q = deque()
#         maxChar = 'a'
#         for i, ch in enumerate(s):
#             if ch == maxChar:
#                 q.append((i,i+1))
#             elif ch > maxChar:
#                 maxChar = ch
#                 q.clear()
#                 q.append((i,i+1))
                
#         while len(q) > 1:
#             n = len(q)
#             tmp = deque()
#             maxChar = 'a'
#             end = -1
#             for i in range(n):
#                 front = q.popleft()
#                 if front[0] != end and front[1] < len(s) and s[front[1]] >= maxChar:
#                     if s[front[1]] > maxChar:
#                         tmp.clear()
#                     maxChar = s[front[1]]
#                     tmp.append((front[0],front[1]+1))
#                 end = front[1]
#             q = tmp.copy()
#         return s[q[0][0]:]
                    
    
# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         i, indexes = 0, list(range(len(s)))
#         while len(indexes) > 1:
#             new = []
#             mx = max([s[i + j] for j in indexes if i + j < len(s)])
#             for k, j in enumerate(indexes):
#                 if k - 1 >= 0 and indexes[k - 1] + i == j:
#                     continue
#                 if i + j >= len(s):
#                     break
#                 if s[i + j] == mx:
#                     new.append(j)
#             i += 1
#             indexes = new
#         return s[indexes[0]:]


# https://oi.men.ci/suffix-array-notes/
# Submission Result: Time Limit Exceeded 
   
# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         maxn = 26
#         n = len(s)
#         buc = [0]*(maxn+1)
#         a = [0]*(n+1)
#         rk = [0]*(n+1)
#         for i, ch in enumerate(s):
#             a[i+1] = ord(ch)-ord('a')+1
#             buc[a[i+1]] += 1
#         for i in range(1,maxn+1,1):
#             buc[i] += buc[i-1]
#         for i in range(1,n+1,1):
#             rk[i] = buc[a[i]-1]+1
            
#         t = 1
#         fir = [0]*(n+1)
#         sec = [0]*(n+1)
#         sa = [0]*(n+1)
#         tmp = [0]*(n+1)
#         while t <= n:
#             for i in range(1,n+1,1):
#                 fir[i] = rk[i]
#                 if i+t <= n:
#                     sec[i] = rk[i+t]
#                 else:
#                     sec[i] = 0
#             buc = [0]*(n+1)
#             for i in range(1,n+1,1):
#                 buc[sec[i]] += 1
#             for i in range(1,n+1,1):
#                 buc[i] += buc[i-1]
            
#             for i in range(1,n+1,1):
#                 buc[sec[i]] -= 1
#                 tmp[n-buc[sec[i]]] = i
#             buc = [0]*(n+1)
            
#             for i in range(1,n+1,1):
#                 buc[fir[i]] += 1
#             for i in range(1,n+1,1):
#                 buc[i] += buc[i-1]
#             for i in range(1,n+1,1):
#                 j = tmp[i]
#                 sa[buc[fir[j]]] = j
#                 buc[fir[j]] -= 1
#             last = 0
#             flag = True
#             for i in range(1,n+1,1):
#                 if last == 0:
#                     rk[sa[i]] = 1
#                 elif fir[sa[i]] == fir[last] and sec[sa[i]] == sec[last]:
#                     rk[sa[i]] = rk[last]
#                     flag = False
#                 else:
#                     rk[sa[i]] = rk[last]+1
#                 last = sa[i]   
#             if flag:
#                 break
                
#             t *= 2
#         return s[sa[-1]-1:]


# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         i, j, k = 0, 1, 0
#         n = len(s)
#         while j + k < n:
#             if i + k == j:
#                 j = j + k
#             elif s[i+k] == s[j+k]:
#                 k += 1
#                 continue
#             elif s[i+k] > s[j+k]:
#                 j = j + k + 1
#             else:
#                 i = j + 1
#                 i, j = j, i
#             k = 0
#         return s[i:]

# https://stackoverflow.com/questions/21409561/max-suffix-of-a-list
# https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/O(n)-time-and-O(1)-space-solution-with-proof
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j = j + k + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        return s[i:]


class Solution:
    def lastSubstring(self, s: str) -> str:
        # Python Version
        n = len(s)
        sec = s+'a'*n
        k, i, j = 0, 0, 1
        while k < n and i < n and j < n:
            if sec[(i + k)] == sec[(j + k)]:
                k += 1
            else:
                if sec[(i + k)] < sec[(j + k)]:
                    i = i + k + 1
                else:
                    j = j + k + 1
                if i == j:
                    i += 1
                k = 0
        i = min(i, j)
        return s[i:]