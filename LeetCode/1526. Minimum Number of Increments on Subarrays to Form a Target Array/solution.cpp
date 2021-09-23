class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        int pre = 0, res = 0;
        for (auto cur : target){
            res += max(0,cur-pre);
            pre = cur;
        }
        return res;
    }
};