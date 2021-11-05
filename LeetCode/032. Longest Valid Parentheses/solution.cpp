class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> st;
        int n = s.length(), res = 0;
        for (int i = 0; i < n; i++){
            if (!st.empty() && s[st.back()] == '(' && s[i] == ')'){
                    st.pop_back();
                    res = max(res, i-(st.empty() ? -1 : st.back()));
                }
            else{
                st.push_back(i);
            }
        }
        return res;
    }
};