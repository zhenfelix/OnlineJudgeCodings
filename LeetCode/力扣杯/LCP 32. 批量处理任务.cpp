// const int inf = 0x3f3f3f3f;
// const int MAXN = 200005;

// struct Edge{
//     int from, to, weight, pre;
//     Edge() = default;
//     Edge(int f, int t, int w, int p)
//         : from(f), to(t), weight(w), pre(p)
//         {}
//     friend ostream& operator<< (ostream& out, Edge& e){
//         out << e.from << " " << e.to << " " << e.weight << " " << e.pre << endl;
//         return out;
//     }
// };

// Edge edges[MAXN*4];
// int head[MAXN];
// int cnt;

// void addEdge(int a, int b, int w){
//     edges[cnt] = Edge(a, b, w, head[a]);
//     head[a] = cnt;
//     cnt++;
// }

// void spfa(vector<int> &dist, int s){
//     int n = dist.size();
//     queue<int> q;
//     vector<bool> inqueue(n, false);
//     dist[s] = 0;
//     q.push(s);
//     inqueue[s] = true;
//     while(!q.empty()){
//         int cur = q.front();q.pop();
//         inqueue[cur] = false;
//         for (int i = head[cur]; i != 0; i = edges[i].pre){
//             int nxt = edges[i].to;
//             int w = edges[i].weight;
//             if (dist[nxt] < dist[cur] + w){
//                 dist[nxt] = dist[cur] + w;
//                 if (!inqueue[nxt]){
//                     inqueue[nxt] = true;
//                     q.push(nxt);
//                 }
//             }
//         }
//     }
// }


// class Solution {
// public:
//     int processTasks(vector<vector<int>>& tasks) {
//         map<int,int> mp;
//         for (auto &item : tasks){
//             mp.insert({item[0],1});
//             mp.insert({item[1]+1,1});
//         }
//         int n = mp.size();
//         vector<int> h(n, 0);
//         vector<int> dist(n, -inf);
//         int idx = 0;
//         for (auto &[k, v] : mp){
//             h[idx] = k;
//             v = idx++;
//         }
//         // for (auto &[k, v] : mp){
//         //     cout << k << " " << v << endl;
//         // }
//         cnt = 1;
//         memset(head, 0, sizeof(int)*n);
//         for (int i = 1; i < n; i++){
//             addEdge(i-1,i,0);
//             addEdge(i,i-1,h[i-1]-h[i]);
//         }
//         for (auto &item : tasks){
//             addEdge(mp[item[0]], mp[item[1]+1], item[2]);
//         }
//         // for (int i = 0; i < cnt; i++){
//         //     cout << edges[i];
//         // }
//         spfa(dist, 0);
//         // for (int i = 0; i < n; i++){
//         //     cout << dist[i] << " ";
//         // }
//         return dist[n-1];

//     }
// };



const int inf = 0x3f3f3f3f;

class Solution
{
public:
    int processTasks(vector<vector<int>> &tasks)
    {
        sort(tasks.begin(), tasks.end());
        map<int, int> mp, mono;
        mono.insert({-inf, -inf});
        for (auto &item : tasks)
        {
            mp.insert({item[0], 1});
            mp.insert({item[1] + 1, 1});
        }
        int n = mp.size();
        vector<int> h(n, 0);
        vector<int> dist(n, 0);
        int idx = 0;
        for (auto &[k, v] : mp)
        {
            h[idx] = k;
            v = idx++;
        }
        // for (auto &[k, v] : mp){
        //     cout << k << " " << v << endl;
        // }

        int cur = 0;
        for (auto &item : tasks)
        {
            int p = mp[item[0]];
            int q = mp[item[1] + 1];
           
            for(; cur <= p; cur++)
                if (cur){
                    dist[cur] = max(dist[cur], dist[cur-1]);
                    auto left = mono.upper_bound(-h[cur]);
                    left--;
                    dist[cur] = max(dist[cur], left->second + h[cur]);
                    }
            dist[q] = max(dist[q], dist[p] + item[2]);
            auto right = mono.upper_bound(-h[q]);
            right--;
            if (dist[q] - h[q] <= right->second)
                continue;
            mono[-h[q]] = dist[q] - h[q];
            auto it = mono.find(-h[q]);
            it++;
            for (; it != mono.end() && dist[q] - h[q] >= it->second;)
                it = mono.erase(it);
        }
        for (; cur < n; cur++)
            if (cur)
            {
                dist[cur] = max(dist[cur], dist[cur - 1]);
                auto left = mono.upper_bound(-h[cur]);
                left--;
                dist[cur] = max(dist[cur], left->second + h[cur]);
            }
        // for (auto &item : tasks){
        //     cout << item[0] << " " << item[1] << " " << item[2] << "\n";
        // }
        // for (int i = 0; i < n; i++)
        // {
        //     printf("%03d ", h[i]);
        // }
        // cout << "\n";
        // for (int i = 0; i < n; i++){
        //     printf("%03d ", dist[i]);
        // }
        // cout << "\n";
        return dist[n - 1];
    }
};