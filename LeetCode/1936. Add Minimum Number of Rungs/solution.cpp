class Solution {
public:
    int addRungs(vector<int>& rungs, int dist) {
        int pre = 0, res = 0;
        for (auto cur : rungs){
            res += (cur-pre-1)/dist;
            pre = cur;
        }
        return res;
    }
};