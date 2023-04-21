#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        int n,k;
        cin >> n >> k;
        vector<int> arr(n), brr(k);
        for (int i = 0; i < n; i++) cin >> arr[i];
        for (int i = 0; i < k; i++) cin >> brr[i];
        sort(arr.begin(), arr.end(), greater{});
        sort(brr.begin(), brr.end());
        ll ans = 0;
        for (int i = 0; i < k; i++) {
            ans += arr[i];
        }
        int j = k-1;
        for (int i = 0; i < k; i++) {
            if (brr[i] == 1) ans += arr[i];
            else {
                j += brr[i]-1;
                ans += arr[j];
            }
        }
        cout << ans << endl;
    }
}