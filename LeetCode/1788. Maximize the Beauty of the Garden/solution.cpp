const int inf = 0x3f3f3f3f;

class Solution {
public:
    int maximumBeauty(vector<int>& flowers) {
        map<int,int> mp;
        vector<int> presums = {0};
        int res = -inf, n = flowers.size();
        for (int i = 0; i < n; i++){
            presums.push_back(presums.back()+max(0,flowers[i]));
            if (mp.find(flowers[i]) == mp.end()){
                mp[flowers[i]] = i;
            }
            else{
                int left = mp[flowers[i]];
                res = max(res, flowers[i]*2+presums[i]-presums[left+1]);
            }
        }
        return res;
    }
};