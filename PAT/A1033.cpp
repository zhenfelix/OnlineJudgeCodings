#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 510;
const int INF = 1000000000;

struct station {
    double price, dis; //价格、与起点的距离 }st [maxn];
}st[maxn];

bool cmp(station a, station b) {
    return a.dis < b.dis; //按距离从小到大排序
}

int main(){
    int n;
    double cmax, d, davg;
//    freopen("input.txt", "r", stdin);
    scanf("%lf%lf%lf%d", &cmax, &d, &davg, &n);
    for(int i=0;i<n;i++){
        scanf("%lf%lf", &st[i].price, &st[i].dis);
    }
    st[n].price=0;
    st[n].dis=d;
    sort(st,st+n,cmp);
    
    if(st[0].dis!=0){
        printf("The maximum travel distance = 0.00\n");
    }
    else{
        int now=0;
        double ans=0, nowTank=0, MAX=cmax*davg;
        while(now < n){
            
            int k=-1;
            double minPrice=INF;
            for(int i=now+1; i<=n && st[now].dis+MAX>=st[i].dis; i++){
                
                if(st[i].price < minPrice){
                    k=i;
                    minPrice=st[i].price;
                }
//                printf("%d %lf\n",i,minPrice);
                if(minPrice < st[now].price)break;
            }
            
            if(k==-1)break;
            double needed = (st[k].dis - st[now].dis)/davg;
//            printf("%d\n", k);
//            printf("%d %lf %lf\n",now, needed*davg, nowTank*davg);
            if(minPrice < st[now].price){
                ans += (needed-nowTank)*st[now].price;
                nowTank = 0;
//                if(needed>nowTank){
//                    ans += (needed-nowTank)*st[now].price;
//                    nowTank = 0;
//                }
//                else{
//                    nowTank -= needed;
//                }
                
                
            }
            else{
                ans += (cmax-nowTank)*st[now].price;
                nowTank = cmax-needed;
            }
            
            now = k;
        }
        if(now == n){
            printf("%.2f\n", ans);
        }
        else{
            printf("The maximum travel distance = %.2f\n", st[now].dis+MAX);
        }
    }
    return 0;
    
}
