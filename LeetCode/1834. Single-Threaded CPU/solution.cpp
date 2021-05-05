

// class Solution {
// public:
//     vector<int> getOrder(vector<vector<int>>& tasks) {
//         priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,greater<>> pq_task;
//         priority_queue<tuple<int,int>,vector<tuple<int,int>>,greater<>> pq_cpu;
//         for (int i=0; i < tasks.size(); i++)
//         {
//             pq_task.push(make_tuple(tasks[i][0],i,tasks[i][1]));
//         }
//         vector<int> res;
//         long long now = 0;
//         while (!pq_task.empty() || !pq_cpu.empty())
//         {
//             bool consume = false;
//             if (!pq_task.empty())
//             {
//                 auto [t,idx,cost] = pq_task.top();
//                 if (t <= now)
//                 {
//                     pq_task.pop();
//                     pq_cpu.push(make_tuple(cost,idx));
//                     consume = true;
//                 }
//                 else if (pq_cpu.empty())
//                     now = t;
//             }
//             if (!consume && !pq_cpu.empty())
//             {
//                 auto [cost,idx] = pq_cpu.top();
//                 pq_cpu.pop();
//                 now += cost;
//                 res.push_back(idx);

//             }
//         }
//         return res;
//     }
// };


class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        vector<tuple<int, int, int>> v;
        for (int i = 0; i < tasks.size(); i++) {
            v.emplace_back(tasks[i][0], tasks[i][1], i);
        }
        sort(v.begin(), v.end(), greater<>());
        vector<int> ans;
        long long now = 1;
        while (!pq.empty() || !v.empty()) {
            while (!v.empty() && get<0>(v.back()) <= now) {
                pq.emplace(get<1>(v.back()), get<2>(v.back()));
                v.pop_back();
            }
            if (!pq.empty())
            {
                auto [t, i] = pq.top();
                pq.pop();
                ans.emplace_back(i);
                now += t;
            }
            else
                now = (long long)get<0>(v.back());
            
        }
        return ans;
    }
};