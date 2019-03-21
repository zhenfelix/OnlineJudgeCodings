class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n=heights.size();
        vector<int> left(n,0),right(n,0);
        stack<pair<int,int>> st;
        int ans=0;
        for(int i=0;i<heights.size();i++){
            while(!st.empty() && st.top().first>=heights[i]){
                left[i]+=(1+st.top().second);
                st.pop();
            }

            st.push(make_pair(heights[i],left[i]));
        }
        while(!st.empty())st.pop();
        for(int i=heights.size()-1;i>=0;i--){
            int cc=0;
            while(!st.empty() && st.top().first>=heights[i]){
                right[i]+=(1+st.top().second);
                st.pop();
            }

            st.push(make_pair(heights[i],right[i]));
        }
        for(int i=0;i<heights.size();i++){
            ans=max(ans,(left[i]+right[i]+1)*heights[i]);
        }
        return ans;
    }
};