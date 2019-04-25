#include<cstdio>
#include<string>
#include<queue>
#include<vector>
#include<map>
using namespace std;

//typedef queue<int> g;
vector<queue<int>> q;
queue<int> Q;
map<int,int> group;
map<int,int>g2q;

int main(){
//    freopen("uva540.txt","r",stdin);
//    freopen("ans.txt","w",stdout);
    int n,casek=0;
    while(scanf("%d",&n)!=EOF&&n){
        q.clear();group.clear();g2q.clear();
        while(!Q.empty()) Q.pop();
        for(int i=0;i<n;i++){
            int t;
            scanf("%d",&t);
            for(int j=0;j<t;j++){
                int tmp;
                scanf("%d",&tmp);
                group[tmp]=i;
            }
        }
        printf("Scenario #%d\n",++casek);
        char str[10];int x;
        while(1){
            scanf("%s",str);
            if(str[0]=='E'){
                scanf("%d",&x);
                if(!g2q.count(group[x])){
                    g2q[group[x]]=q.size();
                    queue<int> tmp;
                    tmp.push(x);
                    q.push_back(tmp);
                    Q.push(g2q[group[x]]);
                }
                else{
                    if(q[g2q[group[x]]].size()==0)Q.push(g2q[group[x]]);
                    o//g2q[group] the mapping could exist even Q has poped the coreesponding q[index]
                    q[g2q[group[x]]].push(x);
                }
            }
            else if(str[0]=='D'){
//                while(q[Q.front()].empty())Q.pop();
                printf("%d\n",q[Q.front()].front());
                q[Q.front()].pop();
                if(q[Q.front()].empty())Q.pop();//
            }
            else {
                printf("\n");
                break;
            }
        }
    }
    printf("\n");
    return 0;
}

