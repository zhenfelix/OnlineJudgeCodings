class Solution:
    def ringGame(self, c: List[int]) -> int:
        n=len(c)
        hb=1
        for i in range(n):
            while not hb*2>c[i]:
                hb<<=1
        #得到最大bit
        me=max(c)
        def check(x):#判定x是否可以成功遍历数组
            if x>=me:
                return True
            vis=[0]*n
            tot=0#总共已经遍历的数
            cc=c.copy()#复制原数组，因为我们需要进行修改
            l=[(i-1)%n for i in range(n)]#等价与链表的pre指针
            r=[(i+1)%n for i in range(n)]#等价与链表的nxt指针
            def dfs(i,x):
                vis[i]=1
                cc[i]=x
                nonlocal tot
                tot+=1
                nl=l[i]#当前数pre指针
                nr=r[i]#当前数nxt指针
                while tot<n:
                    f=False
                    if cc[nl]<=x:#如果左边可以去，就删除当前数，将分数记在左边
                        x|=cc[nl]
                        if not vis[nl]:
                            tot+=1
                        vis[nl]=1
                        cc[nl]=x
                        l[nr]=nl
                        r[nl]=nr
                        nl=l[nl]
                        f=True
                        continue
                    if c[nr]<=x:#如果右边可以去，就删除当前数，将分数记在左边
                        x|=cc[nr]
                        if not vis[nr]:tot+=1
                        vis[nr]=1
                        cc[nr]=x
                        l[nr]=nl
                        r[nl]=nr
                        nr=r[nr]
                        f=True
                    if not f:
                        break
            for i,a in enumerate(cc):
                if not vis[i] and a<=x:#对i位置开始遍历
                    dfs(i,x|a)
            return tot==n
        cur=hb
        hb>>=1
        while hb:
            if not check(cur+hb-1):#判断这位1需不需要
                cur+=hb
            hb>>=1
        return cur


作者：weak-chicken
链接：https://leetcode-cn.com/problems/K8GULz/solution/onlogmaxchallengejie-fa-by-weak-chicken-38xk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def ringGame(self, c: List[int]) -> int:
        n=len(c)
        hb=1
        for i in range(n):
            while not hb*2>c[i]:
                hb<<=1
        #得到最大bit
        me=max(c)
        def check(x):#判定x是否可以成功遍历数组
            if x>=me:
                return True
            vis=[0]*n
            tot=0#总共已经遍历的数
            cc=c.copy()#复制原数组，因为我们需要进行修改
            l=[(i-1)%n for i in range(n)]#等价与链表的pre指针
            r=[(i+1)%n for i in range(n)]#等价与链表的nxt指针
            def bfs(i,x):
                q = [(c[i],i)]
                cnt = 0
                seen = set()
                seen.add(i)
                cc[i] |= x
                while q:
                    val, node = heapq.heappop(q)
                    if val > x:
                        break
                    left = l[node]
                    right = r[node]
                    r[left] = right
                    l[right] = left
                    vis[node] = 1
                    cnt += 1
                    # x |= val
                    x |= cc[node]
                    if left not in seen:
                        heapq.heappush(q,(c[left],left))
                        seen.add(left)
                        cc[left] |= x
                    if right not in seen:
                        heapq.heappush(q,(c[right],right))
                        seen.add(right)
                        cc[right] |= x
                return cnt

            for i,a in enumerate(c):
                if not vis[i] and a<=x:#对i位置开始遍历
                    tot += bfs(i,x)
                    # print(vis)
            # print(x,tot)
            # print(cc)
            # print(vis)
            # print("\n")
            return tot==n
        cur=hb
        hb>>=1
        while hb:
            if not check(cur+hb-1):#判断这位1需不需要
                cur+=hb
            hb>>=1
        return cur



























class Solution:
    def ringGame(self, c: List[int]) -> int:
        n=len(c)
        hb=1
        for i in range(n):
            while not hb*2>c[i]:
                hb<<=1
        #得到最大bit
        me=max(c)
        def check(x):#判定x是否可以成功遍历数组
            if x>=me:
                return True
            tot=0#总共已经遍历的数
            dp=c.copy()#复制原数组，因为我们需要进行修改
            l=[(i-1)%n for i in range(n)]#等价与链表的pre指针
            r=[(i+1)%n for i in range(n)]#等价与链表的nxt指针
            vis = [0]*n
            def bfs(i,x):
                nonlocal tot
                left = right = i
                while tot < n:
                    if min(c[left],c[right]) > x:
                        break
                    if left == right == i:
                        cur = i
                        left = l[i]
                        right = r[i]
                    elif c[left] < c[right]:
                        cur = left
                        left = l[left]
                    else:
                        cur = right
                        right = r[right]
                    vis[cur] = 1
                    tot += 1
                    x |= dp[cur]
                    ll = l[cur]
                    rr = r[cur]
                    dp[ll] |= x
                    dp[rr] |= x
                    r[ll] = rr
                    l[rr] = ll
                    

                return 

            for i,a in enumerate(c):
                if not vis[i] and a<=x:#对i位置开始遍历
                    bfs(i,x)
            #         print(vis)
            # print(x,tot,n)
            # print(dp)
            # print(vis)
            # print("\n")
            return tot==n
        cur=hb
        hb>>=1
        while hb:
            if not check(cur+hb-1):#判断这位1需不需要
                cur+=hb
            hb>>=1
        return cur
