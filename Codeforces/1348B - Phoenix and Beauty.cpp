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
        int n,k;
        cin >> n >> k;
        unordered_map<int,int> mp;
        vector<int> arr(n),base,ans;
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            if (!mp.count(arr[i])){
                mp[arr[i]] = base.size();
                base.push_back(arr[i]);
            }
        }
        while (base.size() < k)     
        {
            base.push_back(1);
        }
        
        if (base.size() > k) {
            cout << -1 << endl;
            continue;
        }
        for (int i = 0; i < n; i++){
            while (base[ans.size()%k] != arr[i])
            {
                ans.push_back(base[ans.size()%k]);
            }
            ans.push_back(arr[i]);
        }
        int m = ans.size();
        cout << m << endl;
        for (int i = 0; i < m; i++){
            cout << ans[i];
            if (i < m-1) cout << " ";
            else cout << endl;
        }
        
    }
    
    return 0;
}