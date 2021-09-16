const int maxn = 1e4+5;

class Solution {
public:
    int minimumSwitchingTimes(vector<vector<int>>& source, vector<vector<int>>& target) {
        vector<int> cc(maxn,0);
        for (auto vs : source)
            for (auto color : vs){
                cc[color]++;
                // cout << color << " " << cc[color] << endl;
            }
        for (auto vs : target)
            for (auto color : vs)
                cc[color]--;
        int res = 0;
        for (int color = 1; color < maxn; color++){
            if (cc[color] > 0)
                // cout << cc[color] << endl;
                res += abs(cc[color]);
        }
        return res/2;
    }
};


const int maxn = 1e4+5;

class Solution {
public:
    int minimumSwitchingTimes(vector<vector<int>>& source, vector<vector<int>>& target) {
        vector<int> cc(maxn,0);
        for (auto vs : source)
            for (auto color : vs){
                cc[color]++;
                // cout << color << " " << cc[color] << endl;
            }
        for (auto vs : target)
            for (auto color : vs)
                cc[color]--;
        int res = 0;
        for (int color = 1; color < maxn; color++){
            if (cc[color] > 0)
                // cout << cc[color] << endl;
                res += abs(cc[color]);
        }
        return res;
    }
};
