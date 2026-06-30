# Last updated: 30/06/2026, 21:42:07
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        date = datetime.date(year,month,day)
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return days[date.weekday()] 