class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        for (auto &query: queries) {
            int x = query[0], y = query[1], r = query[2];
            int cnt = 0;
            for (auto &point : points) {
                int dx = x - point[0], dy = y - point[1];
                if (dx * dx + dy * dy <= r * r)
                    cnt++;
            }
            ans.emplace_back(cnt);
        }
        return ans;
    }
};