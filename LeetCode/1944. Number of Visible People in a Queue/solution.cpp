class Solution
{
public:
    vector<int> canSeePersonsCount(vector<int> &heights)
    {
        stack<int> st;
        // cout << std::numeric_limits<int>::infinity() << endl;
        st.push(std::numeric_limits<int>::max());
        int n = heights.size();
        vector<int> ans(n);
        // cout << st.size() << endl;
        for (int i = n - 1; i >= 0; i--)
        {
            int cnt = 0;
            while (st.top() < heights[i])
            {
                cnt++;
                st.pop();
            }
            ans[i] = cnt+(st.top() != std::numeric_limits<int>::max());
            st.push(heights[i]);
            
        }
        return ans;
    }
};