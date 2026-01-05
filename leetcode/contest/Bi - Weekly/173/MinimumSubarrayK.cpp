class Solution {
public:
    int minLength(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> cnt;
        int l=0,res = INT_MAX;
        int sm = 0;
        for(int i=0;i<n;i++){
            if(cnt[nums[i]] == 0) sm+=nums[i];
            cnt[nums[i]]++;

            while(sm >= k){
                res = min(res , i-l+1);
                cnt[nums[l]]--;

                if(cnt[nums[l]] == 0) sm -= nums[l];
                l++;
            }
        }

        if(res == INT_MAX) return -1;
        return res;
    }
};