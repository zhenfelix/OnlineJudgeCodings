class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        sort(tasks.begin(), tasks.end(), [](vector<int> &a, vector<int> &b){
            return a[1]-a[0] > b[1]-b[0];
        });
        int res = 0, cur = 0;
        for (auto &task : tasks){
            int c = task[0], q = task[1];
            res += max(cur,q)-cur;
            cur = max(cur,q);
            cur -= c;
        }
        return res;
    }
};