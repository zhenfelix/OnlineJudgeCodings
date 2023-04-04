#include <iostream>
#include <algorithm>

using namespace std;

const int N = 18 + 2;
int a[N], sum[N]; //a 小猫重量 sum 车现载重
int n, w;
int res;

void dfs(int u, int cnt) //u 当前第几只猫，cnt当前车的数量
{
    if (cnt >= res)
        return; //如果车的数量大于现实存在的猫咪的个数，或者历史最优的数值，返回
    if (u > n - 1)
    {
        res = cnt;
        return;
    } //如果考虑完了n只即所有猫咪，则更新答案

    for (int i = 0; i < cnt; i++)
        if (sum[i] + a[u] <= w) //检查现有的所有车的重量，是否能放猫
        {
            sum[i] += a[u];
            dfs(u + 1, cnt);
            sum[i] -= a[u];
        }

    sum[cnt] = a[u]; //新增一辆车，初始重量是当前猫的重量
    dfs(u + 1, cnt + 1);
    sum[cnt] = 0;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("contests/input", "r", stdin);
#endif
    cin >> n >> w;

    res = n;

    for (int i = 0; i < n; i++)
        cin >> a[i];

    // sort(a, a + n, [](int a, int b)
    //      { return a > b; }); //反序排序 优化了搜索顺序 lambda表达式
    sort(a, a + n, greater{});

    dfs(0, 0);

    cout << res;

    return 0;
}



#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int n, w[19], f[20][1<<18], W;
int main(){
    memset(f, 0x3f, sizeof f);
    scanf("%d%d", &n, &W);
    for(int i=1; i<=n; i++){
        scanf("%d", &w[i]);
        f[1][1<<(i-1)]=w[i];
    }
    f[1][0]=0;
    for(int i=1; i<=n; i++){ //枚举车 
        for(int j=0; j<(1<<n); j++){ //枚举状态
            if(f[i][j]!=0x3f3f3f3f){//如果这辆车被更新过 才能用来更新其他的
                for(int k=1; k<=n; k++){//枚举猫   
                    if( W-f[i][j]>=w[k] && (j&(1<<(k-1)))==0 )//如果能装下就装 
                        f[i][j|(1<<(k-1))]=min(f[i][j|(1<<(k-1))],f[i][j]+w[k]);//使已用体积最小 
                    else f[i+1][j|(1<<(k-1))]=min(f[i+1][j|(1<<(k-1))],w[k]);//如果装不下就再开一辆车 
                } 
            }
        }
        if(f[i][(1<<n)-1]!=0x3f3f3f3f){ 
        //由于i从前往后循环，第一次所有猫都装下时，则为最少需要用车的数量 
            printf("%d\n",i);
            return 0;
        }
    }
    return 0;
}

// 作者：wwwxkxk
// 链接：https://www.acwing.com/solution/AcWing/content/2755/
// 来源：AcWing
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。