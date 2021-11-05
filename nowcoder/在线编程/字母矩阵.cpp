// 前缀和+滑动窗口
// 时间复杂度O(NMK)

// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 5e2 + 10;
const int maxk = 28;

int n, m, k;
char arr[maxn][maxn];
int prefix[maxn][maxn][maxk];
int cnt[maxk];


void solve()
{
    char dummy;
    scanf("%d%d%d", &n, &m, &k);
    getchar();
    memset(prefix, 0, maxn * maxn * maxk * sizeof(int));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            scanf("%c", &arr[i][j]);
//            cout << i << " " << j << " " << arr[i][j] << endl;
            for (int ch = 0; ch < 26; ch++){
                prefix[i+1][j+1][ch] = prefix[i+1][j][ch]+prefix[i][j+1][ch]-prefix[i][j][ch];
                prefix[i+1][j+1][ch] += (ch == arr[i][j]-'a');
            }
        }
        getchar();
    }
    int res = inf;
    for (int row = 0; row < n; row++){
        int left = 0, right = 0;
        for (; right < m; right++){
            int cc = 0;
            memset(cnt, 0, maxk*sizeof(int));
            int sz = right-left+1;
            int row2 = min(n-1, row+sz-1);
            if (row2 < row+sz-1)
                left++;
            for (int ch = 0; ch < 26; ch++){
                cnt[ch] = prefix[row2+1][right+1][ch]-prefix[row2+1][left][ch]-prefix[row][right+1][ch]+prefix[row][left][ch];
                cc += (cnt[ch] > 0);
            }
            while (cc >= k){
                res = min(res, right-left+1);
//                cout << row << " " << row2 << " " << left << " " << right << endl;
                cc = 0;
                memset(cnt, 0, maxk * sizeof(int));
                left += 1;
                sz = right-left+1;
                row2 = row+sz-1;
                for (int ch = 0; ch < 26; ch++)
                {
                    cnt[ch] = prefix[row2 + 1][right + 1][ch] - prefix[row2 + 1][left][ch] - prefix[row][right + 1][ch] + prefix[row][left][ch];
                    cc += (cnt[ch] > 0);
                }
            }
        }
    }
    res = res < inf ? res : -1;
    printf("%d\n", res);
}

int main()
{
//    freopen("input", "r", stdin);
    solve();
}
