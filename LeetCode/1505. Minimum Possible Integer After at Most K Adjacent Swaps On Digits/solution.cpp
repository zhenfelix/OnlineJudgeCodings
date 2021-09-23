const int inf = 0x3f3f3f3f;
const int maxn = 3e5+5;
int holes[maxn];



class Solution {
public:
    int query(int i){
        int res = 0;
        for (int j = i; j; j -= (j&-j))
            res += holes[j];
        return res;
    }
    void update(int i, int delta){
        for (int j = i; j <= maxn; j += (j&-j))
            holes[j] += delta;
    }
    string minInteger(string num, int k) {
        vector<vector<int>> pos(10);
        memset(holes, 0, maxn*sizeof(int));
        int n = num.size();
        for (int i = n-1; i >= 0; i--)
            pos[num[i]-'0'].push_back(i);
        string res;
        for (int i = 0; i < n; i++){
            for (int ch = 0; ch < 10; ch++){
                if (pos[ch].empty())
                    continue;
                int j = pos[ch].back();
                int h = query(j+1);
                // cout << i << " h: " << h << endl;
                if (k >= j-h){
                    pos[ch].pop_back();
                    res.push_back(num[j]);
                    update(j+1,1);
                    k -= (j-h);
                    // cout << i << " " << k << endl;
                    break;
                }
            }
        }
        return res;
    }
};









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