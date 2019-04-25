#include<iostream>
#include <map>
#include <cstring>
using namespace std;

//typedef pair<int, int> pii;
//map<pii,int>record;
const int maxn=5010;//memory usage limited
map<int,int> id2mat;
int mat[maxn][maxn];
void id_generate(int id){
    if(!id2mat.count(id))id2mat[id]=id2mat.size();
}
int main() {
//    freopen("uva10763.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    int n;
    while (scanf("%d",&n)==1&&n) {
        memset(mat, 0, sizeof(mat));
        id2mat.clear();
        for(int i=0;i<n;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            id_generate(a);id_generate(b);
            mat[id2mat[a]][id2mat[b]]++;
        }
        bool flag=true;
        for(int i=0;i<id2mat.size();i++){
            if(!flag)break;
            for(int j=i+1;j<id2mat.size();j++){
                if(!flag)break;
                if(mat[i][j]!=mat[j][i])flag=false;
            }
        }
        if(flag)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
    
}

