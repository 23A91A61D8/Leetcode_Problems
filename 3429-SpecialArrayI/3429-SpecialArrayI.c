// Last updated: 09/09/2025, 14:17:02

bool isArraySpecial(int* nums, int numsSize) {
    for (int i = 0; i < numsSize - 1; i++) {
        if ((nums[i] % 2) == (nums[i + 1] % 2)) {
            return false;
        }
    }
    return true;
}
