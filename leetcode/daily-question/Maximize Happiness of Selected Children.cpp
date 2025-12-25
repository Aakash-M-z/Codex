class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        long long res = 0;
        int c = 0;
        sort(happiness.begin(), happiness.end(), greater<int>());
        for(int i = 0;i<k;i++){
            if(happiness[i] > 1) res += max(happiness[i] - c , 0);
            c++;
                    }

        if (res) return res;
        return 1;
    }
};