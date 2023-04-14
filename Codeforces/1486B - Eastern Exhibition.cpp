
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1e9+7;

int calc(vector<int> arr) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    return arr[n/2]-arr[n/2-1]+1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input","r",stdin);
    int t, n;
    cin >> t;
    while (t--)
    {
        cin >> n;
        vector<int> xs(n), ys(n);
        for (int i = 0; i < n; i++) {
            cin >> xs[i] >> ys[i];
        }
        if (n&1) {
            cout << 1 << endl;
            continue;
        }
        cout << (ll)calc(xs)*calc(ys) << endl;
     }
    
    return 0;
}
