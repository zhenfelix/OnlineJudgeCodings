#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
//#include <pair>
using namespace std;

void print_vec(vector<int> &ans){
    for(int i=0;i<ans.size();i++){cout<<ans[i];if(i<ans.size()-1)cout<<" ";}
    cout<<endl;
    return ;
}

void dfs(vector<int> &nums, vector<int> &ans, int idx, int n, bool &greater, bool &less){
    if(idx*2+1>n-1){print_vec(ans);return;}
    if (idx*2+2<=n-1) {
        int tmp=nums[idx*2+2];
        if(tmp>ans.back())less=true;
        else if(tmp<ans.back())greater=true;
        ans.push_back(tmp);
        dfs(nums, ans, idx*2+2, n, greater, less);
        ans.pop_back();
    }
    int tmp=nums[idx*2+1];
    if(tmp>ans.back())less=true;
    else if(tmp<ans.back())greater=true;
    ans.push_back(tmp);
    dfs(nums, ans, idx*2+1, n, greater, less);
    ans.pop_back();
    return;
}

int main()
{
//    freopen("input.txt","r",stdin);
    int n,tmp;
    bool greater=false, less=false;
    vector<int> nums, ans;
    cin>>n;
    for(int i=0;i<n;i++){cin>>tmp;nums.push_back(tmp);}
    ans.push_back(nums[0]);
    dfs(nums, ans, 0, n, greater, less);
    if(greater&&less)cout<<"Not Heap"<<endl;
    else if(greater)cout<<"Max Heap"<<endl;
    else if(less)cout<<"Min Heap"<<endl;
    return 0;
}

