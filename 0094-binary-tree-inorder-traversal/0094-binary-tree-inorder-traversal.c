/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void countNodes(struct TreeNode* root, int* count) {
    if (root == NULL) return;

    countNodes(root->left, count);
    (*count)++;
    countNodes(root->right, count);
}

void fillArray(struct TreeNode* root, int* arr, int* index) {
    if (root == NULL) return;

    fillArray(root->left, arr, index);
    arr[*index] = root->val;
    (*index)++;
    fillArray(root->right, arr, index);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;

    // First pass: count nodes
    countNodes(root, returnSize);

    // Allocate result array
    int* arr = malloc((*returnSize) * sizeof(int));
    if (arr == NULL) return NULL;

    // Second pass: fill array
    int index = 0;
    fillArray(root, arr, &index);

    return arr;
}