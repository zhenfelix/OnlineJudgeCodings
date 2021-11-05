#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int,int>;

const int maxn = 1e4+10;
char s[maxn];
int n;
ll d, c, m;



void solve(){
    for (int i = 0; i < n; i++)
        cin >> s[i];
    int j = 0;
    for (; j < n; j++){
        if (s[j] == 'D'){
            if (d <= 0)
                break;
            d -= 1;
            c += m;
        }
        else{
            if (c <= 0)
                break;
            c -= 1;
        }
    }
    for (; j < n; j++){
        if (s[j] == 'D'){
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
    return;
}

int main()
{
    // freopen("input", "r", stdin);
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++){
        cin >> n >> d >> c >> m;
        cout << "Case #" << i << ": ";
        solve();
        
        // if (flag)
        //     cout << "YES" << endl;
        // else
        //     cout << "NO" << endl;
    }
}
