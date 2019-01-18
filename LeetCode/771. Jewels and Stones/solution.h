class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int cnt=0;
        set<char> s;
        for(int i=0;i<J.length();i++)s.insert(J[i]);
        for(int i=0;i<S.length();i++)if(s.count(S[i]))cnt++;
        return cnt;
    }
};