
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
    int n, m, k, a, b;
    cin >> n >> m >> k;
    vector<vector<int>> mat(n,vector<int>(n, false));
    for (int i = 0; i < m; i++){
        cin >> a >> b;
        mat[a-1][b-1] = true;
        mat[b-1][a-1] = true;
    }
    int r;
    cin >> r;
    for (int i = 0; i < r; i++){
        unordered_set<int> seen;
        vector<int> color(n);
        for (int j = 0; j < n; j++){
            cin >> color[j];
            seen.insert(color[j]);
        }
        if (seen.size() != k){
            if (seen.size() < k) cout << "Error: Too few species.\n";
            else cout << "Error: Too many species.\n";
        }
        else{
            bool flag = true;
            for (int p = 0; p < n; p++){
                for (int q = p+1; q < n; q++){
                    if (mat[p][q] && color[p] == color[q]){
                        flag = false;
                        break;
                    }
                }
                if (!flag) break;
            }
            if (flag) cout << "Yes\n";
            else cout << "No\n";
        }
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
