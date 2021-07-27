class Solution {
public:
    vector<vector<long long>> splitPainting(vector<vector<int>>& segments) {
        vector<pair<int,int>> arr;
        for (auto &seg : segments){
            // arr.push_back({seg[0],seg[2]});
            // arr.push_back({seg[1],-seg[2]});
            arr.emplace_back(seg[0],seg[2]);
            arr.emplace_back(seg[1],-seg[2]);
        }
        sort(arr.begin(), arr.end());
        vector<vector<long long>> res;
        long long color = 0;
        int pre = 0;
        for (auto &[cur, c] : arr){
            if (color > 0 && cur > pre){
                res.push_back({pre,cur,color});
            }
            color += c;
            pre = cur;
        }
        return res;
    }
};