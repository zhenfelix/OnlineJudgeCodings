
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
    vector<int> arr(2);
    cin >> arr[0] >> arr[1];
    int n, m;
    cin >> n >> m;
    vector<vector<int>> mat(n,vector<int>(m));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++) cin >> mat[i][j];
    }
    vector<bool> ignored(n,false);
    const int maxn = 1e5+10;
    vector<bool> diff(maxn,false), seen(maxn,false);
    diff[abs(arr[0]-arr[1])] = true;
    seen[arr[0]] = true;
    seen[arr[1]] = true;
    int cnt = 0;
    for (int j = 0; j < m; j++){
        for (int i = 0; i < n; i++){
            if (ignored[i]) continue;
            bool flag = false;
            if (diff[mat[i][j]])
                flag = true;
            if (seen[mat[i][j]])
                flag = false;
            if (flag) {
                arr.push_back(mat[i][j]);
                seen[mat[i][j]] = true;
                for (auto &x : arr)
                    diff[abs(x - mat[i][j])] = true;
            }
            else{
                cout << "Round #" << j+1 << ": " << i+1 << " is out.\n";
                ignored[i] = true;
                cnt++;
            }
        }
    }
    if (cnt == n) cout << "No winner.\n";
    else {
        cout << "Winner(s):";
        for (int i = 0; i < n; i++) if (!ignored[i]) cout << " " << i+1;
        cout << "\n";
    }
    return;
}



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#ifndef ONLINE_JUDGE
    freopen("contests/input", "r", stdin);
#endif
    solve();

}
