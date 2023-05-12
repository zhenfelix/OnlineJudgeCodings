#include<vector>
#include<iostream>

using namespace std;

struct Node {
    int val;
    Node *nxt;
    Node(int v): val(v), nxt(nullptr) {}
    Node() = default;
};

void printList(Node *head) {
    while (head) {
        cout << head->val << ' ';
        head = head->nxt;
    }
    cout << endl;
    return;
}

Node* constructList(vector<int> &arr) {
   Node* dummy = new Node();
   Node* cur = dummy;
   for (auto &a : arr) {
    cur->nxt = new Node(a);
    cur = cur->nxt;
   }
   return dummy->nxt;
}

Node* reverse_list_k (Node *head, int k) {
    Node *dummy = new Node();
    dummy->nxt = head;
    Node *tail = dummy, *cur = head, *pre, *nxt;
    while (cur) {
        Node *t = cur;
        int i;
        for (i = 0, pre = nullptr; cur && i < k; i++) {
            nxt = cur->nxt;
            cur->nxt = pre;
            pre = cur;
            cur = nxt;
        }
        tail->nxt = pre;
        tail = t;
    }
    return dummy->nxt;

}

int main() {
    vector<int> arr {1,2,3,4,5,6,7,8};
    Node *head = constructList(arr);
    printList(head);
    head = reverse_list_k(head,3);
    printList(head);
    return 0;
}