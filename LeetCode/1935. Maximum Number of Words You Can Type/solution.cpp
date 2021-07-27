class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
       vector<bool> broken(26, false);
       for (auto ch : brokenLetters){
        broken[ch-'a'] = true;
       }
       int res = 0, cnt = 0;
       for (auto ch : text){
        if (ch == ' '){
            res += (cnt == 0);
            cnt = 0;
        }
        else{
            cnt += (broken[ch-'a']);
        }
       }
       return res + (cnt==0);
    }
};