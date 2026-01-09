/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void f(TreeNode*  root, long long &sum){
        if(root==nullptr)
        return;
        sum+=root->val;
        f(root->left,sum);
        f(root->right,sum);
    }
    long long g(TreeNode* root, long long &ans ,long long &sum){

        if(root==nullptr)
        return 0;
        int mod=1e9+7;
        int valleft=g(root->left,ans, sum);
        ans=max(ans,(1LL*(valleft)*(sum-valleft)));

        int valR=g(root->right,ans, sum);
        ans=max(ans,((1LL*valR*(sum-valR))));


        return root->val+valleft+valR;

    }
    int maxProduct(TreeNode* root) {
        long long sum=0;
        long long ans=0;
        f(root,sum);
        g(root,ans,sum);
        int mod=1e9+7;
        return ans%mod;
    }
};