class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        int n= words.size();
        vector<vector<string>> a;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
            if(j!=i)
            {
                for(int k=0;k<n;k++)
                if(k!=i && k!=j){
                    for(int l =0;l<n;l++)
                    if(l!=i && l!=j && l!=k){ 
                        if(words[i][0] == words[j][0] && words[i][3] == words[k][0] && words[l][0] == words[j][3] && words[l][3] == words[k][3]) {
                            a.push_back({words[i],words[j],words[k],words[l]});
                        }
                    }
                }
            }
        }
        sort(a.begin(),a.end());
        return a;
    }
};