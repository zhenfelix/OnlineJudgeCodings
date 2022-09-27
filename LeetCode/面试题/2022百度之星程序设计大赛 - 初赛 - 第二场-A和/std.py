from collections import *
from functools import *

import heapq
def main():
    n,q,k,x = map(int,input().split())
    arr = list(map(int,input().split()))
    h = []
    h2 = []
    c = 0
    ans = [(i,float('inf')) for i in range(n)]
    index = 0
    for i in range(n):
        if not h:
            heapq.heappush(h,(arr[i],i))
            c += arr[i]
            if k == 1 :
                if c >= x:
                    while index <= i:
                        ans[index] = (index,i)
                        index += 1
                heapq.heappop(h)
                c = 0
        else:
            heapq.heappush(h,(arr[i],i))
            c += arr[i]
            if len(h) > k:
                p = heapq.heappop(h)
                heapq.heappush(h2,(-p[0],p[1]))
                c -= p[0]
            while len(h) <= k and c >= x:
                ans[index] = (index,i)
                for j in range(len(h)):
                    if (arr[index],index) == h[j]:
                        h[-1],h[j] = h[j],h[-1]
                        h.pop()
                        heapq.heapify(h)
                        c -= arr[index]
                        while h2:
                            p = heapq.heappop(h2)
                            if p[1] > index:
                                heapq.heappush(h,(-p[0],p[1]))
                                c -= p[0] 
                                break
                        break
                index += 1
            
    # print(ans)        

    for i in range(q):
        l,r = map(int,input().split())
        if ans[l-1][1] <= r-1:
            print('Y')
        else:
            print('N')

if __name__ == '__main__':
    main()