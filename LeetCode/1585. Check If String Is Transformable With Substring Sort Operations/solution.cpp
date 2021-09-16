class Solution
{
public:
    bool isTransformable(string s, string t)
    {
        int n = s.length();
        vector<vector<int>> pos(10);
        for (int i = n - 1; i >= 0; i--)
            pos[s[i] - '0'].push_back(i);
        for (auto ch : t)
        {
            int x = ch - '0';
            if (pos[x].empty())
                return false;
            int rank = pos[x].back();
            for (int r = 0; r < x; r++)
                if (!pos[r].empty() && pos[r].back() < rank)
                    return false;
            pos[x].pop_back();
        }
        return true;
    }
};