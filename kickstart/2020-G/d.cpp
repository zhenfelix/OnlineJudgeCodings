#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

typedef long long ll;
#define MAXN 5000

double dfs(int i, int j, vector<vector<double>> &memo, vector<ll> &presum)
{
    // printf("%d %d\n",i,j);
    if (memo[i][j]>=0)return memo[i][j];
    if (i>=j)return 0;
    
    double res = 0;
    for (int k = i; k < j; k++)
    {
        res += (dfs(i,k,memo,presum)+dfs(k+1,j,memo,presum)+presum[j+1]-presum[i])/(j-i);
    }
    memo[i][j] = res;
    return res;
}

// double solve(vector<int> &arr, int n)
// {
//  vector<vector<double>> memo(MAXN, vector<double>(MAXN,-1));
//  // for(int i=0;i<n;i++)for(int j=0;j<n;j++)printf("%.8f ",memo[i][j]);
//  vector<ll> presum(MAXN,0);
//  for (int i = 0; i < n; i++) presum[i + 1] = presum[i] + arr[i];
//  // printf("%d\n",n);
//  // for (int i = 0; i < n; i++)printf("%d ", arr[i]);
//  // printf("\n");
//  // for (int i = 0; i <= n; i++)printf("%lld ", presum[i]);
//  return dfs(0, n - 1, memo, presum);
//  // return 0;
// }

double solve(vector<int> &arr, int n)
{
    double res = 0;
    for (int mid = 0; mid < n-1; mid++)
    {
        for (int i = 0; i <= mid; i++)res += arr[i] / (double)(mid - i + 1);
        for (int i = mid+1; i < n; i++)res += arr[i] / (double)(i-mid);
    }
    return res;
}

int main()
{
//  freopen("input.txt","r",stdin);
    int T, N;
    scanf("%d", &T);
    vector<int> a(MAXN,0);
    for (int i = 1; i <= T; i++)
    {
        scanf("%d",&N);
        for (int j = 0; j < N; j++)
            scanf("%d", &a[j]);
        double res = solve(a,N);
        printf("Case #%d: %.8f\n", i, res);
    }
    return 0;
}