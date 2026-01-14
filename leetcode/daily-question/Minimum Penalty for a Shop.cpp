class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size();

        // Count total Y's initially (shop closed all day)
        int penalty = 0;
        for (char c : customers) {
            if (c == 'Y') penalty++;
        }

        int minPenalty = penalty;
        int ans = 0;

        // Move closing hour from 0 to n
        for (int j = 0; j < n; j++) {
            // hour j moves from closed → open
            if (customers[j] == 'Y')
                penalty--;   // Y no longer causes closed penalty
            else
                penalty++;   // N now causes open penalty

            if (penalty < minPenalty) {
                minPenalty = penalty;
                ans = j + 1;
            }
        }

        return ans;
    }
};
