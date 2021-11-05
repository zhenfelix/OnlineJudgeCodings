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
