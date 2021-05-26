class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        map<int,int> delta;
        for (auto &log : logs){
            auto a = log[0];
            auto b = log[1];
            delta[a]++;
            delta[b]--;
        }
        int res = 0, year = -1, cur = 0;
        for (int i = 1950; i <= 2050; i++){
            cur += delta[i];
            if (cur > res){
                res = cur;
                year = i;
            }
        }
        return year;

    }
};