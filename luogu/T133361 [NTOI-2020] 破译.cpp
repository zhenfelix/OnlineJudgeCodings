#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 5e4 + 5;
const int INF = 0x7fffffff;

int arr[MAXN], n, m;
int op, lo, hi;

int func(int target){
    int left=1;int right=0;int sums=0;
    while (sums!=target) {
        if(sums<target){
            right++;
            sums += right;
        }
        else{
            sums -= left;
            left++;
        }
    }
    return right-left+1;
}


signed main(void)
{
//    freopen("input.txt", "r", stdin);
    memset(arr, 0, sizeof arr);

    scanf("%d %d", &n, &m);
    for (int i=1; i<=n; i++) {
        scanf("%d",&arr[i]);
//        printf("%d ",arr[i]);
    }
    for (int i=0; i<m; i++) {
        scanf("%d %d %d",&op,&lo,&hi);
        if(op==1){
            for (int i=lo; i<=hi; i++) {
                arr[i]=func(arr[i]);
            }
        }
        else{
            int res = 0;
            for (int i=lo; i<=hi; i++) {
                res += arr[i];
            }
            printf("%d\n",res);
        }
    }
    return 0;
}
