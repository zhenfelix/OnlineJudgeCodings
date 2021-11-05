#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;
using pii = pair<int,int>;

const int maxn = 3e5+10;
const int maxm = 10;

int arr[maxn][maxm];
int mp[1<<maxm];
int n, m, x, y;

bool check(int mx){
    memset(mp, -1, sizeof(int)*(1<<m));
    for (int i = 0; i < n; i++){
        int a = 0;
        for (int j = 0; j < m; j++){
            a = (a<<1)|(arr[i][j]>=mx);
        }
        mp[a] = i;
    }
    for (int i = 0; i < (1<<m); i++){
        for (int j = 0; j < (1<<m); j++){
            if (mp[i]>=0 && mp[j]>=0 && (i|j) == (1<<m)-1){
                x = mp[i];
                y = mp[j];
                return true;
            }
                
        }
    }
    return false;
}


void solve(){
    int lo = 0, hi = 1e9;
    while (lo <= hi){
        int mid = (lo+hi)/2;
        if (check(mid))
            lo = mid + 1;
        else
            hi = mid - 1;
    }
    check(hi);
    cout << x+1 << " " << y+1 << endl;
    // cout << hi << endl;
}

int main()
{
    // freopen("input", "r", stdin);
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
    solve();
}
