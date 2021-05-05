class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = queries.size();
        vector<int> ans(n, -1);
        vector<pair<int,int>>queries_sorted;
        for (int i = 0; i < n; i++)
            queries_sorted.push_back({queries[i],i});
        sort(queries_sorted.begin(), queries_sorted.end());
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        sort(intervals.begin(), intervals.end());
        int m = intervals.size();
        int cur = 0;
        for (auto [q, i] : queries_sorted){
            while (cur < m && intervals[cur][0] <= q){
                int a = intervals[cur][0], b = intervals[cur][1];
                int len = b - a + 1;
                pq.push({len, b});
                cur++;
            }
            while (!pq.empty() && pq.top().second < q)
                pq.pop();
            if (!pq.empty())
                ans[i] = pq.top().first;
        }
        return ans;

    }
};