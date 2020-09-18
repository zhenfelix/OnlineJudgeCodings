#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn=(1<<20)+50;;
int n,m,q[maxn],a[maxn],v1[maxn],v2[maxn];
ll rev[50],nor[50];
void init(int o,int l,int r,ll rev[],int nums[]){
    if(r==l){
        return;
    }
    int mid=(l+r)/2;
    init(o-1,l,mid,rev,nums);
    init(o-1,mid+1,r,rev,nums);
    ll no=0,re=0;
    int i=l,j=mid+1,k=l;
    for (i=l,j=mid+1,k=l;i<=mid && j<=r;){
        if(nums[i]<=nums[j]){
            a[k++]=nums[i];
            i++;
        }
        else{
            a[k++]=nums[j];
            re+=1L*mid+1-i;
            j++;
        }
    }
    if(i<=mid){
        while (i<=mid){
            a[k++]=nums[i++];
        }
    }
    if(j<=r){
        while (j<=r){
            a[k++]=nums[j++];
        }
    }
    rev[o]+=re;
    for (i=l;i<=r;i++){
        nums[i]=a[i];
    }
 
}
 
ll solve(int o){
    for (int i=o;i>=0;i--){
        swap(nor[i],rev[i]);
    }
    ll ans=0;
    for (int i=0;i<=n;i++){
        ans+=rev[i];
    }
    return ans;
}
 
int main(){
    cin>>n;
    int temp;
    //vector<int> v1,v2;
    for (int i=0;i<(1<<n);i++){
        scanf("%d",&temp);
        v1[i]=temp;
        v2[i]=temp;

    }
    cin>>m;
    for (int i=0;i<m;i++){
        scanf("%d",&q[i]);
    }
    memset(nor,0,sizeof(nor));
    memset(rev,0,sizeof(rev));
    init(n,0,(1<<n)-1,rev,v1);
    reverse(v2,v2+(1<<n));
    init(n,0,(1<<n)-1,nor,v2);

    for (int i=0;i<m;i++){
        cout<<solve(q[i])<<endl;
    }
}