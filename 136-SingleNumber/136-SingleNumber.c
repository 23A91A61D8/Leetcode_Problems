// Last updated: 09/09/2025, 14:19:59
int singleNumber(int* nums, int numsSize) {
    int result = 0;
    for (int i = 0; i < numsSize; i++) {
        result = result ^ nums[i];  // XOR with each number
    }   // ^ is used XOR operation
    
    return result;
}
