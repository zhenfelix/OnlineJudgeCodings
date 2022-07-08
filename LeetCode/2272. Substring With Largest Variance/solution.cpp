class Solution {
public:
    int largestVariance(string s) {
        int n = s.size();
        int ans = 0;
        for (char x = 'a'; x <= 'z'; x++) for (char y = 'a'; y <= 'z'; y++) if (x != y) {
            vector<int> f(n + 1);
            int t = 0, mn = 1e9;
            for (int i = 1, j = 0; i <= n; i++) {
                char c = s[i - 1];
                if (c == x) f[i] = ++t;
                else if (c == y) {
                    f[i] = --t;
                    while (j < i) mn = min(mn, f[j++]);
                }
                else f[i] = t;
                ans = max(ans, f[i] - mn);
            }
        }
        return ans;
    }
};



// 作者：tsreaper
// 链接：https://leetcode.cn/problems/substring-with-largest-variance/solution/by-tsreaper-d748/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int largestVariance(string s) {
        int n = s.size();
        int ans = 0;
        for (char x = 'a'; x <= 'z'; x++) for (char y = 'a'; y <= 'z'; y++) if (x != y) {
            int t = 0, mn2 = 1e9, mn = 0;
            for (int i = 0; i < n; i++) {
                char c = s[i];
                if (c == x) ++t;
                else if (c == y) {
                    --t;
                    mn2 = mn;
                    mn = min(mn, t);
                }
                ans = max(ans, t - mn2);
            }
        }
        return ans;
    }
};

class Solution {
    int a[10005],b[10005],c[10005];
public:
    int largestVariance(string s) {
        int n=s.size(),x,y,i,j,ans=0;
        for(x='a';x<='z';x++)for(y='a';y<='z';y++)if(x!=y)
        {
            for(i=0;i<n;i++)if(s[i]==x)a[i+1]=a[i]+1;
            else if(s[i]==y)a[i+1]=a[i]-1;
            else a[i+1]=a[i];
            for(i=1;i<=n;i++)b[i]=min(b[i-1],a[i]);
            for(c[n]=a[n],i=n-1;i;i--)c[i]=max(c[i+1],a[i]);
            for(i=0;i<n;i++)if(s[i]==y)ans=max(ans,c[i+1]-b[i]);
        }
        return ans;
    }
};