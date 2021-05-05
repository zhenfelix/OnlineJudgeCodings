class Solution
{
public:
    string reverseStr(string s, int k)
    {
        int cur = 0, n = s.length();
        while (cur < n)
        {
            reverse(s.begin() + cur, s.begin() + min(cur + k, n));
            cur += k * 2;
        }
        return s;
    }
};
