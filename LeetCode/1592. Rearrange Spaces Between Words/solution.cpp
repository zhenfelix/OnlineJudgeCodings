class Solution {
public:
    string reorderSpaces(string text) {
        int cnt = 0;
        for (auto ch : text)
            cnt += (ch == ' ');
        string tmp;
        vector<string> words;
        text += ' ';
        for (auto ch : text){
            if (ch == ' '){
                if (!tmp.empty()){
                    words.push_back(tmp);
                    tmp = "";
                }
            }
            else{
                tmp.push_back(ch);
            }
        }
        int len = words.size();
        cout << len << endl;
        string space(len==1?0:cnt/(len-1), ' '), tail(len==1?cnt:cnt%(len-1), ' ');
        string ans;
        for (int i = 0; i < len; i++){
            // ans += words[i];
            // ans += i == len-1 ? tail : space;
            ans.append(words[i]);
            if (i == len-1)
                ans.append(tail);
            else
                ans.append(space);
        }
        return ans;

    }
};