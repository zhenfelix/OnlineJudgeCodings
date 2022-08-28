class Node {
public:
    int val;
    Node *pre, *nxt;

    Node(int val): val(val), pre(this), nxt(this){}
};

class MyCircularDeque {
public:
    int k, sz;
    Node *dummy;
    MyCircularDeque(int k): k(k), sz(0) {
        dummy = new Node(-1);
    }
    
    bool insertFront(int value) {
        if (isFull()) return false;
        Node *nxt = dummy->nxt;
        Node *cur = new Node(value);
        dummy->nxt = cur;
        cur->pre = dummy;
        nxt->pre = cur;
        cur->nxt = nxt;
        sz++;
        return true;
    }
    
    bool insertLast(int value) {
        if (isFull()) return false;
        Node *pre = dummy->pre;
        Node *cur = new Node(value);
        dummy->pre = cur;
        cur->nxt = dummy;
        pre->nxt = cur;
        cur->pre = pre;
        sz++;
        return true;
    }
    
    bool deleteFront() {
        if (isEmpty()) return false;
        Node* cur = dummy->nxt;
        Node* nxt = cur->nxt;
        dummy->nxt = nxt;
        nxt->pre = dummy;
        delete cur;
        sz--;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()) return false;
        Node* cur = dummy->pre;
        Node* pre = cur->pre;
        dummy->pre = pre;
        pre->nxt = dummy;
        delete cur;
        sz--;
        return true;
    }

    int getFront() {
        if (isEmpty()) return -1;
        return dummy->nxt->val;
    }
    
    int getRear() {
        if (isEmpty()) return -1;
        return dummy->pre->val;
    }
    
    bool isEmpty() {
        return sz == 0;
    }
    
    bool isFull() {
        return sz == k;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */