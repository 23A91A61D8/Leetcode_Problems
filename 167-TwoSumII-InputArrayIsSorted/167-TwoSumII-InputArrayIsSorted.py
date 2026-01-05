# Last updated: 05/01/2026, 22:04:41
1class Solution(object):
2    def twoSum(self, numbers, target):
3        index1 = 0
4        index2 = len(numbers) - 1
5        while index1 < index2:
6            curr_sum = numbers[index1] + numbers[index2]
7            if curr_sum == target:
8                return [index1 + 1, index2 + 1]
9            elif curr_sum < target:
10                index1 += 1
11            else:
12                index2 -= 1
13