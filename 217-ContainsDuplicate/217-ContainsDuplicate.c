// Last updated: 09/09/2025, 14:19:33
void merge(int *A,int l,int m,int h) {
	int i=l,j=m+1,k=0;
	int result[h-l+1];
	while(i<=m&&j<=h) {
		if(A[i]<=A[j]) {
			result[k]=A[i];
			i++;
			k++;
		}
		else {
			result[k]=A[j];
			j++;
			k++;
		}
	}
	while(i<=m) {
		result[k]=A[i];
		i++;
		k++;
	}
	while(j<=h) {
		result[k]=A[j];
		j++;
		k++;
	}
	k=0;
	for(i=l;i<=h;i++) {
		A[i]=result[k];
		k++;
	}
}
void merge_sort(int *A,int l,int h) {
	if(l<h) {
		int m=(l+h)/2;
		merge_sort(A,l,m); 
		merge_sort(A,m+1,h);  
		merge(A,l,m,h);
	}
}
bool containsDuplicate(int* nums, int numsSize) {
    int found=0;
    merge_sort(nums,0,numsSize-1);
    for(int i=0;i<numsSize-1;i++) {
    if(nums[i]==nums[i+1]) {
        found=1;
    }
    }
    if(found==1){
        return true;
    }
    else{
        return false;
    }
}
