class TextEditor {
public:
    list<char> text;
    list<char>::iterator cur;
    TextEditor() {
        text.push_back('^');
        text.push_back('$');
        cur = text.end();
        cur--;
        // cout << *cur << endl;
    }
    
    void addText(string s) {
        for (auto ch : s)
            text.insert(cur, ch);
        // debug();
    }
    
    int deleteText(int k) {
        cur--;
        int cnt = 0;
        while (*cur != '^' && k){
            k--;
            cnt++;
            cur--;
        }
        cur++;
        for (int i = 0; i < cnt; i++)
            cur = text.erase(cur);
        // debug();
        return cnt;
    }
    
    string cursorLeft(int k) {
        while (k && *prev(cur) != '^')
            cur--,k--;
        return display();
    }
    
    string cursorRight(int k) {
        while (k && *cur != '$')
            cur++,k--;
        return display();
    }

    string display(){
        // debug();
        auto it = prev(cur);
        for (int i = 0; i < 10 && *it != '^'; it--, i++);
        it++;
        string ans;
        for (; it != cur; it++)
            ans.push_back(*it);
        return ans;
    }

    void debug(){
        for (auto it = text.begin(); it != text.end(); it++)
            cout << *it ;
        cout << endl;
        cout << *cur << endl;
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */




class TextEditor {
    list<char> lst;
    list<char>::iterator cur;

    string print() {
        string ret;
        auto it = cur;
        for (int i = 0; i < 10; i++) {
            if (it == lst.begin()) break;
            it = prev(it);
            ret.push_back(*it);
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }

public:
    TextEditor() {
        cur = lst.begin();
    }
    
    void addText(string text) {
        for (char c : text) lst.insert(cur, c);
    }
    
    int deleteText(int k) {
        int ret = 0;
        while (k && cur != lst.begin()) {
            cur = prev(cur);
            cur = lst.erase(cur);
            k--; ret++;
        }
        return ret;
    }
    
    string cursorLeft(int k) {
        while (k && cur != lst.begin()) {
            cur = prev(cur);
            k--;
        }
        return print();
    }
    
    string cursorRight(int k) {
        while (k && cur != lst.end()) {
            cur = next(cur);
            k--;
        }
        return print();
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/twBVIo/view/D3cCpt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class TextEditor {
    list<char> l;
    list<char>::iterator cur = l.begin();

public:
    TextEditor() {}

    void addText(string text) {
        for (char ch : text)
            l.insert(cur, ch);
    }

    int deleteText(int k) {
        int k0 = k;
        for (; k && cur != l.begin(); --k)
            cur = l.erase(prev(cur));
        return k0 - k;
    }

    string text() {
        string s;
        auto it = cur;
        for (int k = 10; k && it != l.begin(); --k) {
            it = prev(it);
            s += *it;
        }
        reverse(s.begin(), s.end());
        return s;
    }

    string cursorLeft(int k) {
        for (; k && cur != l.begin(); --k)
            cur = prev(cur);
        return text();
    }

    string cursorRight(int k) {
        for (; k && cur != l.end(); --k)
            cur = next(cur);
        return text();
    }
};


作者：endlesscheng
链接：https://leetcode.cn/problems/design-a-text-editor/solution/lian-biao-mo-ni-pythonjavacgo-by-endless-egw4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。