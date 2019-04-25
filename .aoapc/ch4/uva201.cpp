#include<cstdio>
#include<cstring>
const int maxn=15;
int num[maxn];
bool H[maxn][maxn],V[maxn][maxn];
bool check(int row,int col,int size){
    bool flag=true;
    for(int tmp=row;tmp<row+size;tmp++)if(!V[tmp][col]||!V[tmp][col+size])return false;
    for(int tmp=col;tmp<col+size;tmp++)if(!H[row][tmp]||!H[row+size][tmp])return false;
    return flag;
}
int main(){
    // freopen("uva201.txt","r",stdin);
    // freopen("ans.txt","w",stdout);
    int t=0,n,m;
    while(scanf("%d%d\n",&n,&m)==2){
        if(t!=0){
            printf("\n");
            for(int i=0;i<34;i++)printf("*");
            printf("\n\n");
        }
        t++;
        memset(H,0,sizeof(H));
        memset(V,0,sizeof(V));
        memset(num,0,sizeof(num));
        for(int i=0;i<m;i++){
            char ch;
            int row,col;
            scanf("%c%d%d\n",&ch,&row,&col);
            if(ch=='H')H[row][col]=true;
            else V[col][row]=true;
        }
        for(int s=1;s<=n-1;s++){
            for(int r=1;r+s<=n;r++){
                for(int c=1;c+s<=n;c++)if(check(r,c,s))num[s]++;
            }
        }
        bool tag=true;
        printf("Problem #%d\n\n",t);
        for(int s=1;s<=n-1;s++){
            if(num[s]){
                printf("%d square (s) of size %d\n",num[s],s);
                tag=false;
            }
        }
        if(tag)printf("No completed squares can be found.\n");
    }
    return 0;
}


