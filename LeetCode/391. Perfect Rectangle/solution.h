class Solution {
private:
    struct comp {
        bool operator () (const pair<int, int>& a, const pair<int, int>& b) { return a.second <= b.first; }
    };
    
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        int area = 0, xmin = INT_MAX, ymin = INT_MAX, xmax = INT_MIN, ymax = INT_MIN;
        vector<vector<int>> verticalEdges;  // x, insertion/deletion event, ysmall, ylarge
        multiset<pair<int, int>, comp> s;   // for detecting overlaps
        
        // Calculate area, and configure verticalEdges
        for (auto v : rectangles) {
            area += (v[2] - v[0]) * (v[3] - v[1]);
            xmin = min(xmin, v[0]), ymin = min(ymin, v[1]), xmax = max(xmax, v[2]), ymax = max(ymax, v[3]);
            verticalEdges.push_back({v[0], 1, v[1], v[3]}), verticalEdges.push_back({v[2], -1, v[1], v[3]});
        }
        if (area != (xmax - xmin) * (ymax - ymin)) { return false; }
        
        // Check if any overlap exists
        sort(verticalEdges.begin(), verticalEdges.end());
        for (auto v : verticalEdges) {
            auto it = s.find(make_pair(v[2], v[3]));
            if (v[1] > 0) {                             // left edge, insertion event
                if (it != s.end()) { return false; }    // found an overlap
                s.insert(make_pair(v[2], v[3]));
            } else {                                    // right edge, deletion event
                s.erase(it);
            }
        }
        return true;
    }
};