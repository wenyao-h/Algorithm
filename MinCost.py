class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m = len(cost)
        n = len(cost[0])
        dp = [[100000] * (1 << n) for i in range(m + n)]
        for i in range(m):
            if i == 0:
                pre_status = 0
                for j in range(n):
                    status = pre_status | (1 << j)
                    dp[i][status] = min(dp[i][status], cost[i][j])
            else:
                for pre_status in range(1 << n):
                    if dp[i - 1][pre_status] >= 100000:
                        continue
                    for j in range(n):
                        status = pre_status | (1 << j)
                        dp[i][status] = min(dp[i][status], dp[i - 1][pre_status] + cost[i][j])
            # print(i, dp[i])
        min_cost = []
        for j in range(n):
            mcost = 100000
            for i in range(m):
                mcost = min(cost[i][j], mcost)
            min_cost.append(mcost)
        for j in range(n):
            for pre_status in range(1 << n):
                if dp[m + j - 1][pre_status] >= 100000:
                    continue
                if pre_status & (1 << j) != 0:
                    dp[m + j][pre_status] = min(dp[m + j][pre_status], dp[m + j - 1][pre_status])
                else:
                    status = pre_status | (1 << j)
                    dp[m + j][status] = min(dp[m + j][status], dp[m + j - 1][pre_status] + min_cost[j])
            # print(j, dp[m + j])
        return dp[-1][-1]