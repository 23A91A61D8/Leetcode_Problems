// Last updated: 30/06/2026, 21:41:00
class Solution {
    public char kthCharacter(int k) {
        StringBuilder word = new StringBuilder("a");

        while (word.length() < k) {
            StringBuilder next = new StringBuilder();
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                // next character in alphabet, wrap around 'z' → 'a'
                char nextChar = (char) ((c == 'z') ? 'a' : (c + 1));
                next.append(nextChar);
            }
            word.append(next);
        }

        return word.charAt(k - 1);
    }
}
