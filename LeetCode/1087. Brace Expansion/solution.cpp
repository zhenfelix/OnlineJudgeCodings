class Solution {
public:
    vector<string> expand(string s) {
        vector<string> res = {""};
        vector<char> candidates;
        int cnt = 0;
        for (auto ch : s){
            if (ch == ',')
                continue;
            else if (ch == '{')
                cnt++;
            else if (ch == '}')
                cnt--;
            else
                candidates.push_back(ch);
            if (cnt == 0){
                sort(candidates.begin(), candidates.end());
                vector<string> tmp;
                for (auto ss : res){
                    for (auto ch : candidates){
                        tmp.push_back(ss+ch);
                    }
                }
                swap(res,tmp);
                candidates.clear();
            }
        }
        return res;
    }
};