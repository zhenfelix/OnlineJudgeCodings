class Solution {
public:
    bool checkIfPangram(string sentence) {
        set<char> ss;
        for (char ch : sentence)
            ss.insert(ch);
        return ss.size() == 26;
    }
};


    
class Solution {
public:
    bool checkIfPangram(string s) {
        return set<char>(s.begin(), s.end()).size() == 26;
    }

};