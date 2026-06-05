# Last updated: 05/06/2026, 16:13:32
1class Solution(object):
2    def distanceTraveled(self, mainTank, additionalTank):
3        """
4        :type mainTank: int
5        :type additionalTank: int
6        :rtype: int
7        """
8        distance = 0
9
10        while mainTank >= 5:
11
12            mainTank -= 5
13            distance += 50
14
15            if additionalTank > 0:
16                mainTank += 1
17                additionalTank -= 1
18
19        distance += mainTank * 10
20
21        return distance
22        