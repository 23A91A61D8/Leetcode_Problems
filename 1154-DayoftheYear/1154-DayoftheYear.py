# Last updated: 22/07/2026, 22:36:25
1class Solution(object):
2    def dayOfYear(self, date):
3        year, month, day = map(int, date.split('-'))
4        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
5        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
6            days_in_month[1] = 29
7        return sum(days_in_month[:month-1]) + day