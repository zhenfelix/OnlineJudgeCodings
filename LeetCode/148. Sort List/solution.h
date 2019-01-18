// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode(int x) : val(x), next(NULL) {}
//  * };
//  */
// class Solution {
// public:
//     ListNode* mergeList(ListNode* left, ListNode *right){
//         if((!left)||(!right))return left==NULL?right:left;
//         if(left->val<=right->val){
//             left->next=mergeList(left->next,right);
//             return left;
//         }
//         else{
//             right->next=mergeList(left,right->next);
//             return right;
//         }
//     }
//     ListNode* midList(ListNode* head){
//         ListNode *slow=head, *fast=head, *pre=head;;
//         while(fast&&fast->next){
//             fast=fast->next->next;
//             pre=slow;
//             slow=slow->next;
//         }
//         pre->next=NULL;
//         return slow;
//     }

//     ListNode* sortList(ListNode* head) {
//         if(!head)return head;
//         ListNode* mid=midList(head);
//         if(mid==head)return head;
//         ListNode *left=sortList(head);
//         ListNode *right=sortList(mid);
//         return mergeList(left,right);
//     }
// };

class Solution{
public:
  ListNode* sortList(ListNode* head){
      bool done = (!head);
    // Keep partitioning our list into bigger sublists length. Starting with a size of 1 and doubling each time
    for (int step = 1; !done; step *= 2) {
      done = true;
      ListNode** next_ptr = &head;
      ListNode* remaining = head;
      ListNode* list[2];
      do {
        // Split off two sublists of size step
        for (auto& sub_head : list) {
          sub_head = remaining;
          ListNode* tail = nullptr;
          for (int i = 0; i < step && remaining; ++i, remaining = remaining->next) {
            tail = remaining;
          }
          // Terminate our sublist
          if (tail) {
            tail->next = nullptr;
          }
        }

        // We're done if these are the first two sublists in this pass and they
        // encompass the entire primary list
        done &= !remaining;

        // If we have two sublists, merge them into one
        if (list[1]) {
          while (list[0] || list[1]) {
            int idx = (!list[1] || list[0] && list[0]->val <= list[1]->val) ? 0 : 1;
            *next_ptr = list[idx];
            list[idx] = list[idx]->next;
            next_ptr = &(**next_ptr).next;
          }

          // Terminate our new sublist
          *next_ptr = nullptr;
        } else {
          // Only a single sublist, no need to merge, just attach to the end
          *next_ptr = list[0];
        }
      } while (remaining);
    }
    return head;
  }  
    
};

//c++ and java, legit solution. O(nlogn) time and O(1) space! No recursion! With detailed explaination
//https://leetcode.com/problems/sort-list/discuss/166324/c++-simple-legitimate-solution.-O(nlogn)-time-and-O(1)-space.-No-recursion!-With-explaination