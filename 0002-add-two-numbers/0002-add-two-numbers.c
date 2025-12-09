/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *reshead=NULL;
    struct ListNode *restail=NULL;
    struct ListNode *temp1=l1;
    struct ListNode *temp2=l2;
    int carry=0;
    while(temp1!=NULL || temp2!=NULL || carry !=0){
        int a,b;
        struct ListNode *res=malloc(sizeof(struct ListNode));
        if(temp1==NULL){
            a=0;
        }else{
            a=temp1->val;
        }
        if(temp2==NULL){
            b=0;
        }else{
            b=temp2->val;
        }
        if((a+b+carry)>=10){
            res->val=(a+b+carry)%10;
            carry=(a+b+carry)/10;
            res->next=NULL;
            if(reshead==NULL){
                reshead=res;
                restail=res;
            }else{
                restail->next=res;
                restail=res;
            }
        }else{
            res->val=a+b+carry;
            carry=0;
            res->next=NULL;
            if(reshead==NULL){
                reshead=res;
                restail=res;
            }else{
                restail->next=res;
                restail=res;
            }
        }
       if(temp1!=NULL) temp1=temp1->next;
       if(temp2!=NULL) temp2=temp2->next; 
    }
    return reshead;
}