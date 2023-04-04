#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        vector<int> lessthan(n,0);
        for (int i = 0; i < n; i++){
            for (int j = i+1; j < n; j++)
            if (arr[j] < arr[i]) lessthan[i]++;
        }
        ll ans = 0;
        for (int c = 0; c < n; c++){
            ll s = 0;
            for (int a = c-1; a >= 0; a--){
                if (arr[a] < arr[c]) ans += s;
                if (arr[c] < arr[a]) lessthan[a]--;
                s += lessthan[a];
            }
        }
        cout << ans << endl;
    }
    
    return 0;
}