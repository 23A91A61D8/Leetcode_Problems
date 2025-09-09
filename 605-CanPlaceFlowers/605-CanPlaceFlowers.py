# Last updated: 09/09/2025, 14:18:57
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
       
        flowerbed = [0] + flowerbed + [0]
        
        
        for i in range(1, len(flowerbed) - 1):
           
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1  
                n -= 1            
                if n == 0:        
                    return True
        return n <= 0
