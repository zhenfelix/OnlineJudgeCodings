class Solution {
public:
    int halveArray(vector<int>& nums) {
        long long sm = 0;
        priority_queue<long double> q;
        for (int x : nums) sm += x, q.push(x);
        long double now = 0;
        int ans = 0;
        while (now * 2 < sm) {
            long double x = q.top(); q.pop();
            now += x / 2;
            q.push(x / 2);
            ans++;
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode-cn.com/circle/discuss/bdMSIh/view/vxDgMk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



typedef long long ll;
const int N=100005;
ll a[N];
class Solution {
public:
    int halveArray(vector<int>& b) {
        int n=b.size(),l=0,ans=0; ll s=0;
        for (int i=0;i<n;++i)a[i]=(ll)b[i]<<18,s+=a[i];
        ll s1=s/2;
        while (s>s1){
            int mid=(l+n)/2,cnt=0;
            nth_element(a+l,a+mid,a+n);
            ll v=a[mid],_s=s;
            for (int i=mid;i<n;++i){
                int t=64-__builtin_clzll(a[i]/v);
                cnt+=t; s-=a[i]-(a[i]>>t);
            }
            if (s>=s1){
                ans+=cnt;
                for (int i=mid;i<n;++i)
                    while (a[i]>=v)a[i]/=2;
            }
            else {
                s=_s;
                if (l==n-1)s-=a[l],a[l]/=2,s+=a[l],++ans;
                l=mid;
            }
        }
        return ans;
    }
};


作者：hqztrue
链接：https://leetcode-cn.com/problems/minimum-operations-to-halve-array-sum/solution/onsuan-fa-by-hqztrue-jalf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



typedef long long ll;
const int N=100005;
ll a[N];
class Solution {
public:
    void my_nth_element(ll arr[], int left, int mid, int right){
        while (left < right){
            int lo = left, hi = left;
            for (int i = left; i <= right; i++){
                if (arr[i] == arr[right]){
                    swap(arr[i], arr[hi]);
                    hi++;
                }
                else if(arr[i] < arr[right]){
                    ll tmp = arr[i];
                    arr[i] = arr[hi];
                    arr[hi] = arr[lo];
                    arr[lo] = tmp;
                    lo++;hi++;
                }
            }
            if (lo <= mid && mid < hi)
                break;
            if (mid >= hi)
                left = hi;
            else
                right = lo-1;
        }
        return;
    }

    int halveArray(vector<int>& b) {
        int n=b.size(),l=0,ans=0; ll s=0;
        std::random_shuffle(b.begin(), b.end());
        for (int i=0;i<n;++i)a[i]=(ll)b[i]<<18,s+=a[i];
        // for (int i=0;i<n;++i)if(a[i]<=0)cout << a[i] << " ";
        // for (int i=0;i<n;++i)cout << a[i] << " ";
        // cout << "finish" << endl;
        ll s1=s/2;
        while (s>s1){
            int mid=(l+n)/2,cnt=0;
            my_nth_element(a, l,mid,n-1);
            ll v=a[mid],_s=s;
            // for (int i=0;i<n;++i)if(a[i]<=0)cout << a[i] << " ";
            // for (int i=0;i<n;++i)cout << a[i] << " ";
            // cout << endl;
            // cout << l << " " << mid << " " << n-1 << " " << v << endl;
            for (int i=mid;i<n;++i){
                // cout << a[i] << " ";
                int t=64-__builtin_clzll(a[i]/v);
                cnt+=t; s-=a[i]-(a[i]>>t);
            }
            // cout << endl;
            if (s>=s1){
                ans+=cnt;
                for (int i=mid;i<n;++i)
                    while (a[i]>=v)a[i]/=2;
            }
            else {
                s=_s;
                if (l==n-1)s-=a[l],a[l]/=2,s+=a[l],++ans;
                l=mid;
            }
        }
        return ans;
    }
};