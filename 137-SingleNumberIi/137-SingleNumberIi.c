// Last updated: 09/09/2025, 14:19:57
#include <stdio.h>

int singleNumber(int* nums, int numsSize) {
    int result = 0;

    for (int i = 0; i < 32; i++) {
        int bitCount = 0;

        for (int j = 0; j < numsSize; j++) {
            if ((nums[j] >> i) & 1) {
                bitCount++;
            }
        }

        if (bitCount % 3 != 0) {
            result |= ((unsigned int)1 << i); // Fix applied here
        }
    }

    return result;
}
