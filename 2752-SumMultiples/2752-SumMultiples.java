// Last updated: 09/09/2025, 14:17:06
class Solution {
    public int sumOfMultiples(int n) { 
       int sum=0;
       for(int i=0;i<=n;i++) {
        if(i%3==0 || i%5==0 || i%7==0) {
            sum=sum+i;
        }
       }
       return sum;
    }
}