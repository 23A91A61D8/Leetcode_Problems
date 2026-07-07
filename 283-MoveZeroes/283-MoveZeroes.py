# Last updated: 07/07/2026, 22:30:27
1class Solution(object):
2    def moveZeroes(self, nums):
3        insert_pos = 0
4        for num in nums:
5            if num != 0:
6                nums[insert_pos] = num
7                insert_pos += 1
8        while insert_pos < len(nums):
9            nums[insert_pos] = 0
10            insert_pos += 1