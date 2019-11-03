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