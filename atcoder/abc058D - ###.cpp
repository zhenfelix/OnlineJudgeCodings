#include<bits/stdc++.h>

using namespace std;
using ll = long long;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("input","r",stdin);
    #endif
    int n, m;
    cin >> n >> m;
    ll MOD = 1e9+7;
    ll ans = 0, tot = 0, s = 0, a, b;
    for (int i = 0; i < n; i++) {
        cin >> a;
        tot = (tot+a*i-s+MOD)%MOD;
        s = (s+a)%MOD;
    }
    s = 0;
    for (int j = 0; j < m; j++) {
        cin >> b;
        ans = (ans+(b*j-s+MOD)%MOD*tot)%MOD;
        s = (s+b)%MOD;
    }
    cout << ans << endl;
    return 0;
}


#include<bits/stdc++.h>
using namespace std;

#define pb emplace_back
#define mp make_pair

using ll = long long;
using pii = pair<int,int>;

constexpr int mod = 1e9 + 7;
constexpr int inf = 0x3f3f3f3f;
constexpr int N = 2e5 + 10;

int n, m;

ll read(int n){
  ll pre = 0, ret = 0;
  ll x;
  for(int i=1; i<=n; ++i){
    cin >> x;
    ret = (ret + x * (i - 1) % mod - pre) % mod;
    if(ret < 0) ret += mod;
    pre = ((pre + x) % mod + mod) % mod;
  }
  return ret;
}

void _main(){
  cin >> n >> m;
  ll s1 = read(n);
  ll s2 = read(m);
  cout << s1 * s2 % mod << '\n';
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr); cout.tie(nullptr);
  _main();
  cout.flush();
  return 0;
}
