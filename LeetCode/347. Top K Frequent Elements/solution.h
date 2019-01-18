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
//     vector<int> topKFrequent(vector<int>& nums, int k) {
//         vector<int> ans;
//         unordered_map<int,int> table;
//         unordered_map<int,int> cc;
//         for(int x:nums){
//             int idx;
//             if(table.find(x)!=table.end()){
//                 idx=table[x];
//                 cc[x]++;
//                 while(idx>0&&cc[ans[idx]]>cc[ans[idx-1]]){
//                     int tmp=table[ans[idx]];
//                     table[ans[idx]]=table[ans[idx-1]];
//                     table[ans[idx-1]]=tmp;
//                     swap(ans[idx],ans[idx-1]);
//                     idx--;
//                 }
//             }
//             else{
//                 table[x]=ans.size();
//                 cc[x]=1;
//                 ans.push_back(x);
//             }
//         }
//         k=ans.size()-k;
//         while(k--)ans.pop_back();
//         return ans;
//     }
// };

// class Solution {
// public:
//     vector<int> topKFrequent(vector<int>& nums, int k) {
//         vector<int> res;
//         if (!nums.size()) return res;
//         unordered_map<int, int> cnt;
//         for (auto num : nums) cnt[num]++;
//         vector<vector<int>> bucket(nums.size() + 1);
//         for (auto kv : cnt) {
//             bucket[kv.second].push_back(kv.first);
//         }

//         for (int i = bucket.size() - 1; i >= 0; --i) {
//             for (int j = 0; j < bucket[i].size(); ++j){
//                 res.push_back(bucket[i][j]);
//                 if (res.size() == k) return res;
//             }
//         }

//         return res;
//     }
// };


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        unordered_map<int, int> cnt;
        for (auto num : nums) cnt[num]++;
        for (auto kv : cnt) {
            pq.push({kv.second, kv.first});
            while (pq.size() > k) pq.pop();
        }
        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};