class Solution {
public:
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        int n = cars.size();
        vector<int> st;
        vector<double> ans(n,-1);
        for (int i = n-1; i >= 0; i--){
            int pos = cars[i][0], speed = cars[i][1];
            while (!st.empty() && ((speed <= cars[st.back()][1]) || ((ans[st.back()] > -1) && ((speed-cars[st.back()][1])*ans[st.back()] <= cars[st.back()][0]-pos))))
                st.pop_back();
            if (!st.empty())
                ans[i] = (double)(cars[st.back()][0]-pos)/(speed-cars[st.back()][1]);
            st.push_back(i);
        }
        return ans;
    }
};