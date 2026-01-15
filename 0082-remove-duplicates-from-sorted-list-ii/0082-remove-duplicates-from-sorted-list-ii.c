/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode  *temp=head;
    struct ListNode *prev = malloc(sizeof(struct ListNode));
    struct ListNode *connect = malloc(sizeof(struct ListNode));
    struct ListNode *dummy;
    prev->val=0;
    prev->next=head;
    dummy=prev;
    while(temp!=NULL){
        if (temp->next !=NULL && temp->val==temp->next->val){
            connect->val=temp->val;
            while(temp->next !=NULL && temp->next->val==connect->val){
                temp=temp->next;
            }
            prev->next=temp->next;
            temp=prev->next;
        }
        else{
            prev=temp;
            temp=temp->next;
        }
    }
    return dummy->next;
}