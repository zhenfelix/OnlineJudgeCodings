#define LOCAL
#define _USE_MATH_DEFINES
#include <array>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <complex>
#include <cmath>
#include <numeric>
#include <bitset>
#include <functional>
#include <random>
#include <ctime>

using namespace std;

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}
template <typename T, size_t N>
ostream& operator <<(ostream& out, const array<T, N>& a) {
  out << "["; bool first = true;
  for (auto& v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "]";
  return out;
}
template <typename T>
ostream& operator <<(ostream& out, const vector<T>& a) {
  out << "["; bool first = true;
  for (auto v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "]";
  return out;
}
template <typename T, class Cmp>
ostream& operator <<(ostream& out, const set<T, Cmp>& a) {
  out << "{"; bool first = true;
  for (auto& v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "}";
  return out;
}
template <typename T, class Cmp>
ostream& operator <<(ostream& out, const multiset<T, Cmp>& a) {
  out << "{"; bool first = true;
  for (auto& v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "}";
  return out;
}
template <typename U, typename T, class Cmp>
ostream& operator <<(ostream& out, const map<U, T, Cmp>& a) {
  out << "{"; bool first = true;
  for (auto& p : a) { out << (first ? "" : ", "); out << p.first << ":" << p.second; first = 0;} out << "}";
  return out;
}
#ifdef LOCAL
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
#else
#define trace(...) 42
#endif
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << ": " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << ": " << arg1 << " |";
  __f(comma + 1, args...);
}

template <class T> auto vect(const T& v, int n) { return vector<T>(n, v); }
template <class T, class... D> auto vect(const T& v, int n, D... m) {
  return vector<decltype(vect(v, m...))>(n, vect(v, m...));
}

using int64 = long long;
using int128 = __int128_t;
using ii = pair<int, int>;
#define SZ(x) (int)((x).size())
template <typename T> static constexpr T inf = numeric_limits<T>::max() / 2;
const int MOD = 1e9 + 7;
// const int MOD = 998244353;
mt19937_64 mrand(random_device{}());
int64 rnd(int64 x) { return mrand() % x; }
constexpr inline int lg2(int64 x) { return x == 0 ? -1 : sizeof(int64) * 8 - 1 - __builtin_clzll(x); }
constexpr inline int64 p2ceil(int64 x) { return 1LL << (lg2(x - 1) + 1); }
template <class T> void out(const vector<T>& a) { for (int i = 0; i < SZ(a); ++i) cout << a[i] << " \n"[i + 1 == SZ(a)]; }
template <class T> bool ckmin(T& a, const T& b) { return b < a ? a = b, 1 : 0; }
template <class T> bool ckmax(T& a, const T& b) { return a < b ? a = b, 1 : 0; }
template <class T> void dedup(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()), v.end()); }
inline void add_mod(int& x, int y) { x += y; if (x >= MOD) x -= MOD; }
inline void sub_mod(int& x, int y) { x += MOD - y; if (x >= MOD) x -= MOD; }
inline int mod(int x) { return x >= MOD ? x - MOD : x; }

struct fast_ios {
  fast_ios() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(10);
  };
} fast_ios_;

class Solution {
public:
    int stringCount(int n) {
        auto dp = vect<int>(-1, n, 3, 2, 2);
        function<int(int, int, int, int)> solve =
            [&](int pos, int cntA, int cntB, int cntC) {
            if (pos == n) return cntA == 2 && cntB == 1 && cntC == 1 ? 1 : 0;
            int& ret = dp[pos][cntA][cntB][cntC];
            if (ret >= 0) return ret;
            ret = 0;
            add_mod(ret, solve(pos + 1, min(2, cntA + 1), cntB, cntC));
            add_mod(ret, solve(pos + 1, cntA, 1, cntC));
            add_mod(ret, solve(pos + 1, cntA, cntB, 1));
            add_mod(ret, solve(pos + 1, cntA, cntB, cntC) * 23LL % MOD);
            return ret;
        };
        int ret = solve(0, 0, 0, 0);
        return ret;
    }
};




class Solution {
public:
    #define o int(1e9 + 7)
    void inc(int &x, int y) {
        if ((x += y) >= o) x -= o;
    }
    int stringCount(int n) {
        vector<vector<vector<vector<int>>>> dp(n + 1, vector<vector<vector<int>>>(2, vector<vector<int>>(2, vector<int>(3))));
        dp[0][0][0][0] = 1;
        for (int i = 0; i < n; ++i) {
            for (int x = 0; x < 2; ++x) {
                for (int y = 0; y < 2; ++y) {
                    for (int z = 0; z < 3; ++z) {
                        inc(dp[i + 1][min(x + 1, 1)][y][z], dp[i][x][y][z]);
                        inc(dp[i + 1][x][min(y + 1, 1)][z], dp[i][x][y][z]);
                        inc(dp[i + 1][x][y][min(z + 1, 2)], dp[i][x][y][z]);
                        inc(dp[i + 1][x][y][z], dp[i][x][y][z] * 23ll % o);
                    }
                }
            }
        }
        return dp[n][1][1][2];
    }
};
