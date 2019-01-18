#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;


// class Solution {
// public:
//     bool isPalindrome(string s) {
//         int n=0;
//         for(int i=0;i<s.size();i++){
//             if((s[i]>='a'&& s[i]<='z')||(s[i]>='0'&& s[i]<='9'))s[n++]=s[i];
//             else if(s[i]>='A'&& s[i]<='Z')s[n++]=s[i]-'A'+'a';
//         }
//         for(int i=0;i<n/2;i++){
//             if(s[i]!=s[n-1-i])return false;
//         }
//         return true;
//     }
// };

class Solution {
public:
    
bool isPalindrome(string s) {
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) { // Move 2 pointers from each end until they collide
        while (isalnum(s[i]) == false && i < j) i++; // Increment left pointer if not alphanumeric
        while (isalnum(s[j]) == false && i < j) j--; // Decrement right pointer if no alphanumeric
        if (toupper(s[i]) != toupper(s[j])) return false; // Exit and return error if not match
    }
    
    return true;
}
};

