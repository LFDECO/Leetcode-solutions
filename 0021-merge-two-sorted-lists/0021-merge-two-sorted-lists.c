/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* reshead=NULL;
    struct ListNode* restail=NULL;
    struct ListNode* temp1=list1;
    struct ListNode* temp2=list2;
    struct ListNode* temp3=list1;
    struct ListNode* temp4=list2;
    int count1=0;
    int count2=0;
    int count3=0;
    int temp;
    while(temp1!=NULL){
        count1++;
        temp1=temp1->next;
    }
    
    while(temp2!=NULL){
        count2++;
        temp2=temp2->next;
    }
    
    int rescount=count1+count2;
    if (rescount == 0) return NULL;
    int *arr = malloc((size_t)rescount * sizeof(int));
    while(temp3!=NULL){
        arr[count3]=temp3->val;
        count3++;
        temp3=temp3->next;
    }
    while(temp4!=NULL){
        arr[count3]=temp4->val;
        count3++;
        temp4=temp4->next;
    }
    for(int i = 0; i < rescount - 1; i++) {
        for(int j = 0; j < rescount - i - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    for(int i=0;i<rescount;i++){
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=arr[i];
        newnode->next=NULL;
        if(reshead==NULL){
            reshead=newnode;
            restail=newnode;
        }else{
            restail->next=newnode;
            restail=newnode;
        }
    }
    return reshead;
}