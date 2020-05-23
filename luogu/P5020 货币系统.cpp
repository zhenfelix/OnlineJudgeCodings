#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
//#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define N 110
#define M 25010
int t,n;
int arr[N], dp[M];
int main(){
//    freopen("input.txt", "r", stdin);
    scanf("%d",&t);
//    scanf("%d %d %d",&n,&m,&q);
    while (t--) {
        memset(dp,0,sizeof(dp));
        dp[0]=1;
        scanf("%d",&n);
        for (int i=0; i<n; i++)scanf("%d",&arr[i]);
        sort(arr,arr+n);
        int res = n;
        for (int i=0; i<n; i++) {
            if (dp[arr[i]])res--;
            else{
                for (int j=arr[i]; j<=arr[n-1]; j++) {
                    dp[j] |= dp[j-arr[i]];
                }
            }
        }
        printf("%d\n",res);
        
    }
   
    return 0;
}
