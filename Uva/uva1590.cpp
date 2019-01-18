#include<cstdio>
const int maxn=1010;
unsigned ip[maxn]={0};
void print_bi(unsigned x){
    unsigned radix=1;
    for(int i=31;i>=0;i--){
        printf("%d",x/(radix<<i));
        x=x%(1<<i);
    }
    printf("\n");
    return;
}
unsigned strip_ones(unsigned x){
    unsigned radix=1,y=0;
    int i;
    for(i=31;i>=0;i--){
        if(x/(radix<<i)==0)break;
        x=x%(1<<i);
        y=(y<<1)+1;
    }
    return y<<(i+1);
}
void print_net(unsigned x){
    unsigned radix=1;
    for(int i=24;i>=0;i=i-8){
        printf("%d",x/(radix<<i));
        if(i==0)printf("\n");
        else printf(".");
        x=x%(radix<<i);
    }
    return;
}
int main(){
//    freopen("uva1590.txt","r",stdin);
//    freopen("ans.txt", "w", stdout);
    int n;
    while(scanf("%d",&n)==1&&n){
        unsigned re=1;
        unsigned front,bi=0,ans=(((re<<31)-1)<<1)+1,MIN=ans;
        for(int i=0;i<n;i++){
            unsigned a=0;
            for(int j=0;j<4;j++){
                unsigned tmp;
                scanf("%d",&tmp);
                getchar();
                a=(a<<8)+tmp;
                
            }
            ip[i]=a;
            if(ip[i]<MIN)MIN=ip[i];
            //            print_bi(ip[i]);
        }
        front=ip[0];
        for(int i=0;i<n;i++){
            bi=~(front^ip[i]);
            ans=ans&bi;
            //            print_bi(bi);
            //            print_bi(ans);
        }
        ans=strip_ones(ans);
        MIN=ans&MIN;
        //        print_bi(MIN);
        //        print_bi(ans);
        print_net(MIN);
        print_net(ans);
    }
    //    unsigned re=1;
    //    print_bi((re<<31)-1);
    //    print_bi((re<<32)-1);
    //    print_bi((re<<32));
    //    print_bi((((re<<31)-1)<<1)+1);
    return 0;
}

