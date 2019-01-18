class Solution {
public:
    bool isAnagram(string s, string t) {
        int len1=s.size();
        int len2=t.size();
        vector<int> vec(26, 0);
        if(len1!=len2)return false;
        for(int i=0;i<len1;i++){
            vec[s[i]-'a']++;
            vec[t[i]-'a']--;
        }
        for(int i=0;i<vec.size();i++){
            if(vec[i]!=0)return false;
        }
        return true;
    }
};