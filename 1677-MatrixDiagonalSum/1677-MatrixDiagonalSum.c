// Last updated: 09/09/2025, 14:17:42
int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum=0;
    for(int i=0;i<matSize;i++)
    {
        sum+=mat[i][i]+mat[i][matSize -i-1];

    }
    if(matSize % 2==1)
    {
        sum-=mat[matSize/2][matSize/2];
    }
    return sum;
}