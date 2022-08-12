//Fenwick tree solution
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

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 20;

int t, n, m, x, y, c, q, _clock, k, l;

int cnt[maxn], arr[maxn];
ll A[maxn], B[maxn];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

void update(int pos, int delta, ll ax[]){
    while (pos < maxn){
        ax[pos] += delta;
        pos += pos&(-pos);
    }
}

int query(int pos, ll ax[]){
    int sums = 0;
    while (pos){
        sums += ax[pos];
        pos -= pos&(-pos);
    }
    return sums;
}

void update_range(int lo, int hi, int delta){
    update(lo, delta, A); update(lo, delta*lo, B);
    update(hi+1, -delta, A); update(hi+1, -delta*(hi+1), B);
}

int query_range(int lo, int hi){
    ll sums = 0;
    sums += (hi+1)*query(hi, A)-query(hi, B);
    sums -= lo*query(lo-1,A)-query(lo-1,B);
    return sums;
}

int find_continuous(int pos, int val){
    if (val == 1){
        ll lo = pos, hi = maxn-1;
        while (lo <= hi){
            ll mid = (lo+hi)/2;
            if (query_range(pos,mid) < mid-pos+1) hi = mid-1;
            else lo = mid+1;
        }
        return hi-pos+1;
    }
    else{
        ll lo = pos, hi = maxn-1;
        while (lo <= hi){
            ll mid = (lo+hi)/2;
            if (query_range(pos,mid) > 0) hi = mid-1;
            else lo = mid+1;
        }
        return hi - pos + 1;
    }
}

void update_bit(int pos, int delta){
    if (delta == 1){
        int sz = find_continuous(pos,1);
        if (sz > 0)
            update_range(pos, pos + sz-1, -1);
        update_range(pos + sz, pos + sz, 1);
    }
    else{
        int sz = find_continuous(pos, 0);
        if (sz > 0)
            update_range(pos, pos + sz - 1, 1);
        update_range(pos + sz, pos + sz, -1);
    }
}


int solve()
{
    scanf("%d%d\n", &k, &l);
    int p = arr[k]; arr[k] = l;
    update_bit(p,-1); update_bit(l,1);
    ll lo = 1, hi = maxn-1;
    int tot = query_range(1,maxn-1);
    // cout << tot << endl;
    while (lo <= hi){
        ll mid = (lo+hi)/2;
        int tmp = query_range(1,mid);
        if (tmp < tot) lo = mid+1;
        else hi = mid-1;
    }
    return lo;
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d%d\n", &n, &q);
    for (int i = 1; i <= n; i++){
        scanf("%d", &x);
        cnt[x]++;
        arr[i] = x;
    }
    memset(A, 0, maxn*sizeof(ll));
    memset(B, 0, maxn*sizeof(ll));
    // cout << query_range(1, maxn - 1) << endl;
    for (int i = 1, cur = 0; i < maxn; i++){
        cur += cnt[i];
        if (cur&1){
            update_range(i,i,1);
        }
        cur >>= 1;
    }
    // cout << query_range(1,maxn-1) << endl;
    for(int i = 0; i < q; i++){
        printf("%d\n", solve());
    }

}



//binary search on segment tree

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

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 20;

int t, n, m, x, y, c, q, _clock, k, pre, cur, last;
int tree[maxn*4], lazy[maxn*4], arr[maxn], cnt[maxn];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

void init(ll idx, ll lo, ll hi){
    if (lo == hi){
        tree[idx] = cnt[lo];
        return;
    }
    ll mid = (lo+hi)/2;
    init(idx*2, lo, mid);
    init(idx*2+1, mid+1, hi);
    tree[idx] = tree[idx*2] + tree[idx*2+1];
    return;
}

void push_down(ll idx, ll lo, ll hi){
    if (lazy[idx] != 0){
        tree[idx] += lazy[idx]*(hi-lo+1);
        if (lo < hi){
            lazy[idx*2] += lazy[idx];
            lazy[idx*2+1] += lazy[idx];
        }
        lazy[idx] = 0;
    }
}

ll query(ll idx, ll lo, ll hi, ll l, ll r){
    push_down(idx, lo, hi);
    if (hi < l || lo > r) return 0;
    if (l <= lo && r >= hi) return tree[idx];
    ll mid = (lo+hi)/2;
    ll sums = 0;
    sums += query(idx*2, lo, mid, l, r);
    sums += query(idx*2+1, mid+1, hi, l, r);
    return sums;
}

void update(ll idx, ll lo, ll hi, ll l, ll r, int delta)
{
    push_down(idx, lo, hi);
    if (hi < l || lo > r)
        return;
    if (l <= lo && r >= hi){
        lazy[idx] += delta;
        push_down(idx, lo, hi);
        return;
    }
    ll mid = (lo + hi) / 2;
    update(idx * 2, lo, mid, l, r, delta);
    update(idx * 2 + 1, mid + 1, hi, l, r, delta);
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
    return;
}

ll bs(ll idx, ll lo, ll hi, ll target){
    if (lo == hi) return lo;
    ll mid = (lo+hi)/2;
    push_down(idx*2, lo, mid);
    push_down(idx*2+1, mid+1, hi);
    if (tree[idx*2] < target){
        return bs(idx*2+1, mid+1, hi, target-tree[idx*2]);
    }
    else{
        return bs(idx*2, lo, mid, target);
    }
}

ll bs(ll idx, ll lo, ll hi, ll target, ll sums, ll pos, int continuous)
{
    if (lo == hi)
        return lo;
    ll mid = (lo + hi) / 2;
    push_down(idx * 2, lo, mid);
    push_down(idx * 2 + 1, mid + 1, hi);
    if (mid < pos || tree[idx*2]+sums == target+(mid-pos+1)*continuous)
    {
        return bs(idx * 2 + 1, mid + 1, hi, target, sums+tree[idx * 2], pos, continuous);
    }
    else
    {
        return bs(idx * 2, lo, mid, target, sums, pos, continuous);
    }
}



void simulate(int pos, int delta){
    ll target = query(1, 1, maxn-1, 0, pos-1);
    if (delta == 1){
        ll reach = bs(1, 1, maxn-1, target, 0, pos, 1);
        if (reach > pos) update(1, 1, maxn-1, pos, reach-1, -1);
        update(1, 1, maxn-1, reach, reach, 1);
    }
    else{
        ll reach = bs(1, 1, maxn-1, target, 0, pos, 0);
        if (reach > pos) update(1, 1, maxn-1, pos, reach-1, 1);
        update(1, 1, maxn-1, reach, reach, -1);
    }
}

void debug_tree()
{
    printf("tree bit: ");
    for (int i = 0; i <= 10; i++)
    {
        printf("%lld ", query(1, 1, maxn - 1, i, i));
    }
    printf("\n");
}

void debug_cnt()
{
    printf("cnt: ");
    for (int i = 0; i <= 10; i++)
    {
        printf("%d ", cnt[i]);
    }
    printf("\n");
}

void solve()
{
    scanf("%d%d", &k, &x);
    y = arr[k]; arr[k] = x;
    simulate(y,-1);
    simulate(x,1);
    int tot = query(1,1,maxn-1,1,maxn-1);
    int ans = bs(1,1,maxn-1,tot);
    // debug_tree();
    printf("%d\n", ans);
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d%d\n", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &arr[i]);
        cnt[arr[i]]++;
    }
    ll plus = 0;
    for (int i = 1; i < maxn; i++){
        plus += cnt[i];
        cnt[i] = (plus&1);
        plus >>= 1;
    }
    // debug_cnt();
    init(1, 1, maxn-1);
    // debug_tree();
    for (int i = 0; i < q; i++){
        solve();
    }
}


// segment tree solution
#include <bits/stdc++.h>
using namespace std;

struct LazySeg
{
  int l, r;
  int val = 0, tag = 0;
  bool is_lazy = false;
  LazySeg *l_child = NULL, *r_child = NULL;

  LazySeg(int _l, int _r)
  {
    l = _l;
    r = _r;
    if (r - l > 1)
    {
      int m = (l + r) / 2;
      l_child = new LazySeg(l, m);
      r_child = new LazySeg(m, r);
    }
  }
  ~LazySeg()
  {
    delete l_child;
    delete r_child;
  }
  void unlazy()
  {
    if (!is_lazy)
      return;
    val = (r - l) * tag;
    if (r - l <= 1)
      return;
    l_child->tag = tag;
    l_child->is_lazy = true;
    r_child->tag = tag;
    r_child->is_lazy = true;
    tag = 0;
    is_lazy = false;
  }
  void update(int from, int to, int x)
  {
    unlazy();
    if (from >= r || l >= to)
      return;
    if (from <= l && to >= r)
    {
      tag = x;
      is_lazy = true;
      unlazy();
    }
    else
    {
      l_child->update(from, to, x);
      r_child->update(from, to, x);
      val = l_child->val + r_child->val;
    }
  }
  int query(int from, int to)
  {
    if (from >= r || l >= to)
      return 0;
    unlazy();
    if (from <= l && to >= r)
      return val;
    else
    {
      if (l_child == NULL)
        return 0;
      return l_child->query(from, to) + r_child->query(from, to);
    }
  }
  //pre = prefix in [l,k)
  int max_right(int k, int pre, int v)
  {
    unlazy();
    if (r - l == 1)
    {
      if (val == v)
        return l;
      else
        return l - 1;
    }
    l_child->unlazy();
    int mid = (l + r) / 2;
    if (mid <= k)
    {
      return r_child->max_right(k, pre - l_child->val, v);
    }
    else if (l_child->val - pre == v * (mid - k))
    {
      //left to mid-1 has all 1's => answer must be >= mid-1
      return r_child->max_right(mid, 0, v);
    }
    else
    {
      return l_child->max_right(k, pre, v);
    }
  }
  //suff = suffix
  int get_answer()
  {
    unlazy();
    if (r - l == 1)
    {
      return l;
    }
    r_child->unlazy();
    if (r_child->val == 0)
    {
      //[mid to end] are all 0
      return l_child->get_answer();
    }
    else
    {
      return r_child->get_answer();
    }
  }
};

signed main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, q;
  cin >> n >> q;
  LazySeg tr(0, 200100);

  auto add = [&](int x)
  {
    int y = tr.max_right(x, tr.query(0, x), 1) + 1;
    if (y == x)
    { //no carry; just change 0 to 1
      tr.update(x, x + 1, 1);
    }
    else
    { //there is a carry; set the whole block of 1's to 0
      tr.update(x, y, 0);
      tr.update(y, y + 1, 1);
    }
  };

  auto remove = [&](int x)
  {
    int y = tr.max_right(x, tr.query(0, x), 0) + 1;
    if (y == x)
    {
      tr.update(x, x + 1, 0);
    }
    else
    {
      tr.update(x, y, 1);
      tr.update(y, y + 1, 0);
    }
  };
  vector<int> a(n);
  for (int i = 0; i < n; ++i)
  {
    cin >> a[i];
    add(a[i]);
  }
  while (q--)
  {
    int k, l;
    cin >> k >> l;
    k--;
    remove(a[k]);
    add(l);
    a[k] = l;
    cout << tr.get_answer() << "\n";
  }
}










//bit set solution
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

// Super Idol的笑容
//    都没你的甜
//  八月正午的阳光
//    都没你耀眼
//  热爱105°C的你
// 滴滴清纯的蒸馏水

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ii pair<ll, ll>
#define iii pair<ii, ll>
#define fi first
#define se second
#define endl '\n'
#define debug(x) cout << #x << ": " << x << endl

#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define lb lower_bound
#define ub upper_bound

#define rep(x, start, end) for (int x = (start) - ((start) > (end)); x != (end) - ((start) > (end)); ((start) < (end) ? x++ : x--))
#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()

mt19937 rng(chrono::system_clock::now().time_since_epoch().count());

struct bitset
{
  unsigned long long arr[3130] = {};
  unsigned long long AF = -1ull;

  void flip(int l, int r)
  {
    arr[l / 64] ^= (1ull << (l % 64)) - 1;
    if (r % 64 == 63)
      arr[r / 64] ^= AF;
    else
      arr[r / 64] ^= (1ull << (r % 64 + 1)) - 1;
    l /= 64, r /= 64;
    if (l == r)
      return;
    arr[l] ^= AF;

    for (int x = l + 1; x < r; x++)
      arr[x] ^= AF;
  }

  int get(int i)
  {
    if (arr[i / 64] & (1ull << (i % 64)))
      return 1;
    else
      return 0;
  }

  int get1(int i)
  {
    //search [i%64,64) on i/64 first
    unsigned long long mask = AF ^ ((1ull << (i % 64)) - 1);

    i = i / 64;
    unsigned long long temp = arr[i] & mask;
    if (temp)
      return i * 64 + __builtin_ctzll(temp);
    i++;
    while (true)
    {
      if (arr[i] == 0)
        i++;
      else
        return i * 64 + __builtin_ctzll(arr[i]);
    }
  }

  int get0(int i)
  {
    //search [i%64,64) on i/64 first
    unsigned long long mask = AF ^ ((1ull << (i % 64)) - 1);

    i = i / 64;
    unsigned long long temp = (arr[i] ^ AF) & mask;
    if (temp)
      return i * 64 + __builtin_ctzll(temp);
    i++;
    while (true)
    {
      if (arr[i] == AF)
        i++;
      else
        return i * 64 + __builtin_ctzll(arr[i] ^ AF);
    }
  }

  int gethigh()
  {
    int i = 3129;
    while (true)
    {
      if (arr[i] == 0)
        i--;
      else
        return i * 64 + 63 - __builtin_clzll(arr[i]);
    }
  }
} BS;

int n, q;
int arr[200005];

void add(int i)
{
  BS.flip(i, BS.get0(i));
}

void del(int i)
{
  BS.flip(i, BS.get1(i));
}

signed main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin.exceptions(ios::badbit | ios::failbit);

  cin >> n >> q;
  rep(x, 1, n + 1) cin >> arr[x];
  rep(x, 1, n + 1) add(arr[x]);

  int a, b;
  while (q--)
  {
    cin >> a >> b;
    del(arr[a]);
    arr[a] = b;
    add(arr[a]);

    cout << BS.gethigh() << endl;
  }
}