// class Solution {
// public:
//     vector<vector<string>> groupAnagrams(vector<string>& strs) {
//         unordered_map<string, vector<string>> mp;
//         for (string s : strs) {
//             string t = s; 
//             sort(t.begin(), t.end());
//             mp[t].push_back(s);
//         }
//         vector<vector<string>> anagrams;
//         for (auto m : mp) { 
//             // vector<string> anagram(m.second.begin(), m.second.end());
//             anagrams.push_back(m.second);
//         }
//         return anagrams;
//     }
// };

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<int, vector<string>> mp;
        vector<vector<string>> anagrams;
        vector<int> primes{2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107};
        for(auto str: strs){
            int hash=1;
            for(int i=0;i<str.length();i++)hash*=primes[str[i]-'a'];
            mp[hash].push_back(str);
        }
        for(auto m: mp)anagrams.push_back(m.second);
        return anagrams;
    }
};