const int inf = 0x3f3f3f3f;

class Solution {
public:
    vector<int> closestRoom(vector<vector<int>>& rooms, vector<vector<int>>& queries) {
        int k = queries.size(), n = rooms.size();
        vector<int> ans(k), idx(k);
        for (int i = 0; i < k; i++)
            idx[i] = i;
        sort(idx.begin(), idx.end(), [&](int a, int b){
            if(queries[a][1] == queries[b][1])
                return queries[a][0] < queries[b][0];
            return queries[a][1] > queries[b][1];
        });
        sort(rooms.begin(), rooms.end(), [](const vector<int> &a, const vector<int> &b){
            if(a[1] == b[1])
                return a[0] < b[0];
            return a[1] > b[1];
        });
        set<int> mp;
        int cur = 0;
        for (int i = 0; i < k; i++){
            int pid = queries[idx[i]][0];
            int msz = queries[idx[i]][1];
            while (cur < n && rooms[cur][1] >= msz){
                mp.insert(rooms[cur][0]);
                cur++;
            }
            auto it = mp.lower_bound(pid);
            int a = -inf, b = inf;
            if (it != mp.end()){
                b = *it;
            }
            if (it != mp.begin()){
                it--;
                a = *it;
            }
            if (a == -inf && b == inf)
                ans[idx[i]] = -1;
            else if (pid-a <= b-pid)
                ans[idx[i]] = a;
            else
                ans[idx[i]] = b;
        }
        return ans;

    }
};












struct Block {
    // block 中最小的房间 size
    int min_size = INT_MAX;
    // block 中的房间 id
    vector<int> ids;
    // 原始数据
    vector<pair<int, int>> origin;

    Block() = default;

    // 加入一个房间
    void insert(int id, int size) {
        origin.emplace_back(id, size);
        ids.push_back(id);
        min_size = min(min_size, size);
    }

    // 添加完所有房间后，将房间 id 排序，便于后续二分
    void sort() {
        ::sort(ids.begin(), ids.end());
    }

    // 封装一下二分函数，找最小的大于等于它的
    int geq(int preferred) {
        auto it = lower_bound(ids.begin(), ids.end(), preferred);
        return it == ids.end() ? -1 : *it;
    }

    // 封装一下二分函数，找最大的严格小于它的
    int lt(int preferred) {
        auto it = upper_bound(ids.begin(), ids.end(), preferred);
        return it == ids.begin() ? -1 : *prev(it);
    }
};

class Solution {
private:
    static constexpr int BLOCK_SIZE = 300;

public:
    vector<int> closestRoom(vector<vector<int>>& rooms, vector<vector<int>>& queries) {
        int n = rooms.size();
        int q = queries.size();

        // 按照 size 升序排序
        sort(rooms.begin(), rooms.end(), [](const auto& r1, const auto& r2) { return r1[1] < r2[1]; });

        // 每 BLOCK_SIZE 个房间放进一个 block
        vector<Block> blocks;
        for (int i = 0; i < n; ++i) {
            if (i % BLOCK_SIZE == 0) {
                blocks.emplace_back();
            }
            blocks.back().insert(rooms[i][0], rooms[i][1]);
        }
        for (auto&& block: blocks) {
            block.sort();
        }

        vector<int> ans(q, -1);
        for (int i = 0; i < q; ++i) {
            int preferred = queries[i][0];
            int minsize = queries[i][1];
            int mindiff = INT_MAX;
            for (auto it_block = blocks.rbegin(); it_block != blocks.rend(); ++it_block) {
                auto&& block = *it_block;
                // block 中最小 size 的房间大于等于 minsize，整个 block 都可以选择
                if (block.min_size >= minsize) {
                    int c1 = block.geq(preferred);
                    if (c1 != -1 && c1 - preferred < mindiff) {
                        mindiff = c1 - preferred;
                        ans[i] = c1;
                    }
                    int c2 = block.lt(preferred);
                    if (c2 != -1 && preferred - c2 <= mindiff) {
                        mindiff = preferred - c2;
                        ans[i] = c2;
                    }
                }
                else {
                    // 只有部分都可以选择，遍历一下所有的房间
                    auto&& rooms = block.origin;
                    for (auto it_room = rooms.rbegin(); it_room != rooms.rend(); ++it_room) {
                        if (it_room->second >= minsize) {
                            int diff = abs(it_room->first - preferred);
                            if (diff < mindiff || (diff == mindiff && it_room->first < ans[i])) {
                                mindiff = diff;
                                ans[i] = it_room->first;
                            }
                        }
                        else {
                            break;
                        }
                    }
                    // 再之前的 block 一定都严格小于 minsize，可以直接退出
                    break;
                }
            }
        }
        return ans;
    }
};

