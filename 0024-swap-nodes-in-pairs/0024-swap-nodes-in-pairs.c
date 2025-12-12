/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
 if (head == NULL || head->next == NULL)
        return head;

    struct ListNode *prev = NULL;
    struct ListNode *curr = head;
    head = head->next;  

    while (curr != NULL && curr->next != NULL) {
        struct ListNode *next = curr->next;
        struct ListNode *after = next->next;

        next->next = curr;
        curr->next = after;
        if (prev != NULL)
            prev->next = next;

        prev = curr;
        curr = after;
    }

    return head;
}