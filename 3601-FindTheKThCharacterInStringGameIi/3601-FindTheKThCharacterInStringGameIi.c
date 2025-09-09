// Last updated: 09/09/2025, 14:16:57
#include <stdio.h>

long long len[105];
int ops[105];

char nextChar(char c) {
    return (c == 'z') ? 'a' : c + 1;
}

char findChar(int idx, long long k) {
    if (idx == -1) return 'a'; // base string

    if (ops[idx] == 0) {
        // word = word + word
        if (k <= len[idx]) {
            return findChar(idx - 1, k);
        } else {
            return findChar(idx - 1, k - len[idx]);
        }
    } else {
        // word = word + transformed_word
        if (k <= len[idx]) {
            return findChar(idx - 1, k);
        } else {
            char c = findChar(idx - 1, k - len[idx]);
            return nextChar(c);
        }
    }
}

char kthCharacter(long long k, int* operations, int operationsSize) {
    // Copy ops to global array for simplicity
    for (int i = 0; i < operationsSize; i++) ops[i] = operations[i];

    len[0] = 1;
    for (int i = 1; i <= operationsSize; i++) {
        len[i] = len[i-1] * 2;
        if (len[i] > 1e15) len[i] = 1e15; // cap to avoid overflow
    }

    return findChar(operationsSize - 1, k);
}
