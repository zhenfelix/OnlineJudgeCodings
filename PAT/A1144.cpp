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

const int N=100010;
vector<bool> mp(N,false);

int main()
{
    // freopen("input.txt","r",stdin);
    int n;
    cin>>n;
    while (n--) {
        int tmp;
        cin>>tmp;
        if(tmp>0&&tmp<N&&mp[tmp]==false)mp[tmp]=true;
    }
    int ans=1;
    while (1) {
        if(mp[ans]==false)break;
        ans++;
    }
    cout<<ans<<endl;
    return 0;
}

