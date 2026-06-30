# Last updated: 30/06/2026, 21:44:04
class Solution(object):
    def twoSum(self, numbers, target):
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            curr_sum = numbers[index1] + numbers[index2]
            if curr_sum == target:
                return [index1 + 1, index2 + 1]
            elif curr_sum < target:
                index1 += 1
            else:
                index2 -= 1
