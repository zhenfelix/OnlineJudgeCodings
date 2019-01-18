#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>
//#include <pair>
using namespace std;

void PostOrder(vector<int> &nums, vector<int> &ans, int i, int n, bool &MAX, bool &MIN){
    if(i>n-1)return;
    if(2*i+1<=n-1){
        if(nums[i]>nums[2*i+1])MAX=true;
        else if(nums[i]<nums[2*i+1])MIN=true;
        PostOrder(nums, ans , i*2+1, n, MAX, MIN);
    }
    if(2*i+2<=n-1){
        if(nums[i]>nums[2*i+2])MAX=true;
        else if(nums[i]<nums[2*i+2])MIN=true;
        PostOrder(nums, ans , i*2+2, n, MAX, MIN);
    }
    ans.push_back(nums[i]);
}


int main()
{
    freopen("input.txt","r",stdin);
    int n,m;
    cin>>m>>n;
    
    while (m--) {
        bool MAX=false, MIN=false;
        vector<int> nums(n,0),ans;
        for (int i=0; i<n; i++)cin>>nums[i];
        PostOrder(nums , ans , 0, n , MAX , MIN);
        if(MAX&&MIN)cout<<"Not Heap"<<endl;
        else if(MAX)cout<<"Max Heap"<<endl;
        else if(MIN)cout<<"Min Heap"<<endl;
        for(int i=0; i<n; i++){
            cout<<ans[i];
            if(i<n-1)cout<<" ";
        }
        cout<<endl;
    }

    return 0;
}

