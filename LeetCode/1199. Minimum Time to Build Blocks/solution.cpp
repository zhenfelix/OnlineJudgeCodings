class Solution {
public:
    int minBuildTime(vector<int>& blocks, int split) {
        sort(blocks.begin(), blocks.end(), greater<>());
        auto check = [&](int t){
            // cout << t << endl;
            int cnt = 1;
            for (auto b : blocks){
                while (t-b >= split && cnt < 2000){
                    cnt *= 2;
                    t -= split;
                }
                cnt--;
                // cout << b << " " << cnt << " " << t << endl;
                if (cnt < 0 || t < b)
                    return false;
            }
            return true;
        };
        int mx = *max_element(blocks.begin(), blocks.end());
        int lo = mx, hi = mx+2000;
        while (lo <= hi){
            int mid = (lo+hi)/2;
            if (check(mid))
                hi = mid-1;
            else
                lo = mid+1;
        }
        return lo;
    }
};














class Solution {
public:
    
    bool check(int lim, vector<int>& blocks, int n, int sp){
        int cur=1, last=0;
        for (int i=0; i<n; i++){
            int tim=lim-blocks[i]-last;
            tim/=sp;
            if (tim>0){
                // printf("Split Times : %d\n", tim);
                for (int j=0; j<tim && cur<=n-i; j++) { cur*=2; }
                last+=tim*sp;
            }
            cur--;
            if (cur<0) return false;
            
        }
        return true;
    }
    
    int minBuildTime(vector<int>& blocks, int split) {
        int n=blocks.size();
        sort(blocks.begin(), blocks.end()); reverse(blocks.begin(), blocks.end());
                                                    
        int left=blocks[0], right=1e9, ans=1e9;
        while(left<=right){
            int mid=(left+right)/2;
            if (check(mid, blocks, n, split)){
                ans=min(ans, mid);
                right=mid-1;
            }else left=mid+1;
        }
        
        return ans;
    }
};