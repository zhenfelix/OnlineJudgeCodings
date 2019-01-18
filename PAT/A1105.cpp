#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>
using namespace std;




int main()
{
    // freopen("input.txt","r",stdin);
    int N,n,m;
    cin>>N;
    vector<int> nums(N);
    for(int i=0;i<N;i++)cin>>nums[i];
    sort(nums.begin(), nums.end(), greater<int>());
    n=sqrt(N);
    while (N%n!=0)n--;
    m=N/n;
    vector<vector<int>> mat(m,vector<int>(n,0));
    int i=0,j=0,k=0;
    while (k<N) {
        while(k<N&&j<n&&mat[i][j]==0)mat[i][j++]=nums[k++];
        i++;j--;
        while(k<N&&i<m&&mat[i][j]==0)mat[i++][j]=nums[k++];
        i--;j--;
        while(k<N&&j>=0&&mat[i][j]==0)mat[i][j--]=nums[k++];
        i--;j++;
        while(k<N&&i>=0&&mat[i][j]==0)mat[i--][j]=nums[k++];
        i++;j++;
    }
    for (int i=0; i<m ; i++) {
        for (int j=0; j<n ; j++) {
            cout<<mat[i][j];
            if(j<n-1)cout<<" ";
            else cout<<endl;
        }
    }
    return 0;
}

