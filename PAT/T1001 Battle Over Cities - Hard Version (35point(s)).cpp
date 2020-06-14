// #include<stdio.h>
// #include<vector>
// #include<algorithm>
// using namespace std;
// #define MAXN 512
// #define DEBUG 0
// #define INF 0x7fffffff
// struct edge {
//     int b, e, c;
//     edge(int _b, int _e, int _c) {
//         b = _b, e = _e, c = _c;
//     }
//     bool operator<(const edge& obj)const {
//         return c < obj.c;
//     }
// };
// vector<edge> es;
// vector<int> ans;
// int b, e, c, f, N, M, worstv;
// int root[MAXN];

// int findroot(int x) {
//     if (root[x] != x) {
//         root[x] = findroot(root[x]);
//     }
//     return root[x];
// }

// int getcost(int k) {
//     int linkcount = 0, cost = 0;
//     for (int i = 1; i <= N; i++) {
//         root[i] = i;
//     }
//     for (auto item : es) {
//         b = item.b, e = item.e;
//         if (b == k || e == k)continue;
//         int rb = findroot(b), re = findroot(e);
//         if (rb != re) {
//             cost += item.c;
//             root[rb] = re;
//             linkcount++;
//             if (linkcount == N - 2) {
//                 return cost;
//             }
//         }
//     }
//     return INF;
// }
// int main() {
//     if (DEBUG) {
//         freopen("in.txt", "r", stdin);
//     }
//     scanf("%d%d", &N, &M);
//     for (int i = 0; i < M; i++) {
//         scanf("%d%d%d%d", &b, &e, &c, &f);
//         if (f == 1) c = 0;
//         es.push_back(edge(b, e, c));
//     }
//     sort(es.begin(), es.end());
//     for (int i = 1; i <= N; i++) {
//         int v = getcost(i);
//         if (v > worstv) {
//             worstv = v;
//             ans.clear();
//             ans.push_back(i);
//         }
//         else if (v == worstv) {
//             ans.push_back(i);
//         }
//     }
//     if (worstv == 0) {
//         printf("0\n");
//     }
//     else {
//         int len = ans.size();
//         for (int i = 0; i < len; i++) {
//             printf("%d", ans[i]);
//             if (i == len - 1)printf("\n");
//             else printf(" ");
//         }
//     }
//     return 0;
// }



#include <algorithm>
#include <cstdio>
using namespace std;

#define Log(format, ...) // printf(format, ##__VA_ARGS__)

struct Node {
    int u, v, w;
    Node(int _u = 0, int _v = 0, int _w = 0) : u(_u), v(_v), w(_w) {}
    bool operator<(const Node &rhs) const { return w < rhs.w; }
};

const int maxn = 505;
int ans[maxn];
Node edge[maxn * maxn];
int edgePos;

void addEdge(Node e) {
    edge[edgePos++] = e;
    Log("addEdge %d -> %d cost %d\n", e.u, e.v, e.w);
}

int f[maxn];
int ufs(int x) { return f[x] == x ? x : f[x] = ufs(f[x]); }
int Kruskal(int n, int m, int d) {
    int cost = 0;
    for (int i = 0; i <= n; ++i)
        f[i] = i;

    for (int i = 0; i < m; ++i) {
        int u = edge[i].u, v = edge[i].v;
        int x = ufs(u), y = ufs(v);
        Log("\t\t%d(%d) %d(%d)\n", u, x, v, y);
        if (u != d && v != d && x != y) { //　不连接被占领的城市
            Log("\t\tconnect %d -> %d cost %d\n", u, v, edge[i].w);
            f[x] = y;
            cost += edge[i].w;
        }
    }
    int root = 1 == d ? ufs(2) : ufs(1);
    for (int i = 1; i <= n; ++i) {
        if (i != d && ufs(i) != root)
            cost = -1; // 无法连通
    }
    return cost;
}

int main() {
    freopen("input.txt", "r", stdin);
    int n, m;
    scanf("%d%d", &n, &m);
    edgePos = 0;
    for (int i = 0; i < m; ++i) {
        int u, v, w, s;
        scanf("%d%d%d%d", &u, &v, &w, &s);
        addEdge(Node(u, v, s ? 0 : w));
    }
    sort(edge, edge + m);

    int ansPos = 0, maxCost = 0;
    for (int i = 1; i <= n; ++i) {
        int cost = Kruskal(n, m, i);
        Log("Test %d cost %d\n", i, cost);
        if (maxCost != -1 && (cost > maxCost || cost == -1)) {
            maxCost = cost;
            ansPos = 0;
            ans[ansPos++] = i;
            Log("\tmax value update.\n");
        } else if (cost == maxCost) {
            ans[ansPos++] = i;
            Log("\tadd to ans.\n");
        }
    }

    if (maxCost == 0) {
        printf("0");
    } else {
        for (int i = 0; i < ansPos; ++i) {
            if (i)
                printf(" ");
            printf("%d", ans[i]);
        }
    }
    printf("\n");

    return 0;
}