class Solution {
public:
    int stoneGameVI(vector<int>& aliceValues, vector<int>& bobValues) {
        int n = aliceValues.size(), flag = 1, sums = 0;
        vector<int> t(n,0), idx(n);
        for (int i = 0; i < n; i++)
            t[i] = aliceValues[i] + bobValues[i], idx[i] = i;
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return t[a] > t[b];
        });
        for (auto i : idx){
            // cout << sums << " " << x;
            if (flag == 1)
                sums += aliceValues[i];
            else
                sums -= bobValues[i];
            flag = -flag;
        }
        if (sums == 0)
            return 0;
        if (sums > 0)
            return 1;
        return -1;
    }
};