class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        inf = 1e9
        ans = [inf]*n 
        st = [n-1]
        for i in range(n-1)[::-1]:
            # print(st)
            while st and (cars[st[-1]][-1] >= cars[i][-1] or cars[st[-1]][0]+cars[st[-1]][-1]*ans[st[-1]] >= cars[i][0]+cars[i][-1]*ans[st[-1]]):
                j = st.pop()
            
            if st:
                ans[i] = (cars[st[-1]][0]-cars[i][0])/(cars[i][-1]-cars[st[-1]][-1])
            st.append(i)
        return [a if a < inf else -1 for a in ans] 
                


class Solution:
    def getCollisionTimes(self, A):
        stack = []
        n = len(A)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = A[i]
            while stack and (s <= A[stack[-1]][1] or (A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (A[stack[-1]][0] - p) / (s - A[stack[-1]][1])
            stack.append(i)
        return res        


class Solution:
    def getCollisionTimes(self, A):
        stack = []
        n = len(A)
        res = [float('inf')] * n
        for i in range(n-1, -1, -1):
            p, s = A[i]
            while stack and (s <= A[stack[-1]][1] or (A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]]):
                stack.pop()
            if stack:
                res[i] = (A[stack[-1]][0] - p) / (s - A[stack[-1]][1])
            stack.append(i)
        return [t if t < float('inf') else -1 for t in res]        


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n, epsilon = len(cars), 0.0000001
        ans = [float('inf')]*n
        st = [(float('inf'),cars[-1][-1])]
        for i in range(n-1)[::-1]:
            dist = cars[i+1][0] - cars[i][0]
            t = 0
            # print(st,dist)
            while st and dist > epsilon:
                T, speed = st[-1]
                if st[-1][0] == float('inf') and cars[i][-1] <= speed:
                    # st.append((float('inf'),cars[i][-1]))
                    dist = float('inf')
                    t = float('inf')
                    break
                
                if dist + (T-t)*(speed-cars[i][-1]) < 0:
                    t += dist/(cars[i][-1]-speed)
                    dist = 0
                else:
                    dist += (T-t)*(speed-cars[i][-1])
                    t = T
                    st.pop()
            st.append((t,cars[i][-1]))
            ans[i] = t
        return [t if t < float('inf') else -1 for t in ans]



