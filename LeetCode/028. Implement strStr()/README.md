### brute force

recursion version
```c++
class Solution {
public:
    int stridx(string haystack, string needle,int a,int b,int idx,int len){
        if(b==needle.size())return idx;
        if(a==haystack.size())return -1;
        if(haystack[a]==needle[b]){
            a++;b++;len++;
            return stridx(haystack, needle, a, b, idx,len);
        }
        else{
            idx++;
            return stridx(haystack, needle, a-len+1, 0, idx, 0);
        }

    }
    int strStr(string haystack, string needle) {
        return stridx(haystack, needle, 0, 0, 0, 0);
    }
};

```

loop iteration version
```c++
class Solution {
public:

    int strStr(string haystack, string needle) {
        int idx=0,a=0,b=0,len=0;
        while(1){
            if(b==needle.size())return idx;
            if(a==haystack.size())return -1;
            while(haystack[a]==needle[b]){
                a++;b++;len++;
                if(b==needle.size())return idx;
            }
            idx++;
            a=a-len+1;
            b=0;len=0;
        }
    }
};

```
clean c code
```c
int strStr(char *haystack, char *needle) {
        if (!haystack || !needle) return -1;
        for (int i = 0; ; ++i) {
            for (int j = 0; ; ++j) {
                if (needle[j] == 0) return i;
                if (haystack[i + j] == 0) return -1;
                if (haystack[i + j] != needle[j]) break;
            }
        }
    }
```


### KMP
