// Last updated: 09/09/2025, 14:19:24
int missingNumber(int* nums, int numsSize) {
    int sum1=(numsSize*(numsSize+1))/2;
    int arr_sum=0;
    for(int i=0;i<numsSize;i++)
    {
        arr_sum = arr_sum+nums[i];
    }
    return sum1 - arr_sum;
}