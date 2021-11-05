/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *dummy = new ListNode();
        ListNode *head = dummy;
        auto compare = [&](int a, int b) { return lists[a]->val > lists[b]->val; };
        priority_queue<int, vector<int>, decltype(compare)> pq(compare);
        int n = lists.size();
        for (int i = 0; i < n; i++) if(lists[i]) pq.push(i);
        while (!pq.empty()){
            int i = pq.top(); pq.pop();
            head->next = lists[i];
            head = head->next;
            lists[i] = head->next;
            if (lists[i])
                pq.push(i);
        }
        return dummy->next;
    }
};