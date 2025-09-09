// Last updated: 09/09/2025, 14:20:12
void sortColors(int* nums, int numsSize) {
    int i,j;
    for(i=0;i<numsSize-1;i++) {
        for(j=0;j<numsSize-1;j++) {
            if(nums[j]>nums[j+1]){
                int temp;
                temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
            }
        }
    }
}