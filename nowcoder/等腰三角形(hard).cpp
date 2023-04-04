// 链接：https://ac.nowcoder.com/acm/contest/52441/F
// 来源：牛客网

// 时间限制：C/C++ 1秒，其他语言2秒
// 空间限制：C/C++ 262144K，其他语言524288K
// 64bit IO Format: %lld
// 题目描述
// 给定 nn 个坐标，求其中 33 个坐标能表示一个等腰三角形的组数。

// 三点共线不算三角形，等边三角形为特殊的等腰三角形。
// 输入描述:

// 第一行一个整数 n(0≤n≤3000)n(0≤n≤3000)。
// 其后 nn 行每行两个整数 xi,yi(−500≤xi,yi≤500)xi​,yi​(−500≤xi​,yi​≤500)，保证没有重复坐标。

// 输出描述:

// 一行一个整数答案。

// 示例1
// 输入
// 复制

// 4
// 1 1
// -1 1
// -1 -1
// 1 -1

// 输出
// 复制

// 4

/**
 * Created by megurine on 2023/03/24 20:30:31.
 * 诸天神佛，佑我上分！
 **/
#include <bits/stdc++.h>

using namespace std;

#define fastIO() ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr)
#define itr(it) begin(it), end(it)
typedef long long ll;
typedef pair<int, int> PII;
typedef double db;
typedef long double ld;
typedef unsigned uint;
typedef unsigned long long ull;
#define endl '\n'
#define YES() void(cout << "YES\n")
#define NO() void(cout << "NO\n")

template<typename T>
void chmax(T &a, T b) { if (b > a) a = b; }

template<typename T>
void chmin(T &a, T b) { if (b < a) a = b; }

int dist(PII &a, PII &b) {
    int x = a.first - b.first;
    int y = a.second - b.second;
    return x * x + y * y;
}

int fn(int x, int y) {
    return (x + 1000) * 2001 + y + 1000;
}

void elysia() {
    int n;
    cin >> n;
    vector<PII> p(n);
    for (auto &[x, y]: p) cin >> x >> y;
    vector<int> st(5e6 + 10), mp(2e6 + 10);
    ll ans = 0;
    for (int i = 0, x1, y1; i < n; ++i) {
        tie(x1, y1) = p[i];
        for (int j = 0, x2, y2; j < n; ++j) {
            if (j == i) continue;
            tie(x2, y2) = p[j];
            x2 -= x1, y2 -= y1;
            int d = dist(p[i], p[j]);
            ans += mp[d]++;
            if (st[fn(-x2, -y2)]) {
                --ans;
            }
            st[fn(x2, y2)] = 1;
        }
        for (int j = 0, x2, y2; j < n; ++j) {
            if (j == i) continue;
            tie(x2, y2) = p[j];
            x2 -= x1, y2 -= y1;
            mp[dist(p[i], p[j])] = 0;
            st[fn(x2, y2)] = 0;
        }
    }
    cout << ans << endl;
}

int main() {
#ifdef MEGURINE
#define fr(x) freopen(x, "r", stdin)
#define fw(x) freopen(x, "w", stdout)
    fr("../input.txt");
    fw("../output.txt");
    clock_t start = clock();
#endif
    fastIO();
    int T = 1;
//    cin >> T;
    cout << fixed << setprecision(12);
    while (T--) {
        elysia();
    }
    cout.flush();
#ifdef MEGURINE
    clock_t end = clock();
    cout << "\n\nRunning Time : " << (double) (end - start) / CLOCKS_PER_SEC * 1000 << "ms" << endl;
#endif
    return 0;
}