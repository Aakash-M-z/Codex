import java.util.*;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g); // sort children greed
        Arrays.sort(s); // sort cookies

        int i = 0, j = 0;
        int res = 0;

        while (i < g.length && j < s.length) {
            if (s[j] >= g[i]) {
                res++;   // child is happy
                i++;     // next child
                j++;     // next cookie
            } else {
                j++;     // cookie too small
            }
        }
        return res;
    }
}
