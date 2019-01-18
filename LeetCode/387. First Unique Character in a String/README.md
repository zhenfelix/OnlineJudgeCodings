Hash table acceleration
```c++
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> m;
        for (auto &c : s) {
            m[c]++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (m[s[i]] == 1) return i;
        }
        return -1;
    }
};
```

```c++
class Solution {
public:
    int firstUniqChar(string s) {
        int length = s.length();
        int flags[256];
        for(int i = 0;i<256;++i){
            flags[i] = 0;
        }
        for(int i = 0;i<length;++i){
                int pos = (int)s[i];
                flags[pos] = flags[pos]+1;
        }
        for(int i = 0;i<length;++i){
            if(flags[(int)s[i]]==1){
                return i;
            }
        }
        return -1;
    }
};
```


```c++
class Solution {
    int letters[26] {};
public:
    int firstUniqChar(string s) {
        for(char c: s) letters[c-'a']++;
        for(int i=0;i<s.size();++i) if(letters[s[i]-'a']==1) return i;
        return -1;
    }
};
```
