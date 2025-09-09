// Last updated: 09/09/2025, 14:19:39
int hammingWeight(unsigned int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}
