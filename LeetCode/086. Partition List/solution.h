/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *left=new ListNode(0), *right=new ListNode(0);
        ListNode *tail_left=left, *tail_right=right;
        while(head!=nullptr){
            if(head->val<x){
                tail_left->next=head;
                tail_left=head;
            }
            else{
                tail_right->next=head;
                tail_right=head;
            }
            head=head->next;
        }
        tail_left->next=right->next;
        tail_right->next=nullptr;
        return left->next;
    }
};