#include<cstdio>
int a[3][3],A[3]={3,5,7};
int s(int k){
    if(k==2)return a[2][2];
    int i,j;
    for(i=k+1;i<3;i++){
        for(j=0;j<A[i];j++){
            if((j*A[k]+a[k][k])%A[i]==a[k][i]){
                a[k+1][i]=j;
                break;
            }
        }
    }
    return s(k+1)*A[k]+a[k][k];
}
int main(){
    for(int m=0;m<3;m++)scanf("%d",&a[0][m]);
    printf("%d\n", s(0));
    return 0;
}
