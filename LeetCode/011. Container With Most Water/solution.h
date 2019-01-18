class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans=0,len=height.size();
        int i=0,j=len-1;
        while(i<j){
            int h=min(height[i],height[j]);
            ans=max(ans,(j-i)*h);
            while(i<j&&height[i]<=h)i++;
            while(i<j&&height[j]<=h)j--;
        }
        return ans;
    }
};

    // 1 x ------- o
    // 2 x x
    // 3 x x x
    // 4 x x x x
    // 5 x x x x x
    // 6 x x x x x x

    //   1 2 3 4 5 6
    // 1 x ------- o
    // 2 x x       o
    // 3 x x x     |
    // 4 x x x x   |
    // 5 x x x x x |
    // 6 x x x x x x

    //   1 2 3 4 5 6
    // 1 x ------- o
    // 2 x x - o o o
    // 3 x x x o | |
    // 4 x x x x | |
    // 5 x x x x x |
    // 6 x x x x x x 