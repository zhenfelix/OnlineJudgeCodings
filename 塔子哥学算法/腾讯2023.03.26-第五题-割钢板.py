
# 2023.03.26-第五题-割钢板
# 题目内容

# 塔子哥是一位著名的锻造家，他经常需要切割钢板来制作各种家具和工艺品。今天，他拿到了一块非常大的矩形钢板，需要将其切割成多个小钢板来制作家具。

# 为了使得切割后的小钢板能够充分利用，塔子哥需要仔细地规划每一条切割线的位置。他希望每条切割线都是斜着的，因为这样可以得到更多的小钢板。同时，他也想要确保钢板的美观程度，所以每条切割线的斜率只能是 −1−1 或 11。

# 为了更好地规划切割线的位置，塔子哥先将钢板放到笛卡尔坐标系中，左下角的坐标为 (0,0)(0,0)，左上角的坐标为 (0,H)(0,H)，右下角的坐标为 (W,0)(W,0)，右上角的坐标为 (W,H)(W,H)。然后，他画了 mm 条标记线，并将每条标记线的位置表示为两个整数坐标点 (xi,1,yi,1)(xi,1​,yi,1​) 和 (xi,2,yi,2)(xi,2​,yi,2​)，这样他就可以用锯子沿着每条标记线进行切割。

# 现在，塔子哥想知道，如果按照这些标记线进行切割，会得到多少个小钢板。
# 输入描述

# 第一行输入两个正整数 HH ， WW 表示钢板的高度和长度

# 第二行输入一个正整数 mm 表示标记线的条数。

# 接下来 mm 行每行四个正整数xi,1,yi,1,xi,2,yi,2xi,1​,yi,1​,xi,2​,yi,2​ 表示标记线经过的坐标点。（ 1≤H,W≤500,1≤m≤103,0≤xi,1,xi,2≤W,0≤yi,1,yi,2≤H1≤H,W≤500,1≤m≤103,0≤xi,1​,xi,2​≤W,0≤yi,1​,yi,2​≤H ）

# 数据保证(xi,1,yi,1)≠(xi,2,yi,2)(xi,1​,yi,1​)=(xi,2​,yi,2​)

# 注：如果某条线段出现了多次，按照一次统计即可。
# 输出描述

# 输出小钢板的个数。
# 样例
# 样例一

# 输入

# 1 1
# 1
# 0 0 1 1

# 输出

# 2

# 样例二

# 输入

# 2 2
# 2
# 0 0 1 1
# 0 1 1 0

# 输出

# 4


h,w = list(map(int,input().split()))
m = int(input())
seen = set()
for _ in range(m):
    x1,y1,x2,y2 = list(map(int,input().split()))
    k = (y1-y2)//(x1-x2)
    z = y1-k*x1 
    seen.add((k,z))

parent = list(range(h*w*4))
def find(u):
    pu = u
    while parent[u] != u:
        u = parent[u]
    while pu != u:
        tmp = parent[pu]
        parent[pu] = u
        pu = tmp 
    return pu 
def connect(u,v):
    ru, rv = find(u), find(v)
    if ru != rv:
        parent[ru] = rv 
    return
def get(x,y,d):
    return (y*w+x)*4+d 
for y in range(h):
    for x in range(w):
        if x:
            connect(get(x,y,3),get(x-1,y,1))
        if y:
            connect(get(x,y,0),get(x,y-1,2))
        if (1,y-x) not in seen:
            connect(get(x,y,0),get(x,y,3))
            connect(get(x,y,1),get(x,y,2))
        if (-1,y+1+x) not in seen:
            connect(get(x,y,0),get(x,y,1))
            connect(get(x,y,3),get(x,y,2))
print(len(set([find(u) for u in range(h*w*4)])))


        