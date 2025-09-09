// Last updated: 09/09/2025, 14:20:21
int lengthOfLastWord(char* s) {
    int len = strlen(s);
    int i = len - 1;

    // Step 1: Skip trailing spaces
    while (i >= 0 && s[i] == ' ') {
        i--;
    }

    // Step 2: Count the length of the last word
    int count = 0;
    while (i >= 0 && s[i] != ' ') {
        count++;
        i--;
    }

    return count;
}