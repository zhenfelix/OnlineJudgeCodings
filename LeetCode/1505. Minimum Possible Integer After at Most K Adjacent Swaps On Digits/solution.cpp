class Solution {
    int t[30005],b[30005];
    queue<int> a[10];
    string ans;
public:
    string minInteger(string num, int k) {
        int n=num.size(),i,j,l,o;
        for(i=0;i<n;i++)a[num[i]-'0'].push(i);
        ans="";
        for(i=0;i<n;i++)
        {
            for(o=0;o<10;o++)if(!a[o].empty())
            {
                for(j=a[o].front(),l=0;j;j^=j&-j)l+=t[j];
                if(a[o].front()-l<=k)
                {
                    k-=a[o].front()-l;
                    ans+=o+'0';
                    b[a[o].front()]=1;
                    for(j=a[o].front()+1;j<=n;j+=j&-j)t[j]++;
                    a[o].pop();
                    break;
                }
            }
        }
        for(i=0;i<n;i++)if(!b[i])ans+=num[i];
        return ans;
    }
};