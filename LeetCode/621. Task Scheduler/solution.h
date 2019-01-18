// class Solution {
// public:
//     int leastInterval(vector<char>& tasks, int n) {
//         priority_queue<int, vector<int>, less<int>> pq;
//         vector<int> v(26,0);
//         int time=0;n++;
//         for(auto ch: tasks)v[ch-'A']++;
//         for(auto vv: v)if(vv>0)pq.push(vv);
//         while(!pq.empty()){
//             queue<int> q;
//             for(int i=0;i<n;i++){
//                 if(!pq.empty()){
//                     int tmp=pq.top();pq.pop();
//                     tmp--;if(tmp>0)q.push(tmp);
//                 }
//                 else if(pq.empty()&&q.empty())break;
//                 time++;
//             }
//             while(!q.empty()){
//                 int tmp=q.front();q.pop();
//                 pq.push(tmp);
//             }
//         }
//         return time;
//     }
// };

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int>mp;
        int count = 0;
        for(auto e : tasks)
        {
            mp[e]++;
            count = max(count, mp[e]);
        }
        
        int ans = (count-1)*(n+1);
        for(auto e : mp) if(e.second == count) ans++;
        return max((int)tasks.size(), ans);
    }
};
// proof by idle slot diagram