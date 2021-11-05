// https://codeforces.com/blog/entry/81821

// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 1e5 + 10;

int t, n;
int en[maxn], rn[maxn];
ll sums[maxn];

void update(int idx, int delta){
    while (idx < maxn){
        sums[idx] += delta;
        idx += idx&(-idx);
    }
}

ll query(int idx){
    ll s = 0;
    while (idx){
       s += sums[idx];
       idx -= idx&(-idx);
    }
    return s;
}

void solve()
{
    cin >> n;
    memset(sums, 0, maxn * sizeof(ll));
    for (int i = 0; i < n; i++){
        cin >> en[i] >> rn[i];
    }

    vector<pii> er;
    ll tot = 0, res = 0;
    int cnt = 0;
    for (int i = 0; i < n; i++){
        er.push_back({en[i]+rn[i],i});
        tot += en[i];
        update(i+1, en[i]);
    }
    sort(er.begin(), er.end());
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int rm = 0; ; rm++){
        while (!er.empty() && er.back().first > tot)
        {
            auto [s, idx] = er.back();
            er.pop_back();
            pq.push(idx);
        }
        if (pq.empty())
            break;
        int idx = pq.top(); pq.pop();
        ll cur = query(idx)+query(n);
        if (cur > res){
            res = cur;
            cnt = rm;
        }
        update(idx+1, -en[idx]);
        tot -= en[idx];
    }
    if (!er.empty()){
        cout << n-er.size() << " INDEFINITELY" << endl;
        return;
    }

    cout << cnt << " " << res << endl;
    return;
}

int main()
{
    // freopen("input", "r", stdin);
    cin >> t;
    for (int i = 0; i < t; i++){
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    
}















#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
typedef long long ll;

template <typename T> void read(T &x) {
  x = 0;
  char c = getchar();
  T sig = 1;
  for (; !isdigit(c); c = getchar())
    if (c == '-')
      sig = -1;
  for (; isdigit(c); c = getchar())
    x = (x << 3) + (x << 1) + c - '0';
  x *= sig;
}

class Solution {
public:
  void solve(int case_num) {
    printf("Case #%d: ", case_num);
    int n;
    read(n);
    vector<int> e(n + 1), r(n + 1);
    priority_queue<pair<int, int>> pq;
    ll sum = 0;
    for (int i = 1; i <= n; ++i) {
      read(e[i]), read(r[i]);
      pq.push({e[i] + r[i], i});
      sum += e[i];
    }
    ll csum = sum;
    while (!pq.empty()) {
      int val = pq.top().first, i = pq.top().second;
      if (val <= csum)
        break;
      else {
        pq.pop();
        csum -= e[i];
      }
    }
    if (!pq.empty()) {
      printf("%d INDEFINITELY\n", n - (int)pq.size());
      return;
    }
    ll max_val = csum = sum, min_del = 0, cdel = 0, cval = sum;
    for (int i = 1; i <= n; ++i) {
      if (e[i] + r[i] <= csum) {
        cval += e[i];
        pq.push({e[i] + r[i], i});
        if (cval > max_val) {
          max_val = cval;
          min_del = cdel;
        }
      } else {
        csum -= e[i];
        cval -= e[i];
        cdel++;
        while (!pq.empty() && pq.top().first > csum) {
          int val = pq.top().first, j = pq.top().second;
          pq.pop();
          csum -= e[j];
          cval -= 2 * e[j];
          cdel++;
        }
      }
    }
    printf("%lld %lld\n", min_del, max_val);
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  read(t);
  for (int i = 1; i <= t; ++i) {
    Solution solution = Solution();
    solution.solve(i);
  }
}


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/article/M1wbLj/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。