/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    struct ListNode * temp = head;
    struct ListNode * temp1 = head;
    struct ListNode * dummy = NULL;
    struct ListNode * dummy1; // after right
    struct ListNode * dummy2 = NULL; // before left
    struct ListNode * dummy3; // original left

    for (int i = 1; i < left; i++) {
        dummy2 = temp;
        temp = temp->next;
    }
    dummy3 = temp;

    for (int i = 1; i < right; i++) {
        temp1 = temp1->next;
    }
    dummy1 = temp1->next;

    if (dummy2 != NULL) dummy2->next = NULL;
    temp1->next = NULL;

    while (temp != NULL) {
        struct ListNode * next = temp->next;
        temp->next = dummy;
        dummy = temp;
        temp = next;
    }

    if (dummy2 != NULL) dummy2->next = dummy;
    else head = dummy;

    dummy3->next = dummy1;

    return head;
}
