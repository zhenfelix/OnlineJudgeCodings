#include<iostream>
#include <algorithm>
using namespace std;
const int maxn=1010;

struct Point{
    int x,y;
}p[maxn];

bool cmp(Point a,Point b){
    if(a.y!=b.y)return a.y<b.y;
    else return a.x<b.x;
}

int main() {
//    freopen("uva1595.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    int T;scanf("%d",&T);
    while (T--) {
        int n;scanf("%d",&n);
        for(int i=0;i<n;i++)scanf("%d%d",&p[i].x,&p[i].y);
        sort(p,p+n,cmp);
        int start=0,center;
        bool flag=true,mark=true;
        while(start<n&&flag){
            int step=0;while(p[start].y==p[start+step].y)step++;
            int i=start,j=start+step-1;
            while(i<=j&&flag){
                int tmp;
                if(i==j)tmp=2*p[i].x;
                else tmp=p[i].x+p[j].x;
                if(mark)center=tmp,mark=false;
                if(!mark&&center!=tmp)flag=false;
                i++;j--;
            }
            start+=step;
        }
        if(flag)printf("YES\n");
        else printf("NO\n");
//        for(int i=0;i<n;i++)printf("%d %d\n",p[i].x,p[i].y);
    }
    return 0;
    
}

