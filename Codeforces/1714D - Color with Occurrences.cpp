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


const int INF = int(1e9) + 5;

void run_case() {
    string T;
    int N;
    cin >> T >> N;
    vector<string> S(N);

    for (auto &s : S)
        cin >> s;

    int L = int(T.size());
    vector<int> dp(L + 1, INF);
    vector<int> previous(L + 1, -1);
    vector<int> previous_which(L + 1, -1);
    vector<int> previous_start(L + 1, -1);
    dp[0] = 0;

    for (int len = 0; len < L; len++)
        for (int i = 0; i < N; i++) {
            int s_len = int(S[i].size());

            for (int start = max(len - s_len, 0); start <= min(L - s_len, len); start++)
                if (T.substr(start, s_len) == S[i]) {
                    if (dp[len] + 1 < dp[start + s_len]) {
                        dp[start + s_len] = dp[len] + 1;
                        previous[start + s_len] = len;
                        previous_which[start + s_len] = i;
                        previous_start[start + s_len] = start;
                    }
                }
        }

    if (dp[L] >= INF) {
        cout << -1 << '\n';
        return;
    }

    cout << dp[L] << '\n';
    int end = L;

    while (end > 0) {
        int which = previous_which[end];
        int start = previous_start[end];
        cout << which + 1 << ' ' << start + 1 << '\n';
        end = previous[end];
    }
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

int t, n, m, x, y, c, q, k, pre, cur, last;
ll MOD = 998244353;
string text, s;


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

void solve()
{
    cin >> text;
    int sz = text.length();
    vector<vector<int>> intervals;
    scanf("%d\n", &n);
    for (int idx = 0; idx < n; idx++){
        cin >> s;
        int szs = s.length();
        if (szs <= sz){
            for (int i = 0; i < sz-szs+1; i++){
                if (text.substr(i, szs) == s) intervals.push_back({i,i+szs-1,idx});
            }
        }
    }
    sort(intervals.begin(), intervals.end(), [&](vector<int> a, vector<int> b){return a > b;});
    // for (auto v : intervals) cout << v << "; ";
    // cout << endl;
    int reach = 0;
    vector<pii> ans;
    while (reach < sz && !intervals.empty()){
        int tmp = reach, w = -1, p = -1;
        while(!intervals.empty() && intervals.back()[0] <= reach){
            if (intervals.back()[1]+1 > tmp){
                tmp = intervals.back()[1] + 1;
                w = intervals.back()[2];
                p = intervals.back()[0];
            }
            intervals.pop_back();
        }
        if (tmp == reach){
            printf("-1\n");
            return;
        }
        ans.push_back({w,p});
        reach = tmp;
    }
    if (ans.empty() || reach < sz){
        printf("-1\n");
        return;
    }
    printf("%d\n", ans.size());
    for (auto [w,p] : ans){
        printf("%d %d\n", w+1, p+1);
    }
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
