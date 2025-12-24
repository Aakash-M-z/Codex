class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int res = 0,cnt = 1;
        int tota = accumulate(apple.begin(),apple.end(),0);
        sort(capacity.begin(), capacity.end(), greater<int>());

        for(int i = 0;i<capacity.size();i++){
            res += capacity[i];
            if(res < tota) cnt++;
        }        

        return cnt;
    }
};