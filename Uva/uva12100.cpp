#include<iostream>
#include <queue>
using namespace std;
const int maxn=10;
int p[maxn]={0};
queue<int>Q;

int main() {
//    freopen("uva12100.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    int kase;scanf("%d",&kase);
    while(kase--){
        for(int i=1;i<10;i++)p[i]=0;
        while (!Q.empty())Q.pop();
        int n,m,id,ans=0;
        bool flag=false;
        scanf("%d%d",&n,&m);
        id=m;
        for(int i=0;i<n;i++){
            int x;scanf("%d",&x);
            p[x]++;
            Q.push(x);
        }
        for(int i=9;i>0;i--){
            while(p[i]&&!flag){
                int tmp=Q.front();
                if(tmp<i){
                    Q.pop();
                    Q.push(tmp);
                }
                else{
                    Q.pop();ans++;p[tmp]--;
                    if(id==0)flag=true;
                }
                id--;
                if(id<0)id+=Q.size();
            }
            if(flag)break;
        }
        printf("%d\n",ans);
    }
    return 0;
    
}

