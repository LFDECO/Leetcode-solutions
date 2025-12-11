/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* todelete;
    struct ListNode *temp=head;
    struct ListNode *temp1=head;
    int count=0;
    while(temp1!=NULL){
        count++;
        temp1=temp1->next;
    }
    int pos=(count-n)+1;
    if(pos==1){
        todelete=head;
        head=head->next;
        free(todelete);
        return head;
    }
    if (pos==count){
        while(temp!=NULL){
            if (temp->next->next==NULL){
                todelete=temp->next;
                temp->next=NULL;
                free(todelete);
                return head;
                break;
            }
            temp=temp->next;
        }
    }
    for(int i=1;i<(pos-1);i++){
        temp=temp->next;
    }
    todelete=temp->next;
    temp->next=todelete->next;
    free(todelete);
    return head;
}