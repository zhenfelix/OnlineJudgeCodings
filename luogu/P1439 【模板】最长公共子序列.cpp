#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

const int MAXN = 1e5 + 5;
const int MAXM = 11;
const int INF = 0x7fffffff;
int n, cnt, dp[MAXN];

int binary_search(int lo, int hi, int target){
    
    while (lo<=hi) {
        int mid=(lo+hi)/2;
        if (dp[mid]<target)lo=mid+1;
        else hi=mid-1;
    }
    return lo;
}

signed main(void)
{
//    freopen("input.txt", "r", stdin);
    unordered_map<int, int> idx;
    cnt = 0;
//    vector<int> dp;
    cin >> n;
    int x;
    for (int i=0; i<n; i++) {
        scanf("%d",&x);
        idx[x] = i;
    }
    for (int i=0; i<n; i++) {
        scanf("%d",&x);
        int j = binary_search(0,cnt-1,idx[x]);
        if(j==cnt)cnt++;
        dp[j]=idx[x];
    }
    printf("%d\n",cnt);
    return 0;
}
