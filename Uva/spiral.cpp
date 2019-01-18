#include<cstdio>
#include<cstring>
const int MAX=6;
int a[MAX][MAX];
int main(){
    int m,n,tol=0,x,y;
    memset(a,0,sizeof(a));
    scanf("%d%d",&m,&n);
    x=-1;y=n-1;
    while(tol<m*n){
        while(x+1<m&&!a[x+1][y])a[++x][y]=++tol;
        while(y-1>=0&&!a[x][y-1])a[x][--y]=++tol;
        while(x-1>=0&&!a[x-1][y])a[--x][y]=++tol;
        while(y+1<n&&!a[x][y+1])a[x][++y]=++tol;
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
