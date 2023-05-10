
#include <bits/stdc++.h>
using namespace std;


int main() {
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin >> n >> m;
    int ans = 0;
    for (;n < m;ans++) {
            if (m&1) m++;
            else m >>= 1;
        }
    cout << ans+n-m << endl;
    return 0;
}