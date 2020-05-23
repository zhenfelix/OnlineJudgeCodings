#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
#define N 7010
ll cost[N],f[N][N],q[N],n,t;
int main(){
//    freopen("input.txt", "r", stdin);
    scanf("%d",&t);
    while(t--){
        scanf("%lld",&n);
        for(int i=1;i<=n;++i)
            scanf("%lld",&cost[i]);
        for(int j=1;j<=n;++j){
            int k, left, right;
            k = j-1, left = n, right = n-1;
            for(int i=j-1;i>=1;i--){
                while (k>=i && f[i][k]>=f[k+1][j])k--;
                k++;
                while (right>=left && q[right]>=k)right--;
                if (i<=k) {
                    while (right>=left && f[q[left]+1][j]+cost[q[left]]>=f[i+1][j]+cost[i])left++;
                    q[--left]=i;
                }
                f[i][j]=f[i][k]+cost[k];
                if(right>=left){
                    f[i][j]=min(f[i][j],f[q[right]+1][j]+cost[q[right]]);
                }
        }
        
    }
        printf("%lld\n", f[1][n]);
    }
    return 0;
}
