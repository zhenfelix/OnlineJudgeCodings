/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    unordered_map<Node*,Node*> old2new;
    Node* copyRandomList(Node* head) {
        if(head==nullptr)return head;
        Node *newhead=new Node(head->val);
        old2new[head]=newhead;
        newhead->next=copyRandomList(head->next);
        newhead->random=old2new[head->random];
        return newhead;
    }
};


// A solution with constant space complexity O(1) and linear time complexity O(N)
// https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
// JAVA
// public RandomListNode copyRandomList(RandomListNode head) {
//   RandomListNode iter = head, next;

//   // First round: make copy of each node,
//   // and link them together side-by-side in a single list.
//   while (iter != null) {
//     next = iter.next;

//     RandomListNode copy = new RandomListNode(iter.label);
//     iter.next = copy;
//     copy.next = next;

//     iter = next;
//   }

//   // Second round: assign random pointers for the copy nodes.
//   iter = head;
//   while (iter != null) {
//     if (iter.random != null) {
//       iter.next.random = iter.random.next;
//     }
//     iter = iter.next.next;
//   }

//   // Third round: restore the original list, and extract the copy list.
//   iter = head;
//   RandomListNode pseudoHead = new RandomListNode(0);
//   RandomListNode copy, copyIter = pseudoHead;

//   while (iter != null) {
//     next = iter.next.next;

//     // extract the copy
//     copy = iter.next;
//     copyIter.next = copy;
//     copyIter = copy;

//     // restore the original list
//     iter.next = next;

//     iter = next;
//   }

//   return pseudoHead.next;
// }