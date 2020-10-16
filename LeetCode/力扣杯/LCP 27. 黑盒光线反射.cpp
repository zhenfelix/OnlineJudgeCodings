class BlackBox {
private:
    // 存储从每个小孔以 y=x 方向射出时，所在的循环的 id 以及在循环中的 id
    vector<pair<int, int>> groupPos;
    // 存储从每个小孔以 y=-x 方向射出时，所在的循环的 id 以及在循环中的 id
    vector<pair<int, int>> groupNeg;
    // 存储每个循环的有序映射
    vector<map<int, int>> groupStats;

public:
    BlackBox(int n, int m) {
        int ptCount = (n + m) * 2;
        groupPos.assign(ptCount, {-1, -1});
        groupNeg.assign(ptCount, {-1, -1});
        for (int i = 0; i < ptCount; ++i) {
            // 如果不是左上角或者右下角的小孔，那么从 y=x 方向射出找循环
            if (i != 0 && i != m + n && groupPos[i].first == -1) {
                createGroup(n, m, i, 1);
            }
            // 如果不是左下角或者右上角的小孔，那么从 y=-x 方向射出找循环
            if (i != m && i != m * 2 + n && groupNeg[i].first == -1) {
                createGroup(n, m, i, -1);
            }
        }
    }

    void createGroup(int n, int m, int index, int direction) {
        int groupId = groupStats.size();
        int groupLoc = 0;
        groupStats.emplace_back();
        // 不断模拟光线的路径，直到走到一个已经遇见过的状态，这样就找到了一个循环
        while (!(direction == 1 && groupPos[index].first != -1) && !(direction == -1 && groupNeg[index].first != -1)) {
            if (direction == 1) {
                groupPos[index] = {groupId, groupLoc++};
                index = (n + m) * 2 - index;
            }
            else {
                groupNeg[index] = {groupId, groupLoc++};
                if (index <= m * 2) {
                    index = m * 2 - index;
                }
                else {
                    index = (m * 2 + n) * 2 - index;
                }
            }
            // 如果小孔不在角上，就改变方向
            if (index != 0 && index != m && index != m + n && index != m * 2 + n) {
                direction = -direction;
            }
        }
    }
    
    int open(int index, int direction) {
        // 插入二元组
        if (auto [groupId, groupLoc] = groupPos[index]; groupId != -1) {
            groupStats[groupId].emplace(groupLoc, index);
        }
        if (auto [groupId, groupLoc] = groupNeg[index]; groupId != -1) {
            groupStats[groupId].emplace(groupLoc, index);
        }

        // 查询
        auto [groupId, groupLoc] = (direction == 1 ? groupPos[index] : groupNeg[index]);
        auto& store = groupStats[groupId];
        if (auto iter = store.upper_bound(groupLoc); iter != store.end()) {
            return iter->second;
        }
        else {
            return store.begin()->second;
        }
    }
    
    void close(int index) {
        // 删除二元组
        if (auto [groupId, groupLoc] = groupPos[index]; groupId != -1) {
            groupStats[groupId].erase(groupLoc);
        }
        if (auto [groupId, groupLoc] = groupNeg[index]; groupId != -1) {
            groupStats[groupId].erase(groupLoc);
        }
    }
};

