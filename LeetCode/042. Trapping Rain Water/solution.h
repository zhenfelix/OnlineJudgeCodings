class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size(),sums=0;
        vector<int> left(n),right(n);
        for(int i=n-1;i>=0;i--){
            if(i==n-1)right[i]=height[i],left[n-1-i]=height[n-1-i];
            else {
                right[i]=max(right[i+1],height[i]);
                left[n-1-i]=max(left[n-1-i-1],height[n-1-i]);
            }
        }
        for(int i=0;i<n;i++)sums+=(min(left[i],right[i])-height[i]);
        return sums;
    }
};