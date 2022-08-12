#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <vector>
using namespace std;

// http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0200r0.html
template<class Fun> class y_combinator_result {
    Fun fun_;
public:
    template<class T> explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}
    template<class ...Args> decltype(auto) operator()(Args &&...args) { return fun_(std::ref(*this), std::forward<Args>(args)...); }
};
template<class Fun> decltype(auto) y_combinator(Fun &&fun) { return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun)); }


template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }

void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef NEAL_DEBUG
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif


void run_case() {
    int S;
    cin >> S;
    int ans = 1e9;

    for (int mask = 0; mask < 1 << 9; mask++) {
        int sum = 0;
        string num;

        for (int i = 0; i < 9; i++)
            if (mask >> i & 1) {
                sum += i + 1;
                num += char('0' + (i + 1));
            }

        if (sum != S)
            continue;

        ans = min(ans, stoi(num));
    }

    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
#ifndef NEAL_DEBUG
    cin.tie(nullptr);
#endif

    int tests;
    cin >> tests;

    while (tests-- > 0)
        run_case();
}







// #include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>
#include <queue>

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 110;

int t, n, m, x, y, c, q, k, last, s;
ll MOD = 998244353;
string text, MX = "999999999";
string dp[10][50];


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

template<class T>
void debug_arr(T a[], int start, int end){
    if (!DEBUG) return;
    for (int i = start; i <= end; i++) cout << a[i] << " ";
    cout << endl;
}

bool myless(string a, string b){
    return a.length() < b.length() || (a.length() == b.length() && a < b);
}

void solve()
{
    scanf("%d", &s);
    for (int i = 1; i <= 9; i++){
        for (int j = 0; j <= s; j++){
            dp[i][j] = MX;
            if (j == 0) dp[i][j] = "";
            else if (j <= 9 && i <= j) dp[i][j] = to_string(j);
        }
    }
    for (int i = 8; i >= 1; i--){
        for (int j = 0; j <= s; j++){
            for (int k = i; k <= 8; k++){
                if (j > k && myless(to_string(k)+dp[k+1][j-k], dp[i][j])) 
                    dp[i][j] = to_string(k)+dp[k+1][j-k];
            }
        }
    }
    cout << dp[1][s] << endl;
    return;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
        solve();
    }

}
