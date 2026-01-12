class Solution {
public:
    long long maxTotal(vector<int>& value, vector<int>& limit) {
        int n = value.size();
        vector<int> vec[n + 1];
        for (int i = 0; i < n; i++) vec[limit[i]].push_back(value[i]);

        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            sort(vec[i].begin(), vec[i].end(), greater<int>());
            for (int j = 0; j < i && j < vec[i].size(); j++) ans += vec[i][j];
        }
        return ans;
    }
};