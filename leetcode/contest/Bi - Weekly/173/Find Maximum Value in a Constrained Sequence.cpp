class Solution {
public:
    int findMaxVal(int n, vector<vector<int>>& restrictions, vector<int>& diff) {
        vector<long long> a(n,LLONG_MAX);
        a[0] = 0;
        int res = 0;
        for(auto &it : restrictions){
            if(a[it[0]] > it[1]) a[it[0]] = it[1];
        }

        for(int i=1;i<n;i++){
            if(a[i] > a[i-1] + diff[i-1]) a[i] = a[i-1] + diff[i-1];
        }

        for(int i= n-2;i>=0;i--){
            if(a[i] > a[i+1] + diff[i]) a[i] = a[i+1] + diff[i];
        }

        for(int it : a){
            if(it > res) res = it; 
        }

        return res;
    }
};