// Last updated: 09/09/2025, 14:17:49
class Solution {
public:
    int kthFactor(int n, int k) {
        vector<int> factors;
        for (int i = 1; i * i <= n; ++i) {
            if (n % i == 0) {
                factors.push_back(i);  // Store the smaller factor
                if (i != n / i) {      // Avoid duplicate when i == n / i
                    factors.push_back(n / i);
                }
            }
        }
        sort(factors.begin(), factors.end());  // Ensure sorted order
        
        return (k <= factors.size()) ? factors[k - 1] : -1;  // Return kth factor or -1 if out of range
    }
};
