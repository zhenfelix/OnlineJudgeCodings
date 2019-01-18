// class Solution {
// public:
//     vector<int> findAnagrams(string s, string p) {
//         vector<int> ans;
//         unordered_map<char,int> cnt;
//         set<char> pset;
//         int total=0;
//         for(auto ch: p){
//             cnt[ch]++;
//             pset.insert(ch);
//         }
//         int len1=s.length(),len2=p.length(),len=pset.size();
//         for(int i=0;i<len2;i++){
//             if(pset.count(s[i])){
//                 if(cnt[s[i]]==0)total--;
//                 cnt[s[i]]--;
//                 if(cnt[s[i]]==0)total++;
//             }
            
//         }
//         for(int i=0;i<len1-len2;i++){
//             if(total==len)ans.push_back(i);
//             if(pset.count(s[i])){
//                 if(cnt[s[i]]==0)total--;
//                 cnt[s[i]]++;
//                 if(cnt[s[i]]==0)total++;
//             }
            
//             if(pset.count(s[i+len2])){
//                 if(cnt[s[i+len2]]==0)total--;
//                 cnt[s[i+len2]]--;
//                 if(cnt[s[i+len2]]==0)total++;
//             }
//         }
//         if(total==len)ans.push_back(len1-len2);

//         return ans;
//     }
// };


// class Solution {
// public:
//  vector<int> findAnagrams(string s, string p) {
//      if (s.length() < p.length())
//          return {};
//      vector<int> count(26, 0), indices;
//      for (int index = 0; index < p.length(); ++index) {
//          ++count[s[index] - 'a'];
//          --count[p[index] - 'a'];
//      }
//      int sum = 0;
//      for (int i : count)
//          sum += i * i;
//      if (sum == 0)
//          indices.push_back(0);
//      for (int index = 1; index + p.length() <= s.length(); ++index) {
//          sum -= 2 * --count[s[index - 1] - 'a'] + 1;
//          sum += 2 * count[s[index - 1 + p.length()] - 'a']++ + 1;
//          if (sum == 0)
//              indices.push_back(index);
//      }
//      return indices;
//  }
// };

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> pv(26,0), sv(26,0), res;
        if(s.size() < p.size())
           return res;
        // fill pv, vector of counters for pattern string and sv, vector of counters for the sliding window
        for(int i = 0; i < p.size(); ++i)
        {
            ++pv[p[i]-'a'];
            ++sv[s[i]-'a'];
        }
        if(pv == sv)
           res.push_back(0);

        //here window is moving from left to right across the string. 
        //window size is p.size(), so s.size()-p.size() moves are made 
        for(int i = p.size(); i < s.size(); ++i) 
        {
             // window extends one step to the right. counter for s[i] is incremented 
            ++sv[s[i]-'a'];
            
            // since we added one element to the right, 
            // one element to the left should be forgotten. 
            //counter for s[i-p.size()] is decremented
            --sv[s[i-p.size()]-'a']; 

            // if after move to the right the anagram can be composed, 
            // add new position of window's left point to the result 
            if(pv == sv)  
               res.push_back(i-p.size()+1);
        }
        return res;
    }
};
