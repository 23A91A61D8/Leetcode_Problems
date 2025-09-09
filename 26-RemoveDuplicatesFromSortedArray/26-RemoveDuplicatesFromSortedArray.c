// Last updated: 09/09/2025, 14:20:30
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int k = 1; // Start from index 1 since first element is always unique

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[k - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
}
