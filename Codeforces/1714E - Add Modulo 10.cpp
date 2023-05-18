
#include <bits/stdc++.h>
using namespace std;


int main() {
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n, a, state = 0;
        cin >> n;
        set<int> cc;
        vector<int> mask(10,0);
        mask[3] = mask[6] = mask[7] = mask[9] = 1;
        for (int i = 0; i < n; i++) {
            cin >> a;
            if (a%10 == 0 || a%10 == 5) {
                state |= 1;
                if (a%10 == 5) a += 5;
                cc.insert(a);
            }
            else {
                state |= 2;
                cc.insert(((a/10)%2)^mask[a%10]);
            }
        }
        if (state == 3 || cc.size() > 1) cout << "No\n";
        else cout << "Yes\n";

    }
    return 0;
}


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
    int N;
    cin >> N;
    vector<int> A(N);

    for (auto &a : A)
        cin >> a;

    bool has5 = false;

    for (auto &a : A)
        has5 = has5 || a % 5 == 0;

    if (has5) {
        for (auto &a : A)
            if (a % 10 == 5)
                a += 5;

        if (all_of(A.begin(), A.end(), [&](int a) { return a == A.front(); })) {
            cout << "YES" << '\n';
            return;
        }

        cout << "NO" << '\n';
        return;
    }

    for (auto &a : A)
        while (a % 10 != 2)
            a += a % 10;

    for (auto &a : A)
        a %= 20;

    if (all_of(A.begin(), A.end(), [&](int a) { return a == A.front(); })) {
        cout << "YES" << '\n';
        return;
    }

    cout << "NO" << '\n';
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




#include <bits/stdc++.h>
// #include <vector>
// #include <set>
// #include <map>
// #include <algorithm>
// #include <climits>
// #include <iostream>
// #include <unordered_map>
// #include <cstring>
// #include <queue>

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

bool solve()
{
    scanf("%d", &n);
    unordered_map<int,unordered_set<int>> mp;
    vector<vector<bool>> flag(10, vector<bool>(2, false));
    vector<bool> cycle(2,false);
    for (int i = 0; i < n; i++){
        scanf("%d", &x);
        int r = x%10;
        x /= 10;
        if (r == 0 || r == 5){
            mp[r].insert(x);
            cycle[0] = true;
        }
        else{
            flag[r][x&1] = true;
            cycle[1] = true;
        }
    }
    if ((cycle[0]&cycle[1])|| mp[0].size() > 1 || mp[5].size() > 1) return false;
    if (!mp[0].empty() && !mp[5].empty()){
        x = *mp[0].begin();
        y = *mp[5].begin();
        if (x != y+1) return false;
    }
    vector<set<int>> candidates(2);
    map<int,int> v2odd = {{1,0},{7,1},{9,1},{3,1},{2,0},{4,0},{8,0},{6,1}};
    for (int i = 1; i < 10; i++){
        if (flag[i][0]&flag[i][1]) return false;
        for (int j = 0; j < 2; j++) if (flag[i][j]) {
            candidates[j].insert(v2odd[i]);
            if (candidates[j].size() > 1) return false;
        }
    }
    if (!candidates[0].empty() && !candidates[1].empty()){
        x = *candidates[0].begin();
        y = *candidates[1].begin();
        if (x == y) return false;
    }

    return true;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
        if (solve()) printf("YES\n");
        else printf("NO\n");
    }

}
