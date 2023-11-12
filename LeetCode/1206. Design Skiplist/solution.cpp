#include<iostream>
#include<string>
#include<set>
#include<time.h>
#include <limits.h>

using namespace std;
template<typename T>
struct Less {
    bool operator () (const T & a , const T & b) const {
        return a < b;
    }
};
template<typename K, typename V,typename Comp = Less<K>>
class skip_list {
protected:
    struct skip_list_node {
        int level;
        const K key;
        V value;
        skip_list_node** forward;
        skip_list_node() :key{ 0 }, value{ 0 }, level{ 0 }, forward{0} {}
        skip_list_node(K k, V v, int l, skip_list_node* nxt = nullptr) :key(k), value(v), level(l) {
            forward = new skip_list_node * [level + 1];
            for (int i = 0; i <= level; ++i) forward[i] = nxt;
        }
        ~skip_list_node() { delete[] forward; }
    };
    using node = skip_list_node;
    void init() {
        srand((uint32_t)time(NULL));
        level = length = 0;
        head->forward = new node * [MAXL + 1];
        for (int i = 0; i <= MAXL; i++)
            head->forward[i] = tail;
    }
    int randomLevel() {
        int lv = 1; while ((rand() & S) < PS) ++lv;
        return MAXL > lv ? lv : MAXL;
    }
    int level;
    int length;
    static const int MAXL = 32;
    static const int P = 4;
    static const int S = 0xFFFF;
    static const int PS = S / P;
    static const int INVALID = INT_MAX;
    node* head, * tail;
    Comp less;
    node* find(const K& key, node** update) {
        node* p = head;
        for (int i = level; i >= 0; i--) {
            while (p->forward[i] != tail && less(p->forward[i]->key, key)) {
                p = p->forward[i];
            }
            update[i] = p;
        }
        p = p->forward[0];
        return p;
    }
    
public:
    struct Iter {
        node* p;
        Iter() : p(nullptr) {};
        Iter(node* rhs) : p(rhs) {}
        node* operator ->()const { return (p);}
        node& operator *() const { return *p;}
        bool operator == (const Iter& rhs) { return rhs.p == p;}
        bool operator != (const Iter& rhs) {return !(rhs.p == p);}
        void operator ++() {p = p->forward[0];}
        void operator ++(int) { p = p->forward[0]; }
    };
   
    skip_list() : head(new node()), tail(new node()), less{Comp()} {
        init();    
    }
    skip_list(Comp _less) : head(new node()), tail(new node()),  less{_less} {
        init();
    }
    void debug() {
        for (int i = MAXL; i >= 0; i--) {
            node *p = head;
            while (p != tail)
            {
                cout << p->key << " ";
                p = p->forward[i];
            }
            cout << endl;
        }
    }

    void insert(const K& key, const V& value) {
        node * update[MAXL + 1];
        node* p = find(key,update);
        // if (p != tail && p->key == key) {
        //     p->value = value;
        //     return;
        // }
        int lv = randomLevel();
        if (lv > level) {
            lv = ++level;
            update[lv] = head;
        }
        node * newNode = new node(key, value, lv);
        for (int i = lv; i >= 0; --i) {
            p = update[i];
            newNode->forward[i] = p->forward[i];
            p->forward[i] = newNode;
        }
        ++length;
    }

    bool erase(const K& key) {
        node* update[MAXL + 1];
        node* p = find(key, update);
        if (p->key != key)return false;
        for (int i = 0; i <= p->level; ++i) {
            update[i]->forward[i] = p->forward[i];
        }
        delete p;
        while (level > 0 && head->forward[level] == tail) --level;
        --length;
        return true;
    }
    Iter find(const K&key) {
        node* update[MAXL + 1];
        node* p = find(key, update);
        if (p == tail)return tail;
        if (p->key != key)return tail;
        return Iter(p);
    }
    bool count(const K& key) {
        node* update[MAXL + 1];
        node* p = find(key, update);
        if (p == tail)return false;
        return key == p->key;
    }
    Iter end() {
        return Iter(tail);
    }   
    Iter begin() {
        return Iter(head->forward[0]);
    }
};

class Skiplist: public skip_list<int,int> {
public:
    Skiplist() : skip_list<int,int>() {

    }
    
    bool search(int target) {
        return count(target);
    }
    
    void add(int num) {
        insert(num,0);
    }
    
    bool erase(int num) {
        return skip_list<int,int>::erase(num);
    }

    void debug() {
        return skip_list<int,int>::debug();
    }
};



const int maxn = 20;
const int inf = 0x3f3f3f3f;

struct Node
{
    int val;
    vector<Node*> nxt;
    Node(int v)
        :val(v)
        {}
    Node(int v, int d)
        :val(v)
        {
            nxt.assign(d,nullptr);
        }
};


class Skiplist {
public:
    Node *head, *tail;
    Skiplist() {
        srand(time(NULL));
        head = new Node(-inf,maxn);
        tail = new Node(inf,maxn);
        for (int i = 0; i < maxn; i++)
            head->nxt[i] = tail;
    }

    bool flipcoin(){
        return (double)rand()/RAND_MAX > 0.5;
    }

    void iter(int target, vector<Node**> &pnxt){
        Node *cur = head;
        for (int i = maxn-1; i >= 0; i--){
            while (cur->nxt[i]->val < target)
                cur = cur->nxt[i];
            pnxt[i] = &(cur->nxt[i]);
        }
    }
    
    bool search(int target) {
        vector<Node**> pnxt(maxn);
        iter(target, pnxt);
        return (*pnxt[0])->val == target;
    }
    
    void add(int num) {
        vector<Node**> pnxt(maxn);
        iter(num, pnxt);
        Node *m = new Node(num);
        for (int i = 0; i < maxn; i++){
            if (i && !flipcoin())
                break;
            m->nxt.push_back(*pnxt[i]);
            *pnxt[i] = m;
        }
    }
    
    bool erase(int num) {
        vector<Node**> pnxt(maxn);
        iter(num, pnxt);
        Node *m = *pnxt[0];
        if (m->val != num)
            return false;
        for (int i = 0; i < maxn; i++){
            if (i == (m->nxt).size())
                break;
            *pnxt[i] = m->nxt[i];
        }
        delete m;
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */




const int maxn = 15;
const int inf = 0x3f3f3f3f;

struct Node
{
    int val;
    Node* nxt[maxn];
    Node(int v)
        :val(v)
        {
            memset(nxt, 0, maxn*sizeof(Node*));
        }
};


class Skiplist {
public:
    Node *head, *tail;
    Skiplist() {
        srand(time(NULL));
        head = new Node(-inf);
        tail = new Node(inf);
        for (int i = 0; i < maxn; i++)
            head->nxt[i] = tail;
    }

    bool flipcoin(){
        return (double)rand()/RAND_MAX > 0.5;
    }

    void iter(int target, Node** pnxt[]){
        Node *cur = head;
        for (int i = maxn-1; i >= 0; i--){
            while (cur->nxt[i]->val < target)
                cur = cur->nxt[i];
            pnxt[i] = &(cur->nxt[i]);
        }
    }
    
    bool search(int target) {
        Node** pnxt[maxn];
        iter(target, pnxt);
        return (*pnxt[0])->val == target;
    }
    
    void add(int num) {
        Node** pnxt[maxn];
        iter(num, pnxt);
        Node *m = new Node(num);
        for (int i = 0; i < maxn; i++){
            if (i && !flipcoin())
                break;
            m->nxt[i] = *pnxt[i];
            *pnxt[i] = m;
        }
    }
    
    bool erase(int num) {
        Node** pnxt[maxn];
        iter(num, pnxt);
        Node *m = *pnxt[0];
        if (m->val != num)
            return false;
        for (int i = 0; i < maxn; i++){
            if (!(m->nxt[i]))
                break;
            *pnxt[i] = m->nxt[i];
        }
        delete m;
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
