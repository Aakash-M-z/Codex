class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& target) {
        unordered_set<int> a;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]!=target[i]){
                a.insert(nums[i]);
            }
        }
        return a.size();
        
    }
};