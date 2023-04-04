测试数据集错误包含了重复元素

// 题目解析以及代码

// 关注公众号:塔子哥学算法，搜索“P1096”即可得到对应题解
// 题目内容

// 米小游拿到了一个集合（集合中元素互不相等）。

// 她想知道，该集合有多少个元素数量大于 11 的子集，满足子集内的元素两两之间互为倍数关系？

// 由于数量可能过大，请对 109+7109+7 取模。
// 输入描述

// 第一行输入一个正整数 nn ，代表集合大小。

// 第二行输入 nn 个正整数 aiai​ ，代表集合的元素。

// 1≤n≤1051≤n≤105

// 1≤ai≤1061≤ai​≤106
// 输出描述

// 一个整数，代表满足题意的子集数量对 对 109+7109+7 取模的值。
// 样例

// 输入

// 5
// 1 2 3 4 5

// 输出

// 6

// 样例解释

// 共有6个合法的子集：

// {1,2},{1,3},{1,4},{1,5},{1,2,4},{2,4}




#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const ll MOD = 1e9+7;

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<int> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<ll> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

template<class T>
void debug_arr(T a[], int start, int end){
    if (!DEBUG) return;
    for (int i = start; i <= end; i++) cout << a[i] << " ";
    cout << endl;
}

bool myless(string a, string b){
    return a.length() < b.length() || (a.length() == b.length() && a < b);
}

ll quickmulti(ll a, ll p){
    ll ans = 1;
    while (p){
        if (p&1) ans = (ans*a)%MOD;
        a = (a*a)%MOD;
        p >>= 1;
    }
    return ans;
}


void solve()
{
    int n, a;
    cin >> n;
    const int nmax = 1e6+10, MOD = 1e9+7;
    ll ans = 0;
    vector<ll> mp(nmax, 0), cc(nmax, 0);
    for (int i = 0; i < n; i++) {
        cin >> a;
        mp[a]=1;
        cc[a]++;
    }
    for (int i = 1; i < nmax; i++){
        if (mp[i]){
            ans = (ans+(mp[i]-1)*cc[i])%MOD;
            for (int j = i+i; j < nmax; j += i){
                if (mp[j] == 0) continue;
                mp[j] = (mp[j]+mp[i])%MOD;
            }
        }
    }
    cout << ans << endl;
    return;
}



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// #ifndef ONLINE_JUDGE
//     freopen("contests/input", "r", stdin);
// #endif
    solve();

}


#include <bits/stdc++.h>

using namespace std;

const long long M = 1000000007;
int a[100010], pos[1000010];
long long dp[100010];

int main()
{
    // freopen("contests/input", "r", stdin);
    memset(pos, -1, sizeof(pos));
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    sort(a, a + n);
    for (int i = 0; i < n; i++)
    {
        pos[a[i]] = i;
    }
    long long ans = 0;
    for (int i = 0; i < n; i++)
    {
        int tmp = a[i];
        for (int j = 1; j * j <= tmp; j++)
        {
            if (tmp % j == 0)
            {
                if (j != tmp / j && pos[tmp / j] > -1)
                {
                    dp[i] = (dp[i] + dp[pos[tmp / j]]) % M;
                }
                if (pos[j] > -1)
                {
                    dp[i] = (dp[i] + dp[pos[j]]) % M;
                }
            }
        }
        ans += dp[i];
        ans %= M;
        dp[i]++;
    }
    cout << ans << endl;
}