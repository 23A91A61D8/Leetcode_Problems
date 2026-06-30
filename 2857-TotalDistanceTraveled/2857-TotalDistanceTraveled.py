# Last updated: 30/06/2026, 21:41:10
class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        distance = 0

        while mainTank >= 5:

            mainTank -= 5
            distance += 50

            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        distance += mainTank * 10

        return distance
        