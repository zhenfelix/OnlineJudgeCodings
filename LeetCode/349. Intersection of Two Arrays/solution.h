#include <vector>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>
#include <unordered_map>
using namespace std;

// class Solution {
// public:
//     vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
//         vector<int> ans;
//         set<int> s1,s2;
//         for(auto x: nums1)s1.insert(x);
//         for(auto x: nums2)if(s1.count(x))s2.insert(x);
//         for(set<int>::iterator it=s2.begin();it!=s2.end();it++)ans.push_back(*it);
//         return ans;
//     }
// };

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> m(nums1.begin(), nums1.end());
        vector<int> res;
        for (auto a : nums2)
            if (m.count(a)) {
                res.push_back(a);
                m.erase(a);
            }
        return res;
    }
};