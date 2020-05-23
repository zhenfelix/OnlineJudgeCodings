// https://www.luogu.com.cn/blog/CodyTheWolf/solution-p5021
// https://oi-wiki.org/dp/tree/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 5e4 + 5, MAXM = MAXN << 1;
const int INF = 0x7fffffff;

int head[MAXM], nxt[MAXM], v[MAXM], w[MAXM], cnt;

int n, m;
int root;

inline void Addline(int x, int y, int z)
{
    v[cnt] = y, w[cnt] = z;
    nxt[cnt] = head[x], head[x] = cnt++;

    return;
}

int dp[MAXN], tag[MAXN];//dp是向上贡献的最长链长度，也就是上面说的点权
int que[MAXN], tail;
int res;//还需要的赛道数

inline void DFS(int x, int from, int lim)
{
    for (int i = head[x]; ~i; i = nxt[i])
        if (v[i] != from)
            DFS(v[i], x, lim);//先下去DP一边，这样就不需要多开数组做后面的贪心了

    tail = 0;
    for (int i = head[x]; ~i; i = nxt[i])
        if (v[i] != from)
            que[++tail] = dp[v[i]] + w[i];//把几条链加进队列

    sort(que + 1, que + tail + 1);//排序

    for (int i = tail; i >= 1 && que[i] >= lim; i--)
        tail--, res--;//先把已经能变成赛道的边直接去掉，他们不需要两两匹配

    for (int i = 1; i <= tail; i++)
        if (tag[i] != x)//这个链没有被选过
        //这里的tag不再存True和False，而是存当前点的编号，这样就不用多次清空数组，而且可以保证不会重复（每个点只访问一次）
        {
            int l = i + 1, r = tail;//二分另外一条链使得能刚好组成赛道
            while (l <= r)
            {
                int mid = ((l + r) >> 1);
                if (que[i] + que[mid] >= lim)
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            int pst = l;
            while (tag[pst] == x && pst <= tail)//因为有可能当前二分到的是已经被选过的链，那么我们贪心往后找一条链，可以证明这样是最优的
                pst++;

            if (pst <= tail)//如果有观察上面的代码，可以发现tail+1是我们的溢出区，这里判断一下
                tag[i] = tag[pst] = x, res--;
        }

    dp[x] = 0;
    for (int i = tail; i >= 1; i--)//找到当前没有选过的最长链，向上传递（其实也就是把链看成是当前点对上面点的贡献）
        if (tag[i] != x)
        {
            dp[x] = que[i];
            break;
        }

    return;
}

signed main(void)
{
    freopen("input.txt", "r", stdin);
    memset(head, -1, sizeof head);

    cin >> n >> m;
    for (int i = 1, x, y, z; i < n; i++)
    {
        scanf("%d %d %d", &x, &y, &z);
        Addline(x, y, z), Addline(y, x, z);
    }

    root = rand() % n + 1;//随机选根

    int l = 0, r = INF, ans = 0;
    while (l <= r)//二分答案
    {
        int mid = ((l + r) >> 1);
        res = m;

        memset(tag, false, sizeof tag);

        DFS(root, 0, mid);
        if (res <= 0)
            // ans = mid, l = mid + 1;
            l = mid + 1;
        else
            r = mid - 1;
    }

    cout << r << endl;

    return 0;
}