/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    struct ListNode* temp=head;
    struct ListNode* temp1=head;
    struct ListNode* temp2=head;
    int n=0;
    while(temp!=NULL){
        n++;
        if (temp->next==NULL){
            temp->next=head;
            break;
        }
        temp=temp->next;
    }
    if (n>0){
        k=k%n;
    }
    if (head==NULL){
        return head;
    }
    if(head->next==NULL){
        return head;
    }
    for (int i = 1; i < (n-k) ; i++){
       temp1=temp1->next;
    }
    head=temp1->next;
    temp1->next=NULL;
    return head;
}