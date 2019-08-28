class TrieNode{
    
public:
    bool isEnd;
    TrieNode *p[26];
    TrieNode(){
        isEnd=false;
        memset(p,0,sizeof(p));
    }
};

class Trie {
private:
    TrieNode *root;
public:
    /** Initialize your data structure here. */
    Trie() {
        root=new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *cur=root;
        for(int i=0;i<word.length();i++){
            if(cur->p[word[i]-'a']==NULL)cur->p[word[i]-'a']=new TrieNode();
            cur=cur->p[word[i]-'a'];
        }
        cur->isEnd=true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *cur=root;
        for(int i=0;i<word.length();i++){
            if(cur->p[word[i]-'a']==NULL)return false;
            cur=cur->p[word[i]-'a'];
        }
        if(cur->isEnd)return true;
        return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *cur=root;
        for(int i=0;i<prefix.length();i++){
            if(cur->p[prefix[i]-'a']==NULL)return false;
            cur=cur->p[prefix[i]-'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */