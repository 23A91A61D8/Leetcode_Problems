// Last updated: 09/09/2025, 14:20:41
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> lastSeen; 
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.size(); right++) {
            char c = s[right];

        
            if (lastSeen.find(c) != lastSeen.end() && lastSeen[c] >= left) {
                left = lastSeen[c] + 1; 
            }

            lastSeen[c] = right; 
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};