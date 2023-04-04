
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
    string s;
    cin >> s;
    bool flag = true;
    int n = s.size();
    auto check = [&] (int x) -> bool{
        if (x < 2) return false;
        for (int i = 2; i*i <= x; i++){
            if (x%i == 0) return false;
        }
        return true;
    };
    for (int start = 0; start < n; start++){
        int v = 0;
        for (int i = start; i < n; i++){
            v = v*10+s[i]-'0';
        }
        cout << s.substr(start) << " ";
        if (check(v)){
            cout << "Yes\n";
        }
        else{
            cout << "No\n";
            flag = false;
        }
    }
    if (flag) cout << "All Prime!\n";
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
