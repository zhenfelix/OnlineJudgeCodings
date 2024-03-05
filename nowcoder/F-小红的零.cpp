// 链接：https://ac.nowcoder.com/acm/contest/69695/F
// 来源：牛客网

// 题目描述
// 小红拿到了一个数组aa，她定义一个区间的权值为区间内所有数的乘积末尾0的数量，求所有区间的权值之和。
// 用数学语言来说，我们称区间[i,j][i,j]权值f(i,j)f(i,j)为区间内所有数乘积末尾0的数目，求∑i=1n∑j=inf(i,j)∑i=1n​∑j=in​f(i,j)。
// 输入描述:

// 第一行输入一个正整数1≤n≤1051≤n≤105
// 第二行输入nn个正整数1≤ai≤1091≤ai​≤109

// 输出描述:

// 输出一个整数代表答案。保证答案不超过10151015

// 示例1
// 输入
// 复制

// 3
// 10 2 5

// 输出
// 复制

// 5

// 说明

// 区间[1,1]的乘积是10，权值为1。
// 区间[1,2]的乘积是20，权值为1。
// 区间[1,3]的乘积是100，权值为2。
// 区间[2,2]的乘积是2，权值为0。
// 区间[2,3]的乘积是10，权值为1。
// 区间[3,3]的乘积是5，权值为0。
// 总权值为5。


#pragma clang diagnostic push
#pragma ide diagnostic ignored "cppcoreguidelines-narrowing-conversions"
#pragma ide diagnostic ignored "hicpp-signed-bitwise"
#pragma GCC optimize ("Ofast,unroll-loops")
#pragma GCC optimize("no-stack-protector,fast-math")

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vll> vvll;
typedef vector<vvll> vvvll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<pll> vpll;
typedef vector<vpll> vvpll;
typedef vector<pdd> vpdd;
typedef vector<vd> vvd;
#define yn(ans) printf("%s\n", (ans)?"Yes":"No");
#define YN(ans) printf("%s\n", (ans)?"YES":"NO");
template<class T> bool chmax(T &a, T b) {
    if (a >= b) return false;
    a = b; return true;
}
template<class T> bool chmin(T &a, T b) {
    if (a <= b) return false;
    a = b; return true;
}
#define FOR(i, s, e, t) for ((i) = (s); (i) < (e); (i) += (t)) 
#define REP(i, e) for (int i = 0; i < (e); ++i) 
#define REP1(i, s, e) for (int i = (s); i < (e); ++i)
#define RREP(i, e) for (int i = (e); i >= 0; --i)
#define RREP1(i, e, s) for (int i = (e); i >= (s); --i)
#define all(v) v.begin(), v.end()
#define pb push_back
#define qb pop_back
#define pf push_front
#define qf pop_front
#define maxe max_element
#define mine min_element
ll inf = 1e18;
#define DEBUG printf("%d\n", __LINE__); fflush(stdout);
template<class T> void print(vector<T> &v, bool withSize = false) {
    if (withSize) cout << v.size() << endl;
    REP(i, v.size()) cout << v[i] << " "; 
    cout << endl;
}
mt19937_64 rng((unsigned int) chrono::steady_clock::now().time_since_epoch().count());

int __FAST_IO__ = []() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    return 0;
}();

class Fenw {
public:
    Fenw(ll _n): n(_n), v(n, 0) {}
    int lowbit(int x) {return x & -x;}
    ll query(int x) {
        ll ans = 0;
        for (int i = x; i > 0; i -= lowbit(i)) ans += v[i];
        return ans;
    }
    void update(int x, ll val) {
        for (int i = x; i < n; i += lowbit(i)) {
            v[i] += val;
        }
    }
private:
    int n;
    vector<ll> v;
};

int main() {
    int N; 
    cin >> N;
    vi p2(N, 0), p5(N, 0);
    int mx = N * 60, base = 20 * N;
    Fenw f2(mx), fc2(mx), f5(mx), fc5(mx);
    fc2.update(base, 1);
    fc5.update(base, 1);
    ll ans = 0;
    REP(i, N) {
        int x;
        cin >> x;
        while (x % 2 == 0) p2[i]++, x /= 2;
        while (x % 5 == 0) p5[i]++, x /= 5;
        if (i > 0) p2[i] += p2[i - 1], p5[i] += p5[i - 1];
        int diff = p2[i] - p5[i];
        ll sum5 = f5.query(diff + base), cnt5 = fc5.query(diff + base);
        ll sum2 = f2.query(mx) - f2.query(diff + base), cnt2 = fc2.query(mx) - fc2.query(diff + base);
        ans += p5[i] * cnt5 - sum5;
        ans += p2[i] * cnt2 - sum2;
        f2.update(diff + base, p2[i]);
        fc2.update(diff + base, 1);
        f5.update(diff + base, p5[i]);
        fc5.update(diff + base, 1);
    }
    cout << ans;
    
    return 0;
}
