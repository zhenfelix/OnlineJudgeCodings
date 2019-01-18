#include <bits/stdc++.h>
using namespace std;
const int maxn = 50000 + 10;
int cnt[maxn],vis[maxn],use[maxn];
struct cmp{
    bool operator()(const int &a,const int &b)const{
        if(cnt[a] != cnt[b])return cnt[a] < cnt[b];
        return a > b;
    }
};
priority_queue<int,vector<int>,cmp>q;
int main()
{
	freopen("A1129.txt","r",stdin);
    int n,k;
    while(~scanf("%d%d",&n,&k)){
        vector<int>tmp;
        for( int i = 0,x; i < n; i++ ){
            scanf("%d",&x);
            int c = 0;
            if(i){
                printf("%d:",x);
                while(c < k && !q.empty()){
                    int t = q.top();
                    vis[t] = 1;
                    tmp.push_back(t);
                    printf(" %d",t);
                    q.pop();c++;
                }
                puts("");
            }
            cnt[x]++;
            if(!use[x]){
                use[x] = 1;
                q.push(x);
            }
            else {
                if(!vis[x]){
                    while(q.top() != x){
                        tmp.push_back(q.top());q.pop();
                    }
                    tmp.push_back(q.top());q.pop();
                }
            }   
            for( int i = 0; i < tmp.size(); i++ )
                q.push(tmp[i]),vis[tmp[i]] = 0;
            tmp.clear();
        }

    }
    return 0;
}
