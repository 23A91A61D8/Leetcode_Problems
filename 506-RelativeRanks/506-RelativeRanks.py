# Last updated: 25/09/2026, 21:13:07
1class Solution(object):
2    def findRelativeRanks(self, score):
3        sorted_score = sorted(score, reverse=True)
4        rank = {}
5        for i in range(len(sorted_score)):
6            if i == 0:
7                rank[sorted_score[i]] = "Gold Medal"
8            elif i == 1:
9                rank[sorted_score[i]] = "Silver Medal"
10            elif i == 2:
11                rank[sorted_score[i]] = "Bronze Medal"
12            else:
13                rank[sorted_score[i]] = str(i + 1)
14        return [rank[x] for x in score]
15