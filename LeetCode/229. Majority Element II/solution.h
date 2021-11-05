class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int,int> cc;
        for (auto x : nums){
            cc[x]++;
            if (cc.size() > 3){
                vector<int> rm;
                for (auto [k,v] : cc){
                    cc[k]--;
                    if (cc[k] == 0)
                        rm.push_back(k);
                }
                for (auto k : rm)
                    cc.erase(k);
            }
        }
        vector<int> res;
        for (auto [k,v] : cc){
            int cnt = 0;
            for (auto x : nums)
                cnt += (x == k);
            if (cnt > n/3)
                res.push_back(k);
        }
        return res;
    }
};

// class Solution {
// public:
//     vector<int> majorityElement(vector<int>& nums) {
//         int a=0,b=1,ca=0,cb=0,n=nums.size();
//         vector<int> ans;
//         for(auto &x: nums){
//             if(x==a){
//                 ca++;
//             }
//             else if(x==b){
//                 cb++;
//             }
//             else{
//                 if(ca>0){ca--;}
//                 else if(ca==0){a=x;ca++;}
//                 if(cb>0){cb--;}
//                 else if(cb==0 && a!=x){b=x;cb++;}
//             }
//         }
//         ca=0;cb=0;
//         for(auto &x: nums){
//             if(x==a)ca++;
//             else if(x==b)cb++;
//         }
//         if(ca>n/3)ans.push_back(a);
//         if(cb>n/3)ans.push_back(b);
//         return ans;
//     }
// };
// Input:
// [1,1,1,2,3,4,5,6]
// Output:
// []
// Expected:
// [1]


class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int a=0,b=1,ca=0,cb=0,n=nums.size();
        vector<int> ans;
        for(auto &x: nums){
            if(x==a){
                ca++;
            }
            else if(x==b){
                cb++;
            }
            else if(ca==0){
                a=x;
                ca++;
            }
            else if(cb==0){
                b=x;
                cb++;
            }
            else{
                ca--;cb--;
            }
        }
        ca=cb=0;
        for(auto &x: nums){
            if(x==a)ca++;
            else if(x==b)cb++;
        }
        if(ca>n/3)ans.push_back(a);
        if(cb>n/3)ans.push_back(b);
        return ans;
    }
};