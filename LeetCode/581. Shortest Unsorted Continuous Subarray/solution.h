class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int len=nums.size();
        int id_min=len,id_max=-1;
        vector<int> vmax(len,INT_MIN);
        vector<int> vmin(len,INT_MAX);
        for(int i=0;i<len;i++){
            vmax[i]=i==0?max(INT_MIN,nums[i]):max(vmax[i-1],nums[i]);
            vmin[len-1-i]=i==0?min(INT_MAX,nums[len-1-i]):min(vmin[len-i],nums[len-1-i]);
        }
        for(int i=0;i<len;i++)if(nums[i]>vmin[i]){
            id_min=i;
            break;
        }
        for(int i=len-1;i>=0;i--)if(nums[i]<vmax[i]){
            id_max=i;
            break;
        }
        return id_max-id_min>0?id_max-id_min+1:0;
    }
};

static const auto __ = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();


// public int findUnsortedSubarray(int[] A) {
//     int n = A.length, beg = -1, end = -2, min = A[n-1], max = A[0];
//     for (int i=1;i<n;i++) {
//       max = Math.max(max, A[i]);
//       min = Math.min(min, A[n-1-i]);
//       if (A[i] < max) end = i;
//       if (A[n-1-i] > min) beg = n-1-i; 
//     }
//     return end - beg + 1;
// }