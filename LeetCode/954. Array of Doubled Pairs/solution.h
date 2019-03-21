class Solution {
public:
    bool canReorderDoubled(vector<int>& A) {
        unordered_map<int,int> mp;
        sort(A.begin(), A.end());
        for(auto &x: A)mp[x]++;
        for(auto &x: A){
            if(mp[x]<=0)continue;
            if(x<0){
                if(mp[x/2]<=0 || x%2==1)return false;
                mp[x]--;
                mp[x/2]--;
            }
            else{
                if(mp[x*2]<=0)return false;
                mp[x]--;
                mp[x*2]--;
            }
        }
        return true;
    }
};


// bool canReorderDoubled(vector<int>& A) {
//         unordered_map<int, int> c;
//         for (int a : A) c[a]++;
//         vector<int> keys;
//         for (auto it : c)
//             keys.push_back(it.first);
//         sort(keys.begin(), keys.end(), [](int i, int j) {return abs(i) < abs(j);});
//         for (int x : keys) {
//             if (c[x] > c[2 * x])
//                 return false;
//             c[2 * x] -= c[x];
//         }
//         return true;
//     }